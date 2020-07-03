#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from collections import OrderedDict
from functools import partial

from vertica_parser import db_catalog
from vertica_parser.analyzer import InsertNode, CTASNode
from vertica_parser.analyzer import SelectNode, SimpleSelectNode
from vertica_parser.analyzer import PredicateNode
from vertica_parser.analyzer import list_cte, list_from, list_predicates


IDENT = r'([_a-z][_a-z0-9]+|"[^"]+")'
COLREF = r'({IDENT}|{IDENT}.{IDENT})'.format(IDENT=IDENT)


class ColSrc(object):
    def __init__(self, node=None, name=None, expr_path=None):
        self.node = node
        self.name = name
        self.expr_path = expr_path or list()

    def wrap(self, expr):
        return ColSrc(self.node, self.name, [expr] + self.expr_path)


def table_name(qualified_name):
    return qualified_name.lower()


def column_name(qualified_name):
    return qualified_name.rpartition('.')[2].strip('"').lower()


def column_rel(qualified_name):
    return qualified_name.rpartition('.')[0].strip('"').lower()


def rewrite_statement(query_node):
    out_cols = OrderedDict()

    if isinstance(query_node, SimpleSelectNode):
        cte_nodes = {table_name(cte.alias): cte.select_clause for cte in list_cte(query_node)}

        # bind input relations
        from_tables = dict()
        for table in list_from(query_node):
            alias = table_name(table.alias or table.table_ref.rpartition('.')[2])

            if table.select_clause:
                from_tables[alias] = rewrite_statement(table.select_clause)

            elif table_name(table.table_ref) in cte_nodes:
                table.select_clause = cte_nodes[table_name(table.table_ref)]
                table.table_ref = None
                table.alias = alias
                from_tables[alias] = rewrite_statement(table.select_clause)

            elif table_name(table.table_ref) in db_catalog.table_columns:
                table_columns = db_catalog.table_columns[table_name(table.table_ref)]
                from_tables[alias] = {c: [ColSrc(table, table_name(table.table_ref) + '.' + c)]
                                      for c in table_columns}

        # pushdown predicates
        for p in list_predicates(query_node):
            pushdown_predicate(p, from_tables)

        # bind output columns
        for c in query_node.column_list:
            deps = []

            for i in c.input_columns:
                col_name = column_name(i)
                rel_name = column_rel(i)

                if rel_name in from_tables:
                    table_columns = from_tables[rel_name]
                    deps.extend([d.wrap(c.expr) for d in table_columns.get(col_name, [])])

            col_name = column_name(c.output_column)
            while col_name in out_cols:
                col_name += ' '
            out_cols[col_name] = deps

    elif isinstance(query_node, SelectNode):

        for (i, select_clause) in enumerate(query_node.simple_select_clauses):
            deps = rewrite_statement(select_clause)
            if i == 0:
                out_cols = deps
            else:
                names = out_cols.keys()
                for j, v in enumerate(deps.values()):
                    out_cols[names[j]].extend(v)

    elif isinstance(query_node, CTASNode):

        deps = rewrite_statement(query_node.select_clause)
        inputs = deps.values()
        for (i, c) in enumerate(query_node.columns):
            out_cols[column_name(c.name)] = inputs[i]

    elif isinstance(query_node, InsertNode):

        deps = rewrite_statement(query_node.select_clause)
        inputs = deps.values()
        for (i, c) in enumerate(query_node.columns):
            if i < len(inputs):  # check for default values
                out_cols[column_name(c.name)] = inputs[i]

        name = table_name(query_node.name)
        for ddl_col in db_catalog.table_columns.get(name, list()):
            if ddl_col not in out_cols.keys():
                out_cols[ddl_col] = list()

    return out_cols


def is_expr_trivial(expr):
    return re.match(r'^({COLREF}'
                    r'|{COLREF}::{IDENT}'
                    r'|{COLREF}::{IDENT}\(\s*\d+\s*\)'
                    r'|{COLREF}::{IDENT}\(\s*\d+\s*,\s*\d+\s*\)'
                    r')$'
                    .format(COLREF=COLREF, IDENT=IDENT),
                    expr.strip(), flags=re.I)


def add_pred(node):
    if not node.filter_predicate:
        node.filter_predicate = PredicateNode(node, 'AND')

    child = PredicateNode(node.filter_predicate)
    node.filter_predicate.elements.append(child)
    return child


def shift_pred_down(pred_type, node):
    if not node.filter_predicate:
        node.filter_predicate = PredicateNode(node, 'AND')

    child = PredicateNode(node.filter_predicate, pred_type)
    node.filter_predicate.elements.append(child)
    node.filter_predicate = child


def shift_pred_up(node):
    child = node.filter_predicate
    node.filter_predicate = node.filter_predicate.parent
    if not child.elements:
        node.filter_predicate.elements.remove(child)


def pushdown_predicate(p, from_tables, table_nodes=None):

    if p.formula not in ('AND', 'OR', 'NOT'):

        if len(p.input_columns) == 1:
            rel_name = column_rel(p.input_columns[0])
            col_name = column_name(p.input_columns[0])

            for src in from_tables.get(rel_name, {}).get(col_name, []):
                if any(not is_expr_trivial(e) for e in src.expr_path if e):
                    continue

                pushdown = add_pred(src.node)
                cast = ''.join([''.join(e.partition('::')[1:]) for e in src.expr_path])
                col = r'\b({t}.{c}|{c})\b'.format(t=rel_name, c=col_name)
                pushdown.formula = re.sub(col, src.name + cast, p.formula, flags=re.I)

        if len(p.input_columns) == 0 and table_nodes:
            for node in table_nodes:
                pushdown = add_pred(node)
                pushdown.formula = p.formula

    elif p.formula == 'AND':
        for e in p.elements:
            pushdown_predicate(e, from_tables)

    elif p.formula == 'OR':
        real_inputs = list()
        for c in p.input_columns:
            real_inputs.extend(from_tables.get(column_rel(c), {}).get(column_name(c), []))

        if len({column_rel(i.name) for i in real_inputs}) != 1:
            return

        table_nodes = {src.node for src in real_inputs}
        map(partial(shift_pred_down, 'OR'), table_nodes)

        for e in p.elements:
            map(partial(shift_pred_down, 'AND'), table_nodes)
            pushdown_predicate(e, from_tables, table_nodes)
            map(shift_pred_up, table_nodes)

        map(shift_pred_up, table_nodes)


def fmt_predicate(p):
    if p.formula in ('AND', 'OR'):
        sep = u' {} '.format(p.formula)
        if len(p.elements) > 1:
            return '(' + sep.join(map(fmt_predicate, p.elements)) + ')'
        else:
            return sep.join(map(fmt_predicate, p.elements))
    elif p.formula == 'NOT':
        return u'NOT ' + fmt_predicate(p.elements[0])
    else:
        return p.formula
