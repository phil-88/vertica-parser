from .parser import make_parser, print_expr, error_list as parser_errors
from .catalog import DatabaseCatalog


class GlobalParser(object):
    instance = None

    def __getattr__(self, item):
        if not GlobalParser.instance:
            GlobalParser.instance = make_parser()
        return getattr(GlobalParser.instance, item)


parser = GlobalParser()
db_catalog = DatabaseCatalog()


from .analyzer import parse_statement, print_node, RootNode, \
    SelectNode, SimpleSelectNode, TableNode, JoinNode, \
    ColumnNode, ColumnDefNode, PredicateNode, \
    CreateNode, CTASNode, ViewNode, \
    InsertNode, UpdateNode, DeleteNode, CopyNode, ExplainNode

from .rewriter import rewrite_statement

__all__ = ['make_parser', 'parser', 'print_expr', 'parser_errors',
           'db_catalog', 'parse_statement', 'print_node',
           'RootNode', 'SelectNode', 'SimpleSelectNode', 'TableNode', 'JoinNode',
           'ColumnNode', 'ColumnDefNode', 'PredicateNode',
           'CreateNode', 'CTASNode', 'ViewNode',
           'InsertNode', 'UpdateNode', 'DeleteNode', 'CopyNode', 'ExplainNode',
           'rewrite_statement']
