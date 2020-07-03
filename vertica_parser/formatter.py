#!/usr/bin/python

import re
from vertica_parser import parser
from vertica_parser import analyzer
from collections import namedtuple


NOBREAK_BEFORE = ('.', '[', ']', ')', ',', ':', '::', '::!', ';')
NOBREAK_AFTER = ('.', '[', '(', '::', '::!')
EXPRESSIONS_WITH_ARGS = (
    'opt_vt_columnGroupList',
    'VColumnGroupElem',
    'opt_proj_list',
    'opt_copy_file_format',
    'copy_node_list',
    'opt_parse_option_list',
    'opt_copy_column_list',
    'copyColumnElem',
    'columnDef',
    'ColConstraintElem',
    'ConstraintElem',
    'opt_column_list',
    'opt_determines_clause',
    'OptInherit',
    'definition',
    'opclass_item',
    'CommentStmt',
    'func_args',
    'proc_args',
    'RemoveAggrStmt',
    'RemoveOperStmt',
    'DropCastStmt',
    'RenameStmt',
    'RuleActionList',
    'opt_name_list',
    'opt_hint_list',
    'prep_type_clause',
    'prep_type_list',
    'execute_param_clause',
    'merge_insert_target_list',
    'insert_rest',
    'ExportStmt',
    'opt_export_column_list',
    'opt_export_target_list',
    'opt_distinct',
    'select_limit',
    'rollup_clause',
    'cube_clause',
    'grouping_sets_clause',
    'grouping_expr',
    'grouping_set_expr',
    'table_sample',
    'join_qual',
    'relation_expr',
    'TypenameWithTypmod',
    'GenericTypeWithLength',
    'BinaryWithLength',
    'BitWithLength',
    'CharacterWithLength',
    'ConstDatetime',
    'non_analytic_function',
    'load_function',
    'row',
    'pattern_clause',
    'regexpprime',
    'within_clause',
    'window_specification',
    'opt_float',
    'opt_numeric',
    'opt_decimal',
    'leading_precision',
    'seconds_precision',
    'opt_parens',
    'qual_Op',
    'qual_all_Op',
    'subquery_Op'
)

NEWLINE_KEYWORDS = (
    'INSERT',
    'DELETE',
    'UPDATE',
    'CREATE',
    'ALTER',
    'DROP',
    'WITH',
    'SELECT',
    'FROM',
    'WHERE',
    'GROUP',
    'HAVING',
    'UNION',
    'MINUNS',
    'EXCEPT',
    'INTERSECT',
)

FmtNode = namedtuple('FmtNode', ['str', 'prevent_deeper'])

try:
  basestring
except NameError:
  basestring = str


def fmt_strip(syntax_node, state):
    if not 'nobreak_after' in state:
        state['nobreak_after'] = True

    if isinstance(syntax_node, basestring):
        res = ''
        if not state.get('nobreak_after') and not syntax_node in NOBREAK_BEFORE and \
           not (state['path'][-1].name in EXPRESSIONS_WITH_ARGS and syntax_node == '('):
            res += ' '
        res += syntax_node
        state['nobreak_after'] = syntax_node in NOBREAK_AFTER
        return FmtNode(res, True)
    else:
        return FmtNode(None, False)


def match(node, name, expr=None):
    if not node:
        return False
    if name and not re.match(name, getattr(node, 'name', 'None')):
        return False
    if expr and not re.match(expr, getattr(node, 'expr', 'None')):
        return False
    return True


def fmt_multiline(node, state):
    if not 'nobreak_after' in state:
        state['nobreak_after'] = True
    if not 'ident' in state:
        state['ident'] = 0

    no_break = any([
        state.get('nobreak_after'),
        node in NOBREAK_BEFORE,
        node == '(' and state['path'][-1].name in EXPRESSIONS_WITH_ARGS
    ])
    is_literal = isinstance(node, basestring)
    br = '' if no_break else ' '
    par1 = state['path'] and state['path'][-1] or None
    par2 = len(state['path']) > 1 and state['path'][-2] or None

    pre = ''
    suf = ''
    # multiple statements
    if node == ';' and match(par1, 'stmtmulti'):
        state['nobreak_after'] = True
        state['ident'] = 0
        suf = '\n'

    # joins
    elif match(par1, 'joined_table', '^table_ref.*') and node == par1.tokens[1]:
        pre = '\n' + ' ' * state['ident']
        state['nobreak_after'] = True
    elif node == '(' and match(par1, 'table_ref'):
        pre = ' '
        state['ident'] += 4
    elif node == ')' and match(par1, 'table_ref'):
        state['ident'] -= 4
        pre = '\n' + ' ' * state['ident']
    elif node == '(' and match(par2, 'table_ref') and match(par1, 'select_with_parens'):
        pre = ' '
        state['ident'] += 4
    elif node == ')' and match(par2, 'table_ref') and match(par1, 'select_with_parens'):
        state['ident'] -= 4
        pre = '\n' + ' ' * state['ident']

    # create statement
    elif node == '(' and match(par1, 'CreateStmt'):
        pre = '\n' + ' ' * state['ident']
    elif node == ')' and match(par1, 'CreateStmt'):
        pre = '\n' + ' ' * state['ident']
        suf = '\n' + ' ' * state['ident']
    elif match(par1, 'TableElementList') and node == par1.tokens[-1]:
        pre = '\n' + ' ' * state['ident'] + ' ' * 4
        state['nobreak_after'] = True

    # select column list
    elif match(par1, 'simple_select') and match(node, 'target_list'):
        state['ident'] += 4
    elif match(par1, 'simple_select') and match(node, 'select_clauses'):
        state['ident'] -= 4
    elif node == ',' and match(par1, 'target_list'):
        suf = '\n' + ' ' * state['ident']
        state['nobreak_after'] = True

    # case clause
    elif match(par1, 'case_expr') and is_literal and node.upper() == 'CASE':
        pre = br
        state['ident'] += 4
    elif match(par1, 'case_expr') and is_literal and node.upper() == 'END':
        state['ident'] -= 4
        pre = '\n' + ' ' * state['ident']
    elif match(par1, 'when_clause') and is_literal and node.upper() == 'WHEN':
        pre = '\n' + ' ' * state['ident']
    elif match(par1, 'case_default') and is_literal and node.upper() == 'ELSE':
        pre = '\n' + ' ' * state['ident']

    # literals
    elif is_literal and node.upper() in NEWLINE_KEYWORDS:
        pre = '\n' + ' ' * state['ident']
        state['nobreak_after'] = True
    elif is_literal:
        pre += br

    if is_literal:
        state['nobreak_after'] = node in NOBREAK_AFTER or '\n' in suf
        return FmtNode(pre + node + suf, True)

    return FmtNode((pre + suf) or None, False)


def fmt_placeholders(syntax_node, state):
    if hasattr(syntax_node, 'expr') and getattr(syntax_node, 'expr') == 'PARAM opt_indirection':
        return fmt_strip(':PARAM', state)
    else:
        return fmt_strip(syntax_node, state)


def fmt_const(syntax_node, state):
    from vertica_parser.analyzer import find_token
    if hasattr(syntax_node, 'name') \
            and getattr(syntax_node, 'name') in ('a_expr', 'b_expr', 'c_expr', 'd_expr') \
            and not find_token(syntax_node, 'columnref', 50):
        return fmt_strip(':CONST', state)
    else:
        return fmt_strip(syntax_node, state)


def format_traversal(syntax_node, chunks, fmt=fmt_strip, state=None):

    if state is None:
        state = {'path': list()}

    fmt_node, prevent_traverse = fmt(syntax_node, state)
    if fmt_node is not None:
        chunks.append(fmt_node)

    if not prevent_traverse:
        state['path'].append(syntax_node)
        for t in getattr(syntax_node, 'tokens', list()):
            format_traversal(t, chunks, fmt, state)
        state['path'].pop()


def format(query, fmt, filter=lambda n: (n,), parser=parser):
    syntax_tree = parser.parse(query, tracking=True)

    subqueries = set()
    for syntax_node in filter(syntax_tree):
        chunks = list()
        format_traversal(syntax_node, chunks, fmt)
        subqueries.add(''.join(chunks))

    subqueries = list(sorted(subqueries))
    Node = namedtuple('Node', ['name', 'expr', 'tokens'])
    res = Node('fmt', 'query ; query', [sep and ';' or q for q in subqueries for sep in range(2)][:-1])

    chunks = list()
    format_traversal(res, chunks, fmt)
    return ''.join(chunks)


orig_parse_select = analyzer.parse_select

def parse_select(syntax_node, query_node):
    if hasattr(syntax_node, 'name') and syntax_node.name == 'select_no_parens':
        query_node.select_container = syntax_node
    orig_parse_select(syntax_node, query_node)

analyzer.parse_select = parse_select


def unwrap_nested_selects(select_stmt):
    from vertica_parser.analyzer import list_from

    if select_stmt.cte_clauses:
        return [select_stmt.select_container]

    if len(select_stmt.simple_select_clauses) > 1:
        return [select_stmt.select_container]

    select_clause = select_stmt.simple_select_clauses[0]
    if not all([c.alias and c.alias.startswith('"') for c in select_clause.column_list]):
        return [select_stmt.select_container]

    node_list = list()
    for t in list_from(select_clause):
        if t.table_ref:
            node_list.append(t.table_ref or t.alias)
        elif t.select_clause:
            node_list += unwrap_nested_selects(t.select_clause)
    return set(node_list)


def select_unwrapper(syntax_node):
    for t in syntax_node.tokens:
        name = getattr(t, 'name', 'literal')
        if name in ('a_stmt', 'stmtblock', 'stmtmulti', 'stmt', 'VSelectStmt'):
            return select_unwrapper(t)
        elif name == 'SelectStmt':
            select_stmt = analyzer.SelectNode(analyzer.RootNode())
            analyzer.parse_select(syntax_node, select_stmt)
            return unwrap_nested_selects(select_stmt)
    return list()


def ddl_unwrapper(syntax_node):
    select_nodes = list()
    for t in syntax_node.tokens:
        name = getattr(t, 'name', 'literal')
        if name in ('a_stmt', 'stmtblock', 'stmtmulti', 'stmt',
                    'ViewStmt', 'CreateAsStmt', 'CreateStmt'):
            select_nodes += ddl_unwrapper(t)
        elif name in ('SelectStmt', 'VSelectStmt'):
            select_nodes.append(t)
    return select_nodes


if __name__ == '__main__':
    import io
    import sys

    with io.open(sys.argv[1], mode="r", encoding="utf-8") as ifile:
        query1 = ifile.read()

    # query2 = format(query1, fmt_const, select_unwrapper)
    # query2 = format(query1, fmt_strip, ddl_unwrapper)
    # query2 = format(query1, fmt_const)
    query2 = format(query1, fmt_multiline)
    print(query2)
    parser.parse(query2)