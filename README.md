PLY based parser for vertica sql statements.

## Examples

Print syntax tree:
```
>>> from vertica_parser import parser, print_expr
>>> print_expr(parser.parse("select 1"))
```

Find all relations in a query:
```
>>> from vertica_parser import parser
>>> from vertica_parser.analyzer import find_all_tokens, stringify
>>> syntax_tree = parser.parse("select * from t1 join t2 using(id)")
>>> relations = find_all_tokens(syntax_tree, 'relation_expr')
>>> print ([stringify(rel) for rel in relations])
```

Format query:
```
>>> from vertica_parser.formatter import format, fmt_multiline
>>> query = """create table t1(id integer, dim varchar, cnt integer) 
... order by dim segmented by hash(id) all nodes; 
... select dim, sum(cnt) from t1 group by dim"""
>>> print (format(query, fmt_multiline))
```

Split statements:
```
>>> from vertica_parser.stmt_split import split_statements
>>> print (split_statements("select 1;select 2"))
```

Traverse analyzer tree:
```
>>> from vertica_parser import make_parser, parse_statement, RootNode, SelectNode
>>> from vertica_parser import InsertNode, UpdateNode, DeleteNode, CopyNode, CreateNode, CTASNode
>>> query = "create t2 as select * from t1; drop table t1;"
>>> parser = make_parser(trap_errors=True)
>>> syntax_tree = parser.parse(query, tracking=True)
>>>
>>> root = RootNode()
>>> parse_statement(syntax_tree, root)
>>> for i in range(len(root.statements)):
>>>     stmt = root.statements[i]
>>>     if isinstance(stmt, SelectNode):
>>>         # handle select
>>>     elif isinstance(stmt, (InsertNode, UpdateNode, DeleteNode, CopyNode)):
>>>         # handle dml
>>>     elif isinstance(stmt, (CreateNode, CTASNode)):
>>>         # handle ddl
```

Error handling:
```
>>> parser = make_parser(trap_errors=True)
>>> syntax_tree = parser.parse(query, tracking=True)
>>> if not syntax_tree:
>>>     raise SyntaxError('Unexpected end of input')
>>> elif parser.lexer.errors:
>>>     raise SyntaxError('Syntax error')
```
