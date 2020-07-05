PLY based parser for vertica sql statements.

Example:

```
>>> from vertica_parser import parser, print_expr
>>> print_expr(parser.parse("select 1"))
```

First run is extremly slow due to cache generating.

