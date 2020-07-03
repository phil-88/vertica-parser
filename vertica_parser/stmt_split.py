#!/usr/bin/python
# -*- coding: utf-8 -*-

from vertica_parser import make_parser, parse_statement, RootNode


def split_statements(sql, ignore_errors=True):
    parser = make_parser(trap_errors=True)
    syntax_tree = parser.parse(sql, tracking=True)

    if not ignore_errors and parser.lexer.errors:
        raise ValueError(parser.lexer.errors[-1])

    root = RootNode()
    pos = list()
    parse_statement(syntax_tree, root, pos)

    statements = list()
    for i in range(len(root.statements)):
        pos_from = pos[i][1]
        pos_to = pos[i + 1][1] if i + 1 < len(pos) else None
        statements.append(sql[pos_from:pos_to])
    return statements


if __name__ == '__main__':
    import io
    import sys

    with io.open(sys.argv[1], mode="r", encoding="utf-8") as ifile:
        sql = ifile.read()

    print('\n--BREAK--\n'.join(split_statements(sql)))
