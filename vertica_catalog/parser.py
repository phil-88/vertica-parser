#!/usr/bin/python

import struct
from decimal import Decimal
from ply.lex import LexToken
from ply.lex import lex
import ply.yacc as yacc
from vertica_catalog.static import TYPE_OIDS, FUNC_OIDS, OP_OIDS

literals = [':', '.', '{', '}', '(', ')']
tokens = ('CAP', 'PROP', 'CONST', 'IDENT')

t_ignore = " \t"
t_CAP = r'[A-Z]{3,10}'
t_PROP = r':[a-zA-Z_][a-zA-Z0-9_]*'
t_CONST = r'(true|false|<>|-?[0-9]+)(\s+\[(\s*-?\d{1,3}\s*)*\])?'
t_IDENT = r'(\\\\"[^"]*"|[a-zA-Z_][a-zA-Z0-9_]*)\.("[^"]*"|[a-zA-Z_][a-zA-Z0-9_]*)'


def get_used_tokens():

    from types import ModuleType, FunctionType, CodeType
    import inspect
    import re

    def collect_strings(g, lvl=5):
        if lvl == 0:
            return []
        if isinstance(g, str):
            return [g]
        if isinstance(g, ModuleType):
            return []
        if isinstance(g, CodeType):
            g = g.co_consts
        if isinstance(g, FunctionType):
            for t in inspect.getmembers(g):
                if t[0] == '__code__':
                    g = t[1].co_consts
                    break
        if isinstance(g, dict):
            g = list(g.keys()) + list(g.values())

        try:
            res = []
            for c in g:
                res += collect_strings(c, lvl - 1)
            return res
        except TypeError:
            return []

    variables = filter(lambda v: v not in (FUNC_OIDS, OP_OIDS), globals().values())
    return [c for v in variables
              for c in collect_strings(v)
              if re.match(r'^[a-z0-9_]+$', c, re.I)]


class CatalogLexer(object):

    def __init__(self):
        self.lexdata = ''
        self.lexpos = 0
        self.lineno = 0

        self.lines = list()
        self.line_count = 0
        self.tokens = list()

        self.used_tokens = set(get_used_tokens())

    def input(self, content):
        self.lexdata = content
        self.lexpos = 0
        self.lineno = 0

        self.lines = content.splitlines(keepends=False)
        self.line_count = len(self.lines)
        self.tokens = list()

    def token(self):
        if self.tokens:
            return self.tokens.pop(0)

        token = None
        while not token:
            if self.lineno >= self.line_count:
                return None

            line = self.lines[self.lineno]
            line_size = len(line)
            line = line.strip()

            if line in literals:
                token = LexToken()
                token.type = line
                token.value = line
                token.lineno = self.lineno
                token.lexpos = self.lexpos
            elif line.startswith('0x'):
                pass
            elif line.startswith(':'):
                cap = line[1:]
                skip = cap not in self.used_tokens and cap > ''

                if skip:
                    line = self.lines[self.lineno]
                    skip_break = line[:len(line) - len(line.lstrip())] + '.'
                    while skip:
                        line = self.lines[self.lineno]
                        skip = not line.startswith(skip_break)
                        self.lexpos += len(line) + 1
                        self.lineno += 1
                    continue

                token = LexToken()
                token.type = 'CAP'
                token.value = cap
                token.lineno = self.lineno
                token.lexpos = self.lexpos
            else:
                prop, _, value = line.partition(':')
                skip = prop not in self.used_tokens and prop > '' and value > ''

                if value and not skip:
                    token = LexToken()
                    token.type = 'CONST'
                    token.value = value
                    token.lineno = self.lineno
                    token.lexpos = self.lexpos + line_size - len(value)
                    self.tokens.append(token)
                if prop and not skip:
                    token = LexToken()
                    token.type = 'PROP'
                    token.value = prop
                    token.lineno = self.lineno
                    token.lexpos = self.lexpos

            self.lexpos += line_size + 1
            self.lineno += 1

        return token


def t_ANY_error(t):
    linepos = max(0, t.lexer.lexdata[:t.lexpos].rfind('\n'))
    print("line %d pos %d: Illegal character '%s'" %
          (t.lexer.lineno, t.lexer.lexpos - linepos, t.value[0]))
    t.lexer.skip(1)


def p_list(p):
    """list : list struct
            | struct """
    if isinstance(p[1], list):
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_struct(p):
    """struct : CAP pairs '.'
              | CAP '.' """
    if p[2] == '.':
        p[0] = {p[1]: {}}
    else:
        p[0] = {p[1]: p[2]}


def p_pairs(p):
    """pairs : pairs PROP value
             | PROP value """
    if isinstance(p[1], dict):
        p[1][p[2]] = p[3]
        p[0] = p[1]
    else:
        p[0] = {p[1]: p[2]}


def p_value(p):
    """value : '{' list '}'
             | '{' '}'
             | struct
             | CONST
             | """
    length = len(p)
    if length == 2:
        p[0] = p[1]
    elif length == 3:
        p[0] = []
    elif length == 4:
        p[0] = p[2]


def p_error(t):
    if t and hasattr(t, 'lexer'):
        linepos = max(0, t.lexer.lexdata[:t.lexpos].rfind('\n'))
        print("line %d pos %d: Syntax error as '%s'" %
              (t.lineno, t.lexpos - linepos, t.value))
    else:
        print("unexpected end of input")


def p_expr(p):
    r"""expr : '{' CAP expr_pairs '}' """
    p[0] = {p[2]: p[3]}


def p_expr_pairs(p):
    r"""expr_pairs : expr_pairs expr_pair
                   | expr_pair """
    if len(p) == 3:
        p[0] = p[2]
        p[0].update(p[1])
    elif len(p) == 2:
        p[0] = p[1]


def p_expr_pair(p):
    r"""expr_pair : PROP '(' expr_list ')'
                  | PROP expr
                  | PROP CONST
                  | PROP IDENT """
    if len(p) == 5:
        p[0] = {p[1]: p[3]}
    else:
        p[0] = {p[1]: p[2]}


def p_expr_list(p):
    r"""expr_list : expr_list expr
                  | expr """
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    elif len(p) == 2:
        p[0] = [p[1]]


def parse_const(c):
    oid = int(c[':consttype'])

    size, _, val = c[':constvalue'].partition(' ')
    size = int(size)
    val = bytes([int(v) & 0xff for v in val.strip('[]').split()])

    if oid == 6 and size == 8:
        return '%d' % struct.unpack("<Q", val)[0]
    if oid == 23 and size == 4:
        return '%d' % struct.unpack("<I", val[0:4])[0]
    elif oid == 16 and size == 16:
        return '%d' % struct.unpack("<Q", val[8:16])[0]
    elif oid == 16 and size == 24:
        i1 = Decimal(struct.unpack("<Q", val[8:16])[0])
        i2 = Decimal(struct.unpack("<Q", val[16:24])[0])
        return str(i1 * 2**64 + i2)
    elif oid in (4, 8, 9, 17, 115, 116, 117) and size >= 4:
        size = struct.unpack("<I", val[0:4])[0] - 4
        return "'%s'" % struct.unpack("%ds" % size, val[4:])[0].decode("utf-8").replace("'", "''")
    elif oid == 5:
        return 'true' if val[0] else 'false'

    return "'0'"


def parse_func(f, state):
    func = FUNC_OIDS.get(int(f[':funcid']), {})
    name = func.get('name', 'unknown')

    if f.get(':args', '<>') != '<>':
        args = [parse_expr(arg, state) for arg in f[':args']]
    else:
        args = []

    if func.get('parse_args'):
        args = func['parse_args'](args)

    fmt = f.get(':funcformat', '0')
    if fmt in ('1', '2'):
        expr = (args or ["null"])[0]
        args = args[1:]
        return '%s::%s' % (expr, name) + \
               ('(%s)' % ','.join(args) if args else '')
    else:
        return '%s(%s)' % (name, ', '.join(args))


def parse_op(op, state):
    o = OP_OIDS.get(int(op.get(':opno')), {})
    name = o.get('oprname', '?')
    args = [parse_expr(arg, state) for arg in op[':args']] if op[':args'] != '<>' else []

    tokens = []
    if o.get('oprleft', '0') != '0':
        tokens.append(args.pop(0))
    if name != '?':
        tokens.append(name)
    if o.get('oprright', '0') != '0':
        tokens.append(args.pop(0))

    return '( %s )' % ' '.join(tokens)


def parse_case(c, state):
    arg = c.get(':arg', '<>')
    if arg != '<>':
        res = ['CASE ' + parse_expr(arg, state)]
    else:
        res = ['CASE']

    args = c.get(':args')
    for a in args:
        branch = a.get('WHEN', {})
        e = parse_expr(branch.get(':expr'), state)
        r = parse_expr(branch.get(':result'), state)
        res.append('WHEN %s THEN %s' % (e, r))

    defresult = c.get(':defresult', '<>')
    if defresult != '<>':
        res.append('ELSE ' + parse_expr(defresult, state))

    return ' '.join(res + ['END'])


def parse_isnull(n, state):
    a = n.get(':arg', '<>')
    t = n.get(':nulltesttype', '<>')
    if a != '<>' and t != '<>':
        return parse_expr(a, state) + {'1': ' is not null', '0': ' is null'}.get(t)
    else:
        return ':isnull'


def parse_predicate(p, state):
    op = p.get(':boolop')
    args = p.get(':args')
    if op and args:
        return op.join([parse_expr(a, state) for a in args])
    return ':predicate'


def indirect_ident(n):
    m = re.match('^' + t_IDENT + '$', n)
    if m:
        return m.groups()[-1]
    return n


def parse_var(v, state):
    no = v[':varattno']
    cols = {c['attNum']: c['attName'] for c in state.get('columns', [])}
    return cols.get(no) or indirect_ident(v[':varname'])


def parse_expr(expr, state):

    if 'expr_lexer' not in state:
        lexer = lex()
        state['expr_lexer'] = lexer
    if 'expr_parser' not in state:
        parser = yacc.yacc(start='expr', check_recursion=False, write_tables=False, debug=False)
        state['expr_parser'] = parser

    syntax_tree = None
    if isinstance(expr, dict):
        syntax_tree = expr
    elif isinstance(expr, str):
        syntax_tree = state['expr_parser'].parse(expr, lexer=state['expr_lexer'])

    if not syntax_tree:
        return "'0'"

    if syntax_tree.get('VAR'):
        return parse_var(syntax_tree['VAR'], state)
    elif syntax_tree.get('CONST'):
        return parse_const(syntax_tree['CONST'])
    elif syntax_tree.get('FUNCEXPR'):
        return parse_func(syntax_tree['FUNCEXPR'], state)
    elif syntax_tree.get('OPEXPR'):
        return parse_op(syntax_tree['OPEXPR'], state)
    elif syntax_tree.get('CASE'):
        return parse_case(syntax_tree['CASE'], state)
    elif syntax_tree.get('NULLTEST'):
        return parse_isnull(syntax_tree['NULLTEST'], state)
    elif syntax_tree.get('BOOLEXPR'):
        return parse_predicate(syntax_tree['BOOLEXPR'], state)

    return ":expr"


def format_column(c, state):
    if c.get('attIsIdentity') == 'true':
        return '"%s" IDENTITY' % c['attName']

    t = c['dataType']['DataType']
    type = TYPE_OIDS.get(int(t['typeoid']))
    if not type:
        typename = 'varchar'
    elif callable(type[1]):
        typename = type[1](t)
    else:
        typename = type[0]

    modifiers = []
    if c.get('attHasDef') == 'true':
        modifiers.append("DEFAULT %s" % parse_expr(c['defaultValue'], state))
    if c.get('attHasSetUsing') == 'true':
        modifiers.append("SET USING %s" % parse_expr(c['setUsingValue'], state))
    if c.get('attNotNull') == 'true':
        modifiers.append("NOT NULL")

    return '"%s"\t%s' % (c['attName'], '\t'.join([typename] + modifiers))


def escape_ident(n):
    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', n):
        return n
    return '"' + n.replace(r'"', r'\"') + '"'


def read_drop_commit(stmt, obj_type, state, ddl):
    commit = stmt.get('CommitRecord', {})
    for obj in commit.get('droppedObjects', []):
        oid = obj['uint64']['_']
        if oid in state['ind']:
            ddl[state['ind'][oid]] = ''
        elif oid in state[obj_type]:
            ddl.append('drop {} if exists {} cascade;'.format(obj_type, state[obj_type][oid]))


def view_relation_exists(rel, state):
    i = rel['ViewRelationInfo']
    n = state['schema'].get(i['relationNameSpaceId'], 'public') + '.' + i['relationName']
    return n in state['valid_relations']


def read_catalog_file(path, state=None, ddl=None):
    lexer = CatalogLexer()
    parser = yacc.yacc(check_recursion=False, write_tables=False, debug=False)

    if path.endswith('.gz'):
        import gzip
        with gzip.open(path, 'r') as ifile:
            content = ifile.read().decode('utf-8', errors='ignore')
    else:
        with open(path, mode='r', newline='\n', encoding='ascii', errors='ignore') as ifile:
            content = ifile.read()

    content = re.sub("[\x0d\x0c\x0b\x1c\x1d\x1e\x85\u2028\u2029]", "", content)

    syntax_tree = parser.parse(content, lexer=lexer)
    incomplete = list()

    if ddl is None:
        ddl = []
    if not syntax_tree:
        return ddl
    if state is None:
        state = {}
    state.setdefault('schema', {})
    state.setdefault('sequence', {})
    state.setdefault('table', {})
    state.setdefault('view', {})
    state.setdefault('ind', {})
    state.setdefault('valid_relations', set())
    state.setdefault('incomplete', list())

    for stmt in syntax_tree:
        read_drop_commit(stmt, 'schema', state, ddl)

        schema = stmt.get('Schema')
        if not schema:
            continue
        if schema.get('isSys') == 'true':
            continue

        name = escape_ident(schema['name'])
        state['schema'][schema['oid']] = name
        ddl.append("create schema if not exists {};".format(name))

    for stmt in syntax_tree + state['incomplete']:
        read_drop_commit(stmt, 'sequence', state, ddl)

        seq = stmt.get('Sequence')
        if not seq:
            continue
        if seq['table'] != '0':
            continue
        if seq['schema'] not in state['schema']:
            incomplete.append(stmt)
            continue

        state['sequence'][seq['oid']] = state['schema'][seq['schema']] + '.' + seq['name']

        stmt_ddl = "create sequence if not exists {schema}.{name};".format(
            schema=state['schema'][seq['schema']],
            name=seq['name']
        )

        if seq['oid'] in state['ind']:
            ddl[state['ind'][seq['oid']]] = stmt_ddl
        else:
            state['ind'][seq['oid']] = len(ddl)
            ddl.append(stmt_ddl)

    for stmt in syntax_tree + state['incomplete']:
        read_drop_commit(stmt, 'table', state, ddl)

        table = stmt.get('Table')
        if not table:
            continue
        if table.get('isSys') == 'true':
            continue
        if table.get('isTemp') == 'true':
            continue
        if table['schema'] not in state['schema']:
            incomplete.append(stmt)
            continue

        state['table'][table['oid']] = state['schema'][table['schema']] + '.' + table['name']
        columns = [a['Attribute'] for a in table['attributes'] if 'Attribute' in a][:-1]
        state['columns'] = columns

        partition = None
        if table.get('serializedPartitionExpr'):
            partition = parse_expr(table['serializedPartitionExpr'], state)

        stmt_ddl = "create table if not exists {schema}.{name}\n(\n {columns}\n)".format(
            schema=state['schema'][table['schema']],
            name=table['name'],
            columns=',\n '.join([format_column(c, state) for c in columns])
        ) + '\nunsegmented all nodes' \
          + (partition and '\npartition by ' + partition + ';' or ';')

        if table['oid'] in state['ind']:
            ddl[state['ind'][table['oid']]] = stmt_ddl
        else:
            state['ind'][table['oid']] = len(ddl)
            ddl.append(stmt_ddl)

    for stmt in syntax_tree + state['incomplete']:
        read_drop_commit(stmt, 'view', state, ddl)

        view = stmt.get('View')
        if not view:
            continue
        if view.get('isSys') == 'true':
            continue
        if view['schema'] not in state['schema']:
            incomplete.append(stmt)
            continue
        if any([not view_relation_exists(t, state) for t in view['viewViews']]):
            incomplete.append(stmt)
            continue

        state['view'][view['oid']] = state['schema'][view['schema']] + '.' + view['name']
        state['valid_relations'].add(state['schema'][view['schema']] + '.' + view['name'])

        stmt_ddl = "create or replace view {schema}.{name} as {query};".format(
            schema=state['schema'][view['schema']],
            name=view['name'],
            query=view['queryString'].replace(r'\\', '\\')
        )

        if view['oid'] in state['ind']:
            ddl[state['ind'][view['oid']]] = stmt_ddl
        else:
            state['ind'][view['oid']] = len(ddl)
            ddl.append(stmt_ddl)

    state['incomplete'] = incomplete
    return ddl


import os.path
import re


def get_number(filename):
    m = re.match(r'([^0-9]+)([0-9]+).+', filename)
    if m:
        return int(m.group(2))
    else:
        return -1


def stmt_priority(stmt_ddl):
    if stmt_ddl.startswith('create schema'):
        return 1
    if stmt_ddl.startswith('create sequence'):
        return 2
    if stmt_ddl.startswith('create table'):
        return 3
    if stmt_ddl.startswith('create or replace view'):
        return 4
    return 10


def read_catalog(path):
    chkpt_dir = os.path.join(path, 'Checkpoints')
    txn_dir = os.path.join(path, 'Txnlogs')

    completed = lambda d: os.path.isfile(os.path.join(chkpt_dir, d, 'completed'))
    last_chkpt = sorted(filter(completed, os.listdir(chkpt_dir)), key=get_number)[-1]
    commit = get_number(last_chkpt)

    chkpt_files = filter(lambda f: re.match(r'chkpt_[0-9]+\.cat\.gz', f),
                         os.listdir(os.path.join(chkpt_dir, last_chkpt)))
    txn_files = filter(lambda f: get_number(f) > commit, os.listdir(txn_dir))

    state = {}
    ddl = []
    for chkpt_file in sorted(chkpt_files, key=get_number):
        read_catalog_file(os.path.join(chkpt_dir, last_chkpt, chkpt_file), state, ddl)
    for txn_file in sorted(txn_files, key=get_number):
        read_catalog_file(os.path.join(txn_dir, txn_file), state, ddl)

    return sorted(ddl, key=stmt_priority)


if __name__ == '__main__':
    import sys

    if os.path.isdir(sys.argv[1]):
        ddl = read_catalog(sys.argv[1])
        print('\n\n'.join(ddl))
    elif os.path.isfile(sys.argv[1]):
        ddl = read_catalog_file(sys.argv[1])
        print('\n\n'.join(ddl))
    else:
        print('file not found')
