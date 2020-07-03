#!/usr/bin/python
# -*- coding: utf-8 -*-

import io
import sys

from vertica_parser import parser, parse_statement, print_node
from vertica_parser import RootNode, CTASNode, InsertNode, DeleteNode, UpdateNode, CopyNode
from vertica_parser import SelectNode, SimpleSelectNode, TableNode, JoinNode


def table_name(qualified_name):
    return qualified_name.lower()


def ellipsis_list(list):
    if len(list) > 5:
        return list[:5] + ['...']
    else:
        return list


def list_relations(input_list):
    output_list = list()

    front = list()
    front.extend(input_list)

    while front:
        n = front.pop(0)
        if isinstance(n, TableNode):
            output_list.append(n)

        elif isinstance(n, JoinNode):
            front.append(n.left_table)
            front.append(n.right_table)

    return output_list


def list_leaf_tables(input_list, cte_list):
    output_list = list()

    cte_nodes = {table_name(cte.alias): cte.select_clause for cte in cte_list}
    visited_cte = set()

    front = list()
    front.extend(list_relations(input_list))

    while front:
        n = front.pop(0)
        assert(isinstance(n, TableNode))

        if n.select_clause:
            cte_list = n.select_clause.cte_clauses
            from_list = n.select_clause.simple_select_clauses[0].from_list
            front.extend(list_relations(from_list))
            cte_nodes.update({table_name(cte.alias): cte.select_clause for cte in cte_list})

        elif table_name(n.table_ref or n.alias) in cte_nodes:
            cte_name = table_name(n.table_ref or n.alias)
            if cte_name not in visited_cte:
                visited_cte.add(cte_name)

                cte = TableNode(None)
                cte.alias = cte_name
                cte.select_clause = cte_nodes[cte_name]
                front.append(cte)

        else:
            output_list.append(n)

    return output_list


def get_select_inputs(stmt):
    from_clause = stmt.simple_select_clauses[0].from_list
    cte_clause = stmt.cte_clauses
    tables = [src.table_ref or src.alias for src in list_leaf_tables(from_clause, cte_clause)]
    return list(filter(None, tables))


def describe_stmt(stmt):
    if isinstance(stmt, SelectNode):
        from_clause = stmt.simple_select_clauses[0].from_list
        cte_clause = stmt.cte_clauses

        relations = [src.table_ref or src.alias for src in list_relations(from_clause)]
        relations = list(filter(None, relations))

        tables = [src.table_ref or src.alias for src in list_leaf_tables(from_clause, cte_clause)]
        tables = list(filter(None, tables))

        if len(relations) == 1 and relations != tables:
            return 'SELECT FROM {} [{}]'.format(relations[0], ', '.join(ellipsis_list(tables)))

        elif relations:
            return 'SELECT FROM ' + ', '.join(ellipsis_list(relations))

    elif isinstance(stmt, InsertNode):
        return 'INSERT INTO ' + stmt.name

    elif isinstance(stmt, DeleteNode):
        return 'DELETE FROM ' + stmt.name

    elif isinstance(stmt, UpdateNode):
        return 'UPDATE ' + stmt.name

    elif isinstance(stmt, CTASNode):
        return 'CTAS ' + stmt.name

    elif isinstance(stmt, CopyNode):
        return 'COPY ' + stmt.name

    return None


def describe_sql(sql):
    root = RootNode()
    parse_statement(parser.parse(sql), root)
    for stmt in root.statements:
        descr = describe_stmt(stmt)
        if descr:
            return descr
    return None


if __name__ == '__main__':

    with io.open(sys.argv[1], mode="r", encoding="utf-8") as ifile:
        sql = ifile.read()

    print (describe_sql(sql))
