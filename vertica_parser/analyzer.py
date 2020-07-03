#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from vertica_parser import db_catalog
from vertica_parser.parser import Expr


class Node(object):
    def __init__(self, parent):
        self.parent = parent


class RootNode(Node):
    def __init__(self):
        super(RootNode, self).__init__(None)
        self.statements = list()


class SelectNode(Node):
    def __init__(self, parent):
        super(SelectNode, self).__init__(parent)
        self.cte_clauses = list()
        self.simple_select_clauses = list()
        self.limit = None


class SimpleSelectNode(Node):
    def __init__(self, parent):
        super(SimpleSelectNode, self).__init__(parent)
        self.is_distinct = False
        self.column_list = list()
        self.from_list = list()
        self.where_clause = None
        self.groupby_list = list()


class TableNode(Node):
    def __init__(self, parent):
        super(TableNode, self).__init__(parent)
        self.alias = None
        self.select_clause = None
        self.table_ref = None
        self.filter_predicate = None


class JoinNode(Node):
    def __init__(self, parent):
        super(JoinNode, self).__init__(parent)
        self.left_table = None
        self.right_table = None
        self.join_type = None
        self.join_predicate = None


class FunctionNode(Node):
    def __init__(self, parent):
        super(FunctionNode, self).__init__(parent)
        self.func_name = None
        self.partition_list = list()
        self.orderby_list = list()


class ColumnNode(Node):
    def __init__(self, parent):
        super(ColumnNode, self).__init__(parent)
        self.alias = None
        self.expr = None
        self.func = None
        self.input_columns = list()
        self.output_column = None


class ColumnDefNode(Node):
    def __init__(self, parent):
        super(ColumnDefNode, self).__init__(parent)
        self.name = None
        self.type = None
        self.constraint = None
        self.encoding = None
        self.rank = None


class CreateNode(Node):
    def __init__(self, parent):
        super(CreateNode, self).__init__(parent)
        self.name = None
        self.temp = None
        self.columns = list()


class CTASNode(Node):
    def __init__(self, parent):
        super(CTASNode, self).__init__(parent)
        self.name = None
        self.temp = None
        self.columns = list()
        self.select_clause = None


class InsertNode(Node):
    def __init__(self, parent):
        super(InsertNode, self).__init__(parent)
        self.name = None
        self.columns = list()
        self.select_clause = None


class DeleteNode(Node):
    def __init__(self, parent):
        super(DeleteNode, self).__init__(parent)
        self.name = None
        self.where_clause = None


class UpdateNode(Node):
    def __init__(self, parent):
        super(UpdateNode, self).__init__(parent)
        self.name = None
        self.alias = None
        self.from_clause = None
        self.update_list = list()
        self.where_clause = None


class CopyNode(Node):
    def __init__(self, parent):
        super(CopyNode, self).__init__(parent)
        self.name = None
        self.columns = list()


class PredicateNode(Node):
    def __init__(self, parent, formula=None):
        super(PredicateNode, self).__init__(parent)
        self.formula = formula  # AND OR NOT expression
        self.elements = list()
        self.input_columns = list()


class ViewNode(Node):
    def __init__(self, parent):
        super(ViewNode, self).__init__(parent)
        self.name = None
        self.columns = list()
        self.select_clause = None
        self.create_or_replace = False


class ExplainNode(Node):
    def __init__(self, parent):
        super(ExplainNode, self).__init__(parent)
        self.stmt = None


def find_all_nodes(node, search_class):
    found_nodes = set()
    seen_nodes = set()

    front = [node]
    while front:
        n = front.pop(0)
        if isinstance(n, search_class):
            found_nodes.add(n)

        if isinstance(n, list):
            front.extend(n)
        if isinstance(n, Node):
            if n in seen_nodes:
                continue
            seen_nodes.add(n)
            front.extend(vars(n).values())

    return found_nodes


def name(token):
    return getattr(token, 'name', None)


try:
    unicode
except NameError:
    unicode = str


def stringify(token):
    if not isinstance(token, Expr):
        return unicode(token)
    return ' '.join([stringify(t) for t in token.tokens])\
        .replace(' . ', '.')\
        .replace(' :: ', '::')\
        .replace(' !:: ', '!::')\
        .replace(' [ ', '[')\
        .replace(' ( ', '(')\
        .replace(' ] ', '] ')\
        .replace(' ) ', ') ')\
        .replace(' : ', ' :')


def normalize(qualified_name):
    if not qualified_name:
        return qualified_name
    return '.'.join([part.strip('"').lower() for part in qualified_name.split('.')])


def alias(token):
    if name(token) == 'alias_clause':
        if stringify(token.tokens[0]).lower() == 'as':
            return stringify(token.tokens[1])
        else:
            return stringify(token.tokens[0])
    return None


def find_token(syntax_node, node_name, level):
    if level < 1:
        return None

    found = None
    for t in getattr(syntax_node, 'tokens', list()):
        if found:
            break
        if name(t) == node_name:
            found = t
        else:
            found = find_token(t, node_name, level - 1)

    return found


def find_all_tokens(syntax_node, node_name):
    found_tokens = list()
    for t in getattr(syntax_node, 'tokens', list()):
        if name(t) == node_name:
            found_tokens.append(t)
        found_tokens.extend(find_all_tokens(t, node_name))
    return found_tokens


def find_expr(syntax_node, expr_formula):
    found_tokens = list()
    for t in getattr(syntax_node, 'tokens', list()):
        if hasattr(t, 'expr') and getattr(t, 'expr') == expr_formula:
            found_tokens.append(t)
        else:
            found_tokens.extend(find_expr(t, expr_formula))
    return found_tokens


def list_params(syntax_node):
    param_expr = find_expr(syntax_node, 'PARAM opt_indirection')
    return list(set([str(e.tokens[0]) for e in param_expr]))


def unpivot_list(syntax_node, list_name, element_name):
    assert(name(syntax_node) == list_name)

    elements = list()

    list_tokens = list()
    list_tokens.extend(syntax_node.tokens)
    while list_tokens:
        t = list_tokens.pop(0)
        if name(t) == element_name:
            elements.insert(0, t)
        elif name(t) == list_name:
            list_tokens.extend(t.tokens)

    return elements


def unpivot_expression(syntax_node, expr_formula, expr_element):
    assert(name(syntax_node) == expr_element)
    assert(syntax_node.expr == expr_formula)

    elements = list()

    token = syntax_node
    while token:
        next = None
        for t in getattr(token, 'tokens', list()):
            if name(t) == expr_element and t.expr == expr_formula:
                next = token.tokens[0]
            elif name(t) == expr_element:
                elements.insert(0, t)
        token = next

    return elements


def parse_statement(syntax_node, query_node, positions=None):

    switch = {
        'ViewStmt': (parse_view, ViewNode),
        'CreateAsStmt': (parse_ctas, CTASNode),
        'CreateStmt': (parse_create, CreateNode),
        'InsertStmt': (parse_insert, InsertNode),
        'UpdateStmt': (parse_update, UpdateNode),
        'DeleteStmt': (parse_delete, DeleteNode),
        'CopyStmt': (parse_copy, CopyNode),
        'SelectStmt': (parse_select, SelectNode),
        'ExplainStmt': (parse_explain, ExplainNode),
    }

    if positions is None:
        positions = list()

    for t in getattr(syntax_node, 'tokens', list()):
        if name(t) == "a_stmt":
            positions.append((t.line, t.pos))
            n = RootNode()
            parse_statement(t, n, None)
            query_node.statements.append((n.statements or [None])[0])
        elif name(t) in switch:
            parse_node, node_class = switch.get(name(t))
            n = node_class(query_node)
            parse_node(t, n)
            query_node.statements.append(n)
        elif name(t) in ('stmtblock', 'stmtmulti', 'stmt', 'VSelectStmt'):
            parse_statement(t, query_node, positions)


def parse_explain(syntax_node, query_node):
    assert (name(syntax_node) == 'ExplainStmt')
    stmt = find_token(syntax_node, 'ExplainableStmt', 1)

    n = RootNode()
    parse_statement(stmt, n, None)
    query_node.stmt = (n.statements or [None])[0]


def parse_create(syntax_node, query_node):
    assert (name(syntax_node) == 'CreateStmt')
    query_node.name = stringify(find_token(syntax_node, 'qualified_name', 1))

    opt_temp = find_token(syntax_node, 'OptTemp', 1)
    if opt_temp:
        query_node.temp = stringify(opt_temp)

    f = find_token(syntax_node, 'OptTableElementList', 1)
    if f:
        column_list = [stringify(t.tokens[0].tokens[0])
                       for t in find_all_tokens(f, 'TableElement')
                       if name(t.tokens[0]) == 'columnDef']
    else:
        like_table = stringify(find_token(syntax_node, 'TableLikeClause', 1).tokens[1])
        column_list = db_catalog.table_columns.get(normalize(like_table), list())

    for c in column_list:
        n = ColumnDefNode(query_node)
        n.name = c
        query_node.columns.append(n)

    db_catalog.table_columns[normalize(query_node.name)] = [normalize(c.name) for c in query_node.columns]


def parse_ctas(syntax_node, query_node):
    assert (name(syntax_node) == 'CreateAsStmt')
    query_node.name = stringify(find_token(syntax_node, 'qualified_name', 1))

    opt_temp = find_token(syntax_node, 'OptTemp', 1)
    if opt_temp:
        query_node.temp = stringify(opt_temp)

    query_node.select_clause = SelectNode(query_node)
    parse_select(find_token(syntax_node, 'VSelectStmt', 1), query_node.select_clause)

    f = find_token(syntax_node, 'vt_columnGroupList', 2)
    if f:
        column_list = map(lambda t: stringify(t.tokens[0]).strip(), find_all_tokens(f, 'VColumnElem'))
    else:
        column_list = map(lambda t: t.output_column.rpartition('.')[2], query_node.select_clause.simple_select_clauses[0].column_list)

    for c in column_list:
        n = ColumnDefNode(query_node)
        n.name = c
        query_node.columns.append(n)

    db_catalog.table_columns[normalize(query_node.name)] = [normalize(c.name) for c in query_node.columns]


def parse_insert(syntax_node, query_node):
    assert (name(syntax_node) == 'InsertStmt')
    query_node.name = stringify(find_token(syntax_node, 'qualified_name', 1))
    query_node.select_clause = SelectNode(query_node)
    parse_select(find_token(syntax_node, 'VSelectStmt', 2), query_node.select_clause)

    f = find_token(syntax_node, 'insert_column_list', 2)
    if f:
        column_list = map(lambda x: stringify(x).strip(), unpivot_list(f, 'insert_column_list', 'insert_column_item'))
    else:
        column_list = db_catalog.table_columns.get(normalize(query_node.name), list())

    for c in column_list:
        n = ColumnDefNode(query_node)
        n.name = c
        query_node.columns.append(n)


def parse_copy(syntax_node, query_node):
    assert (name(syntax_node) == 'CopyStmt')
    query_node.name = stringify(find_token(syntax_node, 'qualified_name', 1))

    f = find_token(syntax_node, 'opt_copy_column_list', 1)
    if f:
        column_list = [stringify(t.tokens[0].tokens[0])
                       for t in find_all_tokens(f, 'copyColumnElem')
                       if name(t.tokens[0]) == 'columnref']
    else:
        column_list = db_catalog.table_columns.get(normalize(query_node.name), list())

    for c in column_list:
        n = ColumnDefNode(query_node)
        n.name = c
        query_node.columns.append(n)


def parse_update(syntax_node, query_node):
    assert (name(syntax_node) == 'UpdateStmt')
    query_node.name = stringify(find_token(syntax_node.tokens[2], 'qualified_name', 2))
    alias = find_token(syntax_node.tokens[2], 'ColId', 1)
    query_node.alias = stringify(alias) if alias else None

    parse_update_list(syntax_node.tokens[4], query_node)

    table_ref = find_token(syntax_node.tokens[5], 'table_ref', 2)
    if table_ref:
        query_node.from_clause = create_table_node(table_ref, query_node)

    parse_where(syntax_node.tokens[6], query_node)


def parse_delete(syntax_node, query_node):
    assert (name(syntax_node) == 'DeleteStmt')
    query_node.name = stringify(find_token(syntax_node.tokens[3], 'qualified_name', 1))
    parse_where(syntax_node.tokens[4], query_node)


def parse_view(syntax_node, query_node):
    assert (name(syntax_node) == 'ViewStmt')
    query_node.name = stringify(find_token(syntax_node, 'qualified_name', 1))
    query_node.select_clause = SelectNode(query_node)
    query_node.create_or_replace = syntax_node.expr.startswith('CREATE OR REPLACE')
    parse_select(find_token(syntax_node, 'SelectStmt', 1), query_node.select_clause)

    f = find_token(syntax_node, 'columnList', 2)
    if f:
        column_list = map(lambda t: stringify(t.tokens[0]).strip(), find_all_tokens(f, 'columnElem'))
    else:
        column_list = map(lambda t: t.output_column.rpartition('.')[2], query_node.select_clause.simple_select_clauses[0].column_list)

    for c in column_list:
        n = ColumnDefNode(query_node)
        n.name = c
        query_node.columns.append(n)

    db_catalog.table_columns[normalize(query_node.name)] = [normalize(c.name) for c in query_node.columns]


def parse_select(syntax_node, query_node):

    for t in getattr(syntax_node, 'tokens', list()):
        if name(t) == 'common_table_expr':
            n = TableNode(query_node)
            query_node.cte_clauses.append(n)
            parse_cte(t, n)
        elif name(t) == 'simple_select' and stringify(t.tokens[0]).upper() == 'SELECT':
            n = SimpleSelectNode(query_node)
            query_node.simple_select_clauses.append(n)
            parse_simple_select(t, n)
        elif name(t) == 'select_limit':
            query_node.limit = stringify(find_token(t, 'select_limit_value', 3))
        else:
            parse_select(t, query_node)


def parse_cte(syntax_node, query_node):
    """name opt_name_list AS '(' SelectStmt ')'"""
    assert (name(syntax_node) == 'common_table_expr')

    query_node.alias = stringify(syntax_node.tokens[0])
    query_node.select_clause = SelectNode(query_node)
    parse_select(syntax_node.tokens[4], query_node.select_clause)


def parse_simple_select(syntax_node, query_node):
    """SELECT hint_clause opt_distinct target_list select_clauses"""
    assert (name(syntax_node) == 'simple_select')

    query_node.is_distinct = 'DISTINCT' in syntax_node.tokens[2].tokens
    parse_from(syntax_node.tokens[4].tokens[0], query_node)
    parse_target_list(syntax_node.tokens[3], query_node)
    parse_where(syntax_node.tokens[4].tokens[1], query_node)
    parse_groupby(syntax_node.tokens[4].tokens[3], query_node)

    bind_input_columns(query_node)


def parse_target_list(syntax_node, query_node):

    for t in getattr(syntax_node, 'tokens', list()):

        if name(t) == 'target_list':
            parse_target_list(t, query_node)

        elif name(t) == 'target_el' and t.tokens[0] == '*':
            expand_star_columns(query_node, None)

        elif name(t) == 'target_el' and '.*' in stringify(t.tokens[0]):
            rel_token = find_token(t.tokens[0], 'relation_name', 3)
            expand_star_columns(query_node, stringify(rel_token))

        elif name(t) == 'target_el':

            c = ColumnNode(query_node)
            c.expr = stringify(t.tokens[0])  # a_expr
            query_node.column_list.append(c)
            parse_expr(t.tokens[0], c)

            if len(t.tokens) == 3 and t.tokens[2].name == 'ColLabel':
                c.alias = stringify(t.tokens[2])

            elif len(t.tokens) == 2 and t.tokens[1].name == 'BareColLabel':
                c.alias = stringify(t.tokens[1])

            c_expr = find_token(t.tokens[0], 'c_expr', 1)
            if not c_expr and t.tokens[0].expr == 'a_expr TYPECAST Typename hint_clause':
                c_expr = find_token(t.tokens[0].tokens[0], 'c_expr', 1)

            columnref = find_token(c_expr, 'columnref', 1)
            func_expr = find_token(c_expr, 'func_expr', 1)
            case_expr = find_token(c_expr, 'case_expr', 1)
            any_output = None

            if find_token(func_expr, 'analytic_function', 1):
                f = FunctionNode(c)
                f.func_name = normalize(stringify(find_token(func_expr, 'func_name', 3)))
                f.func_name = (f.func_name.rpartition('.')[0] or 'public') + '.' + f.func_name.rpartition('.')[2]
                c.func = f

                over_clause = find_token(func_expr, 'over_clause', 3)

                partition_clause = find_token(over_clause, 'opt_partition_clause', 3)
                partition_expr = find_token(partition_clause, 'expr_list', 2)
                if partition_expr:
                    token_list = unpivot_list(partition_expr, 'expr_list', 'a_expr')
                    f.partition_list = [stringify(t).strip() for t in token_list]

                orderby_clause = find_token(over_clause, 'opt_orderby_clause', 3)
                orderby_expr = find_token(orderby_clause, 'orderby_list', 2)
                if orderby_expr:
                    token_list = unpivot_list(orderby_expr, 'orderby_list', 'orderby')
                    f.orderby_list = [stringify(t.tokens[0]).strip() for t in token_list]

                any_output = (f.func_name in db_catalog.transform_functions) and 'any'

            alias_guess = None
            if not c.alias:
                c_token = columnref or case_expr or any_output or func_expr or '?column?'
                alias_guess = re.sub(r'[\(\[ ].*', '', stringify(c_token)).strip('"').rpartition('.')[2]

            c.output_column = normalize(c.alias or alias_guess)


def parse_update_list(syntax_node, query_node):
    assert (isinstance(query_node, UpdateNode))

    for t in getattr(syntax_node, 'tokens', list()):

        if name(t) == 'update_target_list':
            parse_update_list(t, query_node)

        elif name(t) == 'update_target_el':

            c = ColumnNode(query_node)
            c.expr = stringify(t.tokens[3])  # a_expr
            parse_expr(t.tokens[3], c)

            indirection = find_token(t.tokens[1], 'attr_name', 3)
            c.alias = stringify(indirection or t.tokens[0])
            c.output_column = normalize(c.alias)

            query_node.update_list.append(c)


def list_cte(query_node):
    cte_list = list()

    if isinstance(query_node, SelectNode):
        cte_list.extend(query_node.cte_clauses)

    if query_node.parent:
        cte_list.extend([cte for cte in list_cte(query_node.parent) if cte != query_node])

    return cte_list


def list_from(select_node):
    assert (isinstance(select_node, SimpleSelectNode))
    from_list = list()

    front = list()
    front.extend(select_node.from_list)
    while front:
        n = front.pop(0)
        if isinstance(n, TableNode):
            from_list.append(n)

        elif isinstance(n, JoinNode):
            front.append(n.left_table)
            front.append(n.right_table)

    return from_list


def list_joins(select_node):
    assert (isinstance(select_node, SimpleSelectNode))
    join_list = list()

    front = list()
    front.extend(select_node.from_list)
    while front:
        n = front.pop(0)

        if isinstance(n, JoinNode):
            join_list.append(n)
            front.append(n.left_table)
            front.append(n.right_table)

    return join_list


def list_predicates(select_node):
    predicate_list = list()

    for j in list_joins(select_node):
        if j.join_predicate:
            predicate_list.append(j.join_predicate)

    predicate_list.append(select_node.where_clause)

    return predicate_list


def unpivot_predicates(predicate_list):
    flattened_list = list()

    front = list()
    front.extend(predicate_list)
    while front:
        n = front.pop(0)

        if isinstance(n, PredicateNode):
            flattened_list.append(n)

        front.extend(n.elements)

    return flattened_list


def expand_star_columns(select_node, star_rel):

    cte_columns = dict()
    for cte in list_cte(select_node):
        cols = [c.output_column for c in cte.select_clause.simple_select_clauses[0].column_list]
        cte_columns[normalize(cte.alias)] = cols

    for n in list_from(select_node):
        table_name = None
        cols = list()

        if n.table_ref and (star_rel is None or normalize(n.alias or n.table_ref.rpartition('.')[2]) == normalize(star_rel)):

            if normalize(n.table_ref) in cte_columns:
                cols = cte_columns[normalize(n.table_ref)]
            elif normalize(n.table_ref) in db_catalog.table_columns:
                cols = db_catalog.table_columns[normalize(n.table_ref)]
            table_name = n.alias or n.table_ref.rpartition('.')[2]

        if n.select_clause and (star_rel is None or normalize(n.alias) == normalize(star_rel)):

            cols = [c.output_column for c in n.select_clause.simple_select_clauses[0].column_list]
            table_name = n.alias

        for c in cols:
            column_node = ColumnNode(select_node)
            column_node.output_column = c
            column_node.expr = table_name + '.' + c
            column_node.input_columns = [normalize(table_name) + '.' + c]
            select_node.column_list.append(column_node)


def column_table_name(table_node, column_name, table_columns):
    if isinstance(table_node, JoinNode):
        left_rel = column_table_name(table_node.left_table, column_name, table_columns)
        right_rel = column_table_name(table_node.right_table, column_name, table_columns)

        if column_name in table_columns.get(right_rel, list()):
            return right_rel
        else:
            return left_rel
    else:
        return normalize(table_node.alias or table_node.table_ref)


def bind_column_name(column_expr, column_table_lookup):
    col_name = column_expr.rpartition('.')[2].lower()
    rel_name = column_expr.rpartition('.')[0].lower()
    if not rel_name and col_name in column_table_lookup:
        return column_table_lookup[col_name].rpartition('.')[2] + '.' + col_name
    else:
        return column_expr.lower()


def bind_input_columns(select_node):
    cte_columns = dict()
    for cte in list_cte(select_node):
        cols = [c.output_column for c in cte.select_clause.simple_select_clauses[0].column_list]
        cte_columns[normalize(cte.alias)] = cols

    from_columns = dict()
    for table in list_from(select_node):
        cols = list()
        if table.select_clause:
            cols = [c.output_column for c in table.select_clause.simple_select_clauses[0].column_list]
        elif normalize(table.table_ref) in cte_columns:
            cols = cte_columns[normalize(table.table_ref)]
        elif normalize(table.table_ref) in db_catalog.table_columns:
            cols = db_catalog.table_columns[normalize(table.table_ref)]
        from_columns[normalize(table.alias or table.table_ref)] = cols

    column_table = {c: t for t in from_columns for c in from_columns[t]}

    for c in select_node.column_list:
        c.input_columns = [bind_column_name(i, column_table) for i in c.input_columns]
        if c.func:
            c.func.partition_list = [bind_column_name(pc, column_table) for pc in c.func.partition_list]
            c.func.orderby_list = [bind_column_name(oc, column_table) for oc in c.func.orderby_list]

    for j in list_joins(select_node):
        if j.join_predicate.formula == 'USING':

            join_products = list()
            for c in j.join_predicate.elements:
                rel_left = column_table_name(j.join_predicate.left_table, c, from_columns)
                rel_right = column_table_name(j.join_predicate.right_table, c, from_columns)

                n = PredicateNode(j.join_predicate)
                n.input_columns = [rel_left + '.' + c, rel_right + '.' + c]
                n.formula = n.input_columns[0] + ' = ' + n.input_columns[1]

                join_products.append(n)

            j.join_predicate.formula = 'AND'
            j.join_predicate.elements = join_products
            j.join_predicate.input_columns = list(set([i for n in join_products for i in n.input_columns]))

    for c in unpivot_predicates(list_predicates(select_node)):
        c.input_columns = [bind_column_name(i, column_table) for i in c.input_columns]

    select_node.groupby_list = [bind_column_name(c, column_table) for c in select_node.groupby_list]


def parse_expr(syntax_node, query_node):

    for t in getattr(syntax_node, 'tokens', list()):
        if name(t) and name(t).startswith('select'):
            query_node.input_columns.append('semi-join')
        elif name(t) == 'columnref':
            query_node.input_columns.append(normalize(stringify(t)))
        else:
            parse_expr(t, query_node)


def parse_from(syntax_node, query_node):
    for t in getattr(syntax_node, 'tokens', list()):
        if name(t) == 'table_ref':
            n = create_table_node(t, query_node)
            query_node.from_list.append(n)
        else:
            parse_from(t, query_node)


def create_table_node(syntax_node, query_node):
    assert (name(syntax_node) == 'table_ref')

    tokens = getattr(syntax_node, 'tokens', list())
    alias_clause = find_token(syntax_node, 'alias_clause', 1)

    for t in tokens:
        if name(t) == 'relation_expr':
            n = TableNode(query_node)
            n.alias = alias(alias_clause) if alias else None
            n.table_ref = stringify(find_token(t, 'qualified_name', 1))
            return n

        elif name(t) == 'select_with_parens':
            n = TableNode(query_node)
            n.alias = alias(alias_clause) if alias else None
            n.select_clause = SelectNode(n)
            parse_select(t, n.select_clause)
            return n

        elif name(t) == 'joined_table':
            n = JoinNode(query_node)
            parse_join(t, n)
            return n


def is_join_token(x):
    return (name(x) or stringify(x).upper()) in ('NATURAL', 'CROSS', 'JOIN', 'join_type')


def parse_join(syntax_node, query_node):
    assert (name(syntax_node) == 'joined_table')

    if name(syntax_node.tokens[1]) == 'joined_table':
        syntax_node = syntax_node.tokens[1]

    tables = list(filter(lambda x: name(x) == 'table_ref', syntax_node.tokens))
    join_type = map(stringify, filter(is_join_token, syntax_node.tokens))
    join_predicate = find_token(syntax_node, 'join_qual', 1)

    query_node.left_table = create_table_node(tables[0], query_node)
    query_node.right_table = create_table_node(tables[1], query_node)
    query_node.join_type = ' '.join(join_type)

    query_node.join_predicate = PredicateNode(query_node)
    using_predicate = find_token(join_predicate, 'name_list', 1)
    on_predicate = find_token(join_predicate, 'a_expr', 1)
    parse_predicate(using_predicate or on_predicate, query_node.join_predicate)


def parse_predicate(t, query_node):

    if name(t) == 'a_expr':

        if t.expr == 'c_expr' and t.tokens[0].expr == "'(' a_expr ')'":
            parse_predicate(t.tokens[0].tokens[1], query_node)

        elif t.expr == 'a_expr AND a_expr':
            query_node.formula = 'AND'
            for el in unpivot_expression(t, 'a_expr AND a_expr', 'a_expr'):
                n = PredicateNode(query_node)
                parse_predicate(el, n)
                query_node.elements.append(n)

        elif t.expr == 'a_expr OR a_expr':
            query_node.formula = 'OR'
            for el in unpivot_expression(t, 'a_expr OR a_expr', 'a_expr'):
                n = PredicateNode(query_node)
                parse_predicate(el, n)
                query_node.elements.append(n)

        elif t.expr == 'NOT a_expr':
            query_node.formula = 'NOT'
            n = PredicateNode(query_node)
            parse_predicate(t.tokens[1], n)
            query_node.elements.append(n)

        else:
            query_node.formula = stringify(t).strip()

        parse_expr(t, query_node)

    elif name(t) == 'name_list':
        assert (isinstance(query_node.parent, JoinNode))

        query_node.formula = 'USING'
        query_node.input_columns = [normalize(stringify(el)) for el in unpivot_list(t, 'name_list', 'name')]


def parse_where(syntax_node, query_node):
    assert (name(syntax_node) == 'where_clause')
    query_node.where_clause = PredicateNode(query_node)
    predicate_token = find_token(syntax_node, 'a_expr', 1)
    parse_predicate(predicate_token, query_node.where_clause)


def parse_groupby(syntax_node, query_node):
    assert (name(syntax_node) == 'group_clause')
    groupby_lists = find_token(syntax_node, 'groupby_expr_list', 2)
    if groupby_lists:
        token_list = unpivot_list(groupby_lists, 'groupby_expr_list', 'groupby_expr')
        query_node.groupby_list = [stringify(t).strip() for t in token_list]


def print_node(n):
    import json
    import jsonpickle
    import re
    s = jsonpickle.encode(n)
    s = re.sub('"(py/id|py/object)": ([^{},]*|\{[^}]*\}),', '', s)
    s = re.sub(', "(py/id|py/object)": ([^{},]*|\{[^}]*\})', '', s)
    s = re.sub('"(py/id|py/object)": ([^{},]*|\{[^}]*\})', '', s)
    print(json.dumps(json.loads(s), indent=2))
