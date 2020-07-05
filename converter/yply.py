#!/usr/local/bin/python
# yply.py
#
# Author: David Beazley (dave@dabeaz.com)
# Date  : October 2, 2006
#
# Converts a UNIX-yacc specification file into a PLY-compatible
# specification.   To use, simply do this:
#
#   % python yply.py [-nocode] inputfile.y >myparser.py
#
# The output of this program is Python code. In the output,
# any C code in the original file is included, but is commented.
# If you use the -nocode option, then all of the C code in the
# original file is discarded.
#
# Disclaimer:  This just an example I threw together in an afternoon.
# It might have some bugs.  However, it worked when I tried it on
# a yacc-specified C++ parser containing 442 rules and 855 parsing
# states.
#

import sys
sys.path.insert(0, "../..")

import ylex
import yparse

from ply import *

if len(sys.argv) == 1:
    print("usage : yply.py [-nocode] inputfile")
    raise SystemExit

if len(sys.argv) == 3:
    if sys.argv[1] == '-nocode':
        yparse.emit_code = 0
    else:
        print("Unknown option '%s'" % sys.argv[1])
        raise SystemExit
    filename = sys.argv[2]
else:
    filename = sys.argv[1]

print("#!/usr/bin/python")
print("# -*- coding: utf-8 -*-")
print("")

yacc.parse(open(filename).read(), debug=False)

print("""


from ply import *
import sys
import io


def make_parser(trap_errors=False):
    lexer = lex.lex()
    if trap_errors:
        lexer.errors = list()
    parser = yacc.yacc()
    parser.lexer = lexer
    return parser


def print_expr(expr, no=1, level=1):
    if not getattr(expr, 'tokens', None):
        print(' ' * level, no, ' ', expr)
        return

    print (' ' * level, no, ' ', expr.name, '[', expr.expr, ']', ':', '(')
    for (i, t) in enumerate(expr.tokens):
        print_expr(t, i + 1, level + 1)
    print (' ' * level, no, ' ', ')')


def run_interactive():
    while 1:
        try:
            s = input('sql > ')
        except EOFError:
            break
        if not s:
            continue
        print_expr(yacc.parse(s))


if __name__ == '__main__':
    make_parser()

    if len(sys.argv) == 2:
        with io.open(sys.argv[1], mode="r", encoding="utf-8") as ifile:
            content = ifile.read()
            print_expr(yacc.parse(content))
    else:
        run_interactive()

""")

