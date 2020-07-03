#!/usr/bin/python
# -*- coding: utf-8 -*-


class DatabaseCatalog(object):

    def __init__(self):
        self.table_columns = dict()
        self.transform_functions = set()

    def load(self, credits):
        import vertica_python
        with vertica_python.connect(**credits) as con:
            cursor = con.cursor('dict')

            cursor.execute("""
                select table_schema, table_name, column_name
                from v_catalog.columns
                union all
                select max(table_schema) over(partition by projection_id),
                    projection_name, projection_column_name
                from v_catalog.projection_columns
                union all
                select table_schema, table_name, column_name
                from v_catalog.view_columns
                """)

            for row in cursor.fetchall():
                table_name = (row['table_schema'] + '.' + row['table_name']).lower()
                self.table_columns.setdefault(table_name, list()).append(row['column_name'].lower())

            cursor.execute("""
                select schema_name, function_name
                from v_catalog.user_functions
                where procedure_type = 'User Defined Transform'
                """)

            for row in cursor.fetchall():
                func_name = (row['schema_name'] + '.' + row['function_name']).lower()
                self.transform_functions.add(func_name)

