# parser for Unix yacc-based grammars
#
# Author: David Beazley (dave@dabeaz.com)
# Date  : October 2, 2006

import re

import ylex
tokens = ylex.tokens

from ply import *

tokenlist = []
preclist = []

emit_code = 1
rulecount = 1


def p_yacc(p):
    '''yacc : defsection rulesection'''


def p_defsection(p):
    '''defsection : definitions SECTION
                  | SECTION'''
    p.lexer.lastsection = 1

    tokens_with_rules = ['SCONST', 'FCONST', 'BCONST', 'XCONST', 'ICONST',
                         'PARAM', 'TYPECAST', 'HINT_BEGIN', 'HINT_END', 'IDENT']

    keyword_dict = {(t[0:-2] if t.endswith('_P') else t): t
                    for t in set(tokenlist)
                    if re.match(r'^[A-Z_]+$', t) and t not in tokens_with_rules}

    print("tokens = ", repr(list(set(tokenlist + ['IDENT']))))
    print("")

    print("keywords = ", repr(keyword_dict))
    print("")

    print("literals = [';', ',', '!', '*', '[', '=', '-', '/', '|', '%', ')', ']', '<', '(', '^', '+', '>', '.']")
    print("")

    print("t_ignore = ' \\t'")
    print("")
    print("")

    print("error_list = list()")
    print("")
    print("")

    print("def t_comment_ignore(t):")
    print("    r'[-][-][^\\n]*'")
    print("")
    print("")

    print("def t_TYPECAST(t):")
    print("    r'::[!]?'")
    print("    t.type = 'TYPECAST'")
    print("    return t")
    print("")
    print("")

    print("def t_FCONST_1(t):")
    print("    r'[0-9]*[.][0-9]+([Ee][-+]?[0-9]+)?'")
    print("    t.type = 'FCONST'")
    print("    return t")
    print("")
    print("")

    print("def t_FCONST_2(t):")
    print("    r'[0-9]+[.]([Ee][-+]?[0-9]+)?'")
    print("    t.type = 'FCONST'")
    print("    return t")
    print("")
    print("")

    print("def t_FCONST_3(t):")
    print("    r'[0-9]+([Ee][-+]?[0-9]+)'")
    print("    t.type = 'FCONST'")
    print("    return t")
    print("")
    print("")

    print("def t_ICONST_1(t):")
    print("    r'0[xX][0-9a-fA-F][0-9a-fA-F]*'")
    print("    t.type = 'ICONST'")
    print("    return t")
    print("")
    print("")

    print("def t_ICONST_2(t):")
    print("    r'[0-9][0-9]*'")
    print("    t.type = 'ICONST'")
    print("    return t")
    print("")
    print("")

    print("def t_PARAM_1(t):")
    print("    r'[\\\\][0-9][0-9]*'")
    print("    t.type = 'PARAM'")
    print("    return t")
    print("")
    print("")

    print("def t_PARAM_2(t):")
    print("    r'<\[[^\]]*\](\.\[[^\]]*\])*>'")
    print("    t.type = 'PARAM'")
    print("    return t")
    print("")
    print("")

    print("def t_PARAM_3(t):")
    print("    r':[a-zA-Z_][a-zA-Z_0-9]*'")
    print("    t.type = 'PARAM'")
    print("    return t")
    print("")
    print("")

    print("def t_BCONST(t):")
    print("    r\"[bB]('[^']*')+\"")
    print("    t.type = 'BCONST'")
    print("    return t")
    print("")
    print("")

    print("def t_XCONST(t):")
    print("    r\"[xX]('[^']*')+\"")
    print("    t.type = 'XCONST'")
    print("    return t")
    print("")
    print("")

    print("def t_SCONST_1(t):")
    print("    r\"[eE]'([^'\\\\]|\\\\.)*'\"")
    print("    t.type = 'SCONST'")
    print("    return t")
    print("")
    print("")

    print("def t_SCONST_2(t):")
    print("    r\"('[^']*')+\"")
    print("    t.type = 'SCONST'")
    print("    return t")
    print("")
    print("")

    print("def t_SCONST_3(t):")
    print("    r\"[$][$]((?![$][$]).)*[$][$]\"")
    print("    t.type = 'SCONST'")
    print("    return t")
    print("")
    print("")

    print("def t_IDENT_1(t):")
    print("    r'[a-zA-Z_][a-zA-Z_0-9]*'")
    print("    t.type = keywords.get(t.value.upper(), 'IDENT')")
    print("    return t")
    print("")
    print("")

    print("def t_IDENT_2(t):")
    print("    r'\"[^\"]+\"'")
    print("    t.type = 'IDENT'")
    print("    return t")
    print("")
    print("")

    print("def t_Op_Cmp(t):")
    print("    r'(<=>|[=<>!]=|<>)'")
    print("    t.type = 'Op_Cmp'")
    print("    return t")
    print("")
    print("")

    print("def t_Op_SS(t):")
    print("    r'//'")
    print("    t.type = 'Op_SS'")
    print("    return t")
    print("")
    print("")

    print("def t_Op_1(t):")
    print("    r'(<<|>>|\|\|/|\|\||\|/|!!|~[*]|~[~#][*]?|!~[~#][*]?)'")
    print("    t.type = 'Op'")
    print("    return t")
    print("")
    print("")

    print("def t_Op_2(t):")
    print("    r'[\|\&\#\~\!\@]'")
    print("    t.type = 'Op'")
    print("    return t")
    print("")
    print("")

    print("def t_HINT_BEGIN(t):")
    print("    r'[/][*]\s*[+]'")
    print("    t.type = 'HINT_BEGIN'")
    print("    return t")
    print("")
    print("")

    print("def t_HINT_END(t):")
    print("    r'[*][/]'")
    print("    t.type = 'HINT_END'")
    print("    return t")
    print("")
    print("")

    print("states = (")
    print("    ('multilinecomment', 'exclusive'),")
    print(")")
    print("")
    print("")

    print("def t_multilinecommentstart(t):")
    print("    r'/\*\s*[^+]'")
    print("    t.lexer.begin('multilinecomment')")
    print("")
    print("")

    print("def t_multilinecomment_end(t):")
    print("    r'\*/'")
    print("    t.lexer.begin('INITIAL')")
    print("")
    print("")

    print("def t_multilinecomment_newline(t):")
    print("    r'\\n'")
    print("    t.lexer.lineno += len(t.value)")
    print("")
    print("")

    print("def t_multilinecomment_content(t):")
    print("    r'((?![*][/]).)+'")
    print("")
    print("")

    print("def t_multilinecomment_error(t):")
    print("    return t_error(t)")
    print("")
    print("")

    print("t_multilinecomment_ignore = t_ignore")
    print("")
    print("")

    print("def t_newline(t):")
    print("    r'\\n+'")
    print("    t.lexer.lineno += len(t.value)")
    print("")
    print("")

    print("def t_error(t):")
    print("    errors = getattr(t.lexer, 'errors', error_list)")
    print("    linepos = max(0, t.lexer.lexdata[:t.lexpos].rfind('\\n'))")
    print("    errors.append(\"line %d pos %d: Illegal character '%s'\" %")
    print("                  (t.lexer.lineno, t.lexer.lexpos - linepos, t.value[0]))")
    print("    print(errors[-1])")
    print("    t.lexer.skip(1)")
    print("")
    print("")

    print("precedence = ", repr(preclist))
    print("")
    print("# -------------- RULES ----------------")
    print("")
    print("")

    print("def p_error(t):")
    print("    if t is not None:")
    print("        errors = getattr(t.lexer, 'errors', error_list)")
    print("        linepos = max(0, t.lexer.lexdata[:t.lexpos].rfind('\\n'))")
    print("        errors.append(\"line %d pos %d: Illegal character '%s'\" %")
    print("                      (t.lineno, t.lexpos - linepos, t.value))")
    print("        print(errors[-1])")
    print("        t.lexer.skip(1)")
    print("    else:")
    print("        error_list.append(\"Unexpected end of input\")")
    print("        print(error_list[-1])")
    print("")
    print("")

    print("class Expr:")
    print("    def __init__(self, name, expr, tokens, token):")
    print("        self.name = name")
    print("        self.expr = expr")
    print("        self.tokens = tokens")
    print("        self.line = token.lineno(0)")
    print("        self.pos = token.lexpos(0)")
    print("")
    print("")


def p_rulesection(p):
    '''rulesection : rules SECTION'''

    print("def p_CopyFromStaging(p):")
    print("    '''a_stmt : COPY FROM IDENT SCONST'''")
    print("    p[0] = Expr('a_stmt', 'COPY FROM IDENT SCONST', p[1:] if len(p or []) > 1 else [], p)")
    print("")
    print("")
    print("# -------------- RULES END ----------------")
    print_code(p[2], 0)


def p_definitions(p):
    '''definitions : definitions definition
                   | definition'''


def p_definition_literal(p):
    '''definition : LITERAL'''
    print_code(p[1], 0)


def p_definition_start(p):
    '''definition : START ID'''
    print("start = '%s'" % p[2])


def p_definition_token(p):
    '''definition : toktype opttype idlist optsemi '''
    t = []
    for i in p[3]:
        if i[0] not in "'\"":
            tokenlist.append(i)
            t.append(i)
        else:
            t.append(i[1:-1])
    if p[1] == '%left':
        preclist.append(('left',) + tuple(t))
    elif p[1] == '%right':
        preclist.append(('right',) + tuple(t))
    elif p[1] == '%nonassoc':
        preclist.append(('nonassoc',) + tuple(t))


def p_toktype(p):
    '''toktype : TOKEN
               | LEFT
               | RIGHT
               | NONASSOC'''
    p[0] = p[1]


def p_opttype(p):
    '''opttype : '<' ID '>'
               | empty'''


def p_idlist(p):
    '''idlist  : idlist optcomma tokenid
               | tokenid'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1]
        p[1].append(p[3])


def p_tokenid(p):
    '''tokenid : ID 
               | ID NUMBER
               | QLITERAL
               | QLITERAL NUMBER'''
    p[0] = p[1]


def p_optsemi(p):
    '''optsemi : ';'
               | empty'''


def p_optcomma(p):
    '''optcomma : ','
                | empty'''


def p_definition_type(p):
    '''definition : TYPE '<' ID '>' namelist optsemi'''
    # type declarations are ignored


def p_namelist(p):
    '''namelist : namelist optcomma ID
                | ID'''


def p_definition_union(p):
    '''definition : UNION CODE optsemi'''
    # Union declarations are ignored


def p_rules(p):
    '''rules   : rules rule
               | rule'''
    if len(p) == 2:
        rule = p[1]
    else:
        rule = p[2]

    # Print out a Python equivalent of this rule

    embedded = []      # Embedded actions (a mess)
    embed_count = 0

    rulename = rule[0]
    #rulecount = 1
    global rulecount
    for r in rule[1]:
        # r contains one of the rule possibilities
        print("def p_%s_%d(p):" % (rulename, rulecount))
        prod = []
        prodcode = ""
        for i in range(len(r)):
            item = r[i]
            if item[0] == '{':    # A code block
                if i == len(r) - 1:
                    prodcode = item
                    break
                else:
                    # an embedded action
                    embed_name = "_embed%d_%s" % (embed_count, rulename)
                    prod.append(embed_name)
                    embedded.append((embed_name, item))
                    embed_count += 1
            else:
                prod.append(item)
        print('''    """%s : %s"""''' % (rulename, " ".join(prod)))
        # Emit code
        print_code(prodcode, 4)
        print('''    p[0] = Expr("""%s""", """%s""", p[1:] if len(p or []) > 1 else [], p)''' %
              (rulename, " ".join(prod)))
        print()
        print()
        rulecount += 1

    for e, code in embedded:
        print("def p_%s(p):" % e)
        print("    '''%s : '''" % e)
        print_code(code, 4)
        print()
        print()


def p_rule(p):
    '''rule : ID ':' rulelist ';' '''
    p[0] = (p[1], [p[3]])


def p_rule2(p):
    '''rule : ID ':' rulelist morerules ';' '''
    p[4].insert(0, p[3])
    p[0] = (p[1], p[4])


def p_rule_empty(p):
    '''rule : ID ':' ';' '''
    p[0] = (p[1], [[]])


def p_rule_empty2(p):
    '''rule : ID ':' morerules ';' '''

    p[3].insert(0, [])
    p[0] = (p[1], p[3])


def p_morerules(p):
    '''morerules : morerules '|' rulelist
                 | '|' rulelist
                 | '|'  '''

    if len(p) == 2:
        p[0] = [[]]
    elif len(p) == 3:
        p[0] = [p[2]]
    else:
        p[0] = p[1]
        p[0].append(p[3])

#   print("morerules", len(p), p[0])


def p_rulelist(p):
    '''rulelist : rulelist ruleitem
                | ruleitem'''

    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1]
        p[1].append(p[2])


def p_ruleitem(p):
    '''ruleitem : ID
                | QLITERAL
                | CODE
                | PREC'''
    p[0] = p[1]


def p_empty(p):
    '''empty : '''


def p_error(p):
    pass


yacc.yacc(debug=0)


def print_code(code, indent):
    if not emit_code:
        return
    codelines = code.splitlines()
    for c in codelines:
        print("%s# %s" % (" " * indent, c))
