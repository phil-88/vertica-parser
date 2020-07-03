#!/usr/bin/python
# -*- coding: utf-8 -*-

tokens =  ['PASSWORD_LIFE_TIME', 'TEMP', 'TO', 'LOCK_P', 'ALSO', 'CLASS', 'LISTEN', 'PRECISION', 'REINDEX', 'TEMPLATE', 'BYTES', 'HCATALOG_DB', 'NOCREATEDB', 'AUTO_INC', 'AUTHENTICATION', 'DEC', 'ELSE', 'CHARACTERISTICS', 'WHERE', 'UPDATE', 'LESS', 'NCHAR', 'PLACING', 'PASSWORD_MIN_SYMBOLS', 'WITH', 'AS', 'EXCEPTION', 'INCLUDE', 'ESCAPE', 'HCATALOG_USER', 'CHARACTER', 'RESOURCE', 'RESTRICT', 'CLUSTER', 'BACKWARD', 'ANALYTIC', 'HINT_END', 'IMPLICIT_P', 'FORCE', 'HCATALOG_SLOW_TRANSFER_TIME', 'COMPLEX', 'EVENTS_P', 'INTERSECT', 'HOUR_P', 'INSENSITIVE', 'TRUSTED', 'YEAR_P', 'EXISTS', 'ICONST', 'CAST', 'METHOD', 'ISNULL', 'PRIOR', 'VERTICA', 'EXCLUDING', 'NODES', 'CHARACTERS', 'TRIGGER', 'NULL_P', 'TIMESTAMP', 'RAW', 'FALSE_P', 'NOTNULL', 'BRANCH', 'NUMBER_P', 'UNLOCK_P', 'AVAILABLE', 'DATETIME', 'IN_P', 'STABLE', 'PATH', 'RUNTIMEPRIORITY', 'OF', 'VALINDEX', 'BIGINT', 'NULLAWARE', 'PREPASS', 'FORMAT', 'SELECT', 'ZSTD_COMP', 'DEFAULT', 'LOAD', 'READ', 'FULL', 'CURSOR', 'UNI', 'MODE', 'INOUT', 'PARAM', 'REPLACE', 'SAVE', 'SECOND_P', 'INTERPOLATE', 'PSDATE', 'SOURCE', 'EXECUTE', 'DESC', 'OVERLAY', 'DEFERRABLE', 'LANGUAGE', 'SCONST', 'ERROR_P', 'CHAIN', 'EXECUTIONPARALLELISM', 'MAXQUERYMEMORYSIZE', 'DIRECTED', 'DROP', 'INTERVAL', 'IMMUTABLE', 'MAXPAYLOAD', 'CORRELATION', 'OLD', 'EXCLUDE', 'PROFILE', 'MINUTE_P', 'INCLUDING', 'BEGIN_P', 'SECURITY', 'HAVING', 'BALANCE', 'CHECKPOINT', 'RESULTS', 'FAULT', 'HOSTNAME', 'TIMESTAMPTZ', 'CASE', 'EXTERNAL', 'USING', 'FOREIGN', 'EXCLUSIVE', 'FOR', 'ROUTE', 'HCATALOG_SCHEMA', 'SERIALIZABLE', 'HIGH', 'CACHE', 'WRITE', 'OVER', 'DISABLE', 'ANALYZE', 'LOCALTIME', 'RENAME', 'PASSWORD_REUSE_TIME', 'HOLD', 'CASCADE', 'PASSWORD', 'CUSTOM_PARTITIONS', 'SYSTEM', 'TIMESERIES', 'ILIKE', 'REFRESH', 'DURABLE', 'BROADCAST', 'RUNTIMETHRESHOLD', 'SPLIT', 'TYPECAST', 'Op_Cmp', 'GRACEPERIOD', 'TIMESTAMPDIFF', 'RESET', 'CUSTOM', 'USAGE', 'PASSWORD_MIN_LOWERCASE_LETTERS', 'ROUTING', 'RECOVER', 'ACCESS', 'UNPACKER', 'QUOTE', 'TRANSFORM', 'CURRENT_SCHEMA', 'PREVIOUS_P', 'HCATALOG_SLOW_TRANSFER_LIMIT', 'FUNCTIONS', 'MANAGED', 'PARAMETER', 'EVENT_P', 'RELEASE', 'SUBSTRING', 'VIEW', 'PLANNEDCONCURRENCY', 'SAVEPOINT', 'EPOCH_P', 'PRESERVE', 'UNBOUNDED', 'NETWORK', 'MATCHED', 'AUTO', 'COMMITTED', 'PROCEDURE', 'MAXCONCURRENCYGRACE', 'FLOAT_P', 'ADMIN', 'RANDOM', 'ENABLE', 'PROJECTIONS', 'SECONDS_P', 'RLE', 'INT_P', 'CATALOGPATH', 'HANDLER', 'MERGEOUT', 'COMMONDELTA_COMP', 'OVERLAPS', 'UNCOMMITTED', 'INITIALLY', 'OR', 'SEMIALL', 'REMOVE', 'INVOKER', 'BZIP_COMP', 'SUBNET', 'PASSWORD_GRACE_TIME', 'pg_vbool', 'VOLATILE', 'DISCONNECT', 'DELIMITER', 'MONTH_P', 'ROLE', 'MILLISECONDS_P', 'IDENTITY_P', 'ADDRESS', 'EXPIRE', 'LIBRARY', 'ENCODED', 'RETURN', 'ENFORCELENGTH', 'CONTROL', 'ROLES', 'INTEGER', 'NOTIFIER', 'DOMAIN_P', 'SCHEMA', 'LEVEL', 'IF_P', 'UNKNOWN', 'SIMILAR', 'ADD', 'DAY_P', 'DEFAULTS', 'PARQUET', 'UMINUS', 'EXTRACT', 'MATCH', 'CREATEUSER', 'POLICY', 'DELTARANGE_COMP_SP', 'WORK', 'HCATALOG_CONNECTION_TIMEOUT', 'SHOW', 'MAXCONNECTIONS', 'PASSWORD_MIN_LETTERS', 'CLEAR', 'NO', 'PASSWORD_MIN_DIGITS', 'DELIMITERS', 'DISABLED', 'BETWEEN', 'TRICKLE', 'FREEZE', 'CURRENT_TIME', 'NOTIFY', 'MODEL', 'DEALLOCATE', 'EXCEPT', 'vmem', 'TABLESAMPLE', 'MAXCONCURRENCY', 'SKIP', 'TREAT', 'NONE', 'AGGREGATE', 'VARYING', 'DEFINER', 'EACH', 'CHAR_LENGTH', 'CURRENT_USER', 'GLOBAL', 'ABORT_P', 'ANALYSE', 'TEMPORARY', 'STRICT_P', 'STATEMENT', 'SIMPLE', 'TIME', 'MONEY', 'TABLE', 'EPHEMERAL', 'WINDOW', 'INHERITS', 'EXTEND', 'MAXMEMORYSIZE', 'KEY', 'IS', 'VALIDATE', 'LOCALTIMESTAMP', 'LARGE_P', 'RULE', 'REVOKE', 'SOFTTYPECAST', 'Op', 'DATAPATH', 'REJECTMAX', 'PROCEDURAL', 'WITHIN', 'COMMUNAL', 'BLOCK_DICT', 'INTERFACE', 'REPEATABLE', 'FCONST', 'SSL_CONFIG', 'CURRENT_TIMESTAMP', 'INSERT', 'INDEX', 'FLEX', 'VALUE_P', 'XCONST', 'FILESYSTEM', 'PREPARE', 'DATABASE', 'LATEST', 'IMMEDIATE', 'NEXT', 'SMALLINT', 'GRANT', 'SETS', 'TRIM', 'HINT_BEGIN', 'RIGHT', 'TIMESTAMPADD', 'LIKE', 'OPERATOR', 'END_P', 'OWNER', 'REFERENCES', 'VERBOSE', 'LOCATION', 'BEST', 'TRUNCATE', 'NATURAL', 'LIMIT', 'CHARACTER_LENGTH', 'LEADING', 'THEN', 'PERMANENT', 'DOUBLE_P', 'USER', 'BOTH', 'OPTVER', 'PRIMARY', 'POOL', 'UNINDEXED', 'ROWS', 'ival1', 'DELTAVAL', 'PRIVILEGES', 'TOKENIZER', 'PINNED', 'TUNING', 'ISOLATION', 'LANCOMPILER', 'NOWAIT', 'Op_SS', 'ENCODING', 'ZSTD_HIGH_COMP', 'ALL', 'IDLESESSIONTIMEOUT', 'STDOUT', 'AT', 'LAST_P', 'WHEN', 'BEFORE', 'FORWARD', 'FETCH', 'ENABLED', 'SCROLL', 'FLEXIBLE', 'PARTITION', 'ASC', 'OBJECT_P', 'CONSTRAINTS', 'STORAGE', 'FILLER', 'PARTIAL', 'OPTIMIZER', 'HOURS_P', 'ORDER', 'COPY', 'MINVALUE', 'SHARED', 'GROUPED', 'AUTHORIZATION', 'START', 'UNCOMPRESSED', 'COLLATE', 'CROSS', 'CYCLE', 'ANNOTATED', 'WITHOUT', 'CUBE', 'REAL', 'BOOLEAN_P', 'TOAST', 'WEBSERVICE_PORT', 'DECIMAL_P', 'ONLY', 'PARAMETERS', 'CHECK', 'SEARCH_PATH', 'MATERIALIZE', 'UNION', 'NATIVE', 'vpath', 'TRUE_P', 'ACCOUNT', 'ZSTD_FAST_COMP', 'BLOCKDICT_COMP', 'FUNCTION', 'INSTEAD', 'PRIORITY', 'PORT', 'IDENT', 'TERMINATOR_P', 'GROUPING', 'HCATALOG', 'DIRECTGROUPED', 'BLOCK', 'ACTION', 'TLS', 'REJECTED_P', 'CSV', 'NAME_P', 'NULLCOLS', 'PASSWORD_REUSE_MAX', 'TINYINT', 'SYSID', 'NOTHING', 'STANDBY', 'ROLLBACK_P', 'PASSWORD_LOCK_TIME', 'FILTER', 'DEFINE', 'ILIKEB', 'CREATEDB', 'RECURSIVE', 'TRANSACTION', 'CURRENT_DATE', 'QUERY', 'UNLISTEN', 'VARCHAR', 'SOME', 'TIMETZ', 'RECORD_P', 'FROM', 'ENCLOSED', 'CHAR_P', 'VACUUM', 'ZSTD', 'COLUMN', 'AFTER', 'CLOSE', 'PERCENT', 'COLSIZES', 'TABLES', 'OTHERS', 'VALIDATOR', 'PARTITIONING', 'MEDIUM', 'REORGANIZE', 'CPUAFFINITYMODE', 'IGNORE', 'SEGMENTED', 'UNLIMITED', 'MERGE', 'TIES', 'PROJECTION', 'OCTETS', 'EXCEPTIONS', 'DISTINCT', 'SINGLEINITIATOR', 'STDIN', 'VALUES', 'UNIQUE', 'GZIP', 'INCREMENT', 'TEMPSPACECAP', 'SESSION', 'TOLERANCE', 'CONSTRAINT', 'DEFERRED', 'TEXT', 'OPTION', 'INTO', 'PARSER', 'MEMORYCAP', 'FAILED_LOGIN_ATTEMPTS', 'NUMERIC', 'COMMIT', 'SHARE', 'VARCHAR2', 'ANY', 'IDENTIFIED', 'Iend_epoch', 'BYTEA', 'FOLLOWING', 'CURRENT_DATABASE', 'MEMORYSIZE', 'CPUAFFINITYSET', 'STEMMER', 'GCDDELTA', 'BY', 'HOST', 'FIRST_P', 'WAIT', 'DO', 'ROW', 'ASSERTION', 'NOT', 'ACCESSRANK', 'VARBINARY', 'RECHECK', 'OUTER_P', 'MOVE', 'CURRENT_P', 'SYSDATE', 'LZO', 'LIKEB', 'QUEUETIMEOUT', 'AND', 'MICROSECONDS_P', 'LABEL', 'PASSWORD_MIN_UPPERCASE_LETTERS', 'WEBHDFS_ADDRESS', 'JSON', 'BIT', 'CALLED', 'LOCAL', 'SET', 'MINUS', 'SEQUENCES', 'OFF', 'STREAM_P', 'DETERMINES', 'ORC', 'PRECEDING', 'PATTERN', 'PREFER', 'DATA_P', 'ENCRYPTED', 'INTERVALYM', 'UUID', 'BASENAME', 'RETURNREJECTED', 'GROUP_P', 'CREATE', 'PASSWORD_MAX_LENGTH', 'SMALLDATETIME', 'HIVESERVER2_HOSTNAME', 'TIMEZONE', 'ARRAY', 'DIRECTPROJ', 'GZIP_COMP', 'ACTIVATE', 'SEMI', 'enCodeType', 'ON', 'OPT', 'Istart_epoch', 'ABSOLUTE_P', 'LONG', 'SECURITY_ALGORITHM', 'DEPENDS', 'DELTARANGE_COMP', 'MASK', 'DATEDIFF', 'debug', 'SEQUENCE', 'DEACTIVATE', 'RESTART', 'OIDS', 'LOW', 'BINARY', 'STATISTICS', 'ROLLUP', 'EXPLAIN', 'FIXEDWIDTH', 'ASSIGNMENT', 'UDPARAMETER', 'KSAFE', 'DISTVALINDEX', 'EXPORT', 'GET', 'STRENGTH', 'ZONE', 'NULLSEQUAL', 'TRAILING', 'NATIONAL', 'BATCH', 'CONNECT', 'TYPE_P', 'COMMENT', 'WEBSERVICE_HOSTNAME', 'DECODE', 'SETOF', 'DECLARE', 'FENCED', 'BZIP', 'OFFSET', 'TLSMODE', 'MAXVALUE', 'BCONST', 'DIRECTCOLS', 'DELETE_P', 'JOIN', 'RUNTIMECAP', 'ANTI', 'NOCREATEUSER', 'RANGE', 'NODE', 'ALTER', 'NEW', 'INNER_P', 'UNSEGMENTED', 'NULLS', 'POSITION', 'TABLESPACE', 'OUT_P', 'LEFT', 'MINUTES_P', 'SESSION_USER', 'THAN', 'COLUMNS_COUNT', 'MOVEOUT', 'INPUT_P', 'ACTIVEPARTITIONCOUNT', 'UNIONJOIN', 'DIRECT', 'RELATIVE_P', 'PASSWORD_MIN_LENGTH']

keywords =  {'PASSWORD_LIFE_TIME': 'PASSWORD_LIFE_TIME', 'TO': 'TO', 'PATTERN': 'PATTERN', 'NEXT': 'NEXT', 'TEMP': 'TEMP', 'RETURNREJECTED': 'RETURNREJECTED', 'CLASS': 'CLASS', 'SMALLINT': 'SMALLINT', 'LISTEN': 'LISTEN', 'PRECISION': 'PRECISION', 'REINDEX': 'REINDEX', 'EPOCH': 'EPOCH_P', 'TEMPLATE': 'TEMPLATE', 'SETS': 'SETS', 'BYTES': 'BYTES', 'HCATALOG_DB': 'HCATALOG_DB', 'ENABLED': 'ENABLED', 'NOCREATEDB': 'NOCREATEDB', 'TRIM': 'TRIM', 'AUTO_INC': 'AUTO_INC', 'WHERE': 'WHERE', 'CHARACTERISTICS': 'CHARACTERISTICS', 'TIMESTAMPADD': 'TIMESTAMPADD', 'LIKE': 'LIKE', 'UPDATE': 'UPDATE', 'BEGIN': 'BEGIN_P', 'RECURSIVE': 'RECURSIVE', 'OPERATOR': 'OPERATOR', 'LESS': 'LESS', 'OCTETS': 'OCTETS', 'FORWARD': 'FORWARD', 'ZSTD': 'ZSTD', 'NCHAR': 'NCHAR', 'PLACING': 'PLACING', 'OWNER': 'OWNER', 'REFERENCES': 'REFERENCES', 'PASSWORD_MIN_SYMBOLS': 'PASSWORD_MIN_SYMBOLS', 'ALSO': 'ALSO', 'VERBOSE': 'VERBOSE', 'WITH': 'WITH', 'BEST': 'BEST', 'TRUNCATE': 'TRUNCATE', 'DEPENDS': 'DEPENDS', 'MONTH': 'MONTH_P', 'NATURAL': 'NATURAL', 'LIMIT': 'LIMIT', 'ROLLBACK': 'ROLLBACK_P', 'CHARACTER_LENGTH': 'CHARACTER_LENGTH', 'LEADING': 'LEADING', 'AS': 'AS', 'INCLUDE': 'INCLUDE', 'GRANT': 'GRANT', 'RESOURCE': 'RESOURCE', 'HCATALOG_USER': 'HCATALOG_USER', 'CHARACTER': 'CHARACTER', 'FIXEDWIDTH': 'FIXEDWIDTH', 'NAME': 'NAME_P', 'MEMORYCAP': 'MEMORYCAP', 'OPTVER': 'OPTVER', 'RESTRICT': 'RESTRICT', 'CLUSTER': 'CLUSTER', 'PRIMARY': 'PRIMARY', 'BACKWARD': 'BACKWARD', 'WEBHDFS_ADDRESS': 'WEBHDFS_ADDRESS', 'ANALYTIC': 'ANALYTIC', 'UDPARAMETER': 'UDPARAMETER', 'DELTAVAL': 'DELTAVAL', 'PRIVILEGES': 'PRIVILEGES', 'SYSID': 'SYSID', 'FORCE': 'FORCE', 'PINNED': 'PINNED', 'COMPLEX': 'COMPLEX', 'TUNING': 'TUNING', 'ISOLATION': 'ISOLATION', 'MAXCONCURRENCY': 'MAXCONCURRENCY', 'LANCOMPILER': 'LANCOMPILER', 'USAGE': 'USAGE', 'NOWAIT': 'NOWAIT', 'FIRST': 'FIRST_P', 'ENCODING': 'ENCODING', 'ZSTD_HIGH_COMP': 'ZSTD_HIGH_COMP', 'COMMIT': 'COMMIT', 'INSENSITIVE': 'INSENSITIVE', 'ALL': 'ALL', 'INPUT': 'INPUT_P', 'TRUSTED': 'TRUSTED', 'ANNOTATED': 'ANNOTATED', 'IDLESESSIONTIMEOUT': 'IDLESESSIONTIMEOUT', 'OBJECT': 'OBJECT_P', 'EXISTS': 'EXISTS', 'YEAR': 'YEAR_P', 'STDOUT': 'STDOUT', 'CAST': 'CAST', 'AT': 'AT', 'ACCESS': 'ACCESS', 'LOCAL': 'LOCAL', 'ISNULL': 'ISNULL', 'VERTICA': 'VERTICA', 'STEMMER': 'STEMMER', 'CONSTRAINTS': 'CONSTRAINTS', 'WHEN': 'WHEN', 'EXCLUDING': 'EXCLUDING', 'NODES': 'NODES', 'CHARACTERS': 'CHARACTERS', 'AGGREGATE': 'AGGREGATE', 'TRIGGER': 'TRIGGER', 'FETCH': 'FETCH', 'TIMESTAMP': 'TIMESTAMP', 'RAW': 'RAW', 'FLEXIBLE': 'FLEXIBLE', 'HOUR': 'HOUR_P', 'PARTITION': 'PARTITION', 'EVENTS': 'EVENTS_P', 'ASC': 'ASC', 'ANALYSE': 'ANALYSE', 'NOTNULL': 'NOTNULL', 'THAN': 'THAN', 'BRANCH': 'BRANCH', 'LAST': 'LAST_P', 'STORAGE': 'STORAGE', 'MINUS': 'MINUS', 'FILLER': 'FILLER', 'DEFINER': 'DEFINER', 'AVAILABLE': 'AVAILABLE', 'ABORT': 'ABORT_P', 'STABLE': 'STABLE', 'PATH': 'PATH', 'OPTIMIZER': 'OPTIMIZER', 'SEMI': 'SEMI', 'EXPORT': 'EXPORT', 'RIGHT': 'RIGHT', 'ORDER': 'ORDER', 'VALINDEX': 'VALINDEX', 'CURRENT_USER': 'CURRENT_USER', 'SHARED': 'SHARED', 'BIGINT': 'BIGINT', 'GROUPED': 'GROUPED', 'CONSTRAINT': 'CONSTRAINT', 'NULLAWARE': 'NULLAWARE', 'AUTHORIZATION': 'AUTHORIZATION', 'PREPASS': 'PREPASS', 'FORMAT': 'FORMAT', 'ZSTD_COMP': 'ZSTD_COMP', 'GET': 'GET', 'FUNCTIONS': 'FUNCTIONS', 'DEFAULT': 'DEFAULT', 'DATETIME': 'DATETIME', 'LOAD': 'LOAD', 'READ': 'READ', 'CUBE': 'CUBE', 'PRIOR': 'PRIOR', 'REAL': 'REAL', 'FULL': 'FULL', 'INCREMENT': 'INCREMENT', 'DIRECT': 'DIRECT', 'TOAST': 'TOAST', 'WEBSERVICE_PORT': 'WEBSERVICE_PORT', 'MILLISECONDS': 'MILLISECONDS_P', 'STDIN': 'STDIN', 'UNI': 'UNI', 'INNER': 'INNER_P', 'MODE': 'MODE', 'STREAM': 'STREAM_P', 'INOUT': 'INOUT', 'REPLACE': 'REPLACE', 'CHECKPOINT': 'CHECKPOINT', 'ONLY': 'ONLY', 'LARGE': 'LARGE_P', 'ZONE': 'ZONE', 'INTERPOLATE': 'INTERPOLATE', 'PSDATE': 'PSDATE', 'RESULTS': 'RESULTS', 'SEARCH_PATH': 'SEARCH_PATH', 'MATERIALIZE': 'MATERIALIZE', 'SOURCE': 'SOURCE', 'UNION': 'UNION', 'NATIVE': 'NATIVE', 'HOURS': 'HOURS_P', 'EXECUTE': 'EXECUTE', 'TRUE': 'TRUE_P', 'UNSEGMENTED': 'UNSEGMENTED', 'ZSTD_FAST_COMP': 'ZSTD_FAST_COMP', 'OVERLAY': 'OVERLAY', 'FUNCTION': 'FUNCTION', 'DEFERRABLE': 'DEFERRABLE', 'LANGUAGE': 'LANGUAGE', 'RUNTIMEPRIORITY': 'RUNTIMEPRIORITY', 'PRIORITY': 'PRIORITY', 'TOKENIZER': 'TOKENIZER', 'CHAIN': 'CHAIN', 'EXECUTIONPARALLELISM': 'EXECUTIONPARALLELISM', 'MICROSECONDS': 'MICROSECONDS_P', 'OF': 'OF', 'MAXQUERYMEMORYSIZE': 'MAXQUERYMEMORYSIZE', 'NATIONAL': 'NATIONAL', 'DIRECTED': 'DIRECTED', 'GROUPING': 'GROUPING', 'IMMEDIATE': 'IMMEDIATE', 'DROP': 'DROP', 'INTERVAL': 'INTERVAL', 'DIRECTGROUPED': 'DIRECTGROUPED', 'COPY': 'COPY', 'IMMUTABLE': 'IMMUTABLE', 'WITHOUT': 'WITHOUT', 'DAY': 'DAY_P', 'AND': 'AND', 'GROUP': 'GROUP_P', 'CREATEDB': 'CREATEDB', 'MINUTES': 'MINUTES_P', 'CSV': 'CSV', 'NULLCOLS': 'NULLCOLS', 'PASSWORD_REUSE_MAX': 'PASSWORD_REUSE_MAX', 'CORRELATION': 'CORRELATION', 'TINYINT': 'TINYINT', 'VALUES': 'VALUES', 'BEFORE': 'BEFORE', 'OLD': 'OLD', 'EXCLUDE': 'EXCLUDE', 'PROFILE': 'PROFILE', 'NOTHING': 'NOTHING', 'UUID': 'UUID', 'IGNORE': 'IGNORE', 'STANDBY': 'STANDBY', 'INCLUDING': 'INCLUDING', 'QUERY': 'QUERY', 'PASSWORD_LOCK_TIME': 'PASSWORD_LOCK_TIME', 'FILTER': 'FILTER', 'DEFINE': 'DEFINE', 'COMMENT': 'COMMENT', 'TLS': 'TLS', 'SECURITY': 'SECURITY', 'HAVING': 'HAVING', 'BALANCE': 'BALANCE', 'REJECTED': 'REJECTED_P', 'IDENTITY': 'IDENTITY_P', 'START': 'START', 'FAULT': 'FAULT', 'TIMETZ': 'TIMETZ', 'NOCREATEUSER': 'NOCREATEUSER', 'CURRENT_DATE': 'CURRENT_DATE', 'TRANSACTION': 'TRANSACTION', 'SCROLL': 'SCROLL', 'PERMANENT': 'PERMANENT', 'TIES': 'TIES', 'BOOLEAN': 'BOOLEAN_P', 'LOCATION': 'LOCATION', 'VACUUM': 'VACUUM', 'TIMESTAMPTZ': 'TIMESTAMPTZ', 'UNLISTEN': 'UNLISTEN', 'VARCHAR': 'VARCHAR', 'ELSE': 'ELSE', 'PREVIOUS': 'PREVIOUS_P', 'TERMINATOR': 'TERMINATOR_P', 'SELECT': 'SELECT', 'CASE': 'CASE', 'QUEUETIMEOUT': 'QUEUETIMEOUT', 'EXTERNAL': 'EXTERNAL', 'USING': 'USING', 'FOREIGN': 'FOREIGN', 'FROM': 'FROM', 'EXCLUSIVE': 'EXCLUSIVE', 'RANDOM': 'RANDOM', 'ROUTE': 'ROUTE', 'UNCOMPRESSED': 'UNCOMPRESSED', 'HOSTNAME': 'HOSTNAME', 'SERIALIZABLE': 'SERIALIZABLE', 'ANY': 'ANY', 'HIGH': 'HIGH', 'WINDOW': 'WINDOW', 'ENCRYPTED': 'ENCRYPTED', 'DECIMAL': 'DECIMAL_P', 'CACHE': 'CACHE', 'COLLATE': 'COLLATE', 'OVER': 'OVER', 'DISABLE': 'DISABLE', 'ANALYZE': 'ANALYZE', 'DOMAIN': 'DOMAIN_P', 'COLUMN': 'COLUMN', 'PROCEDURE': 'PROCEDURE', 'LOCALTIME': 'LOCALTIME', 'AFTER': 'AFTER', 'RENAME': 'RENAME', 'PERCENT': 'PERCENT', 'IF': 'IF_P', 'COMMITTED': 'COMMITTED', 'TABLES': 'TABLES', 'DIRECTPROJ': 'DIRECTPROJ', 'DECODE': 'DECODE', 'TLSMODE': 'TLSMODE', 'HOLD': 'HOLD', 'CASCADE': 'CASCADE', 'VALIDATOR': 'VALIDATOR', 'PASSWORD_MIN_LENGTH': 'PASSWORD_MIN_LENGTH', 'PASSWORD': 'PASSWORD', 'CUSTOM_PARTITIONS': 'CUSTOM_PARTITIONS', 'REORGANIZE': 'REORGANIZE', 'TIMESERIES': 'TIMESERIES', 'ILIKE': 'ILIKE', 'CPUAFFINITYMODE': 'CPUAFFINITYMODE', 'REFRESH': 'REFRESH', 'RELATIVE': 'RELATIVE_P', 'THEN': 'THEN', 'SEGMENTED': 'SEGMENTED', 'UNLIMITED': 'UNLIMITED', 'USER': 'USER', 'ACTION': 'ACTION', 'DURABLE': 'DURABLE', 'MERGE': 'MERGE', 'BROADCAST': 'BROADCAST', 'PROJECTION': 'PROJECTION', 'EVENT': 'EVENT_P', 'RUNTIMETHRESHOLD': 'RUNTIMETHRESHOLD', 'SPLIT': 'SPLIT', 'EXCEPTION': 'EXCEPTION', 'DISTINCT': 'DISTINCT', 'SOME': 'SOME', 'GRACEPERIOD': 'GRACEPERIOD', 'TIMESTAMPDIFF': 'TIMESTAMPDIFF', 'RESET': 'RESET', 'SINGLEINITIATOR': 'SINGLEINITIATOR', 'CUSTOM': 'CUSTOM', 'RECOVER': 'RECOVER', 'PASSWORD_MIN_LOWERCASE_LETTERS': 'PASSWORD_MIN_LOWERCASE_LETTERS', 'ROUTING': 'ROUTING', 'UNPACKER': 'UNPACKER', 'GZIP': 'GZIP', 'QUOTE': 'QUOTE', 'TRANSFORM': 'TRANSFORM', 'TEMPSPACECAP': 'TEMPSPACECAP', 'BLOCKDICT_COMP': 'BLOCKDICT_COMP', 'CURRENT_SCHEMA': 'CURRENT_SCHEMA', 'TOLERANCE': 'TOLERANCE', 'ENCLOSED': 'ENCLOSED', 'HCATALOG_SLOW_TRANSFER_LIMIT': 'HCATALOG_SLOW_TRANSFER_LIMIT', 'DEFERRED': 'DEFERRED', 'ESCAPE': 'ESCAPE', 'MANAGED': 'MANAGED', 'SESSION': 'SESSION', 'PARAMETER': 'PARAMETER', 'TEXT': 'TEXT', 'BOTH': 'BOTH', 'INTO': 'INTO', 'PARSER': 'PARSER', 'EXPLAIN': 'EXPLAIN', 'RELEASE': 'RELEASE', 'UNIONJOIN': 'UNIONJOIN', 'SUBSTRING': 'SUBSTRING', 'FAILED_LOGIN_ATTEMPTS': 'FAILED_LOGIN_ATTEMPTS', 'FOR': 'FOR', 'VIEW': 'VIEW', 'CURSOR': 'CURSOR', 'PLANNEDCONCURRENCY': 'PLANNEDCONCURRENCY', 'SAVEPOINT': 'SAVEPOINT', 'SHARE': 'SHARE', 'PRESERVE': 'PRESERVE', 'UNBOUNDED': 'UNBOUNDED', 'NETWORK': 'NETWORK', 'CPUAFFINITYSET': 'CPUAFFINITYSET', 'MEMORYSIZE': 'MEMORYSIZE', 'MATCHED': 'MATCHED', 'AUTO': 'AUTO', 'IDENTIFIED': 'IDENTIFIED', 'MAXCONCURRENCYGRACE': 'MAXCONCURRENCYGRACE', 'BYTEA': 'BYTEA', 'CURRENT': 'CURRENT_P', 'FOLLOWING': 'FOLLOWING', 'CURRENT_DATABASE': 'CURRENT_DATABASE', 'ADMIN': 'ADMIN', 'PARAMETERS': 'PARAMETERS', 'HCATALOG_SCHEMA': 'HCATALOG_SCHEMA', 'ENABLE': 'ENABLE', 'LZO': 'LZO', 'LOCK': 'LOCK_P', 'PROJECTIONS': 'PROJECTIONS', 'UNINDEXED': 'UNINDEXED', 'RLE': 'RLE', 'BY': 'BY', 'HOST': 'HOST', 'CATALOGPATH': 'CATALOGPATH', 'HANDLER': 'HANDLER', 'DO': 'DO', 'MERGEOUT': 'MERGEOUT', 'ROW': 'ROW', 'CHAR': 'CHAR_P', 'DESC': 'DESC', 'RANGE': 'RANGE', 'ASSERTION': 'ASSERTION', 'MINVALUE': 'MINVALUE', 'COMMONDELTA_COMP': 'COMMONDELTA_COMP', 'ROWS': 'ROWS', 'SAVE': 'SAVE', 'BLOCK': 'BLOCK', 'LEFT': 'LEFT', 'DOUBLE': 'DOUBLE_P', 'VARBINARY': 'VARBINARY', 'RECHECK': 'RECHECK', 'PARTITIONING': 'PARTITIONING', 'WAIT': 'WAIT', 'OVERLAPS': 'OVERLAPS', 'MOVE': 'MOVE', 'KSAFE': 'KSAFE', 'COLSIZES': 'COLSIZES', 'UNIQUE': 'UNIQUE', 'UNCOMMITTED': 'UNCOMMITTED', 'INITIALLY': 'INITIALLY', 'OR': 'OR', 'VALUE': 'VALUE_P', 'SEMIALL': 'SEMIALL', 'DATA': 'DATA_P', 'LIKEB': 'LIKEB', 'NUMERIC': 'NUMERIC', 'REMOVE': 'REMOVE', 'ERROR': 'ERROR_P', 'INVOKER': 'INVOKER', 'BZIP_COMP': 'BZIP_COMP', 'SUBNET': 'SUBNET', 'LABEL': 'LABEL', 'PASSWORD_GRACE_TIME': 'PASSWORD_GRACE_TIME', 'PASSWORD_MIN_UPPERCASE_LETTERS': 'PASSWORD_MIN_UPPERCASE_LETTERS', 'MINUTE': 'MINUTE_P', 'WRITE': 'WRITE', 'DIRECTCOLS': 'DIRECTCOLS', 'VOLATILE': 'VOLATILE', 'JSON': 'JSON', 'DISCONNECT': 'DISCONNECT', 'SYSTEM': 'SYSTEM', 'BIT': 'BIT', 'CALLED': 'CALLED', 'NULLS': 'NULLS', 'SET': 'SET', 'DELIMITER': 'DELIMITER', 'ROLE': 'ROLE', 'SEQUENCES': 'SEQUENCES', 'OFF': 'OFF', 'DETERMINES': 'DETERMINES', 'ORC': 'ORC', 'ADDRESS': 'ADDRESS', 'LIBRARY': 'LIBRARY', 'IMPLICIT': 'IMPLICIT_P', 'PREFER': 'PREFER', 'HCATALOG_SLOW_TRANSFER_TIME': 'HCATALOG_SLOW_TRANSFER_TIME', 'ENCODED': 'ENCODED', 'INTERVALYM': 'INTERVALYM', 'RETURN': 'RETURN', 'ENFORCELENGTH': 'ENFORCELENGTH', 'CONTROL': 'CONTROL', 'ROLES': 'ROLES', 'BASENAME': 'BASENAME', 'INTEGER': 'INTEGER', 'NOTIFIER': 'NOTIFIER', 'OPTION': 'OPTION', 'SMALLDATETIME': 'SMALLDATETIME', 'INTERSECT': 'INTERSECT', 'TIMEZONE': 'TIMEZONE', 'RECORD': 'RECORD_P', 'ARRAY': 'ARRAY', 'DELETE': 'DELETE_P', 'GZIP_COMP': 'GZIP_COMP', 'SCHEMA': 'SCHEMA', 'LEVEL': 'LEVEL', 'UNKNOWN': 'UNKNOWN', 'ACTIVATE': 'ACTIVATE', 'SIMILAR': 'SIMILAR', 'ILIKEB': 'ILIKEB', 'ADD': 'ADD', 'DEFAULTS': 'DEFAULTS', 'IN': 'IN_P', 'ON': 'ON', 'OPT': 'OPT', 'PARQUET': 'PARQUET', 'LONG': 'LONG', 'SECURITY_ALGORITHM': 'SECURITY_ALGORITHM', 'CLOSE': 'CLOSE', 'UMINUS': 'UMINUS', 'CREATE': 'CREATE', 'EXTRACT': 'EXTRACT', 'MATCH': 'MATCH', 'DELTARANGE_COMP': 'DELTARANGE_COMP', 'CREATEUSER': 'CREATEUSER', 'ACCOUNT': 'ACCOUNT', 'POLICY': 'POLICY', 'DELTARANGE_COMP_SP': 'DELTARANGE_COMP_SP', 'PASSWORD_REUSE_TIME': 'PASSWORD_REUSE_TIME', 'WORK': 'WORK', 'NOT': 'NOT', 'HCATALOG_CONNECTION_TIMEOUT': 'HCATALOG_CONNECTION_TIMEOUT', 'SHOW': 'SHOW', 'DATEDIFF': 'DATEDIFF', 'UNLOCK': 'UNLOCK_P', 'SEQUENCE': 'SEQUENCE', 'MAXCONNECTIONS': 'MAXCONNECTIONS', 'CHECK': 'CHECK', 'INT': 'INT_P', 'DEACTIVATE': 'DEACTIVATE', 'PASSWORD_MIN_LETTERS': 'PASSWORD_MIN_LETTERS', 'ACCESSRANK': 'ACCESSRANK', 'INSTEAD': 'INSTEAD', 'CLEAR': 'CLEAR', 'STRICT': 'STRICT_P', 'ABSOLUTE': 'ABSOLUTE_P', 'RESTART': 'RESTART', 'PASSWORD_MIN_DIGITS': 'PASSWORD_MIN_DIGITS', 'DELIMITERS': 'DELIMITERS', 'DISABLED': 'DISABLED', 'OTHERS': 'OTHERS', 'END': 'END_P', 'BINARY': 'BINARY', 'TRICKLE': 'TRICKLE', 'FLOAT': 'FLOAT_P', 'FREEZE': 'FREEZE', 'CURRENT_TIME': 'CURRENT_TIME', 'NOTIFY': 'NOTIFY', 'PRECEDING': 'PRECEDING', 'MASK': 'MASK', 'MODEL': 'MODEL', 'DEALLOCATE': 'DEALLOCATE', 'OUT': 'OUT_P', 'ROLLUP': 'ROLLUP', 'EXCEPT': 'EXCEPT', 'TABLESAMPLE': 'TABLESAMPLE', 'AUTHENTICATION': 'AUTHENTICATION', 'SETOF': 'SETOF', 'ASSIGNMENT': 'ASSIGNMENT', 'SKIP': 'SKIP', 'TREAT': 'TREAT', 'PORT': 'PORT', 'NONE': 'NONE', 'VARYING': 'VARYING', 'DISTVALINDEX': 'DISTVALINDEX', 'MEDIUM': 'MEDIUM', 'EACH': 'EACH', 'CHAR_LENGTH': 'CHAR_LENGTH', 'POOL': 'POOL', 'GLOBAL': 'GLOBAL', 'TEMPORARY': 'TEMPORARY', 'STRENGTH': 'STRENGTH', 'STATEMENT': 'STATEMENT', 'FALSE': 'FALSE_P', 'SECOND': 'SECOND_P', 'PARTIAL': 'PARTIAL', 'PASSWORD_MAX_LENGTH': 'PASSWORD_MAX_LENGTH', 'SIMPLE': 'SIMPLE', 'TIME': 'TIME', 'BATCH': 'BATCH', 'CONNECT': 'CONNECT', 'OIDS': 'OIDS', 'MONEY': 'MONEY', 'TABLE': 'TABLE', 'WEBSERVICE_HOSTNAME': 'WEBSERVICE_HOSTNAME', 'LOW': 'LOW', 'CURRENT_TIMESTAMP': 'CURRENT_TIMESTAMP', 'EPHEMERAL': 'EPHEMERAL', 'EXCEPTIONS': 'EXCEPTIONS', 'DECLARE': 'DECLARE', 'DEC': 'DEC', 'FENCED': 'FENCED', 'BZIP': 'BZIP', 'OFFSET': 'OFFSET', 'INHERITS': 'INHERITS', 'MAXVALUE': 'MAXVALUE', 'EXTEND': 'EXTEND', 'MAXMEMORYSIZE': 'MAXMEMORYSIZE', 'OUTER': 'OUTER_P', 'SECONDS': 'SECONDS_P', 'MOVEOUT': 'MOVEOUT', 'KEY': 'KEY', 'BETWEEN': 'BETWEEN', 'IS': 'IS', 'RUNTIMECAP': 'RUNTIMECAP', 'JOIN': 'JOIN', 'STATISTICS': 'STATISTICS', 'VALIDATE': 'VALIDATE', 'METHOD': 'METHOD', 'ANTI': 'ANTI', 'CYCLE': 'CYCLE', 'LOCALTIMESTAMP': 'LOCALTIMESTAMP', 'NODE': 'NODE', 'NULL': 'NULL_P', 'ALTER': 'ALTER', 'RULE': 'RULE', 'NEW': 'NEW', 'REVOKE': 'REVOKE', 'TRAILING': 'TRAILING', 'SOFTTYPECAST': 'SOFTTYPECAST', 'DATAPATH': 'DATAPATH', 'HCATALOG': 'HCATALOG', 'REJECTMAX': 'REJECTMAX', 'PROCEDURAL': 'PROCEDURAL', 'NUMBER': 'NUMBER_P', 'POSITION': 'POSITION', 'TABLESPACE': 'TABLESPACE', 'CROSS': 'CROSS', 'WITHIN': 'WITHIN', 'SYSDATE': 'SYSDATE', 'COMMUNAL': 'COMMUNAL', 'BLOCK_DICT': 'BLOCK_DICT', 'FILESYSTEM': 'FILESYSTEM', 'INTERFACE': 'INTERFACE', 'REPEATABLE': 'REPEATABLE', 'TYPE': 'TYPE_P', 'SESSION_USER': 'SESSION_USER', 'SSL_CONFIG': 'SSL_CONFIG', 'NULLSEQUAL': 'NULLSEQUAL', 'INSERT': 'INSERT', 'EXPIRE': 'EXPIRE', 'COLUMNS_COUNT': 'COLUMNS_COUNT', 'INDEX': 'INDEX', 'FLEX': 'FLEX', 'NO': 'NO', 'ACTIVEPARTITIONCOUNT': 'ACTIVEPARTITIONCOUNT', 'MAXPAYLOAD': 'MAXPAYLOAD', 'PREPARE': 'PREPARE', 'DATABASE': 'DATABASE', 'LATEST': 'LATEST', 'GCDDELTA': 'GCDDELTA'}

literals = [';', ',', '!', '*', '[', '=', '-', '/', '|', '%', ')', ']', '<', '(', '^', '+', '>', '.']

t_ignore = ' \t'


error_list = list()


def t_comment_ignore(t):
    r'[-][-][^\n]*'


def t_TYPECAST(t):
    r'::[!]?'
    t.type = 'TYPECAST'
    return t


def t_FCONST_1(t):
    r'[0-9]*[.][0-9]+([Ee][-+]?[0-9]+)?'
    t.type = 'FCONST'
    return t


def t_FCONST_2(t):
    r'[0-9]+[.]([Ee][-+]?[0-9]+)?'
    t.type = 'FCONST'
    return t


def t_FCONST_3(t):
    r'[0-9]+([Ee][-+]?[0-9]+)'
    t.type = 'FCONST'
    return t


def t_ICONST_1(t):
    r'0[xX][0-9a-fA-F][0-9a-fA-F]*'
    t.type = 'ICONST'
    return t


def t_ICONST_2(t):
    r'[0-9][0-9]*'
    t.type = 'ICONST'
    return t


def t_PARAM_1(t):
    r'[\\][0-9][0-9]*'
    t.type = 'PARAM'
    return t


def t_PARAM_2(t):
    r'<\[[^\]]*\](\.\[[^\]]*\])*>'
    t.type = 'PARAM'
    return t


def t_PARAM_3(t):
    r':[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'PARAM'
    return t


def t_BCONST(t):
    r"[bB]('[^']*')+"
    t.type = 'BCONST'
    return t


def t_XCONST(t):
    r"[xX]('[^']*')+"
    t.type = 'XCONST'
    return t


def t_SCONST_1(t):
    r"[eE]'([^'\\]|\\.)*'"
    t.type = 'SCONST'
    return t


def t_SCONST_2(t):
    r"('[^']*')+"
    t.type = 'SCONST'
    return t


def t_SCONST_3(t):
    r"[$][$]((?![$][$]).)*[$][$]"
    t.type = 'SCONST'
    return t


def t_IDENT_1(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value.upper(), 'IDENT')
    return t


def t_IDENT_2(t):
    r'"[^"]+"'
    t.type = 'IDENT'
    return t


def t_Op_Cmp(t):
    r'(<=>|[=<>!]=|<>)'
    t.type = 'Op_Cmp'
    return t


def t_Op_SS(t):
    r'//'
    t.type = 'Op_SS'
    return t


def t_Op_1(t):
    r'(<<|>>|\|\|/|\|\||\|/|!!|~[*]|~[~#][*]?|!~[~#][*]?)'
    t.type = 'Op'
    return t


def t_Op_2(t):
    r'[\|\&\#\~\!\@]'
    t.type = 'Op'
    return t


def t_HINT_BEGIN(t):
    r'[/][*]\s*[+]'
    t.type = 'HINT_BEGIN'
    return t


def t_HINT_END(t):
    r'[*][/]'
    t.type = 'HINT_END'
    return t


states = (
    ('multilinecomment', 'exclusive'),
)


def t_multilinecommentstart(t):
    r'/\*\s*[^+]'
    t.lexer.begin('multilinecomment')


def t_multilinecomment_end(t):
    r'\*/'
    t.lexer.begin('INITIAL')


def t_multilinecomment_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)


def t_multilinecomment_content(t):
    r'((?![*][/]).)+'


def t_multilinecomment_error(t):
    return t_error(t)


t_multilinecomment_ignore = t_ignore


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    errors = getattr(t.lexer, 'errors', error_list)
    linepos = max(0, t.lexer.lexdata[:t.lexpos].rfind('\n'))
    errors.append("line %d pos %d: Illegal character '%s'" %
                   (t.lexer.lineno, t.lexer.lexpos - linepos, t.value[0]))
    print(errors[-1])
    t.lexer.skip(1)


precedence =  [('nonassoc', 'SET'), ('left', 'UNION', 'EXCEPT', 'MINUS'), ('left', 'INTERSECT'), ('left', 'OR'), ('left', 'AND'), ('right', 'NOT'), ('right', '='), ('left', 'Op_Cmp'), ('nonassoc', '<', '>'), ('nonassoc', 'LIKE', 'ILIKE', 'LIKEB', 'ILIKEB', 'SIMILAR'), ('nonassoc', 'ESCAPE'), ('nonassoc', 'OVERLAPS'), ('nonassoc', 'BETWEEN'), ('nonassoc', 'IN_P'), ('nonassoc', 'IDENT', 'PARTITION', 'RANGE', 'ROWS', 'ROLLUP', 'CUBE'), ('left', 'Op', 'OPERATOR'), ('nonassoc', 'NOTNULL'), ('nonassoc', 'ISNULL'), ('nonassoc', 'IS', 'NULL_P', 'TRUE_P', 'FALSE_P', 'UNKNOWN'), ('left', '|'), ('left', '+', '-'), ('left', '*', '/', 'Op_SS', '%'), ('left', '^'), ('left', 'AT', 'ZONE', 'TIMEZONE', 'LOCAL'), ('right', 'UMINUS'), ('left', '!'), ('left', '[', ']'), ('left', '(', ')'), ('left', 'TYPECAST', 'SOFTTYPECAST'), ('left', '.'), ('left', 'JOIN', 'UNIONJOIN', 'CROSS', 'LEFT', 'FULL', 'RIGHT', 'INNER_P', 'NATURAL', 'COMPLEX', 'SEMI', 'UNI', 'SEMIALL', 'ANTI', 'NULLAWARE')]

# -------------- RULES ----------------


def p_error(t):
    if t is not None:
        errors = getattr(t.lexer, 'errors', error_list)
        linepos = max(0, t.lexer.lexdata[:t.lexpos].rfind('\n'))
        errors.append("line %d pos %d: Illegal character '%s'" %
                      (t.lineno, t.lexpos - linepos, t.value))
        print(errors[-1])
        t.lexer.skip(1)
    else:
        error_list.append("Unexpected end of input")
        print(error_list[-1])


class Expr:
    def __init__(self, name, expr, tokens, token):
        self.name = name
        self.expr = expr
        self.tokens = tokens
        self.line = token.lineno(0)
        self.pos = token.lexpos(0)


def p_stmtblock_1(p):
    """stmtblock : stmtmulti"""
    p[0] = Expr("""stmtblock""", """stmtmulti""", p[1:] if len(p or []) > 1 else [], p)


def p_stmtmulti_2(p):
    """stmtmulti : stmtmulti ';' stmt"""
    p[0] = Expr("""stmtmulti""", """stmtmulti ';' stmt""", p[1:] if len(p or []) > 1 else [], p)


def p_stmtmulti_3(p):
    """stmtmulti : stmt"""
    p[0] = Expr("""stmtmulti""", """stmt""", p[1:] if len(p or []) > 1 else [], p)


def p_stmt_4(p):
    """stmt : a_stmt"""
    p[0] = Expr("""stmt""", """a_stmt""", p[1:] if len(p or []) > 1 else [], p)


def p_stmt_5(p):
    """stmt : """
    p[0] = Expr("""stmt""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_6(p):
    """a_stmt : AlterAccessPolicyStmt"""
    p[0] = Expr("""a_stmt""", """AlterAccessPolicyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_7(p):
    """a_stmt : AlterAddressStmt"""
    p[0] = Expr("""a_stmt""", """AlterAddressStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_8(p):
    """a_stmt : AlterDatabaseSetStmt"""
    p[0] = Expr("""a_stmt""", """AlterDatabaseSetStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_9(p):
    """a_stmt : VAlterProjection"""
    p[0] = Expr("""a_stmt""", """VAlterProjection""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_10(p):
    """a_stmt : AlterDomainStmt"""
    p[0] = Expr("""a_stmt""", """AlterDomainStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_11(p):
    """a_stmt : AlterFaultGroupStmt"""
    p[0] = Expr("""a_stmt""", """AlterFaultGroupStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_12(p):
    """a_stmt : AlterGroupStmt"""
    p[0] = Expr("""a_stmt""", """AlterGroupStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_13(p):
    """a_stmt : AlterHCatalogSchemaStmt"""
    p[0] = Expr("""a_stmt""", """AlterHCatalogSchemaStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_14(p):
    """a_stmt : AlterLibraryStmt"""
    p[0] = Expr("""a_stmt""", """AlterLibraryStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_15(p):
    """a_stmt : AlterLoadBalanceGroupStmt"""
    p[0] = Expr("""a_stmt""", """AlterLoadBalanceGroupStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_16(p):
    """a_stmt : AlterRoutingRuleStmt"""
    p[0] = Expr("""a_stmt""", """AlterRoutingRuleStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_17(p):
    """a_stmt : AlterModelStmt"""
    p[0] = Expr("""a_stmt""", """AlterModelStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_18(p):
    """a_stmt : AlterNotifierStmt"""
    p[0] = Expr("""a_stmt""", """AlterNotifierStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_19(p):
    """a_stmt : AlterProfileStmt"""
    p[0] = Expr("""a_stmt""", """AlterProfileStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_20(p):
    """a_stmt : AlterResourcePoolStmt"""
    p[0] = Expr("""a_stmt""", """AlterResourcePoolStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_21(p):
    """a_stmt : AlterSchemaStmt"""
    p[0] = Expr("""a_stmt""", """AlterSchemaStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_22(p):
    """a_stmt : AlterViewPrivilegesStmt"""
    p[0] = Expr("""a_stmt""", """AlterViewPrivilegesStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_23(p):
    """a_stmt : AlterSeqStmt"""
    p[0] = Expr("""a_stmt""", """AlterSeqStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_24(p):
    """a_stmt : AlterSessionStmt"""
    p[0] = Expr("""a_stmt""", """AlterSessionStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_25(p):
    """a_stmt : AlterTableStmt"""
    p[0] = Expr("""a_stmt""", """AlterTableStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_26(p):
    """a_stmt : AlterTuningRuleStmt"""
    p[0] = Expr("""a_stmt""", """AlterTuningRuleStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_27(p):
    """a_stmt : AlterUserDefaultRoleStmt"""
    p[0] = Expr("""a_stmt""", """AlterUserDefaultRoleStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_28(p):
    """a_stmt : AlterUserSetStmt"""
    p[0] = Expr("""a_stmt""", """AlterUserSetStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_29(p):
    """a_stmt : AlterUserStmt"""
    p[0] = Expr("""a_stmt""", """AlterUserStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_30(p):
    """a_stmt : AlterFunctionStmt"""
    p[0] = Expr("""a_stmt""", """AlterFunctionStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_31(p):
    """a_stmt : AlterAuthStmt"""
    p[0] = Expr("""a_stmt""", """AlterAuthStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_32(p):
    """a_stmt : AlterUDxFenceStmt"""
    p[0] = Expr("""a_stmt""", """AlterUDxFenceStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_33(p):
    """a_stmt : AlterViewStmt"""
    p[0] = Expr("""a_stmt""", """AlterViewStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_34(p):
    """a_stmt : AnalyzeStmt"""
    p[0] = Expr("""a_stmt""", """AnalyzeStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_35(p):
    """a_stmt : CheckPointStmt"""
    p[0] = Expr("""a_stmt""", """CheckPointStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_36(p):
    """a_stmt : ClosePortalStmt"""
    p[0] = Expr("""a_stmt""", """ClosePortalStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_37(p):
    """a_stmt : ClusterStmt"""
    p[0] = Expr("""a_stmt""", """ClusterStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_38(p):
    """a_stmt : CommentStmt"""
    p[0] = Expr("""a_stmt""", """CommentStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_39(p):
    """a_stmt : ConnectStmt"""
    p[0] = Expr("""a_stmt""", """ConnectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_40(p):
    """a_stmt : ConstraintsSetStmt"""
    p[0] = Expr("""a_stmt""", """ConstraintsSetStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_41(p):
    """a_stmt : CopyStmt"""
    p[0] = Expr("""a_stmt""", """CopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_42(p):
    """a_stmt : CopyAccessPolicyStmt"""
    p[0] = Expr("""a_stmt""", """CopyAccessPolicyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_43(p):
    """a_stmt : VCreateProjectionStmt"""
    p[0] = Expr("""a_stmt""", """VCreateProjectionStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_44(p):
    """a_stmt : VNode"""
    p[0] = Expr("""a_stmt""", """VNode""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_45(p):
    """a_stmt : VAlterNode"""
    p[0] = Expr("""a_stmt""", """VAlterNode""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_46(p):
    """a_stmt : CreateAccessPolicyStmt"""
    p[0] = Expr("""a_stmt""", """CreateAccessPolicyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_47(p):
    """a_stmt : CreateAsStmt"""
    p[0] = Expr("""a_stmt""", """CreateAsStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_48(p):
    """a_stmt : CreateAssertStmt"""
    p[0] = Expr("""a_stmt""", """CreateAssertStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_49(p):
    """a_stmt : CreateBranchStmt"""
    p[0] = Expr("""a_stmt""", """CreateBranchStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_50(p):
    """a_stmt : CreateCastStmt"""
    p[0] = Expr("""a_stmt""", """CreateCastStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_51(p):
    """a_stmt : CreateDomainStmt"""
    p[0] = Expr("""a_stmt""", """CreateDomainStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_52(p):
    """a_stmt : CreateFaultGroupStmt"""
    p[0] = Expr("""a_stmt""", """CreateFaultGroupStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_53(p):
    """a_stmt : CreateFunctionStmt"""
    p[0] = Expr("""a_stmt""", """CreateFunctionStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_54(p):
    """a_stmt : CreateGroupStmt"""
    p[0] = Expr("""a_stmt""", """CreateGroupStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_55(p):
    """a_stmt : CreateInterfaceStmt"""
    p[0] = Expr("""a_stmt""", """CreateInterfaceStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_56(p):
    """a_stmt : CreateLoadBalanceGroupStmt"""
    p[0] = Expr("""a_stmt""", """CreateLoadBalanceGroupStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_57(p):
    """a_stmt : CreateRoutingRuleStmt"""
    p[0] = Expr("""a_stmt""", """CreateRoutingRuleStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_58(p):
    """a_stmt : CreateLibraryStmt"""
    p[0] = Expr("""a_stmt""", """CreateLibraryStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_59(p):
    """a_stmt : CreateLocationStmt"""
    p[0] = Expr("""a_stmt""", """CreateLocationStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_60(p):
    """a_stmt : CreateModelStmt"""
    p[0] = Expr("""a_stmt""", """CreateModelStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_61(p):
    """a_stmt : CreateNotifierStmt"""
    p[0] = Expr("""a_stmt""", """CreateNotifierStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_62(p):
    """a_stmt : CreateOpClassStmt"""
    p[0] = Expr("""a_stmt""", """CreateOpClassStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_63(p):
    """a_stmt : CreateProcStmt"""
    p[0] = Expr("""a_stmt""", """CreateProcStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_64(p):
    """a_stmt : CreateProfileStmt"""
    p[0] = Expr("""a_stmt""", """CreateProfileStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_65(p):
    """a_stmt : CreatePLangStmt"""
    p[0] = Expr("""a_stmt""", """CreatePLangStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_66(p):
    """a_stmt : CreateResourcePoolStmt"""
    p[0] = Expr("""a_stmt""", """CreateResourcePoolStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_67(p):
    """a_stmt : CreateRoleStmt"""
    p[0] = Expr("""a_stmt""", """CreateRoleStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_68(p):
    """a_stmt : CreateSchemaStmt"""
    p[0] = Expr("""a_stmt""", """CreateSchemaStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_69(p):
    """a_stmt : CreateSeqStmt"""
    p[0] = Expr("""a_stmt""", """CreateSeqStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_70(p):
    """a_stmt : CreateStmt"""
    p[0] = Expr("""a_stmt""", """CreateStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_71(p):
    """a_stmt : CreateSubnetStmt"""
    p[0] = Expr("""a_stmt""", """CreateSubnetStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_72(p):
    """a_stmt : CreateTableSpaceStmt"""
    p[0] = Expr("""a_stmt""", """CreateTableSpaceStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_73(p):
    """a_stmt : CreateTrigStmt"""
    p[0] = Expr("""a_stmt""", """CreateTrigStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_74(p):
    """a_stmt : CreateTuningRuleStmt"""
    p[0] = Expr("""a_stmt""", """CreateTuningRuleStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_75(p):
    """a_stmt : CreateAuthStmt"""
    p[0] = Expr("""a_stmt""", """CreateAuthStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_76(p):
    """a_stmt : CreateUDXStmt"""
    p[0] = Expr("""a_stmt""", """CreateUDXStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_77(p):
    """a_stmt : CreateUserStmt"""
    p[0] = Expr("""a_stmt""", """CreateUserStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_78(p):
    """a_stmt : CreatedbStmt"""
    p[0] = Expr("""a_stmt""", """CreatedbStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_79(p):
    """a_stmt : CurrentVariableShowStmt"""
    p[0] = Expr("""a_stmt""", """CurrentVariableShowStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_80(p):
    """a_stmt : DeallocateStmt"""
    p[0] = Expr("""a_stmt""", """DeallocateStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_81(p):
    """a_stmt : DeclareCursorStmt"""
    p[0] = Expr("""a_stmt""", """DeclareCursorStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_82(p):
    """a_stmt : DefineStmt"""
    p[0] = Expr("""a_stmt""", """DefineStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_83(p):
    """a_stmt : DeleteStmt"""
    p[0] = Expr("""a_stmt""", """DeleteStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_84(p):
    """a_stmt : DisconnectStmt"""
    p[0] = Expr("""a_stmt""", """DisconnectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_85(p):
    """a_stmt : DropAssertStmt"""
    p[0] = Expr("""a_stmt""", """DropAssertStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_86(p):
    """a_stmt : DropCastStmt"""
    p[0] = Expr("""a_stmt""", """DropCastStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_87(p):
    """a_stmt : DropGroupStmt"""
    p[0] = Expr("""a_stmt""", """DropGroupStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_88(p):
    """a_stmt : DropOpClassStmt"""
    p[0] = Expr("""a_stmt""", """DropOpClassStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_89(p):
    """a_stmt : DropPLangStmt"""
    p[0] = Expr("""a_stmt""", """DropPLangStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_90(p):
    """a_stmt : DropRuleStmt"""
    p[0] = Expr("""a_stmt""", """DropRuleStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_91(p):
    """a_stmt : DropStmt"""
    p[0] = Expr("""a_stmt""", """DropStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_92(p):
    """a_stmt : DropTableSpaceStmt"""
    p[0] = Expr("""a_stmt""", """DropTableSpaceStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_93(p):
    """a_stmt : DropTrigStmt"""
    p[0] = Expr("""a_stmt""", """DropTrigStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_94(p):
    """a_stmt : DropUserStmt"""
    p[0] = Expr("""a_stmt""", """DropUserStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_95(p):
    """a_stmt : DropdbStmt"""
    p[0] = Expr("""a_stmt""", """DropdbStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_96(p):
    """a_stmt : DropAccessPolicyStmt"""
    p[0] = Expr("""a_stmt""", """DropAccessPolicyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_97(p):
    """a_stmt : ExecuteStmt"""
    p[0] = Expr("""a_stmt""", """ExecuteStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_98(p):
    """a_stmt : ExplainStmt"""
    p[0] = Expr("""a_stmt""", """ExplainStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_99(p):
    """a_stmt : FetchStmt"""
    p[0] = Expr("""a_stmt""", """FetchStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_100(p):
    """a_stmt : GrantStmt"""
    p[0] = Expr("""a_stmt""", """GrantStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_101(p):
    """a_stmt : IndexStmt"""
    p[0] = Expr("""a_stmt""", """IndexStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_102(p):
    """a_stmt : InsertStmt"""
    p[0] = Expr("""a_stmt""", """InsertStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_103(p):
    """a_stmt : ListenStmt"""
    p[0] = Expr("""a_stmt""", """ListenStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_104(p):
    """a_stmt : LoadStmt"""
    p[0] = Expr("""a_stmt""", """LoadStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_105(p):
    """a_stmt : LockStmt"""
    p[0] = Expr("""a_stmt""", """LockStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_106(p):
    """a_stmt : NotifyStmt"""
    p[0] = Expr("""a_stmt""", """NotifyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_107(p):
    """a_stmt : PlanStabilityActivatePlanStmt"""
    p[0] = Expr("""a_stmt""", """PlanStabilityActivatePlanStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_108(p):
    """a_stmt : PlanStabilityAssociatePlanStmt"""
    p[0] = Expr("""a_stmt""", """PlanStabilityAssociatePlanStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_109(p):
    """a_stmt : PlanStabilityGetPlanStmt"""
    p[0] = Expr("""a_stmt""", """PlanStabilityGetPlanStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_110(p):
    """a_stmt : PlanStabilityRemovePlanStmt"""
    p[0] = Expr("""a_stmt""", """PlanStabilityRemovePlanStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_111(p):
    """a_stmt : PlanStabilitySavePlanStmt"""
    p[0] = Expr("""a_stmt""", """PlanStabilitySavePlanStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_112(p):
    """a_stmt : PrepareStmt"""
    p[0] = Expr("""a_stmt""", """PrepareStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_113(p):
    """a_stmt : ProfileStmt"""
    p[0] = Expr("""a_stmt""", """ProfileStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_114(p):
    """a_stmt : ReindexStmt"""
    p[0] = Expr("""a_stmt""", """ReindexStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_115(p):
    """a_stmt : RemoveAggrStmt"""
    p[0] = Expr("""a_stmt""", """RemoveAggrStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_116(p):
    """a_stmt : RemoveFuncStmt"""
    p[0] = Expr("""a_stmt""", """RemoveFuncStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_117(p):
    """a_stmt : RemoveProcStmt"""
    p[0] = Expr("""a_stmt""", """RemoveProcStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_118(p):
    """a_stmt : RemoveOperStmt"""
    p[0] = Expr("""a_stmt""", """RemoveOperStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_119(p):
    """a_stmt : RemoveUDXStmt"""
    p[0] = Expr("""a_stmt""", """RemoveUDXStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_120(p):
    """a_stmt : RenameStmt"""
    p[0] = Expr("""a_stmt""", """RenameStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_121(p):
    """a_stmt : RevokeStmt"""
    p[0] = Expr("""a_stmt""", """RevokeStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_122(p):
    """a_stmt : RuleStmt"""
    p[0] = Expr("""a_stmt""", """RuleStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_123(p):
    """a_stmt : ShowDatabaseStmt"""
    p[0] = Expr("""a_stmt""", """ShowDatabaseStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_124(p):
    """a_stmt : ShowNodeStmt"""
    p[0] = Expr("""a_stmt""", """ShowNodeStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_125(p):
    """a_stmt : TransactionStmt"""
    p[0] = Expr("""a_stmt""", """TransactionStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_126(p):
    """a_stmt : TruncateStmt"""
    p[0] = Expr("""a_stmt""", """TruncateStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_127(p):
    """a_stmt : UnlistenStmt"""
    p[0] = Expr("""a_stmt""", """UnlistenStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_128(p):
    """a_stmt : UpdateStmt"""
    p[0] = Expr("""a_stmt""", """UpdateStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_129(p):
    """a_stmt : VariableResetStmt"""
    p[0] = Expr("""a_stmt""", """VariableResetStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_130(p):
    """a_stmt : VariableSetStmt"""
    p[0] = Expr("""a_stmt""", """VariableSetStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_131(p):
    """a_stmt : VariableShowStmt"""
    p[0] = Expr("""a_stmt""", """VariableShowStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_132(p):
    """a_stmt : VSelectIntoStmt"""
    p[0] = Expr("""a_stmt""", """VSelectIntoStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_133(p):
    """a_stmt : VSelectStmt"""
    p[0] = Expr("""a_stmt""", """VSelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_134(p):
    """a_stmt : ViewStmt"""
    p[0] = Expr("""a_stmt""", """ViewStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_135(p):
    """a_stmt : ExportStmt"""
    p[0] = Expr("""a_stmt""", """ExportStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_a_stmt_136(p):
    """a_stmt : VMergeStmt"""
    p[0] = Expr("""a_stmt""", """VMergeStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_VAlterProjection_137(p):
    """VAlterProjection : ALTER PROJECTION qualified_name AlterProjSpec"""
    p[0] = Expr("""VAlterProjection""", """ALTER PROJECTION qualified_name AlterProjSpec""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterProjSpec_138(p):
    """AlterProjSpec : MergeMoveSpec"""
    p[0] = Expr("""AlterProjSpec""", """MergeMoveSpec""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterProjSpec_139(p):
    """AlterProjSpec : RecoverSpec"""
    p[0] = Expr("""AlterProjSpec""", """RecoverSpec""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterProjSpec_140(p):
    """AlterProjSpec : SplitSpec"""
    p[0] = Expr("""AlterProjSpec""", """SplitSpec""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterProjSpec_141(p):
    """AlterProjSpec : RefreshSpec"""
    p[0] = Expr("""AlterProjSpec""", """RefreshSpec""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterProjSpec_142(p):
    """AlterProjSpec : OrderTrimSpec"""
    p[0] = Expr("""AlterProjSpec""", """OrderTrimSpec""", p[1:] if len(p or []) > 1 else [], p)


def p_RecoverSpec_143(p):
    """RecoverSpec : RECOVER qualified_name FROM Iconst ToEpochSpec"""
    p[0] = Expr("""RecoverSpec""", """RECOVER qualified_name FROM Iconst ToEpochSpec""", p[1:] if len(p or []) > 1 else [], p)


def p_RefreshSpec_144(p):
    """RefreshSpec : REFRESH"""
    p[0] = Expr("""RefreshSpec""", """REFRESH""", p[1:] if len(p or []) > 1 else [], p)


def p_ToEpochSpec_145(p):
    """ToEpochSpec : TO Iconst"""
    p[0] = Expr("""ToEpochSpec""", """TO Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_ToEpochSpec_146(p):
    """ToEpochSpec : """
    p[0] = Expr("""ToEpochSpec""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_SplitSpec_147(p):
    """SplitSpec : SPLIT qualified_name FROM Iconst"""
    p[0] = Expr("""SplitSpec""", """SPLIT qualified_name FROM Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_MergeMoveSpec_148(p):
    """MergeMoveSpec : alter_projection_action Vmergeout_range"""
    p[0] = Expr("""MergeMoveSpec""", """alter_projection_action Vmergeout_range""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_projection_action_149(p):
    """alter_projection_action : MERGEOUT"""
    p[0] = Expr("""alter_projection_action""", """MERGEOUT""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_projection_action_150(p):
    """alter_projection_action : MOVEOUT"""
    p[0] = Expr("""alter_projection_action""", """MOVEOUT""", p[1:] if len(p or []) > 1 else [], p)


def p_Vmergeout_range_151(p):
    """Vmergeout_range : FROM Iconst TO Iconst"""
    p[0] = Expr("""Vmergeout_range""", """FROM Iconst TO Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_Vmergeout_range_152(p):
    """Vmergeout_range : UNCOMMITTED"""
    p[0] = Expr("""Vmergeout_range""", """UNCOMMITTED""", p[1:] if len(p or []) > 1 else [], p)


def p_Vmergeout_range_153(p):
    """Vmergeout_range : """
    p[0] = Expr("""Vmergeout_range""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OrderTrimSpec_154(p):
    """OrderTrimSpec : SET sort_clause"""
    p[0] = Expr("""OrderTrimSpec""", """SET sort_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_VCreateProjectionStmt_155(p):
    """VCreateProjectionStmt : CREATE PROJECTION IF_P NOT EXISTS qualified_name hint_clause opt_vt_columnGroupList AS SelectStmt ProjectionClauses"""
    p[0] = Expr("""VCreateProjectionStmt""", """CREATE PROJECTION IF_P NOT EXISTS qualified_name hint_clause opt_vt_columnGroupList AS SelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_VCreateProjectionStmt_156(p):
    """VCreateProjectionStmt : CREATE PROJECTION qualified_name hint_clause opt_vt_columnGroupList AS SelectStmt ProjectionClauses"""
    p[0] = Expr("""VCreateProjectionStmt""", """CREATE PROJECTION qualified_name hint_clause opt_vt_columnGroupList AS SelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_vt_columnGroupList_157(p):
    """opt_vt_columnGroupList : '(' vt_columnGroupList ')'"""
    p[0] = Expr("""opt_vt_columnGroupList""", """'(' vt_columnGroupList ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_vt_columnGroupList_158(p):
    """opt_vt_columnGroupList : """
    p[0] = Expr("""opt_vt_columnGroupList""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_vt_columnGroupList_159(p):
    """vt_columnGroupList : VColumnGroupElem"""
    p[0] = Expr("""vt_columnGroupList""", """VColumnGroupElem""", p[1:] if len(p or []) > 1 else [], p)


def p_vt_columnGroupList_160(p):
    """vt_columnGroupList : vt_columnGroupList ',' VColumnGroupElem"""
    p[0] = Expr("""vt_columnGroupList""", """vt_columnGroupList ',' VColumnGroupElem""", p[1:] if len(p or []) > 1 else [], p)


def p_VColumnGroupElem_161(p):
    """VColumnGroupElem : VColumnElem"""
    p[0] = Expr("""VColumnGroupElem""", """VColumnElem""", p[1:] if len(p or []) > 1 else [], p)


def p_VColumnGroupElem_162(p):
    """VColumnGroupElem : GROUPED '(' VColumnElem ',' vt_columnList ')'"""
    p[0] = Expr("""VColumnGroupElem""", """GROUPED '(' VColumnElem ',' vt_columnList ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_vt_columnList_163(p):
    """vt_columnList : VColumnElem"""
    p[0] = Expr("""vt_columnList""", """VColumnElem""", p[1:] if len(p or []) > 1 else [], p)


def p_vt_columnList_164(p):
    """vt_columnList : vt_columnList ',' VColumnElem"""
    p[0] = Expr("""vt_columnList""", """vt_columnList ',' VColumnElem""", p[1:] if len(p or []) > 1 else [], p)


def p_VColumnElem_165(p):
    """VColumnElem : ColId encode_type index_type opt_access_rank"""
    p[0] = Expr("""VColumnElem""", """ColId encode_type index_type opt_access_rank""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_166(p):
    """encode_type : ENCODING NONE"""
    p[0] = Expr("""encode_type""", """ENCODING NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_167(p):
    """encode_type : ENCODING RLE"""
    p[0] = Expr("""encode_type""", """ENCODING RLE""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_168(p):
    """encode_type : ENCODING BLOCK_DICT"""
    p[0] = Expr("""encode_type""", """ENCODING BLOCK_DICT""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_169(p):
    """encode_type : ENCODING BLOCKDICT_COMP"""
    p[0] = Expr("""encode_type""", """ENCODING BLOCKDICT_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_170(p):
    """encode_type : ENCODING DELTAVAL"""
    p[0] = Expr("""encode_type""", """ENCODING DELTAVAL""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_171(p):
    """encode_type : ENCODING GCDDELTA"""
    p[0] = Expr("""encode_type""", """ENCODING GCDDELTA""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_172(p):
    """encode_type : ENCODING DELTARANGE_COMP"""
    p[0] = Expr("""encode_type""", """ENCODING DELTARANGE_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_173(p):
    """encode_type : ENCODING DELTARANGE_COMP_SP"""
    p[0] = Expr("""encode_type""", """ENCODING DELTARANGE_COMP_SP""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_174(p):
    """encode_type : ENCODING COMMONDELTA_COMP"""
    p[0] = Expr("""encode_type""", """ENCODING COMMONDELTA_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_175(p):
    """encode_type : ENCODING BZIP_COMP"""
    p[0] = Expr("""encode_type""", """ENCODING BZIP_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_176(p):
    """encode_type : ENCODING GZIP_COMP"""
    p[0] = Expr("""encode_type""", """ENCODING GZIP_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_177(p):
    """encode_type : ENCODING ZSTD_COMP"""
    p[0] = Expr("""encode_type""", """ENCODING ZSTD_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_178(p):
    """encode_type : ENCODING ZSTD_FAST_COMP"""
    p[0] = Expr("""encode_type""", """ENCODING ZSTD_FAST_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_179(p):
    """encode_type : ENCODING ZSTD_HIGH_COMP"""
    p[0] = Expr("""encode_type""", """ENCODING ZSTD_HIGH_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_180(p):
    """encode_type : ENCODING AUTO"""
    p[0] = Expr("""encode_type""", """ENCODING AUTO""", p[1:] if len(p or []) > 1 else [], p)


def p_encode_type_181(p):
    """encode_type : """
    p[0] = Expr("""encode_type""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_access_rank_182(p):
    """opt_access_rank : ACCESSRANK IntegerOnly"""
    p[0] = Expr("""opt_access_rank""", """ACCESSRANK IntegerOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_access_rank_183(p):
    """opt_access_rank : """
    p[0] = Expr("""opt_access_rank""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_index_type_184(p):
    """index_type : VALINDEX"""
    p[0] = Expr("""index_type""", """VALINDEX""", p[1:] if len(p or []) > 1 else [], p)


def p_index_type_185(p):
    """index_type : """
    p[0] = Expr("""index_type""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_VSegmentation_186(p):
    """VSegmentation : SEGMENTED BY b_expr vt_segmented_by_MAX"""
    p[0] = Expr("""VSegmentation""", """SEGMENTED BY b_expr vt_segmented_by_MAX""", p[1:] if len(p or []) > 1 else [], p)


def p_VSegmentation_187(p):
    """VSegmentation : UNSEGMENTED NODE qualified_name"""
    p[0] = Expr("""VSegmentation""", """UNSEGMENTED NODE qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_VSegmentation_188(p):
    """VSegmentation : UNSEGMENTED ALL NODES"""
    p[0] = Expr("""VSegmentation""", """UNSEGMENTED ALL NODES""", p[1:] if len(p or []) > 1 else [], p)


def p_VSegmentation_189(p):
    """VSegmentation : SEGMENTED BY b_expr NODES qualified_name_list opt_offset"""
    p[0] = Expr("""VSegmentation""", """SEGMENTED BY b_expr NODES qualified_name_list opt_offset""", p[1:] if len(p or []) > 1 else [], p)


def p_VSegmentation_190(p):
    """VSegmentation : SEGMENTED BY b_expr ALL NODES opt_offset"""
    p[0] = Expr("""VSegmentation""", """SEGMENTED BY b_expr ALL NODES opt_offset""", p[1:] if len(p or []) > 1 else [], p)


def p_VSegmentation_191(p):
    """VSegmentation : PINNED"""
    p[0] = Expr("""VSegmentation""", """PINNED""", p[1:] if len(p or []) > 1 else [], p)


def p_VSegmentation_192(p):
    """VSegmentation : """
    p[0] = Expr("""VSegmentation""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_offset_193(p):
    """opt_offset : OFFSET Iconst"""
    p[0] = Expr("""opt_offset""", """OFFSET Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_offset_194(p):
    """opt_offset : """
    p[0] = Expr("""opt_offset""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_vt_segmented_by_MAX_195(p):
    """vt_segmented_by_MAX : VSegmentedByMAX"""
    p[0] = Expr("""vt_segmented_by_MAX""", """VSegmentedByMAX""", p[1:] if len(p or []) > 1 else [], p)


def p_vt_segmented_by_MAX_196(p):
    """vt_segmented_by_MAX : vt_segmented_by VSegmentedByMAX"""
    p[0] = Expr("""vt_segmented_by_MAX""", """vt_segmented_by VSegmentedByMAX""", p[1:] if len(p or []) > 1 else [], p)


def p_vt_segmented_by_197(p):
    """vt_segmented_by : VSegmentedBy"""
    p[0] = Expr("""vt_segmented_by""", """VSegmentedBy""", p[1:] if len(p or []) > 1 else [], p)


def p_vt_segmented_by_198(p):
    """vt_segmented_by : vt_segmented_by VSegmentedBy"""
    p[0] = Expr("""vt_segmented_by""", """vt_segmented_by VSegmentedBy""", p[1:] if len(p or []) > 1 else [], p)


def p_VSegmentedBy_199(p):
    """VSegmentedBy : NODE qualified_name VALUES LESS THAN a_expr"""
    p[0] = Expr("""VSegmentedBy""", """NODE qualified_name VALUES LESS THAN a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_VSegmentedByMAX_200(p):
    """VSegmentedByMAX : NODE qualified_name VALUES LESS THAN MAXVALUE"""
    p[0] = Expr("""VSegmentedByMAX""", """NODE qualified_name VALUES LESS THAN MAXVALUE""", p[1:] if len(p or []) > 1 else [], p)


def p_VNode_201(p):
    """VNode : CREATE NODE CreateNodeList"""
    p[0] = Expr("""VNode""", """CREATE NODE CreateNodeList""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateNodeDetails_202(p):
    """CreateNodeDetails : name opt_is VNodeParams"""
    p[0] = Expr("""CreateNodeDetails""", """name opt_is VNodeParams""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateNodeList_203(p):
    """CreateNodeList : CreateNodeDetails"""
    p[0] = Expr("""CreateNodeList""", """CreateNodeDetails""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateNodeList_204(p):
    """CreateNodeList : CreateNodeDetails AND CreateNodeList"""
    p[0] = Expr("""CreateNodeList""", """CreateNodeDetails AND CreateNodeList""", p[1:] if len(p or []) > 1 else [], p)


def p_VAlterNode_205(p):
    """VAlterNode : ALTER NODE AlterNodeList"""
    p[0] = Expr("""VAlterNode""", """ALTER NODE AlterNodeList""", p[1:] if len(p or []) > 1 else [], p)


def p_VAlterNodeDetails_206(p):
    """VAlterNodeDetails : name opt_is VNodeParams"""
    p[0] = Expr("""VAlterNodeDetails""", """name opt_is VNodeParams""", p[1:] if len(p or []) > 1 else [], p)


def p_VAlterNodeDetails_207(p):
    """VAlterNodeDetails : name REPLACE"""
    p[0] = Expr("""VAlterNodeDetails""", """name REPLACE""", p[1:] if len(p or []) > 1 else [], p)


def p_VAlterNodeDetails_208(p):
    """VAlterNodeDetails : name REPLACE WITH name"""
    p[0] = Expr("""VAlterNodeDetails""", """name REPLACE WITH name""", p[1:] if len(p or []) > 1 else [], p)


def p_VAlterNodeDetails_209(p):
    """VAlterNodeDetails : name RESET"""
    p[0] = Expr("""VAlterNodeDetails""", """name RESET""", p[1:] if len(p or []) > 1 else [], p)


def p_VAlterNodeDetails_210(p):
    """VAlterNodeDetails : name SET PARAMETER paramarg_list"""
    p[0] = Expr("""VAlterNodeDetails""", """name SET PARAMETER paramarg_list""", p[1:] if len(p or []) > 1 else [], p)


def p_VAlterNodeDetails_211(p):
    """VAlterNodeDetails : name SET paramarg_list"""
    p[0] = Expr("""VAlterNodeDetails""", """name SET paramarg_list""", p[1:] if len(p or []) > 1 else [], p)


def p_VAlterNodeDetails_212(p):
    """VAlterNodeDetails : name CLEAR PARAMETER knob_list"""
    p[0] = Expr("""VAlterNodeDetails""", """name CLEAR PARAMETER knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_VAlterNodeDetails_213(p):
    """VAlterNodeDetails : name CLEAR knob_list"""
    p[0] = Expr("""VAlterNodeDetails""", """name CLEAR knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterNodeList_214(p):
    """AlterNodeList : VAlterNodeDetails"""
    p[0] = Expr("""AlterNodeList""", """VAlterNodeDetails""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterNodeList_215(p):
    """AlterNodeList : AlterNodeList AND VAlterNodeDetails"""
    p[0] = Expr("""AlterNodeList""", """AlterNodeList AND VAlterNodeDetails""", p[1:] if len(p or []) > 1 else [], p)


def p_ShowNodeStmt_216(p):
    """ShowNodeStmt : SHOW NODE name knob_list"""
    p[0] = Expr("""ShowNodeStmt""", """SHOW NODE name knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_ShowNodeStmt_217(p):
    """ShowNodeStmt : SHOW NODE name PARAMETER knob_list"""
    p[0] = Expr("""ShowNodeStmt""", """SHOW NODE name PARAMETER knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_ShowNodeStmt_218(p):
    """ShowNodeStmt : SHOW NODE name ALL"""
    p[0] = Expr("""ShowNodeStmt""", """SHOW NODE name ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_ShowNodeStmt_219(p):
    """ShowNodeStmt : SHOW NODE name PARAMETER ALL"""
    p[0] = Expr("""ShowNodeStmt""", """SHOW NODE name PARAMETER ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_is_220(p):
    """opt_is : IS"""
    p[0] = Expr("""opt_is""", """IS""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_is_221(p):
    """opt_is : """
    p[0] = Expr("""opt_is""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_VNodeParams_222(p):
    """VNodeParams : VHostName DataPath CatalogPath NodeType NodeFaultGroup ExportAddress PortSpecification WaitForJoin"""
    p[0] = Expr("""VNodeParams""", """VHostName DataPath CatalogPath NodeType NodeFaultGroup ExportAddress PortSpecification WaitForJoin""", p[1:] if len(p or []) > 1 else [], p)


def p_VNodeParams_223(p):
    """VNodeParams : VHostName DataPath CatalogPath NodeType NodeFaultGroup ExportAddress PortSpecification CONTROL ControlAddress BroadcastAddress PortSpecification ControlNode WaitForJoin"""
    p[0] = Expr("""VNodeParams""", """VHostName DataPath CatalogPath NodeType NodeFaultGroup ExportAddress PortSpecification CONTROL ControlAddress BroadcastAddress PortSpecification ControlNode WaitForJoin""", p[1:] if len(p or []) > 1 else [], p)


def p_VHostName_224(p):
    """VHostName : HOSTNAME Sconst"""
    p[0] = Expr("""VHostName""", """HOSTNAME Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_VHostName_225(p):
    """VHostName : """
    p[0] = Expr("""VHostName""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_DataPath_226(p):
    """DataPath : DATAPATH DataPathList"""
    p[0] = Expr("""DataPath""", """DATAPATH DataPathList""", p[1:] if len(p or []) > 1 else [], p)


def p_DataPath_227(p):
    """DataPath : """
    p[0] = Expr("""DataPath""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_DataPathList_228(p):
    """DataPathList : Sconst"""
    p[0] = Expr("""DataPathList""", """Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_DataPathList_229(p):
    """DataPathList : DataPathList ',' Sconst"""
    p[0] = Expr("""DataPathList""", """DataPathList ',' Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_WaitForJoin_230(p):
    """WaitForJoin : WAIT FOR JOIN"""
    p[0] = Expr("""WaitForJoin""", """WAIT FOR JOIN""", p[1:] if len(p or []) > 1 else [], p)


def p_WaitForJoin_231(p):
    """WaitForJoin : """
    p[0] = Expr("""WaitForJoin""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_CatalogPath_232(p):
    """CatalogPath : CATALOGPATH Sconst"""
    p[0] = Expr("""CatalogPath""", """CATALOGPATH Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_CatalogPath_233(p):
    """CatalogPath : """
    p[0] = Expr("""CatalogPath""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_NodeType_234(p):
    """NodeType : PERMANENT"""
    p[0] = Expr("""NodeType""", """PERMANENT""", p[1:] if len(p or []) > 1 else [], p)


def p_NodeType_235(p):
    """NodeType : EPHEMERAL"""
    p[0] = Expr("""NodeType""", """EPHEMERAL""", p[1:] if len(p or []) > 1 else [], p)


def p_NodeType_236(p):
    """NodeType : EXECUTE"""
    p[0] = Expr("""NodeType""", """EXECUTE""", p[1:] if len(p or []) > 1 else [], p)


def p_NodeType_237(p):
    """NodeType : STANDBY"""
    p[0] = Expr("""NodeType""", """STANDBY""", p[1:] if len(p or []) > 1 else [], p)


def p_NodeType_238(p):
    """NodeType : """
    p[0] = Expr("""NodeType""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_NodeFaultGroup_239(p):
    """NodeFaultGroup : FAULT GROUP_P name"""
    p[0] = Expr("""NodeFaultGroup""", """FAULT GROUP_P name""", p[1:] if len(p or []) > 1 else [], p)


def p_NodeFaultGroup_240(p):
    """NodeFaultGroup : """
    p[0] = Expr("""NodeFaultGroup""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_ExportAddress_241(p):
    """ExportAddress : EXPORT ON name"""
    p[0] = Expr("""ExportAddress""", """EXPORT ON name""", p[1:] if len(p or []) > 1 else [], p)


def p_ExportAddress_242(p):
    """ExportAddress : EXPORT ON DEFAULT"""
    p[0] = Expr("""ExportAddress""", """EXPORT ON DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_ExportAddress_243(p):
    """ExportAddress : """
    p[0] = Expr("""ExportAddress""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_PortSpecification_244(p):
    """PortSpecification : PORT Iconst"""
    p[0] = Expr("""PortSpecification""", """PORT Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_PortSpecification_245(p):
    """PortSpecification : """
    p[0] = Expr("""PortSpecification""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_ControlAddress_246(p):
    """ControlAddress : HOSTNAME Sconst"""
    p[0] = Expr("""ControlAddress""", """HOSTNAME Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_ControlAddress_247(p):
    """ControlAddress : HOSTNAME DEFAULT"""
    p[0] = Expr("""ControlAddress""", """HOSTNAME DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_ControlAddress_248(p):
    """ControlAddress : """
    p[0] = Expr("""ControlAddress""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_BroadcastAddress_249(p):
    """BroadcastAddress : BROADCAST Sconst"""
    p[0] = Expr("""BroadcastAddress""", """BROADCAST Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_BroadcastAddress_250(p):
    """BroadcastAddress : """
    p[0] = Expr("""BroadcastAddress""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_ControlNode_251(p):
    """ControlNode : NODE name"""
    p[0] = Expr("""ControlNode""", """NODE name""", p[1:] if len(p or []) > 1 else [], p)


def p_ControlNode_252(p):
    """ControlNode : """
    p[0] = Expr("""ControlNode""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_ksafe_num_253(p):
    """ksafe_num : KSAFE Iconst"""
    p[0] = Expr("""ksafe_num""", """KSAFE Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_ksafe_num_254(p):
    """ksafe_num : KSAFE"""
    p[0] = Expr("""ksafe_num""", """KSAFE""", p[1:] if len(p or []) > 1 else [], p)


def p_ksafe_num_255(p):
    """ksafe_num : """
    p[0] = Expr("""ksafe_num""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_ksafe_num_required_256(p):
    """ksafe_num_required : KSAFE Iconst"""
    p[0] = Expr("""ksafe_num_required""", """KSAFE Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_ksafe_num_required_257(p):
    """ksafe_num_required : KSAFE"""
    p[0] = Expr("""ksafe_num_required""", """KSAFE""", p[1:] if len(p or []) > 1 else [], p)


def p_VSelectStmt_258(p):
    """VSelectStmt : SelectStmt"""
    p[0] = Expr("""VSelectStmt""", """SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_VSelectStmt_259(p):
    """VSelectStmt : VHistoricalSelectStmt"""
    p[0] = Expr("""VSelectStmt""", """VHistoricalSelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_VHistoricalSelectStmt_260(p):
    """VHistoricalSelectStmt : EpochOrTime SelectStmt"""
    p[0] = Expr("""VHistoricalSelectStmt""", """EpochOrTime SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_EpochOrTime_261(p):
    """EpochOrTime : EpochSpec"""
    p[0] = Expr("""EpochOrTime""", """EpochSpec""", p[1:] if len(p or []) > 1 else [], p)


def p_EpochOrTime_262(p):
    """EpochOrTime : TimeSpec"""
    p[0] = Expr("""EpochOrTime""", """TimeSpec""", p[1:] if len(p or []) > 1 else [], p)


def p_TimeSpec_263(p):
    """TimeSpec : AT TIME Sconst"""
    p[0] = Expr("""TimeSpec""", """AT TIME Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_EpochSpec_264(p):
    """EpochSpec : EpochNumber"""
    p[0] = Expr("""EpochSpec""", """EpochNumber""", p[1:] if len(p or []) > 1 else [], p)


def p_EpochSpec_265(p):
    """EpochSpec : EpochLatest"""
    p[0] = Expr("""EpochSpec""", """EpochLatest""", p[1:] if len(p or []) > 1 else [], p)


def p_EpochNumber_266(p):
    """EpochNumber : AT EPOCH_P Iconst"""
    p[0] = Expr("""EpochNumber""", """AT EPOCH_P Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_EpochLatest_267(p):
    """EpochLatest : AT EPOCH_P LATEST"""
    p[0] = Expr("""EpochLatest""", """AT EPOCH_P LATEST""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateLoadBalanceGroupStmt_268(p):
    """CreateLoadBalanceGroupStmt : CREATE LOAD BALANCE GROUP_P name opt_with ADDRESS name_list load_balance_policy"""
    p[0] = Expr("""CreateLoadBalanceGroupStmt""", """CREATE LOAD BALANCE GROUP_P name opt_with ADDRESS name_list load_balance_policy""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateLoadBalanceGroupStmt_269(p):
    """CreateLoadBalanceGroupStmt : CREATE LOAD BALANCE GROUP_P name opt_with load_balance_type name_list FILTER Sconst load_balance_policy"""
    p[0] = Expr("""CreateLoadBalanceGroupStmt""", """CREATE LOAD BALANCE GROUP_P name opt_with load_balance_type name_list FILTER Sconst load_balance_policy""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterLoadBalanceGroupStmt_270(p):
    """AlterLoadBalanceGroupStmt : ALTER LOAD BALANCE GROUP_P name ADD ADDRESS name_list"""
    p[0] = Expr("""AlterLoadBalanceGroupStmt""", """ALTER LOAD BALANCE GROUP_P name ADD ADDRESS name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterLoadBalanceGroupStmt_271(p):
    """AlterLoadBalanceGroupStmt : ALTER LOAD BALANCE GROUP_P name DROP ADDRESS name_list"""
    p[0] = Expr("""AlterLoadBalanceGroupStmt""", """ALTER LOAD BALANCE GROUP_P name DROP ADDRESS name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterLoadBalanceGroupStmt_272(p):
    """AlterLoadBalanceGroupStmt : ALTER LOAD BALANCE GROUP_P name DROP ADDRESS name_list ADD ADDRESS name_list"""
    p[0] = Expr("""AlterLoadBalanceGroupStmt""", """ALTER LOAD BALANCE GROUP_P name DROP ADDRESS name_list ADD ADDRESS name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterLoadBalanceGroupStmt_273(p):
    """AlterLoadBalanceGroupStmt : ALTER LOAD BALANCE GROUP_P name ADD FAULT GROUP_P name_list"""
    p[0] = Expr("""AlterLoadBalanceGroupStmt""", """ALTER LOAD BALANCE GROUP_P name ADD FAULT GROUP_P name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterLoadBalanceGroupStmt_274(p):
    """AlterLoadBalanceGroupStmt : ALTER LOAD BALANCE GROUP_P name ADD FAULT GROUP_P name_list SET FILTER TO Sconst"""
    p[0] = Expr("""AlterLoadBalanceGroupStmt""", """ALTER LOAD BALANCE GROUP_P name ADD FAULT GROUP_P name_list SET FILTER TO Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterLoadBalanceGroupStmt_275(p):
    """AlterLoadBalanceGroupStmt : ALTER LOAD BALANCE GROUP_P name DROP FAULT GROUP_P name_list"""
    p[0] = Expr("""AlterLoadBalanceGroupStmt""", """ALTER LOAD BALANCE GROUP_P name DROP FAULT GROUP_P name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterLoadBalanceGroupStmt_276(p):
    """AlterLoadBalanceGroupStmt : ALTER LOAD BALANCE GROUP_P name DROP FAULT GROUP_P name_list ADD FAULT GROUP_P name_list"""
    p[0] = Expr("""AlterLoadBalanceGroupStmt""", """ALTER LOAD BALANCE GROUP_P name DROP FAULT GROUP_P name_list ADD FAULT GROUP_P name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterLoadBalanceGroupStmt_277(p):
    """AlterLoadBalanceGroupStmt : ALTER LOAD BALANCE GROUP_P name RENAME TO name"""
    p[0] = Expr("""AlterLoadBalanceGroupStmt""", """ALTER LOAD BALANCE GROUP_P name RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterLoadBalanceGroupStmt_278(p):
    """AlterLoadBalanceGroupStmt : ALTER LOAD BALANCE GROUP_P name SET POLICY TO Sconst"""
    p[0] = Expr("""AlterLoadBalanceGroupStmt""", """ALTER LOAD BALANCE GROUP_P name SET POLICY TO Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterLoadBalanceGroupStmt_279(p):
    """AlterLoadBalanceGroupStmt : ALTER LOAD BALANCE GROUP_P name SET FILTER TO Sconst"""
    p[0] = Expr("""AlterLoadBalanceGroupStmt""", """ALTER LOAD BALANCE GROUP_P name SET FILTER TO Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_load_balance_type_280(p):
    """load_balance_type : FAULT GROUP_P"""
    p[0] = Expr("""load_balance_type""", """FAULT GROUP_P""", p[1:] if len(p or []) > 1 else [], p)


def p_load_balance_policy_281(p):
    """load_balance_policy : POLICY Sconst"""
    p[0] = Expr("""load_balance_policy""", """POLICY Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_load_balance_policy_282(p):
    """load_balance_policy : """
    p[0] = Expr("""load_balance_policy""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateRoutingRuleStmt_283(p):
    """CreateRoutingRuleStmt : CREATE ROUTING RULE name ROUTE Sconst TO name"""
    p[0] = Expr("""CreateRoutingRuleStmt""", """CREATE ROUTING RULE name ROUTE Sconst TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterRoutingRuleStmt_284(p):
    """AlterRoutingRuleStmt : ALTER ROUTING RULE name RENAME TO name"""
    p[0] = Expr("""AlterRoutingRuleStmt""", """ALTER ROUTING RULE name RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterRoutingRuleStmt_285(p):
    """AlterRoutingRuleStmt : ALTER ROUTING RULE name SET ROUTE TO Sconst"""
    p[0] = Expr("""AlterRoutingRuleStmt""", """ALTER ROUTING RULE name SET ROUTE TO Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterRoutingRuleStmt_286(p):
    """AlterRoutingRuleStmt : ALTER ROUTING RULE name SET GROUP_P TO name"""
    p[0] = Expr("""AlterRoutingRuleStmt""", """ALTER ROUTING RULE name SET GROUP_P TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateInterfaceStmt_287(p):
    """CreateInterfaceStmt : CREATE NETWORK Interface_or_address name ON name opt_with Sconst PortSpecification opt_enabled opt_nocheck"""
    p[0] = Expr("""CreateInterfaceStmt""", """CREATE NETWORK Interface_or_address name ON name opt_with Sconst PortSpecification opt_enabled opt_nocheck""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAddressStmt_288(p):
    """AlterAddressStmt : ALTER NETWORK ADDRESS name RENAME TO name"""
    p[0] = Expr("""AlterAddressStmt""", """ALTER NETWORK ADDRESS name RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAddressStmt_289(p):
    """AlterAddressStmt : ALTER NETWORK ADDRESS name SET TO Sconst PortSpecification"""
    p[0] = Expr("""AlterAddressStmt""", """ALTER NETWORK ADDRESS name SET TO Sconst PortSpecification""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAddressStmt_290(p):
    """AlterAddressStmt : ALTER NETWORK ADDRESS name enable_disable"""
    p[0] = Expr("""AlterAddressStmt""", """ALTER NETWORK ADDRESS name enable_disable""", p[1:] if len(p or []) > 1 else [], p)


def p_enable_disable_291(p):
    """enable_disable : ENABLE"""
    p[0] = Expr("""enable_disable""", """ENABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_enable_disable_292(p):
    """enable_disable : ENABLED"""
    p[0] = Expr("""enable_disable""", """ENABLED""", p[1:] if len(p or []) > 1 else [], p)


def p_enable_disable_293(p):
    """enable_disable : DISABLE"""
    p[0] = Expr("""enable_disable""", """DISABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_enable_disable_294(p):
    """enable_disable : DISABLED"""
    p[0] = Expr("""enable_disable""", """DISABLED""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_nocheck_295(p):
    """opt_nocheck : FORCE"""
    p[0] = Expr("""opt_nocheck""", """FORCE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_nocheck_296(p):
    """opt_nocheck : CHECK"""
    p[0] = Expr("""opt_nocheck""", """CHECK""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_nocheck_297(p):
    """opt_nocheck : """
    p[0] = Expr("""opt_nocheck""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_enabled_298(p):
    """opt_enabled : ENABLED"""
    p[0] = Expr("""opt_enabled""", """ENABLED""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_enabled_299(p):
    """opt_enabled : DISABLED"""
    p[0] = Expr("""opt_enabled""", """DISABLED""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_enabled_300(p):
    """opt_enabled : """
    p[0] = Expr("""opt_enabled""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_Interface_or_address_301(p):
    """Interface_or_address : INTERFACE"""
    p[0] = Expr("""Interface_or_address""", """INTERFACE""", p[1:] if len(p or []) > 1 else [], p)


def p_Interface_or_address_302(p):
    """Interface_or_address : ADDRESS"""
    p[0] = Expr("""Interface_or_address""", """ADDRESS""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateFaultGroupStmt_303(p):
    """CreateFaultGroupStmt : CREATE FAULT GROUP_P name"""
    p[0] = Expr("""CreateFaultGroupStmt""", """CREATE FAULT GROUP_P name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFaultGroupStmt_304(p):
    """AlterFaultGroupStmt : ALTER FAULT GROUP_P name ADD NODE name"""
    p[0] = Expr("""AlterFaultGroupStmt""", """ALTER FAULT GROUP_P name ADD NODE name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFaultGroupStmt_305(p):
    """AlterFaultGroupStmt : ALTER FAULT GROUP_P name DROP NODE name"""
    p[0] = Expr("""AlterFaultGroupStmt""", """ALTER FAULT GROUP_P name DROP NODE name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFaultGroupStmt_306(p):
    """AlterFaultGroupStmt : ALTER FAULT GROUP_P name ADD FAULT GROUP_P name"""
    p[0] = Expr("""AlterFaultGroupStmt""", """ALTER FAULT GROUP_P name ADD FAULT GROUP_P name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFaultGroupStmt_307(p):
    """AlterFaultGroupStmt : ALTER FAULT GROUP_P name DROP FAULT GROUP_P name"""
    p[0] = Expr("""AlterFaultGroupStmt""", """ALTER FAULT GROUP_P name DROP FAULT GROUP_P name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFaultGroupStmt_308(p):
    """AlterFaultGroupStmt : ALTER FAULT GROUP_P name RENAME TO name"""
    p[0] = Expr("""AlterFaultGroupStmt""", """ALTER FAULT GROUP_P name RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateBranchStmt_309(p):
    """CreateBranchStmt : CREATE DATA_P IMMUTABLE BRANCH auth_list opt_count opt_like opt_atver"""
    p[0] = Expr("""CreateBranchStmt""", """CREATE DATA_P IMMUTABLE BRANCH auth_list opt_count opt_like opt_atver""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_count_310(p):
    """opt_count : '*' Iconst"""
    p[0] = Expr("""opt_count""", """'*' Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_count_311(p):
    """opt_count : """
    p[0] = Expr("""opt_count""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_like_312(p):
    """opt_like : LIKE name"""
    p[0] = Expr("""opt_like""", """LIKE name""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_like_313(p):
    """opt_like : """
    p[0] = Expr("""opt_like""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_atver_314(p):
    """opt_atver : AT Iconst"""
    p[0] = Expr("""opt_atver""", """AT Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_atver_315(p):
    """opt_atver : """
    p[0] = Expr("""opt_atver""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateTuningRuleStmt_316(p):
    """CreateTuningRuleStmt : CREATE OptSystem TUNING RULE ColId '(' ColId ',' ColId OptSetTuningParamList ')' AS SelectStmt"""
    p[0] = Expr("""CreateTuningRuleStmt""", """CREATE OptSystem TUNING RULE ColId '(' ColId ',' ColId OptSetTuningParamList ')' AS SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSystem_317(p):
    """OptSystem : SYSTEM"""
    p[0] = Expr("""OptSystem""", """SYSTEM""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSystem_318(p):
    """OptSystem : """
    p[0] = Expr("""OptSystem""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSetTuningParamList_319(p):
    """OptSetTuningParamList : ',' SetParamList"""
    p[0] = Expr("""OptSetTuningParamList""", """',' SetParamList""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSetTuningParamList_320(p):
    """OptSetTuningParamList : """
    p[0] = Expr("""OptSetTuningParamList""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_SetParamList_321(p):
    """SetParamList : ColId '=' IntegerOnly"""
    p[0] = Expr("""SetParamList""", """ColId '=' IntegerOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_SetParamList_322(p):
    """SetParamList : SetParamList ',' ColId '=' IntegerOnly"""
    p[0] = Expr("""SetParamList""", """SetParamList ',' ColId '=' IntegerOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterTuningRuleStmt_323(p):
    """AlterTuningRuleStmt : ALTER TUNING RULE ColId SET SetParamList"""
    p[0] = Expr("""AlterTuningRuleStmt""", """ALTER TUNING RULE ColId SET SetParamList""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterTuningRuleStmt_324(p):
    """AlterTuningRuleStmt : ALTER TUNING RULE ColId DISABLE"""
    p[0] = Expr("""AlterTuningRuleStmt""", """ALTER TUNING RULE ColId DISABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterTuningRuleStmt_325(p):
    """AlterTuningRuleStmt : ALTER TUNING RULE ColId ENABLE"""
    p[0] = Expr("""AlterTuningRuleStmt""", """ALTER TUNING RULE ColId ENABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateUserStmt_326(p):
    """CreateUserStmt : CREATE USER UserId opt_with OptUserList"""
    p[0] = Expr("""CreateUserStmt""", """CREATE USER UserId opt_with OptUserList""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_with_327(p):
    """opt_with : WITH"""
    p[0] = Expr("""opt_with""", """WITH""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_with_328(p):
    """opt_with : """
    p[0] = Expr("""opt_with""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterUserStmt_329(p):
    """AlterUserStmt : ALTER USER UserId opt_with OptUserList"""
    p[0] = Expr("""AlterUserStmt""", """ALTER USER UserId opt_with OptUserList""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterUserSetStmt_330(p):
    """AlterUserSetStmt : ALTER USER UserId SET set_rest"""
    p[0] = Expr("""AlterUserSetStmt""", """ALTER USER UserId SET set_rest""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterUserSetStmt_331(p):
    """AlterUserSetStmt : ALTER USER UserId VariableResetStmt"""
    p[0] = Expr("""AlterUserSetStmt""", """ALTER USER UserId VariableResetStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterUserDefaultRoleStmt_332(p):
    """AlterUserDefaultRoleStmt : ALTER USER UserId DEFAULT ROLE var_list_or_default_all_except"""
    p[0] = Expr("""AlterUserDefaultRoleStmt""", """ALTER USER UserId DEFAULT ROLE var_list_or_default_all_except""", p[1:] if len(p or []) > 1 else [], p)


def p_DropUserStmt_333(p):
    """DropUserStmt : DROP USER IF_P EXISTS user_list opt_drop_behavior"""
    p[0] = Expr("""DropUserStmt""", """DROP USER IF_P EXISTS user_list opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_DropUserStmt_334(p):
    """DropUserStmt : DROP USER user_list opt_drop_behavior"""
    p[0] = Expr("""DropUserStmt""", """DROP USER user_list opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserList_335(p):
    """OptUserList : OptUserList OptUserElem"""
    p[0] = Expr("""OptUserList""", """OptUserList OptUserElem""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserList_336(p):
    """OptUserList : OptUserList IDENTIFIED BY Sconst REPLACE Sconst"""
    p[0] = Expr("""OptUserList""", """OptUserList IDENTIFIED BY Sconst REPLACE Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserList_337(p):
    """OptUserList : OptUserList MAXCONNECTIONS Iconst ON NODE"""
    p[0] = Expr("""OptUserList""", """OptUserList MAXCONNECTIONS Iconst ON NODE""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserList_338(p):
    """OptUserList : OptUserList MAXCONNECTIONS Iconst ON DATABASE"""
    p[0] = Expr("""OptUserList""", """OptUserList MAXCONNECTIONS Iconst ON DATABASE""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserList_339(p):
    """OptUserList : OptUserList MAXCONNECTIONS Iconst"""
    p[0] = Expr("""OptUserList""", """OptUserList MAXCONNECTIONS Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserList_340(p):
    """OptUserList : OptUserList MAXCONNECTIONS NONE"""
    p[0] = Expr("""OptUserList""", """OptUserList MAXCONNECTIONS NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserList_341(p):
    """OptUserList : """
    p[0] = Expr("""OptUserList""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_342(p):
    """OptUserElem : PASSWORD Sconst"""
    p[0] = Expr("""OptUserElem""", """PASSWORD Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_343(p):
    """OptUserElem : ENCRYPTED PASSWORD Sconst"""
    p[0] = Expr("""OptUserElem""", """ENCRYPTED PASSWORD Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_344(p):
    """OptUserElem : IDENTIFIED BY Sconst"""
    p[0] = Expr("""OptUserElem""", """IDENTIFIED BY Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_345(p):
    """OptUserElem : SYSID Iconst"""
    p[0] = Expr("""OptUserElem""", """SYSID Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_346(p):
    """OptUserElem : CREATEDB"""
    p[0] = Expr("""OptUserElem""", """CREATEDB""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_347(p):
    """OptUserElem : NOCREATEDB"""
    p[0] = Expr("""OptUserElem""", """NOCREATEDB""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_348(p):
    """OptUserElem : CREATEUSER"""
    p[0] = Expr("""OptUserElem""", """CREATEUSER""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_349(p):
    """OptUserElem : NOCREATEUSER"""
    p[0] = Expr("""OptUserElem""", """NOCREATEUSER""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_350(p):
    """OptUserElem : IN_P GROUP_P user_list"""
    p[0] = Expr("""OptUserElem""", """IN_P GROUP_P user_list""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_351(p):
    """OptUserElem : PASSWORD EXPIRE"""
    p[0] = Expr("""OptUserElem""", """PASSWORD EXPIRE""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_352(p):
    """OptUserElem : ACCOUNT LOCK_P"""
    p[0] = Expr("""OptUserElem""", """ACCOUNT LOCK_P""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_353(p):
    """OptUserElem : ACCOUNT UNLOCK_P"""
    p[0] = Expr("""OptUserElem""", """ACCOUNT UNLOCK_P""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_354(p):
    """OptUserElem : PROFILE ProfileId"""
    p[0] = Expr("""OptUserElem""", """PROFILE ProfileId""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_355(p):
    """OptUserElem : RESOURCE POOL name"""
    p[0] = Expr("""OptUserElem""", """RESOURCE POOL name""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_356(p):
    """OptUserElem : MEMORYCAP Sconst"""
    p[0] = Expr("""OptUserElem""", """MEMORYCAP Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_357(p):
    """OptUserElem : MEMORYCAP NONE"""
    p[0] = Expr("""OptUserElem""", """MEMORYCAP NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_358(p):
    """OptUserElem : TEMPSPACECAP Sconst"""
    p[0] = Expr("""OptUserElem""", """TEMPSPACECAP Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_359(p):
    """OptUserElem : TEMPSPACECAP NONE"""
    p[0] = Expr("""OptUserElem""", """TEMPSPACECAP NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_360(p):
    """OptUserElem : RUNTIMECAP Sconst"""
    p[0] = Expr("""OptUserElem""", """RUNTIMECAP Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_361(p):
    """OptUserElem : RUNTIMECAP NONE"""
    p[0] = Expr("""OptUserElem""", """RUNTIMECAP NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_362(p):
    """OptUserElem : IDLESESSIONTIMEOUT Sconst"""
    p[0] = Expr("""OptUserElem""", """IDLESESSIONTIMEOUT Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_363(p):
    """OptUserElem : IDLESESSIONTIMEOUT NONE"""
    p[0] = Expr("""OptUserElem""", """IDLESESSIONTIMEOUT NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_364(p):
    """OptUserElem : GRACEPERIOD Sconst"""
    p[0] = Expr("""OptUserElem""", """GRACEPERIOD Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_365(p):
    """OptUserElem : GRACEPERIOD NONE"""
    p[0] = Expr("""OptUserElem""", """GRACEPERIOD NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_366(p):
    """OptUserElem : SEARCH_PATH var_list_or_default"""
    p[0] = Expr("""OptUserElem""", """SEARCH_PATH var_list_or_default""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUserElem_367(p):
    """OptUserElem : SECURITY_ALGORITHM Sconst"""
    p[0] = Expr("""OptUserElem""", """SECURITY_ALGORITHM Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_user_list_368(p):
    """user_list : user_list ',' UserId"""
    p[0] = Expr("""user_list""", """user_list ',' UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_user_list_369(p):
    """user_list : UserId"""
    p[0] = Expr("""user_list""", """UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAccessPolicyStmt_370(p):
    """CreateAccessPolicyStmt : CREATE ACCESS POLICY ON qualified_name FOR ROWS WHERE a_expr optDisableEnableParam"""
    p[0] = Expr("""CreateAccessPolicyStmt""", """CREATE ACCESS POLICY ON qualified_name FOR ROWS WHERE a_expr optDisableEnableParam""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAccessPolicyStmt_371(p):
    """CreateAccessPolicyStmt : CREATE ACCESS POLICY ON qualified_name FOR COLUMN columnElem a_expr optDisableEnableParam"""
    p[0] = Expr("""CreateAccessPolicyStmt""", """CREATE ACCESS POLICY ON qualified_name FOR COLUMN columnElem a_expr optDisableEnableParam""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAccessPolicyStmt_372(p):
    """AlterAccessPolicyStmt : ALTER ACCESS POLICY ON qualified_name FOR ROWS WHERE a_expr optDisableEnableParam"""
    p[0] = Expr("""AlterAccessPolicyStmt""", """ALTER ACCESS POLICY ON qualified_name FOR ROWS WHERE a_expr optDisableEnableParam""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAccessPolicyStmt_373(p):
    """AlterAccessPolicyStmt : ALTER ACCESS POLICY ON qualified_name FOR ROWS optDisableEnableParam"""
    p[0] = Expr("""AlterAccessPolicyStmt""", """ALTER ACCESS POLICY ON qualified_name FOR ROWS optDisableEnableParam""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAccessPolicyStmt_374(p):
    """AlterAccessPolicyStmt : ALTER ACCESS POLICY ON qualified_name FOR COLUMN columnElem a_expr optDisableEnableParam"""
    p[0] = Expr("""AlterAccessPolicyStmt""", """ALTER ACCESS POLICY ON qualified_name FOR COLUMN columnElem a_expr optDisableEnableParam""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAccessPolicyStmt_375(p):
    """AlterAccessPolicyStmt : ALTER ACCESS POLICY ON qualified_name FOR COLUMN columnElem optDisableEnableParam"""
    p[0] = Expr("""AlterAccessPolicyStmt""", """ALTER ACCESS POLICY ON qualified_name FOR COLUMN columnElem optDisableEnableParam""", p[1:] if len(p or []) > 1 else [], p)


def p_CopyAccessPolicyStmt_376(p):
    """CopyAccessPolicyStmt : ALTER ACCESS POLICY ON qualified_name FOR ROWS COPY TO TABLE qualified_name"""
    p[0] = Expr("""CopyAccessPolicyStmt""", """ALTER ACCESS POLICY ON qualified_name FOR ROWS COPY TO TABLE qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_CopyAccessPolicyStmt_377(p):
    """CopyAccessPolicyStmt : ALTER ACCESS POLICY ON qualified_name FOR COLUMN columnElem COPY TO TABLE qualified_name"""
    p[0] = Expr("""CopyAccessPolicyStmt""", """ALTER ACCESS POLICY ON qualified_name FOR COLUMN columnElem COPY TO TABLE qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_DropAccessPolicyStmt_378(p):
    """DropAccessPolicyStmt : DROP ACCESS POLICY ON qualified_name FOR ROWS"""
    p[0] = Expr("""DropAccessPolicyStmt""", """DROP ACCESS POLICY ON qualified_name FOR ROWS""", p[1:] if len(p or []) > 1 else [], p)


def p_DropAccessPolicyStmt_379(p):
    """DropAccessPolicyStmt : DROP ACCESS POLICY ON qualified_name FOR COLUMN columnElem"""
    p[0] = Expr("""DropAccessPolicyStmt""", """DROP ACCESS POLICY ON qualified_name FOR COLUMN columnElem""", p[1:] if len(p or []) > 1 else [], p)


def p_optDisableEnableParam_380(p):
    """optDisableEnableParam : ENABLE"""
    p[0] = Expr("""optDisableEnableParam""", """ENABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_optDisableEnableParam_381(p):
    """optDisableEnableParam : DISABLE"""
    p[0] = Expr("""optDisableEnableParam""", """DISABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateNotifierStmt_382(p):
    """CreateNotifierStmt : CREATE NOTIFIER IF_P NOT EXISTS name optActionName optEnableDisableParam optMaxPayloadParam optMaxMemorySizeParam optIdentifiedByParam optConfirmDeliveryParam optParameters"""
    p[0] = Expr("""CreateNotifierStmt""", """CREATE NOTIFIER IF_P NOT EXISTS name optActionName optEnableDisableParam optMaxPayloadParam optMaxMemorySizeParam optIdentifiedByParam optConfirmDeliveryParam optParameters""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateNotifierStmt_383(p):
    """CreateNotifierStmt : CREATE NOTIFIER name optActionName optEnableDisableParam optMaxPayloadParam optMaxMemorySizeParam optIdentifiedByParam optConfirmDeliveryParam optParameters"""
    p[0] = Expr("""CreateNotifierStmt""", """CREATE NOTIFIER name optActionName optEnableDisableParam optMaxPayloadParam optMaxMemorySizeParam optIdentifiedByParam optConfirmDeliveryParam optParameters""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterNotifierStmt_384(p):
    """AlterNotifierStmt : ALTER NOTIFIER name optActionName optNotifierParams"""
    p[0] = Expr("""AlterNotifierStmt""", """ALTER NOTIFIER name optActionName optNotifierParams""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterNotifierStmt_385(p):
    """AlterNotifierStmt : ALTER NOTIFIER name optNotifierParams"""
    p[0] = Expr("""AlterNotifierStmt""", """ALTER NOTIFIER name optNotifierParams""", p[1:] if len(p or []) > 1 else [], p)


def p_optNotifierParams_386(p):
    """optNotifierParams : notifierParams"""
    p[0] = Expr("""optNotifierParams""", """notifierParams""", p[1:] if len(p or []) > 1 else [], p)


def p_optNotifierParams_387(p):
    """optNotifierParams : """
    p[0] = Expr("""optNotifierParams""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_notifierParams_388(p):
    """notifierParams : notifierParams notifierParam"""
    p[0] = Expr("""notifierParams""", """notifierParams notifierParam""", p[1:] if len(p or []) > 1 else [], p)


def p_notifierParams_389(p):
    """notifierParams : notifierParam"""
    p[0] = Expr("""notifierParams""", """notifierParam""", p[1:] if len(p or []) > 1 else [], p)


def p_notifierParam_390(p):
    """notifierParam : ENABLE"""
    p[0] = Expr("""notifierParam""", """ENABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_notifierParam_391(p):
    """notifierParam : DISABLE"""
    p[0] = Expr("""notifierParam""", """DISABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_notifierParam_392(p):
    """notifierParam : MAXPAYLOAD NONE"""
    p[0] = Expr("""notifierParam""", """MAXPAYLOAD NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_notifierParam_393(p):
    """notifierParam : MAXPAYLOAD Sconst"""
    p[0] = Expr("""notifierParam""", """MAXPAYLOAD Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_notifierParam_394(p):
    """notifierParam : MAXMEMORYSIZE Sconst"""
    p[0] = Expr("""notifierParam""", """MAXMEMORYSIZE Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_notifierParam_395(p):
    """notifierParam : IDENTIFIED BY NONE"""
    p[0] = Expr("""notifierParam""", """IDENTIFIED BY NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_notifierParam_396(p):
    """notifierParam : IDENTIFIED BY Sconst"""
    p[0] = Expr("""notifierParam""", """IDENTIFIED BY Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_notifierParam_397(p):
    """notifierParam : CHECK COMMITTED"""
    p[0] = Expr("""notifierParam""", """CHECK COMMITTED""", p[1:] if len(p or []) > 1 else [], p)


def p_notifierParam_398(p):
    """notifierParam : NO CHECK COMMITTED"""
    p[0] = Expr("""notifierParam""", """NO CHECK COMMITTED""", p[1:] if len(p or []) > 1 else [], p)


def p_notifierParam_399(p):
    """notifierParam : PARAMETERS NONE"""
    p[0] = Expr("""notifierParam""", """PARAMETERS NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_notifierParam_400(p):
    """notifierParam : PARAMETERS Sconst"""
    p[0] = Expr("""notifierParam""", """PARAMETERS Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_optActionName_401(p):
    """optActionName : ACTION Sconst"""
    p[0] = Expr("""optActionName""", """ACTION Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_optIdentifiedByParam_402(p):
    """optIdentifiedByParam : IDENTIFIED BY NONE"""
    p[0] = Expr("""optIdentifiedByParam""", """IDENTIFIED BY NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_optIdentifiedByParam_403(p):
    """optIdentifiedByParam : IDENTIFIED BY Sconst"""
    p[0] = Expr("""optIdentifiedByParam""", """IDENTIFIED BY Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_optIdentifiedByParam_404(p):
    """optIdentifiedByParam : """
    p[0] = Expr("""optIdentifiedByParam""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_optMaxPayloadParam_405(p):
    """optMaxPayloadParam : MAXPAYLOAD NONE"""
    p[0] = Expr("""optMaxPayloadParam""", """MAXPAYLOAD NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_optMaxPayloadParam_406(p):
    """optMaxPayloadParam : MAXPAYLOAD Sconst"""
    p[0] = Expr("""optMaxPayloadParam""", """MAXPAYLOAD Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_optMaxPayloadParam_407(p):
    """optMaxPayloadParam : """
    p[0] = Expr("""optMaxPayloadParam""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_optMaxMemorySizeParam_408(p):
    """optMaxMemorySizeParam : MAXMEMORYSIZE Sconst"""
    p[0] = Expr("""optMaxMemorySizeParam""", """MAXMEMORYSIZE Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_optConfirmDeliveryParam_409(p):
    """optConfirmDeliveryParam : NO CHECK COMMITTED"""
    p[0] = Expr("""optConfirmDeliveryParam""", """NO CHECK COMMITTED""", p[1:] if len(p or []) > 1 else [], p)


def p_optConfirmDeliveryParam_410(p):
    """optConfirmDeliveryParam : CHECK COMMITTED"""
    p[0] = Expr("""optConfirmDeliveryParam""", """CHECK COMMITTED""", p[1:] if len(p or []) > 1 else [], p)


def p_optConfirmDeliveryParam_411(p):
    """optConfirmDeliveryParam : """
    p[0] = Expr("""optConfirmDeliveryParam""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_optParameters_412(p):
    """optParameters : PARAMETERS NONE"""
    p[0] = Expr("""optParameters""", """PARAMETERS NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_optParameters_413(p):
    """optParameters : PARAMETERS Sconst"""
    p[0] = Expr("""optParameters""", """PARAMETERS Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_optParameters_414(p):
    """optParameters : """
    p[0] = Expr("""optParameters""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAuthStmt_415(p):
    """CreateAuthStmt : CREATE AUTHENTICATION name METHOD authMethodName LOCAL optEnableDisableParam"""
    p[0] = Expr("""CreateAuthStmt""", """CREATE AUTHENTICATION name METHOD authMethodName LOCAL optEnableDisableParam""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAuthStmt_416(p):
    """CreateAuthStmt : CREATE AUTHENTICATION name METHOD authMethodName HOST optHOSTParam authHostIPAddress optEnableDisableParam"""
    p[0] = Expr("""CreateAuthStmt""", """CREATE AUTHENTICATION name METHOD authMethodName HOST optHOSTParam authHostIPAddress optEnableDisableParam""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAuthStmt_417(p):
    """AlterAuthStmt : ALTER AUTHENTICATION name METHOD authMethodName LOCAL nonoptEnableDisableParam"""
    p[0] = Expr("""AlterAuthStmt""", """ALTER AUTHENTICATION name METHOD authMethodName LOCAL nonoptEnableDisableParam""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAuthStmt_418(p):
    """AlterAuthStmt : ALTER AUTHENTICATION name METHOD authMethodName HOST optHOSTParam authHostIPAddress nonoptEnableDisableParam"""
    p[0] = Expr("""AlterAuthStmt""", """ALTER AUTHENTICATION name METHOD authMethodName HOST optHOSTParam authHostIPAddress nonoptEnableDisableParam""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAuthStmt_419(p):
    """AlterAuthStmt : ALTER AUTHENTICATION name METHOD authMethodName"""
    p[0] = Expr("""AlterAuthStmt""", """ALTER AUTHENTICATION name METHOD authMethodName""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAuthStmt_420(p):
    """AlterAuthStmt : ALTER AUTHENTICATION name nonoptEnableDisableParam"""
    p[0] = Expr("""AlterAuthStmt""", """ALTER AUTHENTICATION name nonoptEnableDisableParam""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAuthStmt_421(p):
    """AlterAuthStmt : ALTER AUTHENTICATION name LOCAL"""
    p[0] = Expr("""AlterAuthStmt""", """ALTER AUTHENTICATION name LOCAL""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAuthStmt_422(p):
    """AlterAuthStmt : ALTER AUTHENTICATION name HOST optHOSTParam authHostIPAddress"""
    p[0] = Expr("""AlterAuthStmt""", """ALTER AUTHENTICATION name HOST optHOSTParam authHostIPAddress""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAuthStmt_423(p):
    """AlterAuthStmt : ALTER AUTHENTICATION name SET optAuthParamList"""
    p[0] = Expr("""AlterAuthStmt""", """ALTER AUTHENTICATION name SET optAuthParamList""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterAuthStmt_424(p):
    """AlterAuthStmt : ALTER AUTHENTICATION name PRIORITY Iconst"""
    p[0] = Expr("""AlterAuthStmt""", """ALTER AUTHENTICATION name PRIORITY Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_optHOSTParam_425(p):
    """optHOSTParam : TLS"""
    p[0] = Expr("""optHOSTParam""", """TLS""", p[1:] if len(p or []) > 1 else [], p)


def p_optHOSTParam_426(p):
    """optHOSTParam : NO TLS"""
    p[0] = Expr("""optHOSTParam""", """NO TLS""", p[1:] if len(p or []) > 1 else [], p)


def p_optHOSTParam_427(p):
    """optHOSTParam : """
    p[0] = Expr("""optHOSTParam""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_optEnableDisableParam_428(p):
    """optEnableDisableParam : ENABLE"""
    p[0] = Expr("""optEnableDisableParam""", """ENABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_optEnableDisableParam_429(p):
    """optEnableDisableParam : DISABLE"""
    p[0] = Expr("""optEnableDisableParam""", """DISABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_optEnableDisableParam_430(p):
    """optEnableDisableParam : """
    p[0] = Expr("""optEnableDisableParam""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_nonoptEnableDisableParam_431(p):
    """nonoptEnableDisableParam : ENABLE"""
    p[0] = Expr("""nonoptEnableDisableParam""", """ENABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_nonoptEnableDisableParam_432(p):
    """nonoptEnableDisableParam : DISABLE"""
    p[0] = Expr("""nonoptEnableDisableParam""", """DISABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_authMethodName_433(p):
    """authMethodName : Sconst"""
    p[0] = Expr("""authMethodName""", """Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_authHostIPAddress_434(p):
    """authHostIPAddress : Sconst"""
    p[0] = Expr("""authHostIPAddress""", """Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_optAuthParamList_435(p):
    """optAuthParamList : optAuthParamElem"""
    p[0] = Expr("""optAuthParamList""", """optAuthParamElem""", p[1:] if len(p or []) > 1 else [], p)


def p_optAuthParamList_436(p):
    """optAuthParamList : optAuthParamList ',' optAuthParamElem"""
    p[0] = Expr("""optAuthParamList""", """optAuthParamList ',' optAuthParamElem""", p[1:] if len(p or []) > 1 else [], p)


def p_optAuthParamElem_437(p):
    """optAuthParamElem : name '=' Sconst"""
    p[0] = Expr("""optAuthParamElem""", """name '=' Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateProfileStmt_438(p):
    """CreateProfileStmt : CREATE PROFILE ProfileId LIMIT OptProfileList"""
    p[0] = Expr("""CreateProfileStmt""", """CREATE PROFILE ProfileId LIMIT OptProfileList""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterProfileStmt_439(p):
    """AlterProfileStmt : ALTER PROFILE ProfileId LIMIT OptProfileList"""
    p[0] = Expr("""AlterProfileStmt""", """ALTER PROFILE ProfileId LIMIT OptProfileList""", p[1:] if len(p or []) > 1 else [], p)


def p_OptProfileList_440(p):
    """OptProfileList : OptProfileList OptProfileElem"""
    p[0] = Expr("""OptProfileList""", """OptProfileList OptProfileElem""", p[1:] if len(p or []) > 1 else [], p)


def p_OptProfileList_441(p):
    """OptProfileList : """
    p[0] = Expr("""OptProfileList""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptProfileElem_442(p):
    """OptProfileElem : PasswordParamIndex PasswordParamExpr"""
    p[0] = Expr("""OptProfileElem""", """PasswordParamIndex PasswordParamExpr""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamIndex_443(p):
    """PasswordParamIndex : PASSWORD_LIFE_TIME"""
    p[0] = Expr("""PasswordParamIndex""", """PASSWORD_LIFE_TIME""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamIndex_444(p):
    """PasswordParamIndex : PASSWORD_REUSE_MAX"""
    p[0] = Expr("""PasswordParamIndex""", """PASSWORD_REUSE_MAX""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamIndex_445(p):
    """PasswordParamIndex : PASSWORD_REUSE_TIME"""
    p[0] = Expr("""PasswordParamIndex""", """PASSWORD_REUSE_TIME""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamIndex_446(p):
    """PasswordParamIndex : PASSWORD_GRACE_TIME"""
    p[0] = Expr("""PasswordParamIndex""", """PASSWORD_GRACE_TIME""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamIndex_447(p):
    """PasswordParamIndex : PASSWORD_LOCK_TIME"""
    p[0] = Expr("""PasswordParamIndex""", """PASSWORD_LOCK_TIME""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamIndex_448(p):
    """PasswordParamIndex : FAILED_LOGIN_ATTEMPTS"""
    p[0] = Expr("""PasswordParamIndex""", """FAILED_LOGIN_ATTEMPTS""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamIndex_449(p):
    """PasswordParamIndex : PASSWORD_MAX_LENGTH"""
    p[0] = Expr("""PasswordParamIndex""", """PASSWORD_MAX_LENGTH""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamIndex_450(p):
    """PasswordParamIndex : PASSWORD_MIN_LENGTH"""
    p[0] = Expr("""PasswordParamIndex""", """PASSWORD_MIN_LENGTH""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamIndex_451(p):
    """PasswordParamIndex : PASSWORD_MIN_LETTERS"""
    p[0] = Expr("""PasswordParamIndex""", """PASSWORD_MIN_LETTERS""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamIndex_452(p):
    """PasswordParamIndex : PASSWORD_MIN_UPPERCASE_LETTERS"""
    p[0] = Expr("""PasswordParamIndex""", """PASSWORD_MIN_UPPERCASE_LETTERS""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamIndex_453(p):
    """PasswordParamIndex : PASSWORD_MIN_LOWERCASE_LETTERS"""
    p[0] = Expr("""PasswordParamIndex""", """PASSWORD_MIN_LOWERCASE_LETTERS""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamIndex_454(p):
    """PasswordParamIndex : PASSWORD_MIN_DIGITS"""
    p[0] = Expr("""PasswordParamIndex""", """PASSWORD_MIN_DIGITS""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamIndex_455(p):
    """PasswordParamIndex : PASSWORD_MIN_SYMBOLS"""
    p[0] = Expr("""PasswordParamIndex""", """PASSWORD_MIN_SYMBOLS""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamExpr_456(p):
    """PasswordParamExpr : Iconst"""
    p[0] = Expr("""PasswordParamExpr""", """Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamExpr_457(p):
    """PasswordParamExpr : DEFAULT"""
    p[0] = Expr("""PasswordParamExpr""", """DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_PasswordParamExpr_458(p):
    """PasswordParamExpr : UNLIMITED"""
    p[0] = Expr("""PasswordParamExpr""", """UNLIMITED""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateRoleStmt_459(p):
    """CreateRoleStmt : CREATE ROLE UserId"""
    p[0] = Expr("""CreateRoleStmt""", """CREATE ROLE UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateModelStmt_460(p):
    """CreateModelStmt : CREATE MODEL qualified_name"""
    p[0] = Expr("""CreateModelStmt""", """CREATE MODEL qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterModelStmt_461(p):
    """AlterModelStmt : ALTER MODEL relation_expr alter_model_cmds"""
    p[0] = Expr("""AlterModelStmt""", """ALTER MODEL relation_expr alter_model_cmds""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_model_cmds_462(p):
    """alter_model_cmds : alter_model_cmd"""
    p[0] = Expr("""alter_model_cmds""", """alter_model_cmd""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_model_cmds_463(p):
    """alter_model_cmds : alter_model_cmds ',' alter_model_cmd"""
    p[0] = Expr("""alter_model_cmds""", """alter_model_cmds ',' alter_model_cmd""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_model_cmd_464(p):
    """alter_model_cmd : OWNER TO UserId"""
    p[0] = Expr("""alter_model_cmd""", """OWNER TO UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_model_cmd_465(p):
    """alter_model_cmd : SET SCHEMA qualified_schema_name"""
    p[0] = Expr("""alter_model_cmd""", """SET SCHEMA qualified_schema_name""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateGroupStmt_466(p):
    """CreateGroupStmt : CREATE GROUP_P UserId opt_with OptGroupList"""
    p[0] = Expr("""CreateGroupStmt""", """CREATE GROUP_P UserId opt_with OptGroupList""", p[1:] if len(p or []) > 1 else [], p)


def p_OptGroupList_467(p):
    """OptGroupList : OptGroupList OptGroupElem"""
    p[0] = Expr("""OptGroupList""", """OptGroupList OptGroupElem""", p[1:] if len(p or []) > 1 else [], p)


def p_OptGroupList_468(p):
    """OptGroupList : """
    p[0] = Expr("""OptGroupList""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptGroupElem_469(p):
    """OptGroupElem : USER user_list"""
    p[0] = Expr("""OptGroupElem""", """USER user_list""", p[1:] if len(p or []) > 1 else [], p)


def p_OptGroupElem_470(p):
    """OptGroupElem : SYSID Iconst"""
    p[0] = Expr("""OptGroupElem""", """SYSID Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterGroupStmt_471(p):
    """AlterGroupStmt : ALTER GROUP_P UserId add_drop USER user_list"""
    p[0] = Expr("""AlterGroupStmt""", """ALTER GROUP_P UserId add_drop USER user_list""", p[1:] if len(p or []) > 1 else [], p)


def p_add_drop_472(p):
    """add_drop : ADD"""
    p[0] = Expr("""add_drop""", """ADD""", p[1:] if len(p or []) > 1 else [], p)


def p_add_drop_473(p):
    """add_drop : DROP"""
    p[0] = Expr("""add_drop""", """DROP""", p[1:] if len(p or []) > 1 else [], p)


def p_DropGroupStmt_474(p):
    """DropGroupStmt : DROP GROUP_P UserId"""
    p[0] = Expr("""DropGroupStmt""", """DROP GROUP_P UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateResourcePoolStmt_475(p):
    """CreateResourcePoolStmt : CREATE RESOURCE POOL name opt_res_pool_params"""
    p[0] = Expr("""CreateResourcePoolStmt""", """CREATE RESOURCE POOL name opt_res_pool_params""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_res_pool_params_476(p):
    """opt_res_pool_params : res_pool_params"""
    p[0] = Expr("""opt_res_pool_params""", """res_pool_params""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_res_pool_params_477(p):
    """opt_res_pool_params : """
    p[0] = Expr("""opt_res_pool_params""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_params_478(p):
    """res_pool_params : res_pool_params res_pool_param"""
    p[0] = Expr("""res_pool_params""", """res_pool_params res_pool_param""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_params_479(p):
    """res_pool_params : res_pool_param"""
    p[0] = Expr("""res_pool_params""", """res_pool_param""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_480(p):
    """res_pool_param : MEMORYSIZE Sconst"""
    p[0] = Expr("""res_pool_param""", """MEMORYSIZE Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_481(p):
    """res_pool_param : MEMORYSIZE DEFAULT"""
    p[0] = Expr("""res_pool_param""", """MEMORYSIZE DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_482(p):
    """res_pool_param : MAXMEMORYSIZE Sconst"""
    p[0] = Expr("""res_pool_param""", """MAXMEMORYSIZE Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_483(p):
    """res_pool_param : MAXMEMORYSIZE NONE"""
    p[0] = Expr("""res_pool_param""", """MAXMEMORYSIZE NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_484(p):
    """res_pool_param : MAXMEMORYSIZE DEFAULT"""
    p[0] = Expr("""res_pool_param""", """MAXMEMORYSIZE DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_485(p):
    """res_pool_param : MAXQUERYMEMORYSIZE Sconst"""
    p[0] = Expr("""res_pool_param""", """MAXQUERYMEMORYSIZE Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_486(p):
    """res_pool_param : MAXQUERYMEMORYSIZE NONE"""
    p[0] = Expr("""res_pool_param""", """MAXQUERYMEMORYSIZE NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_487(p):
    """res_pool_param : MAXQUERYMEMORYSIZE DEFAULT"""
    p[0] = Expr("""res_pool_param""", """MAXQUERYMEMORYSIZE DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_488(p):
    """res_pool_param : EXECUTIONPARALLELISM Iconst"""
    p[0] = Expr("""res_pool_param""", """EXECUTIONPARALLELISM Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_489(p):
    """res_pool_param : EXECUTIONPARALLELISM AUTO"""
    p[0] = Expr("""res_pool_param""", """EXECUTIONPARALLELISM AUTO""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_490(p):
    """res_pool_param : EXECUTIONPARALLELISM DEFAULT"""
    p[0] = Expr("""res_pool_param""", """EXECUTIONPARALLELISM DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_491(p):
    """res_pool_param : QUEUETIMEOUT Sconst"""
    p[0] = Expr("""res_pool_param""", """QUEUETIMEOUT Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_492(p):
    """res_pool_param : QUEUETIMEOUT Iconst"""
    p[0] = Expr("""res_pool_param""", """QUEUETIMEOUT Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_493(p):
    """res_pool_param : QUEUETIMEOUT NONE"""
    p[0] = Expr("""res_pool_param""", """QUEUETIMEOUT NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_494(p):
    """res_pool_param : QUEUETIMEOUT DEFAULT"""
    p[0] = Expr("""res_pool_param""", """QUEUETIMEOUT DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_495(p):
    """res_pool_param : PRIORITY IntegerOnly"""
    p[0] = Expr("""res_pool_param""", """PRIORITY IntegerOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_496(p):
    """res_pool_param : PRIORITY DEFAULT"""
    p[0] = Expr("""res_pool_param""", """PRIORITY DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_497(p):
    """res_pool_param : PRIORITY HOLD"""
    p[0] = Expr("""res_pool_param""", """PRIORITY HOLD""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_498(p):
    """res_pool_param : PLANNEDCONCURRENCY Iconst"""
    p[0] = Expr("""res_pool_param""", """PLANNEDCONCURRENCY Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_499(p):
    """res_pool_param : PLANNEDCONCURRENCY AUTO"""
    p[0] = Expr("""res_pool_param""", """PLANNEDCONCURRENCY AUTO""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_500(p):
    """res_pool_param : PLANNEDCONCURRENCY DEFAULT"""
    p[0] = Expr("""res_pool_param""", """PLANNEDCONCURRENCY DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_501(p):
    """res_pool_param : RUNTIMEPRIORITY RuntimePriorityValue"""
    p[0] = Expr("""res_pool_param""", """RUNTIMEPRIORITY RuntimePriorityValue""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_502(p):
    """res_pool_param : RUNTIMEPRIORITY DEFAULT"""
    p[0] = Expr("""res_pool_param""", """RUNTIMEPRIORITY DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_503(p):
    """res_pool_param : RUNTIMETHRESHOLD Iconst"""
    p[0] = Expr("""res_pool_param""", """RUNTIMETHRESHOLD Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_504(p):
    """res_pool_param : RUNTIMETHRESHOLD DEFAULT"""
    p[0] = Expr("""res_pool_param""", """RUNTIMETHRESHOLD DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_505(p):
    """res_pool_param : SINGLEINITIATOR simple_boolean"""
    p[0] = Expr("""res_pool_param""", """SINGLEINITIATOR simple_boolean""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_506(p):
    """res_pool_param : SINGLEINITIATOR AUTO"""
    p[0] = Expr("""res_pool_param""", """SINGLEINITIATOR AUTO""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_507(p):
    """res_pool_param : SINGLEINITIATOR DEFAULT"""
    p[0] = Expr("""res_pool_param""", """SINGLEINITIATOR DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_508(p):
    """res_pool_param : MAXCONCURRENCY Iconst"""
    p[0] = Expr("""res_pool_param""", """MAXCONCURRENCY Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_509(p):
    """res_pool_param : MAXCONCURRENCY NONE"""
    p[0] = Expr("""res_pool_param""", """MAXCONCURRENCY NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_510(p):
    """res_pool_param : MAXCONCURRENCY DEFAULT"""
    p[0] = Expr("""res_pool_param""", """MAXCONCURRENCY DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_511(p):
    """res_pool_param : MAXCONCURRENCYGRACE Iconst"""
    p[0] = Expr("""res_pool_param""", """MAXCONCURRENCYGRACE Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_512(p):
    """res_pool_param : RUNTIMECAP Sconst"""
    p[0] = Expr("""res_pool_param""", """RUNTIMECAP Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_513(p):
    """res_pool_param : RUNTIMECAP NONE"""
    p[0] = Expr("""res_pool_param""", """RUNTIMECAP NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_514(p):
    """res_pool_param : RUNTIMECAP DEFAULT"""
    p[0] = Expr("""res_pool_param""", """RUNTIMECAP DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_515(p):
    """res_pool_param : CPUAFFINITYSET Sconst"""
    p[0] = Expr("""res_pool_param""", """CPUAFFINITYSET Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_516(p):
    """res_pool_param : CPUAFFINITYSET Iconst"""
    p[0] = Expr("""res_pool_param""", """CPUAFFINITYSET Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_517(p):
    """res_pool_param : CPUAFFINITYSET NONE"""
    p[0] = Expr("""res_pool_param""", """CPUAFFINITYSET NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_518(p):
    """res_pool_param : CPUAFFINITYSET DEFAULT"""
    p[0] = Expr("""res_pool_param""", """CPUAFFINITYSET DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_519(p):
    """res_pool_param : CPUAFFINITYMODE ANY"""
    p[0] = Expr("""res_pool_param""", """CPUAFFINITYMODE ANY""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_520(p):
    """res_pool_param : CPUAFFINITYMODE SHARED"""
    p[0] = Expr("""res_pool_param""", """CPUAFFINITYMODE SHARED""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_521(p):
    """res_pool_param : CPUAFFINITYMODE EXCLUSIVE"""
    p[0] = Expr("""res_pool_param""", """CPUAFFINITYMODE EXCLUSIVE""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_522(p):
    """res_pool_param : CPUAFFINITYMODE DEFAULT"""
    p[0] = Expr("""res_pool_param""", """CPUAFFINITYMODE DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_523(p):
    """res_pool_param : CASCADE TO name"""
    p[0] = Expr("""res_pool_param""", """CASCADE TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_res_pool_param_524(p):
    """res_pool_param : CASCADE TO DEFAULT"""
    p[0] = Expr("""res_pool_param""", """CASCADE TO DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterResourcePoolStmt_525(p):
    """AlterResourcePoolStmt : ALTER RESOURCE POOL name res_pool_params"""
    p[0] = Expr("""AlterResourcePoolStmt""", """ALTER RESOURCE POOL name res_pool_params""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateSchemaStmt_526(p):
    """CreateSchemaStmt : CREATE SCHEMA OptSchemaName AUTHORIZATION UserId OptDefaultInheritPrivileges OptSchemaEltList"""
    p[0] = Expr("""CreateSchemaStmt""", """CREATE SCHEMA OptSchemaName AUTHORIZATION UserId OptDefaultInheritPrivileges OptSchemaEltList""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateSchemaStmt_527(p):
    """CreateSchemaStmt : CREATE SCHEMA qualified_schema_name OptDefaultInheritPrivileges OptSchemaEltList"""
    p[0] = Expr("""CreateSchemaStmt""", """CREATE SCHEMA qualified_schema_name OptDefaultInheritPrivileges OptSchemaEltList""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateSchemaStmt_528(p):
    """CreateSchemaStmt : CREATE SCHEMA IF_P NOT EXISTS OptSchemaName AUTHORIZATION UserId OptDefaultInheritPrivileges OptSchemaEltList"""
    p[0] = Expr("""CreateSchemaStmt""", """CREATE SCHEMA IF_P NOT EXISTS OptSchemaName AUTHORIZATION UserId OptDefaultInheritPrivileges OptSchemaEltList""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateSchemaStmt_529(p):
    """CreateSchemaStmt : CREATE SCHEMA IF_P NOT EXISTS qualified_schema_name OptDefaultInheritPrivileges OptSchemaEltList"""
    p[0] = Expr("""CreateSchemaStmt""", """CREATE SCHEMA IF_P NOT EXISTS qualified_schema_name OptDefaultInheritPrivileges OptSchemaEltList""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateSchemaStmt_530(p):
    """CreateSchemaStmt : CREATE HCATALOG SCHEMA qualified_schema_name AUTHORIZATION UserId opt_with hcat_opt_list OptDefaultInheritPrivileges"""
    p[0] = Expr("""CreateSchemaStmt""", """CREATE HCATALOG SCHEMA qualified_schema_name AUTHORIZATION UserId opt_with hcat_opt_list OptDefaultInheritPrivileges""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateSchemaStmt_531(p):
    """CreateSchemaStmt : CREATE HCATALOG SCHEMA qualified_schema_name opt_with hcat_opt_list OptDefaultInheritPrivileges"""
    p[0] = Expr("""CreateSchemaStmt""", """CREATE HCATALOG SCHEMA qualified_schema_name opt_with hcat_opt_list OptDefaultInheritPrivileges""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateSchemaStmt_532(p):
    """CreateSchemaStmt : CREATE HCATALOG SCHEMA IF_P NOT EXISTS qualified_schema_name AUTHORIZATION UserId opt_with hcat_opt_list OptDefaultInheritPrivileges"""
    p[0] = Expr("""CreateSchemaStmt""", """CREATE HCATALOG SCHEMA IF_P NOT EXISTS qualified_schema_name AUTHORIZATION UserId opt_with hcat_opt_list OptDefaultInheritPrivileges""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateSchemaStmt_533(p):
    """CreateSchemaStmt : CREATE HCATALOG SCHEMA IF_P NOT EXISTS qualified_schema_name opt_with hcat_opt_list OptDefaultInheritPrivileges"""
    p[0] = Expr("""CreateSchemaStmt""", """CREATE HCATALOG SCHEMA IF_P NOT EXISTS qualified_schema_name opt_with hcat_opt_list OptDefaultInheritPrivileges""", p[1:] if len(p or []) > 1 else [], p)


def p_OptDefaultInheritPrivileges_534(p):
    """OptDefaultInheritPrivileges : DEFAULT INCLUDE SCHEMA PRIVILEGES"""
    p[0] = Expr("""OptDefaultInheritPrivileges""", """DEFAULT INCLUDE SCHEMA PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_OptDefaultInheritPrivileges_535(p):
    """OptDefaultInheritPrivileges : DEFAULT INCLUDE PRIVILEGES"""
    p[0] = Expr("""OptDefaultInheritPrivileges""", """DEFAULT INCLUDE PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_OptDefaultInheritPrivileges_536(p):
    """OptDefaultInheritPrivileges : DEFAULT EXCLUDE SCHEMA PRIVILEGES"""
    p[0] = Expr("""OptDefaultInheritPrivileges""", """DEFAULT EXCLUDE SCHEMA PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_OptDefaultInheritPrivileges_537(p):
    """OptDefaultInheritPrivileges : DEFAULT EXCLUDE PRIVILEGES"""
    p[0] = Expr("""OptDefaultInheritPrivileges""", """DEFAULT EXCLUDE PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_OptDefaultInheritPrivileges_538(p):
    """OptDefaultInheritPrivileges : """
    p[0] = Expr("""OptDefaultInheritPrivileges""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_list_539(p):
    """hcat_opt_list : hcat_opt_list hcat_opt_item"""
    p[0] = Expr("""hcat_opt_list""", """hcat_opt_list hcat_opt_item""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_list_540(p):
    """hcat_opt_list : """
    p[0] = Expr("""hcat_opt_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_541(p):
    """hcat_opt_item : HOSTNAME opt_equal Sconst"""
    p[0] = Expr("""hcat_opt_item""", """HOSTNAME opt_equal Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_542(p):
    """hcat_opt_item : PORT opt_equal Iconst"""
    p[0] = Expr("""hcat_opt_item""", """PORT opt_equal Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_543(p):
    """hcat_opt_item : HIVESERVER2_HOSTNAME opt_equal Sconst"""
    p[0] = Expr("""hcat_opt_item""", """HIVESERVER2_HOSTNAME opt_equal Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_544(p):
    """hcat_opt_item : WEBSERVICE_PORT opt_equal Iconst"""
    p[0] = Expr("""hcat_opt_item""", """WEBSERVICE_PORT opt_equal Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_545(p):
    """hcat_opt_item : WEBHDFS_ADDRESS opt_equal Sconst"""
    p[0] = Expr("""hcat_opt_item""", """WEBHDFS_ADDRESS opt_equal Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_546(p):
    """hcat_opt_item : HCATALOG_SCHEMA opt_equal Sconst"""
    p[0] = Expr("""hcat_opt_item""", """HCATALOG_SCHEMA opt_equal Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_547(p):
    """hcat_opt_item : HCATALOG_DB opt_equal Sconst"""
    p[0] = Expr("""hcat_opt_item""", """HCATALOG_DB opt_equal Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_548(p):
    """hcat_opt_item : HCATALOG_USER opt_equal Sconst"""
    p[0] = Expr("""hcat_opt_item""", """HCATALOG_USER opt_equal Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_549(p):
    """hcat_opt_item : WEBSERVICE_HOSTNAME opt_equal Sconst"""
    p[0] = Expr("""hcat_opt_item""", """WEBSERVICE_HOSTNAME opt_equal Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_550(p):
    """hcat_opt_item : SSL_CONFIG opt_equal Sconst"""
    p[0] = Expr("""hcat_opt_item""", """SSL_CONFIG opt_equal Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_551(p):
    """hcat_opt_item : CUSTOM_PARTITIONS opt_equal Iconst"""
    p[0] = Expr("""hcat_opt_item""", """CUSTOM_PARTITIONS opt_equal Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_552(p):
    """hcat_opt_item : CUSTOM_PARTITIONS opt_equal Sconst"""
    p[0] = Expr("""hcat_opt_item""", """CUSTOM_PARTITIONS opt_equal Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_553(p):
    """hcat_opt_item : CUSTOM_PARTITIONS opt_equal simple_boolean"""
    p[0] = Expr("""hcat_opt_item""", """CUSTOM_PARTITIONS opt_equal simple_boolean""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_554(p):
    """hcat_opt_item : HCATALOG_CONNECTION_TIMEOUT opt_equal Iconst"""
    p[0] = Expr("""hcat_opt_item""", """HCATALOG_CONNECTION_TIMEOUT opt_equal Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_555(p):
    """hcat_opt_item : HCATALOG_SLOW_TRANSFER_LIMIT opt_equal Iconst"""
    p[0] = Expr("""hcat_opt_item""", """HCATALOG_SLOW_TRANSFER_LIMIT opt_equal Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_hcat_opt_item_556(p):
    """hcat_opt_item : HCATALOG_SLOW_TRANSFER_TIME opt_equal Iconst"""
    p[0] = Expr("""hcat_opt_item""", """HCATALOG_SLOW_TRANSFER_TIME opt_equal Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSchemaName_557(p):
    """OptSchemaName : qualified_schema_name"""
    p[0] = Expr("""OptSchemaName""", """qualified_schema_name""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSchemaName_558(p):
    """OptSchemaName : """
    p[0] = Expr("""OptSchemaName""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSchemaEltList_559(p):
    """OptSchemaEltList : OptSchemaEltList schema_stmt"""
    p[0] = Expr("""OptSchemaEltList""", """OptSchemaEltList schema_stmt""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSchemaEltList_560(p):
    """OptSchemaEltList : """
    p[0] = Expr("""OptSchemaEltList""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_schema_stmt_561(p):
    """schema_stmt : CreateStmt"""
    p[0] = Expr("""schema_stmt""", """CreateStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_schema_stmt_562(p):
    """schema_stmt : IndexStmt"""
    p[0] = Expr("""schema_stmt""", """IndexStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_schema_stmt_563(p):
    """schema_stmt : CreateSeqStmt"""
    p[0] = Expr("""schema_stmt""", """CreateSeqStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_schema_stmt_564(p):
    """schema_stmt : CreateTrigStmt"""
    p[0] = Expr("""schema_stmt""", """CreateTrigStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_schema_stmt_565(p):
    """schema_stmt : GrantStmt"""
    p[0] = Expr("""schema_stmt""", """GrantStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_schema_stmt_566(p):
    """schema_stmt : ViewStmt"""
    p[0] = Expr("""schema_stmt""", """ViewStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_schema_stmt_567(p):
    """schema_stmt : VCreateProjectionStmt"""
    p[0] = Expr("""schema_stmt""", """VCreateProjectionStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterHCatalogSchemaStmt_568(p):
    """AlterHCatalogSchemaStmt : ALTER HCATALOG SCHEMA qualified_schema_name SET PARAMETER hcat_opt_list"""
    p[0] = Expr("""AlterHCatalogSchemaStmt""", """ALTER HCATALOG SCHEMA qualified_schema_name SET PARAMETER hcat_opt_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterHCatalogSchemaStmt_569(p):
    """AlterHCatalogSchemaStmt : ALTER HCATALOG SCHEMA qualified_schema_name SET hcat_opt_list"""
    p[0] = Expr("""AlterHCatalogSchemaStmt""", """ALTER HCATALOG SCHEMA qualified_schema_name SET hcat_opt_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterSessionStmt_570(p):
    """AlterSessionStmt : ALTER SESSION SET PARAMETER paramarg_list"""
    p[0] = Expr("""AlterSessionStmt""", """ALTER SESSION SET PARAMETER paramarg_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterSessionStmt_571(p):
    """AlterSessionStmt : ALTER SESSION SET paramarg_list"""
    p[0] = Expr("""AlterSessionStmt""", """ALTER SESSION SET paramarg_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterSessionStmt_572(p):
    """AlterSessionStmt : ALTER SESSION CLEAR PARAMETER knob_list"""
    p[0] = Expr("""AlterSessionStmt""", """ALTER SESSION CLEAR PARAMETER knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterSessionStmt_573(p):
    """AlterSessionStmt : ALTER SESSION CLEAR knob_list"""
    p[0] = Expr("""AlterSessionStmt""", """ALTER SESSION CLEAR knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterSessionStmt_574(p):
    """AlterSessionStmt : ALTER SESSION SET UDPARAMETER opt_namespace paramarg_list"""
    p[0] = Expr("""AlterSessionStmt""", """ALTER SESSION SET UDPARAMETER opt_namespace paramarg_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterSessionStmt_575(p):
    """AlterSessionStmt : ALTER SESSION CLEAR UDPARAMETER opt_namespace knob_list"""
    p[0] = Expr("""AlterSessionStmt""", """ALTER SESSION CLEAR UDPARAMETER opt_namespace knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterSessionStmt_576(p):
    """AlterSessionStmt : ALTER SESSION CLEAR UDPARAMETER ALL opt_namespace"""
    p[0] = Expr("""AlterSessionStmt""", """ALTER SESSION CLEAR UDPARAMETER ALL opt_namespace""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_namespace_577(p):
    """opt_namespace : FOR qualified_name"""
    p[0] = Expr("""opt_namespace""", """FOR qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_namespace_578(p):
    """opt_namespace : """
    p[0] = Expr("""opt_namespace""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableSetStmt_579(p):
    """VariableSetStmt : SET set_rest"""
    p[0] = Expr("""VariableSetStmt""", """SET set_rest""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableSetStmt_580(p):
    """VariableSetStmt : SET LOCAL set_rest"""
    p[0] = Expr("""VariableSetStmt""", """SET LOCAL set_rest""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableSetStmt_581(p):
    """VariableSetStmt : SET SESSION set_rest"""
    p[0] = Expr("""VariableSetStmt""", """SET SESSION set_rest""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_582(p):
    """set_rest : function_name TO var_list_or_default_all_except"""
    p[0] = Expr("""set_rest""", """function_name TO var_list_or_default_all_except""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_583(p):
    """set_rest : function_name '=' var_list_or_default_all_except"""
    p[0] = Expr("""set_rest""", """function_name '=' var_list_or_default_all_except""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_584(p):
    """set_rest : timezone opt_to_or_equalsign zone_value"""
    p[0] = Expr("""set_rest""", """timezone opt_to_or_equalsign zone_value""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_585(p):
    """set_rest : SESSION CHARACTERISTICS AS TRANSACTION transaction_mode_list"""
    p[0] = Expr("""set_rest""", """SESSION CHARACTERISTICS AS TRANSACTION transaction_mode_list""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_586(p):
    """set_rest : SESSION AUTHORIZATION ColId_or_Sconst"""
    p[0] = Expr("""set_rest""", """SESSION AUTHORIZATION ColId_or_Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_587(p):
    """set_rest : SESSION AUTHORIZATION DEFAULT"""
    p[0] = Expr("""set_rest""", """SESSION AUTHORIZATION DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_588(p):
    """set_rest : SESSION RESOURCE POOL name"""
    p[0] = Expr("""set_rest""", """SESSION RESOURCE POOL name""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_589(p):
    """set_rest : SESSION MEMORYCAP Sconst"""
    p[0] = Expr("""set_rest""", """SESSION MEMORYCAP Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_590(p):
    """set_rest : SESSION MEMORYCAP NONE"""
    p[0] = Expr("""set_rest""", """SESSION MEMORYCAP NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_591(p):
    """set_rest : SESSION TEMPSPACECAP Sconst"""
    p[0] = Expr("""set_rest""", """SESSION TEMPSPACECAP Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_592(p):
    """set_rest : SESSION TEMPSPACECAP NONE"""
    p[0] = Expr("""set_rest""", """SESSION TEMPSPACECAP NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_593(p):
    """set_rest : SESSION RUNTIMECAP Sconst"""
    p[0] = Expr("""set_rest""", """SESSION RUNTIMECAP Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_594(p):
    """set_rest : SESSION RUNTIMECAP NONE"""
    p[0] = Expr("""set_rest""", """SESSION RUNTIMECAP NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_595(p):
    """set_rest : SESSION IDLESESSIONTIMEOUT Sconst"""
    p[0] = Expr("""set_rest""", """SESSION IDLESESSIONTIMEOUT Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_596(p):
    """set_rest : SESSION IDLESESSIONTIMEOUT NONE"""
    p[0] = Expr("""set_rest""", """SESSION IDLESESSIONTIMEOUT NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_597(p):
    """set_rest : SESSION GRACEPERIOD Sconst"""
    p[0] = Expr("""set_rest""", """SESSION GRACEPERIOD Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_598(p):
    """set_rest : SESSION GRACEPERIOD NONE"""
    p[0] = Expr("""set_rest""", """SESSION GRACEPERIOD NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_set_rest_599(p):
    """set_rest : ROLE var_list_or_default_all_except"""
    p[0] = Expr("""set_rest""", """ROLE var_list_or_default_all_except""", p[1:] if len(p or []) > 1 else [], p)


def p_timezone_600(p):
    """timezone : TIME ZONE"""
    p[0] = Expr("""timezone""", """TIME ZONE""", p[1:] if len(p or []) > 1 else [], p)


def p_timezone_601(p):
    """timezone : TIMEZONE"""
    p[0] = Expr("""timezone""", """TIMEZONE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_to_or_equalsign_602(p):
    """opt_to_or_equalsign : TO"""
    p[0] = Expr("""opt_to_or_equalsign""", """TO""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_to_or_equalsign_603(p):
    """opt_to_or_equalsign : '='"""
    p[0] = Expr("""opt_to_or_equalsign""", """'='""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_to_or_equalsign_604(p):
    """opt_to_or_equalsign : """
    p[0] = Expr("""opt_to_or_equalsign""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_var_list_or_default_all_except_605(p):
    """var_list_or_default_all_except : var_list_or_default"""
    p[0] = Expr("""var_list_or_default_all_except""", """var_list_or_default""", p[1:] if len(p or []) > 1 else [], p)


def p_var_list_or_default_all_except_606(p):
    """var_list_or_default_all_except : ALL"""
    p[0] = Expr("""var_list_or_default_all_except""", """ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_var_list_or_default_all_except_607(p):
    """var_list_or_default_all_except : ALL EXCEPT var_list"""
    p[0] = Expr("""var_list_or_default_all_except""", """ALL EXCEPT var_list""", p[1:] if len(p or []) > 1 else [], p)


def p_var_list_or_default_608(p):
    """var_list_or_default : var_list"""
    p[0] = Expr("""var_list_or_default""", """var_list""", p[1:] if len(p or []) > 1 else [], p)


def p_var_list_or_default_609(p):
    """var_list_or_default : DEFAULT"""
    p[0] = Expr("""var_list_or_default""", """DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_var_list_610(p):
    """var_list : var_value"""
    p[0] = Expr("""var_list""", """var_value""", p[1:] if len(p or []) > 1 else [], p)


def p_var_list_611(p):
    """var_list : var_list ',' var_value"""
    p[0] = Expr("""var_list""", """var_list ',' var_value""", p[1:] if len(p or []) > 1 else [], p)


def p_var_value_612(p):
    """var_value : opt_boolean"""
    p[0] = Expr("""var_value""", """opt_boolean""", p[1:] if len(p or []) > 1 else [], p)


def p_var_value_613(p):
    """var_value : ColId_or_Sconst"""
    p[0] = Expr("""var_value""", """ColId_or_Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_var_value_614(p):
    """var_value : NumericOnly"""
    p[0] = Expr("""var_value""", """NumericOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_iso_level_615(p):
    """iso_level : READ UNCOMMITTED"""
    p[0] = Expr("""iso_level""", """READ UNCOMMITTED""", p[1:] if len(p or []) > 1 else [], p)


def p_iso_level_616(p):
    """iso_level : READ COMMITTED"""
    p[0] = Expr("""iso_level""", """READ COMMITTED""", p[1:] if len(p or []) > 1 else [], p)


def p_iso_level_617(p):
    """iso_level : REPEATABLE READ"""
    p[0] = Expr("""iso_level""", """REPEATABLE READ""", p[1:] if len(p or []) > 1 else [], p)


def p_iso_level_618(p):
    """iso_level : SERIALIZABLE"""
    p[0] = Expr("""iso_level""", """SERIALIZABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_boolean_619(p):
    """opt_boolean : TRUE_P"""
    p[0] = Expr("""opt_boolean""", """TRUE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_boolean_620(p):
    """opt_boolean : FALSE_P"""
    p[0] = Expr("""opt_boolean""", """FALSE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_boolean_621(p):
    """opt_boolean : ON"""
    p[0] = Expr("""opt_boolean""", """ON""", p[1:] if len(p or []) > 1 else [], p)


def p_simple_boolean_622(p):
    """simple_boolean : TRUE_P"""
    p[0] = Expr("""simple_boolean""", """TRUE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_simple_boolean_623(p):
    """simple_boolean : FALSE_P"""
    p[0] = Expr("""simple_boolean""", """FALSE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_zone_value_624(p):
    """zone_value : Sconst"""
    p[0] = Expr("""zone_value""", """Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_zone_value_625(p):
    """zone_value : IDENT"""
    p[0] = Expr("""zone_value""", """IDENT""", p[1:] if len(p or []) > 1 else [], p)


def p_zone_value_626(p):
    """zone_value : IDENT '/' IDENT"""
    p[0] = Expr("""zone_value""", """IDENT '/' IDENT""", p[1:] if len(p or []) > 1 else [], p)


def p_zone_value_627(p):
    """zone_value : ConstInterval opt_minus Sconst interval_qualifier"""
    p[0] = Expr("""zone_value""", """ConstInterval opt_minus Sconst interval_qualifier""", p[1:] if len(p or []) > 1 else [], p)


def p_zone_value_628(p):
    """zone_value : opt_minus FCONST"""
    p[0] = Expr("""zone_value""", """opt_minus FCONST""", p[1:] if len(p or []) > 1 else [], p)


def p_zone_value_629(p):
    """zone_value : opt_minus Iconst opt_minutes"""
    p[0] = Expr("""zone_value""", """opt_minus Iconst opt_minutes""", p[1:] if len(p or []) > 1 else [], p)


def p_zone_value_630(p):
    """zone_value : DEFAULT"""
    p[0] = Expr("""zone_value""", """DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_zone_value_631(p):
    """zone_value : LOCAL"""
    p[0] = Expr("""zone_value""", """LOCAL""", p[1:] if len(p or []) > 1 else [], p)


def p_ColId_or_Sconst_632(p):
    """ColId_or_Sconst : ColId"""
    p[0] = Expr("""ColId_or_Sconst""", """ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_ColId_or_Sconst_633(p):
    """ColId_or_Sconst : SCONST"""
    p[0] = Expr("""ColId_or_Sconst""", """SCONST""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_minutes_634(p):
    """opt_minutes : ':' Iconst"""
    p[0] = Expr("""opt_minutes""", """':' Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_minutes_635(p):
    """opt_minutes : """
    p[0] = Expr("""opt_minutes""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_CurrentVariableShowStmt_636(p):
    """CurrentVariableShowStmt : SHOW CURRENT_P ALL"""
    p[0] = Expr("""CurrentVariableShowStmt""", """SHOW CURRENT_P ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_CurrentVariableShowStmt_637(p):
    """CurrentVariableShowStmt : SHOW CURRENT_P PARAMETER ALL"""
    p[0] = Expr("""CurrentVariableShowStmt""", """SHOW CURRENT_P PARAMETER ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_CurrentVariableShowStmt_638(p):
    """CurrentVariableShowStmt : SHOW CURRENT_P knob_list"""
    p[0] = Expr("""CurrentVariableShowStmt""", """SHOW CURRENT_P knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_CurrentVariableShowStmt_639(p):
    """CurrentVariableShowStmt : SHOW CURRENT_P PARAMETER knob_list"""
    p[0] = Expr("""CurrentVariableShowStmt""", """SHOW CURRENT_P PARAMETER knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableShowStmt_640(p):
    """VariableShowStmt : SHOW ColId"""
    p[0] = Expr("""VariableShowStmt""", """SHOW ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableShowStmt_641(p):
    """VariableShowStmt : SHOW TIME ZONE"""
    p[0] = Expr("""VariableShowStmt""", """SHOW TIME ZONE""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableShowStmt_642(p):
    """VariableShowStmt : SHOW TRANSACTION ISOLATION LEVEL"""
    p[0] = Expr("""VariableShowStmt""", """SHOW TRANSACTION ISOLATION LEVEL""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableShowStmt_643(p):
    """VariableShowStmt : SHOW SESSION AUTHORIZATION"""
    p[0] = Expr("""VariableShowStmt""", """SHOW SESSION AUTHORIZATION""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableShowStmt_644(p):
    """VariableShowStmt : SHOW RESOURCE POOL"""
    p[0] = Expr("""VariableShowStmt""", """SHOW RESOURCE POOL""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableShowStmt_645(p):
    """VariableShowStmt : SHOW ENABLED ROLES"""
    p[0] = Expr("""VariableShowStmt""", """SHOW ENABLED ROLES""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableShowStmt_646(p):
    """VariableShowStmt : SHOW AVAILABLE ROLES"""
    p[0] = Expr("""VariableShowStmt""", """SHOW AVAILABLE ROLES""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableShowStmt_647(p):
    """VariableShowStmt : SHOW ALL"""
    p[0] = Expr("""VariableShowStmt""", """SHOW ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableShowStmt_648(p):
    """VariableShowStmt : SHOW SESSION ALL"""
    p[0] = Expr("""VariableShowStmt""", """SHOW SESSION ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableShowStmt_649(p):
    """VariableShowStmt : SHOW SESSION PARAMETER ALL"""
    p[0] = Expr("""VariableShowStmt""", """SHOW SESSION PARAMETER ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableShowStmt_650(p):
    """VariableShowStmt : SHOW SESSION knob_list"""
    p[0] = Expr("""VariableShowStmt""", """SHOW SESSION knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableShowStmt_651(p):
    """VariableShowStmt : SHOW SESSION PARAMETER knob_list"""
    p[0] = Expr("""VariableShowStmt""", """SHOW SESSION PARAMETER knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableShowStmt_652(p):
    """VariableShowStmt : SHOW SESSION UDPARAMETER ALL"""
    p[0] = Expr("""VariableShowStmt""", """SHOW SESSION UDPARAMETER ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableResetStmt_653(p):
    """VariableResetStmt : RESET ColId"""
    p[0] = Expr("""VariableResetStmt""", """RESET ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableResetStmt_654(p):
    """VariableResetStmt : RESET TIME ZONE"""
    p[0] = Expr("""VariableResetStmt""", """RESET TIME ZONE""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableResetStmt_655(p):
    """VariableResetStmt : RESET TRANSACTION ISOLATION LEVEL"""
    p[0] = Expr("""VariableResetStmt""", """RESET TRANSACTION ISOLATION LEVEL""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableResetStmt_656(p):
    """VariableResetStmt : RESET SESSION AUTHORIZATION"""
    p[0] = Expr("""VariableResetStmt""", """RESET SESSION AUTHORIZATION""", p[1:] if len(p or []) > 1 else [], p)


def p_VariableResetStmt_657(p):
    """VariableResetStmt : RESET ALL"""
    p[0] = Expr("""VariableResetStmt""", """RESET ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintsSetStmt_658(p):
    """ConstraintsSetStmt : SET CONSTRAINTS constraints_set_list constraints_set_mode"""
    p[0] = Expr("""ConstraintsSetStmt""", """SET CONSTRAINTS constraints_set_list constraints_set_mode""", p[1:] if len(p or []) > 1 else [], p)


def p_constraints_set_list_659(p):
    """constraints_set_list : ALL"""
    p[0] = Expr("""constraints_set_list""", """ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_constraints_set_list_660(p):
    """constraints_set_list : name_list"""
    p[0] = Expr("""constraints_set_list""", """name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_constraints_set_mode_661(p):
    """constraints_set_mode : DEFERRED"""
    p[0] = Expr("""constraints_set_mode""", """DEFERRED""", p[1:] if len(p or []) > 1 else [], p)


def p_constraints_set_mode_662(p):
    """constraints_set_mode : IMMEDIATE"""
    p[0] = Expr("""constraints_set_mode""", """IMMEDIATE""", p[1:] if len(p or []) > 1 else [], p)


def p_CheckPointStmt_663(p):
    """CheckPointStmt : CHECKPOINT"""
    p[0] = Expr("""CheckPointStmt""", """CHECKPOINT""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterViewStmt_664(p):
    """AlterViewStmt : ALTER VIEW qualified_name OWNER TO UserId"""
    p[0] = Expr("""AlterViewStmt""", """ALTER VIEW qualified_name OWNER TO UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterViewStmt_665(p):
    """AlterViewStmt : ALTER VIEW qualified_name SET SCHEMA qualified_schema_name"""
    p[0] = Expr("""AlterViewStmt""", """ALTER VIEW qualified_name SET SCHEMA qualified_schema_name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterSchemaStmt_666(p):
    """AlterSchemaStmt : ALTER SCHEMA qualified_schema_name DEFAULT INCLUDE OptSchemaKeyword PRIVILEGES"""
    p[0] = Expr("""AlterSchemaStmt""", """ALTER SCHEMA qualified_schema_name DEFAULT INCLUDE OptSchemaKeyword PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterSchemaStmt_667(p):
    """AlterSchemaStmt : ALTER SCHEMA qualified_schema_name DEFAULT EXCLUDE OptSchemaKeyword PRIVILEGES"""
    p[0] = Expr("""AlterSchemaStmt""", """ALTER SCHEMA qualified_schema_name DEFAULT EXCLUDE OptSchemaKeyword PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterSchemaStmt_668(p):
    """AlterSchemaStmt : ALTER SCHEMA qualified_schema_name OWNER TO UserId opt_schema_owner_behavior"""
    p[0] = Expr("""AlterSchemaStmt""", """ALTER SCHEMA qualified_schema_name OWNER TO UserId opt_schema_owner_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_schema_owner_behavior_669(p):
    """opt_schema_owner_behavior : CASCADE"""
    p[0] = Expr("""opt_schema_owner_behavior""", """CASCADE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_schema_owner_behavior_670(p):
    """opt_schema_owner_behavior : """
    p[0] = Expr("""opt_schema_owner_behavior""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterViewPrivilegesStmt_671(p):
    """AlterViewPrivilegesStmt : ALTER VIEW qualified_name INCLUDE OptSchemaKeyword PRIVILEGES"""
    p[0] = Expr("""AlterViewPrivilegesStmt""", """ALTER VIEW qualified_name INCLUDE OptSchemaKeyword PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterViewPrivilegesStmt_672(p):
    """AlterViewPrivilegesStmt : ALTER VIEW qualified_name EXCLUDE OptSchemaKeyword PRIVILEGES"""
    p[0] = Expr("""AlterViewPrivilegesStmt""", """ALTER VIEW qualified_name EXCLUDE OptSchemaKeyword PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterViewPrivilegesStmt_673(p):
    """AlterViewPrivilegesStmt : ALTER VIEW qualified_name MATERIALIZE OptSchemaKeyword PRIVILEGES"""
    p[0] = Expr("""AlterViewPrivilegesStmt""", """ALTER VIEW qualified_name MATERIALIZE OptSchemaKeyword PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterTableStmt_674(p):
    """AlterTableStmt : ALTER TABLE relation_expr alter_table_cmds"""
    p[0] = Expr("""AlterTableStmt""", """ALTER TABLE relation_expr alter_table_cmds""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterTableStmt_675(p):
    """AlterTableStmt : ALTER INDEX relation_expr alter_rel_cmds"""
    p[0] = Expr("""AlterTableStmt""", """ALTER INDEX relation_expr alter_rel_cmds""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmds_676(p):
    """alter_table_cmds : alter_table_cmd"""
    p[0] = Expr("""alter_table_cmds""", """alter_table_cmd""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmds_677(p):
    """alter_table_cmds : alter_table_cmds ',' alter_table_cmd"""
    p[0] = Expr("""alter_table_cmds""", """alter_table_cmds ',' alter_table_cmd""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_678(p):
    """alter_table_cmd : ADD opt_column columnDef encode_type opt_proj_list opt_drop_behavior"""
    p[0] = Expr("""alter_table_cmd""", """ADD opt_column columnDef encode_type opt_proj_list opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_679(p):
    """alter_table_cmd : ADD opt_column IF_P NOT EXISTS columnDef encode_type opt_proj_list opt_drop_behavior"""
    p[0] = Expr("""alter_table_cmd""", """ADD opt_column IF_P NOT EXISTS columnDef encode_type opt_proj_list opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_680(p):
    """alter_table_cmd : ADD opt_column columnDef encode_type ALL PROJECTIONS opt_drop_behavior"""
    p[0] = Expr("""alter_table_cmd""", """ADD opt_column columnDef encode_type ALL PROJECTIONS opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_681(p):
    """alter_table_cmd : ADD opt_column IF_P NOT EXISTS columnDef encode_type ALL PROJECTIONS opt_drop_behavior"""
    p[0] = Expr("""alter_table_cmd""", """ADD opt_column IF_P NOT EXISTS columnDef encode_type ALL PROJECTIONS opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_682(p):
    """alter_table_cmd : ALTER opt_column columnElem alter_column_default"""
    p[0] = Expr("""alter_table_cmd""", """ALTER opt_column columnElem alter_column_default""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_683(p):
    """alter_table_cmd : ALTER opt_column columnElem alter_column_setusing"""
    p[0] = Expr("""alter_table_cmd""", """ALTER opt_column columnElem alter_column_setusing""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_684(p):
    """alter_table_cmd : ALTER opt_column columnElem alter_column_defaultusing"""
    p[0] = Expr("""alter_table_cmd""", """ALTER opt_column columnElem alter_column_defaultusing""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_685(p):
    """alter_table_cmd : ALTER opt_column columnElem DROP NOT NULL_P"""
    p[0] = Expr("""alter_table_cmd""", """ALTER opt_column columnElem DROP NOT NULL_P""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_686(p):
    """alter_table_cmd : ALTER opt_column columnElem SET NOT NULL_P"""
    p[0] = Expr("""alter_table_cmd""", """ALTER opt_column columnElem SET NOT NULL_P""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_687(p):
    """alter_table_cmd : ALTER opt_column columnElem SET STATISTICS IntegerOnly"""
    p[0] = Expr("""alter_table_cmd""", """ALTER opt_column columnElem SET STATISTICS IntegerOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_688(p):
    """alter_table_cmd : ALTER opt_column columnElem SET STORAGE ColId"""
    p[0] = Expr("""alter_table_cmd""", """ALTER opt_column columnElem SET STORAGE ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_689(p):
    """alter_table_cmd : DROP opt_column columnElem opt_drop_behavior"""
    p[0] = Expr("""alter_table_cmd""", """DROP opt_column columnElem opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_690(p):
    """alter_table_cmd : DROP opt_column IF_P EXISTS columnElem opt_drop_behavior"""
    p[0] = Expr("""alter_table_cmd""", """DROP opt_column IF_P EXISTS columnElem opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_691(p):
    """alter_table_cmd : ALTER opt_column columnElem SET DATA_P TYPE_P TypenameWithTypmod"""
    p[0] = Expr("""alter_table_cmd""", """ALTER opt_column columnElem SET DATA_P TYPE_P TypenameWithTypmod""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_692(p):
    """alter_table_cmd : ADD TableConstraint"""
    p[0] = Expr("""alter_table_cmd""", """ADD TableConstraint""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_693(p):
    """alter_table_cmd : SET STORAGE copy_storage_mode"""
    p[0] = Expr("""alter_table_cmd""", """SET STORAGE copy_storage_mode""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_694(p):
    """alter_table_cmd : SET ACTIVEPARTITIONCOUNT active_partition_count"""
    p[0] = Expr("""alter_table_cmd""", """SET ACTIVEPARTITIONCOUNT active_partition_count""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_695(p):
    """alter_table_cmd : DROP CONSTRAINT IF_P EXISTS name opt_drop_behavior"""
    p[0] = Expr("""alter_table_cmd""", """DROP CONSTRAINT IF_P EXISTS name opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_696(p):
    """alter_table_cmd : DROP CONSTRAINT name opt_drop_behavior"""
    p[0] = Expr("""alter_table_cmd""", """DROP CONSTRAINT name opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_697(p):
    """alter_table_cmd : ALTER CONSTRAINT name set_constr_status"""
    p[0] = Expr("""alter_table_cmd""", """ALTER CONSTRAINT name set_constr_status""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_698(p):
    """alter_table_cmd : SET WITHOUT OIDS"""
    p[0] = Expr("""alter_table_cmd""", """SET WITHOUT OIDS""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_699(p):
    """alter_table_cmd : CREATE TOAST TABLE"""
    p[0] = Expr("""alter_table_cmd""", """CREATE TOAST TABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_700(p):
    """alter_table_cmd : CLUSTER ON name"""
    p[0] = Expr("""alter_table_cmd""", """CLUSTER ON name""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_701(p):
    """alter_table_cmd : SET WITHOUT CLUSTER"""
    p[0] = Expr("""alter_table_cmd""", """SET WITHOUT CLUSTER""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_702(p):
    """alter_table_cmd : SET SCHEMA qualified_schema_name opt_setschema_behavior"""
    p[0] = Expr("""alter_table_cmd""", """SET SCHEMA qualified_schema_name opt_setschema_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_703(p):
    """alter_table_cmd : PARTITION BY b_expr GROUP_P BY b_expr SET ACTIVEPARTITIONCOUNT active_partition_count opt_reorganize"""
    p[0] = Expr("""alter_table_cmd""", """PARTITION BY b_expr GROUP_P BY b_expr SET ACTIVEPARTITIONCOUNT active_partition_count opt_reorganize""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_704(p):
    """alter_table_cmd : PARTITION BY b_expr GROUP_P BY b_expr opt_reorganize"""
    p[0] = Expr("""alter_table_cmd""", """PARTITION BY b_expr GROUP_P BY b_expr opt_reorganize""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_705(p):
    """alter_table_cmd : PARTITION BY b_expr SET ACTIVEPARTITIONCOUNT active_partition_count opt_reorganize"""
    p[0] = Expr("""alter_table_cmd""", """PARTITION BY b_expr SET ACTIVEPARTITIONCOUNT active_partition_count opt_reorganize""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_706(p):
    """alter_table_cmd : PARTITION BY b_expr opt_reorganize"""
    p[0] = Expr("""alter_table_cmd""", """PARTITION BY b_expr opt_reorganize""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_707(p):
    """alter_table_cmd : REORGANIZE"""
    p[0] = Expr("""alter_table_cmd""", """REORGANIZE""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_708(p):
    """alter_table_cmd : REMOVE PARTITIONING"""
    p[0] = Expr("""alter_table_cmd""", """REMOVE PARTITIONING""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_709(p):
    """alter_table_cmd : INCLUDE OptSchemaKeyword PRIVILEGES"""
    p[0] = Expr("""alter_table_cmd""", """INCLUDE OptSchemaKeyword PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_710(p):
    """alter_table_cmd : EXCLUDE OptSchemaKeyword PRIVILEGES"""
    p[0] = Expr("""alter_table_cmd""", """EXCLUDE OptSchemaKeyword PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_711(p):
    """alter_table_cmd : MATERIALIZE OptSchemaKeyword PRIVILEGES"""
    p[0] = Expr("""alter_table_cmd""", """MATERIALIZE OptSchemaKeyword PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_712(p):
    """alter_table_cmd : FORCE OUTER_P force_outer_lvl"""
    p[0] = Expr("""alter_table_cmd""", """FORCE OUTER_P force_outer_lvl""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_table_cmd_713(p):
    """alter_table_cmd : alter_rel_cmd"""
    p[0] = Expr("""alter_table_cmd""", """alter_rel_cmd""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_proj_list_714(p):
    """opt_proj_list : PROJECTIONS '(' qualified_name_list ')'"""
    p[0] = Expr("""opt_proj_list""", """PROJECTIONS '(' qualified_name_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_proj_list_715(p):
    """opt_proj_list : """
    p[0] = Expr("""opt_proj_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_rel_cmds_716(p):
    """alter_rel_cmds : alter_rel_cmd"""
    p[0] = Expr("""alter_rel_cmds""", """alter_rel_cmd""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_rel_cmds_717(p):
    """alter_rel_cmds : alter_rel_cmds ',' alter_rel_cmd"""
    p[0] = Expr("""alter_rel_cmds""", """alter_rel_cmds ',' alter_rel_cmd""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_rel_cmd_718(p):
    """alter_rel_cmd : OWNER TO UserId"""
    p[0] = Expr("""alter_rel_cmd""", """OWNER TO UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_rel_cmd_719(p):
    """alter_rel_cmd : SET TABLESPACE name"""
    p[0] = Expr("""alter_rel_cmd""", """SET TABLESPACE name""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_column_default_720(p):
    """alter_column_default : SET DEFAULT a_expr"""
    p[0] = Expr("""alter_column_default""", """SET DEFAULT a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_column_default_721(p):
    """alter_column_default : DROP DEFAULT"""
    p[0] = Expr("""alter_column_default""", """DROP DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_column_setusing_722(p):
    """alter_column_setusing : SET USING b_expr"""
    p[0] = Expr("""alter_column_setusing""", """SET USING b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_column_setusing_723(p):
    """alter_column_setusing : DROP SET USING"""
    p[0] = Expr("""alter_column_setusing""", """DROP SET USING""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_column_defaultusing_724(p):
    """alter_column_defaultusing : SET DEFAULT USING b_expr"""
    p[0] = Expr("""alter_column_defaultusing""", """SET DEFAULT USING b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_alter_column_defaultusing_725(p):
    """alter_column_defaultusing : DROP DEFAULT USING"""
    p[0] = Expr("""alter_column_defaultusing""", """DROP DEFAULT USING""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_drop_behavior_726(p):
    """opt_drop_behavior : CASCADE"""
    p[0] = Expr("""opt_drop_behavior""", """CASCADE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_drop_behavior_727(p):
    """opt_drop_behavior : RESTRICT"""
    p[0] = Expr("""opt_drop_behavior""", """RESTRICT""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_drop_behavior_728(p):
    """opt_drop_behavior : """
    p[0] = Expr("""opt_drop_behavior""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_set_constr_status_729(p):
    """set_constr_status : ENABLED"""
    p[0] = Expr("""set_constr_status""", """ENABLED""", p[1:] if len(p or []) > 1 else [], p)


def p_set_constr_status_730(p):
    """set_constr_status : DISABLED"""
    p[0] = Expr("""set_constr_status""", """DISABLED""", p[1:] if len(p or []) > 1 else [], p)


def p_force_outer_lvl_731(p):
    """force_outer_lvl : ICONST"""
    p[0] = Expr("""force_outer_lvl""", """ICONST""", p[1:] if len(p or []) > 1 else [], p)


def p_force_outer_lvl_732(p):
    """force_outer_lvl : """
    p[0] = Expr("""force_outer_lvl""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_setschema_behavior_733(p):
    """opt_setschema_behavior : RESTRICT"""
    p[0] = Expr("""opt_setschema_behavior""", """RESTRICT""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_setschema_behavior_734(p):
    """opt_setschema_behavior : CASCADE"""
    p[0] = Expr("""opt_setschema_behavior""", """CASCADE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_setschema_behavior_735(p):
    """opt_setschema_behavior : """
    p[0] = Expr("""opt_setschema_behavior""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_reorganize_736(p):
    """opt_reorganize : REORGANIZE"""
    p[0] = Expr("""opt_reorganize""", """REORGANIZE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_reorganize_737(p):
    """opt_reorganize : """
    p[0] = Expr("""opt_reorganize""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_active_partition_count_738(p):
    """active_partition_count : Iconst"""
    p[0] = Expr("""active_partition_count""", """Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_active_partition_count_739(p):
    """active_partition_count : DEFAULT"""
    p[0] = Expr("""active_partition_count""", """DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_ClosePortalStmt_740(p):
    """ClosePortalStmt : CLOSE name"""
    p[0] = Expr("""ClosePortalStmt""", """CLOSE name""", p[1:] if len(p or []) > 1 else [], p)


def p_CopyStmt_741(p):
    """CopyStmt : COPY opt_binary qualified_name opt_copy_column_list opt_columns_count opt_parse_option_list opt_copy_from_clause opt_copy_file_format copy_delimiter opt_with copy_opt_udls copy_opt_list copy_opt_commit"""
    p[0] = Expr("""CopyStmt""", """COPY opt_binary qualified_name opt_copy_column_list opt_columns_count opt_parse_option_list opt_copy_from_clause opt_copy_file_format copy_delimiter opt_with copy_opt_udls copy_opt_list copy_opt_commit""", p[1:] if len(p or []) > 1 else [], p)


def p_ExternalTableCopyStmt_742(p):
    """ExternalTableCopyStmt : COPY opt_copy_column_list opt_columns_count opt_parse_option_list opt_copy_from_clause opt_copy_file_format copy_delimiter opt_with copy_opt_udls copy_opt_list copy_opt_commit"""
    p[0] = Expr("""ExternalTableCopyStmt""", """COPY opt_copy_column_list opt_columns_count opt_parse_option_list opt_copy_from_clause opt_copy_file_format copy_delimiter opt_with copy_opt_udls copy_opt_list copy_opt_commit""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_from_clause_743(p):
    """opt_copy_from_clause : copy_from copy_source"""
    p[0] = Expr("""opt_copy_from_clause""", """copy_from copy_source""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_from_clause_744(p):
    """opt_copy_from_clause : """
    p[0] = Expr("""opt_copy_from_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_udls_745(p):
    """copy_opt_udls : copy_opt_source copy_opt_filter_list copy_opt_parser"""
    p[0] = Expr("""copy_opt_udls""", """copy_opt_source copy_opt_filter_list copy_opt_parser""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_source_746(p):
    """copy_opt_source : SOURCE load_function"""
    p[0] = Expr("""copy_opt_source""", """SOURCE load_function""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_source_747(p):
    """copy_opt_source : """
    p[0] = Expr("""copy_opt_source""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_filter_list_748(p):
    """copy_opt_filter_list : copy_filter_list"""
    p[0] = Expr("""copy_opt_filter_list""", """copy_filter_list""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_filter_list_749(p):
    """copy_opt_filter_list : """
    p[0] = Expr("""copy_opt_filter_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_filter_list_750(p):
    """copy_filter_list : copy_filter"""
    p[0] = Expr("""copy_filter_list""", """copy_filter""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_filter_list_751(p):
    """copy_filter_list : copy_filter_list copy_filter"""
    p[0] = Expr("""copy_filter_list""", """copy_filter_list copy_filter""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_filter_752(p):
    """copy_filter : FILTER load_function"""
    p[0] = Expr("""copy_filter""", """FILTER load_function""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_filter_753(p):
    """copy_filter : UNPACKER load_function"""
    p[0] = Expr("""copy_filter""", """UNPACKER load_function""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_parser_754(p):
    """copy_opt_parser : PARSER load_function"""
    p[0] = Expr("""copy_opt_parser""", """PARSER load_function""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_parser_755(p):
    """copy_opt_parser : """
    p[0] = Expr("""copy_opt_parser""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_from_756(p):
    """copy_from : FROM"""
    p[0] = Expr("""copy_from""", """FROM""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_from_757(p):
    """copy_from : TO"""
    p[0] = Expr("""copy_from""", """TO""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_source_758(p):
    """copy_source : copy_file_list"""
    p[0] = Expr("""copy_source""", """copy_file_list""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_source_759(p):
    """copy_source : LOCAL copy_file_list"""
    p[0] = Expr("""copy_source""", """LOCAL copy_file_list""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_source_760(p):
    """copy_source : LOCAL STDIN opt_copy_compr_type"""
    p[0] = Expr("""copy_source""", """LOCAL STDIN opt_copy_compr_type""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_source_761(p):
    """copy_source : STDIN opt_copy_compr_type"""
    p[0] = Expr("""copy_source""", """STDIN opt_copy_compr_type""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_source_762(p):
    """copy_source : EXPORT Sconst"""
    p[0] = Expr("""copy_source""", """EXPORT Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_source_763(p):
    """copy_source : VERTICA export_relation opt_export_column_list"""
    p[0] = Expr("""copy_source""", """VERTICA export_relation opt_export_column_list""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_file_list_764(p):
    """copy_file_list : copy_file_type"""
    p[0] = Expr("""copy_file_list""", """copy_file_type""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_file_list_765(p):
    """copy_file_list : copy_file_list ',' copy_file_type"""
    p[0] = Expr("""copy_file_list""", """copy_file_list ',' copy_file_type""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_file_type_766(p):
    """copy_file_type : copy_file opt_copy_compr_type"""
    p[0] = Expr("""copy_file_type""", """copy_file opt_copy_compr_type""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_file_format_767(p):
    """opt_copy_file_format : NATIVE"""
    p[0] = Expr("""opt_copy_file_format""", """NATIVE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_file_format_768(p):
    """opt_copy_file_format : NATIVE VARCHAR"""
    p[0] = Expr("""opt_copy_file_format""", """NATIVE VARCHAR""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_file_format_769(p):
    """opt_copy_file_format : FIXEDWIDTH COLSIZES '(' widthsList ')'"""
    p[0] = Expr("""opt_copy_file_format""", """FIXEDWIDTH COLSIZES '(' widthsList ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_file_format_770(p):
    """opt_copy_file_format : PARQUET"""
    p[0] = Expr("""opt_copy_file_format""", """PARQUET""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_file_format_771(p):
    """opt_copy_file_format : PARQUET '(' parquet_opt_list ')'"""
    p[0] = Expr("""opt_copy_file_format""", """PARQUET '(' parquet_opt_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_file_format_772(p):
    """opt_copy_file_format : ORC"""
    p[0] = Expr("""opt_copy_file_format""", """ORC""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_file_format_773(p):
    """opt_copy_file_format : ORC '(' orc_opt_list ')'"""
    p[0] = Expr("""opt_copy_file_format""", """ORC '(' orc_opt_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_file_format_774(p):
    """opt_copy_file_format : """
    p[0] = Expr("""opt_copy_file_format""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_parquet_opt_list_775(p):
    """parquet_opt_list : parquetOptElem"""
    p[0] = Expr("""parquet_opt_list""", """parquetOptElem""", p[1:] if len(p or []) > 1 else [], p)


def p_parquet_opt_list_776(p):
    """parquet_opt_list : parquet_opt_list ',' parquetOptElem"""
    p[0] = Expr("""parquet_opt_list""", """parquet_opt_list ',' parquetOptElem""", p[1:] if len(p or []) > 1 else [], p)


def p_parquetOptElem_777(p):
    """parquetOptElem : hive_arg_name '=' Sconst"""
    p[0] = Expr("""parquetOptElem""", """hive_arg_name '=' Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_orc_opt_list_778(p):
    """orc_opt_list : orcOptElem"""
    p[0] = Expr("""orc_opt_list""", """orcOptElem""", p[1:] if len(p or []) > 1 else [], p)


def p_orc_opt_list_779(p):
    """orc_opt_list : orc_opt_list ',' orcOptElem"""
    p[0] = Expr("""orc_opt_list""", """orc_opt_list ',' orcOptElem""", p[1:] if len(p or []) > 1 else [], p)


def p_orcOptElem_780(p):
    """orcOptElem : hive_arg_name '=' Sconst"""
    p[0] = Expr("""orcOptElem""", """hive_arg_name '=' Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_compr_type_781(p):
    """opt_copy_compr_type : GZIP"""
    p[0] = Expr("""opt_copy_compr_type""", """GZIP""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_compr_type_782(p):
    """opt_copy_compr_type : BZIP"""
    p[0] = Expr("""opt_copy_compr_type""", """BZIP""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_compr_type_783(p):
    """opt_copy_compr_type : ZSTD"""
    p[0] = Expr("""opt_copy_compr_type""", """ZSTD""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_compr_type_784(p):
    """opt_copy_compr_type : LZO"""
    p[0] = Expr("""opt_copy_compr_type""", """LZO""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_compr_type_785(p):
    """opt_copy_compr_type : UNCOMPRESSED"""
    p[0] = Expr("""opt_copy_compr_type""", """UNCOMPRESSED""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_compr_type_786(p):
    """opt_copy_compr_type : """
    p[0] = Expr("""opt_copy_compr_type""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptCopy_787(p):
    """OptCopy : copy_storage_mode"""
    p[0] = Expr("""OptCopy""", """copy_storage_mode""", p[1:] if len(p or []) > 1 else [], p)


def p_OptCopy_788(p):
    """OptCopy : """
    p[0] = Expr("""OptCopy""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_storage_mode_789(p):
    """copy_storage_mode : DIRECT"""
    p[0] = Expr("""copy_storage_mode""", """DIRECT""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_storage_mode_790(p):
    """copy_storage_mode : TRICKLE"""
    p[0] = Expr("""copy_storage_mode""", """TRICKLE""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_storage_mode_791(p):
    """copy_storage_mode : AUTO"""
    p[0] = Expr("""copy_storage_mode""", """AUTO""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_storage_mode_792(p):
    """copy_storage_mode : DEFAULT"""
    p[0] = Expr("""copy_storage_mode""", """DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_storage_target_793(p):
    """copy_storage_target : DIRECT"""
    p[0] = Expr("""copy_storage_target""", """DIRECT""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_storage_target_794(p):
    """copy_storage_target : DIRECTCOLS"""
    p[0] = Expr("""copy_storage_target""", """DIRECTCOLS""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_storage_target_795(p):
    """copy_storage_target : DIRECTGROUPED"""
    p[0] = Expr("""copy_storage_target""", """DIRECTGROUPED""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_storage_target_796(p):
    """copy_storage_target : DIRECTPROJ"""
    p[0] = Expr("""copy_storage_target""", """DIRECTPROJ""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_storage_target_797(p):
    """copy_storage_target : TRICKLE"""
    p[0] = Expr("""copy_storage_target""", """TRICKLE""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_storage_target_798(p):
    """copy_storage_target : AUTO"""
    p[0] = Expr("""copy_storage_target""", """AUTO""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_list_799(p):
    """copy_opt_list : copy_opt_list copy_opt_item"""
    p[0] = Expr("""copy_opt_list""", """copy_opt_list copy_opt_item""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_list_800(p):
    """copy_opt_list : """
    p[0] = Expr("""copy_opt_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_rej_clause_801(p):
    """copy_rej_clause : copy_error_list"""
    p[0] = Expr("""copy_rej_clause""", """copy_error_list""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_rej_clause_802(p):
    """copy_rej_clause : TABLE qualified_name"""
    p[0] = Expr("""copy_rej_clause""", """TABLE qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_803(p):
    """copy_opt_item : ABORT_P ON ERROR_P"""
    p[0] = Expr("""copy_opt_item""", """ABORT_P ON ERROR_P""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_804(p):
    """copy_opt_item : BINARY"""
    p[0] = Expr("""copy_opt_item""", """BINARY""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_805(p):
    """copy_opt_item : CSV"""
    p[0] = Expr("""copy_opt_item""", """CSV""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_806(p):
    """copy_opt_item : DELIMITER opt_as Sconst"""
    p[0] = Expr("""copy_opt_item""", """DELIMITER opt_as Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_807(p):
    """copy_opt_item : ENCLOSED opt_by Sconst"""
    p[0] = Expr("""copy_opt_item""", """ENCLOSED opt_by Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_808(p):
    """copy_opt_item : ENFORCELENGTH"""
    p[0] = Expr("""copy_opt_item""", """ENFORCELENGTH""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_809(p):
    """copy_opt_item : ERROR_P TOLERANCE"""
    p[0] = Expr("""copy_opt_item""", """ERROR_P TOLERANCE""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_810(p):
    """copy_opt_item : ESCAPE opt_as Sconst"""
    p[0] = Expr("""copy_opt_item""", """ESCAPE opt_as Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_811(p):
    """copy_opt_item : NO ESCAPE"""
    p[0] = Expr("""copy_opt_item""", """NO ESCAPE""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_812(p):
    """copy_opt_item : EXCEPTIONS opt_as copy_error_list"""
    p[0] = Expr("""copy_opt_item""", """EXCEPTIONS opt_as copy_error_list""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_813(p):
    """copy_opt_item : FORCE NOT NULL_P columnList"""
    p[0] = Expr("""copy_opt_item""", """FORCE NOT NULL_P columnList""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_814(p):
    """copy_opt_item : FORCE QUOTE columnList"""
    p[0] = Expr("""copy_opt_item""", """FORCE QUOTE columnList""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_815(p):
    """copy_opt_item : MANAGED"""
    p[0] = Expr("""copy_opt_item""", """MANAGED""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_816(p):
    """copy_opt_item : NULL_P opt_as Sconst"""
    p[0] = Expr("""copy_opt_item""", """NULL_P opt_as Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_817(p):
    """copy_opt_item : OIDS"""
    p[0] = Expr("""copy_opt_item""", """OIDS""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_818(p):
    """copy_opt_item : QUOTE opt_as Sconst"""
    p[0] = Expr("""copy_opt_item""", """QUOTE opt_as Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_819(p):
    """copy_opt_item : RECORD_P TERMINATOR_P opt_as Sconst"""
    p[0] = Expr("""copy_opt_item""", """RECORD_P TERMINATOR_P opt_as Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_820(p):
    """copy_opt_item : REJECTED_P DATA_P opt_as copy_rej_clause"""
    p[0] = Expr("""copy_opt_item""", """REJECTED_P DATA_P opt_as copy_rej_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_821(p):
    """copy_opt_item : REJECTMAX IntegerOnly"""
    p[0] = Expr("""copy_opt_item""", """REJECTMAX IntegerOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_822(p):
    """copy_opt_item : RETURNREJECTED"""
    p[0] = Expr("""copy_opt_item""", """RETURNREJECTED""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_823(p):
    """copy_opt_item : SKIP IntegerOnly"""
    p[0] = Expr("""copy_opt_item""", """SKIP IntegerOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_824(p):
    """copy_opt_item : SKIP BYTES IntegerOnly"""
    p[0] = Expr("""copy_opt_item""", """SKIP BYTES IntegerOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_825(p):
    """copy_opt_item : STORAGE copy_storage_target"""
    p[0] = Expr("""copy_opt_item""", """STORAGE copy_storage_target""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_826(p):
    """copy_opt_item : STREAM_P NAME_P opt_as Sconst"""
    p[0] = Expr("""copy_opt_item""", """STREAM_P NAME_P opt_as Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_827(p):
    """copy_opt_item : TRAILING NULLCOLS"""
    p[0] = Expr("""copy_opt_item""", """TRAILING NULLCOLS""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_828(p):
    """copy_opt_item : TRIM Sconst"""
    p[0] = Expr("""copy_opt_item""", """TRIM Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_item_829(p):
    """copy_opt_item : copy_storage_target"""
    p[0] = Expr("""copy_opt_item""", """copy_storage_target""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_commit_830(p):
    """copy_opt_commit : COMMIT"""
    p[0] = Expr("""copy_opt_commit""", """COMMIT""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_commit_831(p):
    """copy_opt_commit : NO COMMIT"""
    p[0] = Expr("""copy_opt_commit""", """NO COMMIT""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_opt_commit_832(p):
    """copy_opt_commit : """
    p[0] = Expr("""copy_opt_commit""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_binary_833(p):
    """opt_binary : BINARY"""
    p[0] = Expr("""opt_binary""", """BINARY""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_binary_834(p):
    """opt_binary : """
    p[0] = Expr("""opt_binary""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_delimiter_835(p):
    """copy_delimiter : opt_using DELIMITERS Sconst"""
    p[0] = Expr("""copy_delimiter""", """opt_using DELIMITERS Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_delimiter_836(p):
    """copy_delimiter : """
    p[0] = Expr("""copy_delimiter""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_using_837(p):
    """opt_using : USING"""
    p[0] = Expr("""opt_using""", """USING""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_using_838(p):
    """opt_using : """
    p[0] = Expr("""opt_using""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_error_list_839(p):
    """copy_error_list : copy_file"""
    p[0] = Expr("""copy_error_list""", """copy_file""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_error_list_840(p):
    """copy_error_list : copy_error_list ',' copy_file"""
    p[0] = Expr("""copy_error_list""", """copy_error_list ',' copy_file""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_file_841(p):
    """copy_file : file_name opt_copy_node"""
    p[0] = Expr("""copy_file""", """file_name opt_copy_node""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_node_842(p):
    """opt_copy_node : ON copy_node_list"""
    p[0] = Expr("""opt_copy_node""", """ON copy_node_list""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_node_843(p):
    """opt_copy_node : ON ANY NODE"""
    p[0] = Expr("""opt_copy_node""", """ON ANY NODE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_node_844(p):
    """opt_copy_node : """
    p[0] = Expr("""opt_copy_node""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_node_list_845(p):
    """copy_node_list : name"""
    p[0] = Expr("""copy_node_list""", """name""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_node_list_846(p):
    """copy_node_list : '(' copy_node_list_inner ')'"""
    p[0] = Expr("""copy_node_list""", """'(' copy_node_list_inner ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_node_list_inner_847(p):
    """copy_node_list_inner : name"""
    p[0] = Expr("""copy_node_list_inner""", """name""", p[1:] if len(p or []) > 1 else [], p)


def p_copy_node_list_inner_848(p):
    """copy_node_list_inner : copy_node_list_inner ',' name"""
    p[0] = Expr("""copy_node_list_inner""", """copy_node_list_inner ',' name""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_parse_option_list_849(p):
    """opt_parse_option_list : COLUMN OPTION '(' copyParseList ')'"""
    p[0] = Expr("""opt_parse_option_list""", """COLUMN OPTION '(' copyParseList ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_parse_option_list_850(p):
    """opt_parse_option_list : """
    p[0] = Expr("""opt_parse_option_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_copyParseList_851(p):
    """copyParseList : copyParseElem"""
    p[0] = Expr("""copyParseList""", """copyParseElem""", p[1:] if len(p or []) > 1 else [], p)


def p_copyParseList_852(p):
    """copyParseList : copyParseList ',' copyParseElem"""
    p[0] = Expr("""copyParseList""", """copyParseList ',' copyParseElem""", p[1:] if len(p or []) > 1 else [], p)


def p_copyParseElem_853(p):
    """copyParseElem : ColId copyColumnFeatureList"""
    p[0] = Expr("""copyParseElem""", """ColId copyColumnFeatureList""", p[1:] if len(p or []) > 1 else [], p)


def p_widthsList_854(p):
    """widthsList : Iconst"""
    p[0] = Expr("""widthsList""", """Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_widthsList_855(p):
    """widthsList : widthsList ',' Iconst"""
    p[0] = Expr("""widthsList""", """widthsList ',' Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_column_list_856(p):
    """opt_copy_column_list : '(' copyColumnList ')'"""
    p[0] = Expr("""opt_copy_column_list""", """'(' copyColumnList ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_copy_column_list_857(p):
    """opt_copy_column_list : """
    p[0] = Expr("""opt_copy_column_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnList_858(p):
    """copyColumnList : copyColumnElem"""
    p[0] = Expr("""copyColumnList""", """copyColumnElem""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnList_859(p):
    """copyColumnList : copyColumnList ',' copyColumnElem"""
    p[0] = Expr("""copyColumnList""", """copyColumnList ',' copyColumnElem""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnElem_860(p):
    """copyColumnElem : columnref"""
    p[0] = Expr("""copyColumnElem""", """columnref""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnElem_861(p):
    """copyColumnElem : columnref copyColumnFeatureList"""
    p[0] = Expr("""copyColumnElem""", """columnref copyColumnFeatureList""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnElem_862(p):
    """copyColumnElem : columnref AS a_expr"""
    p[0] = Expr("""copyColumnElem""", """columnref AS a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnElem_863(p):
    """copyColumnElem : columnref FILLER TypenameWithTypmod"""
    p[0] = Expr("""copyColumnElem""", """columnref FILLER TypenameWithTypmod""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnElem_864(p):
    """copyColumnElem : columnref FILLER TypenameWithTypmod copyColumnFeatureList"""
    p[0] = Expr("""copyColumnElem""", """columnref FILLER TypenameWithTypmod copyColumnFeatureList""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnElem_865(p):
    """copyColumnElem : columnref '(' paramarg_list ')'"""
    p[0] = Expr("""copyColumnElem""", """columnref '(' paramarg_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnFeatureList_866(p):
    """copyColumnFeatureList : copyColumnFeature"""
    p[0] = Expr("""copyColumnFeatureList""", """copyColumnFeature""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnFeatureList_867(p):
    """copyColumnFeatureList : copyColumnFeatureList copyColumnFeature"""
    p[0] = Expr("""copyColumnFeatureList""", """copyColumnFeatureList copyColumnFeature""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnFeature_868(p):
    """copyColumnFeature : FORMAT Sconst"""
    p[0] = Expr("""copyColumnFeature""", """FORMAT Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnFeature_869(p):
    """copyColumnFeature : DELIMITER opt_as Sconst"""
    p[0] = Expr("""copyColumnFeature""", """DELIMITER opt_as Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnFeature_870(p):
    """copyColumnFeature : NULL_P opt_as Sconst"""
    p[0] = Expr("""copyColumnFeature""", """NULL_P opt_as Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnFeature_871(p):
    """copyColumnFeature : ENCLOSED opt_by Sconst"""
    p[0] = Expr("""copyColumnFeature""", """ENCLOSED opt_by Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnFeature_872(p):
    """copyColumnFeature : ENFORCELENGTH"""
    p[0] = Expr("""copyColumnFeature""", """ENFORCELENGTH""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnFeature_873(p):
    """copyColumnFeature : ESCAPE opt_as Sconst"""
    p[0] = Expr("""copyColumnFeature""", """ESCAPE opt_as Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnFeature_874(p):
    """copyColumnFeature : NO ESCAPE"""
    p[0] = Expr("""copyColumnFeature""", """NO ESCAPE""", p[1:] if len(p or []) > 1 else [], p)


def p_copyColumnFeature_875(p):
    """copyColumnFeature : TRIM Sconst"""
    p[0] = Expr("""copyColumnFeature""", """TRIM Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_columns_count_876(p):
    """opt_columns_count : COLUMNS_COUNT IntegerOnly"""
    p[0] = Expr("""opt_columns_count""", """COLUMNS_COUNT IntegerOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_columns_count_877(p):
    """opt_columns_count : """
    p[0] = Expr("""opt_columns_count""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateStmt_878(p):
    """CreateStmt : CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges"""
    p[0] = Expr("""CreateStmt""", """CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateStmt_879(p):
    """CreateStmt : CREATE OptTemp TABLE qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges"""
    p[0] = Expr("""CreateStmt""", """CREATE OptTemp TABLE qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateStmt_880(p):
    """CreateStmt : CREATE FLEX OptTemp TABLE qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges"""
    p[0] = Expr("""CreateStmt""", """CREATE FLEX OptTemp TABLE qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateStmt_881(p):
    """CreateStmt : CREATE FLEXIBLE OptTemp TABLE qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges"""
    p[0] = Expr("""CreateStmt""", """CREATE FLEXIBLE OptTemp TABLE qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateStmt_882(p):
    """CreateStmt : CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges"""
    p[0] = Expr("""CreateStmt""", """CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateStmt_883(p):
    """CreateStmt : CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges"""
    p[0] = Expr("""CreateStmt""", """CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateStmt_884(p):
    """CreateStmt : CREATE OptTemp TABLE qualified_name OF qualified_name '(' OptTableElementList ')' OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges"""
    p[0] = Expr("""CreateStmt""", """CREATE OptTemp TABLE qualified_name OF qualified_name '(' OptTableElementList ')' OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateStmt_885(p):
    """CreateStmt : CREATE OptTemp TABLE qualified_name TableLikeClause OptCopy OptInheritPrivileges"""
    p[0] = Expr("""CreateStmt""", """CREATE OptTemp TABLE qualified_name TableLikeClause OptCopy OptInheritPrivileges""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateStmt_886(p):
    """CreateStmt : CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name TableLikeClause OptCopy OptInheritPrivileges"""
    p[0] = Expr("""CreateStmt""", """CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name TableLikeClause OptCopy OptInheritPrivileges""", p[1:] if len(p or []) > 1 else [], p)


def p_VPartition_887(p):
    """VPartition : PARTITION BY b_expr GROUP_P BY b_expr ACTIVEPARTITIONCOUNT active_partition_count"""
    p[0] = Expr("""VPartition""", """PARTITION BY b_expr GROUP_P BY b_expr ACTIVEPARTITIONCOUNT active_partition_count""", p[1:] if len(p or []) > 1 else [], p)


def p_VPartition_888(p):
    """VPartition : PARTITION BY b_expr GROUP_P BY b_expr"""
    p[0] = Expr("""VPartition""", """PARTITION BY b_expr GROUP_P BY b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_VPartition_889(p):
    """VPartition : PARTITION BY b_expr ACTIVEPARTITIONCOUNT active_partition_count"""
    p[0] = Expr("""VPartition""", """PARTITION BY b_expr ACTIVEPARTITIONCOUNT active_partition_count""", p[1:] if len(p or []) > 1 else [], p)


def p_VPartition_890(p):
    """VPartition : PARTITION BY b_expr"""
    p[0] = Expr("""VPartition""", """PARTITION BY b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_VPartition_891(p):
    """VPartition : """
    p[0] = Expr("""VPartition""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptInheritPrivileges_892(p):
    """OptInheritPrivileges : INCLUDE SCHEMA PRIVILEGES"""
    p[0] = Expr("""OptInheritPrivileges""", """INCLUDE SCHEMA PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_OptInheritPrivileges_893(p):
    """OptInheritPrivileges : INCLUDE PRIVILEGES"""
    p[0] = Expr("""OptInheritPrivileges""", """INCLUDE PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_OptInheritPrivileges_894(p):
    """OptInheritPrivileges : EXCLUDE SCHEMA PRIVILEGES"""
    p[0] = Expr("""OptInheritPrivileges""", """EXCLUDE SCHEMA PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_OptInheritPrivileges_895(p):
    """OptInheritPrivileges : EXCLUDE PRIVILEGES"""
    p[0] = Expr("""OptInheritPrivileges""", """EXCLUDE PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_OptInheritPrivileges_896(p):
    """OptInheritPrivileges : """
    p[0] = Expr("""OptInheritPrivileges""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTemp_897(p):
    """OptTemp : TEMPORARY"""
    p[0] = Expr("""OptTemp""", """TEMPORARY""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTemp_898(p):
    """OptTemp : TEMP"""
    p[0] = Expr("""OptTemp""", """TEMP""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTemp_899(p):
    """OptTemp : LOCAL TEMPORARY"""
    p[0] = Expr("""OptTemp""", """LOCAL TEMPORARY""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTemp_900(p):
    """OptTemp : LOCAL TEMP"""
    p[0] = Expr("""OptTemp""", """LOCAL TEMP""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTemp_901(p):
    """OptTemp : GLOBAL TEMPORARY"""
    p[0] = Expr("""OptTemp""", """GLOBAL TEMPORARY""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTemp_902(p):
    """OptTemp : GLOBAL TEMP"""
    p[0] = Expr("""OptTemp""", """GLOBAL TEMP""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTemp_903(p):
    """OptTemp : """
    p[0] = Expr("""OptTemp""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptLocalTempOnly_904(p):
    """OptLocalTempOnly : LOCAL TEMPORARY"""
    p[0] = Expr("""OptLocalTempOnly""", """LOCAL TEMPORARY""", p[1:] if len(p or []) > 1 else [], p)


def p_OptLocalTempOnly_905(p):
    """OptLocalTempOnly : LOCAL TEMP"""
    p[0] = Expr("""OptLocalTempOnly""", """LOCAL TEMP""", p[1:] if len(p or []) > 1 else [], p)


def p_OptLocalTempOnly_906(p):
    """OptLocalTempOnly : """
    p[0] = Expr("""OptLocalTempOnly""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTableElementList_907(p):
    """OptTableElementList : TableElementList"""
    p[0] = Expr("""OptTableElementList""", """TableElementList""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTableElementList_908(p):
    """OptTableElementList : """
    p[0] = Expr("""OptTableElementList""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_TableElementList_909(p):
    """TableElementList : TableElement"""
    p[0] = Expr("""TableElementList""", """TableElement""", p[1:] if len(p or []) > 1 else [], p)


def p_TableElementList_910(p):
    """TableElementList : TableElementList ',' TableElement"""
    p[0] = Expr("""TableElementList""", """TableElementList ',' TableElement""", p[1:] if len(p or []) > 1 else [], p)


def p_TableElement_911(p):
    """TableElement : columnDef encode_type index_type opt_access_rank"""
    p[0] = Expr("""TableElement""", """columnDef encode_type index_type opt_access_rank""", p[1:] if len(p or []) > 1 else [], p)


def p_TableElement_912(p):
    """TableElement : TableLikeClause"""
    p[0] = Expr("""TableElement""", """TableLikeClause""", p[1:] if len(p or []) > 1 else [], p)


def p_TableElement_913(p):
    """TableElement : TableConstraint"""
    p[0] = Expr("""TableElement""", """TableConstraint""", p[1:] if len(p or []) > 1 else [], p)


def p_columnDef_914(p):
    """columnDef : ColId TypenameWithTypmod ColQualList"""
    p[0] = Expr("""columnDef""", """ColId TypenameWithTypmod ColQualList""", p[1:] if len(p or []) > 1 else [], p)


def p_columnDef_915(p):
    """columnDef : ColId IDENT '(' Iconst ')' ColQualList"""
    p[0] = Expr("""columnDef""", """ColId IDENT '(' Iconst ')' ColQualList""", p[1:] if len(p or []) > 1 else [], p)


def p_ColQualList_916(p):
    """ColQualList : ColQualList ColConstraint"""
    p[0] = Expr("""ColQualList""", """ColQualList ColConstraint""", p[1:] if len(p or []) > 1 else [], p)


def p_ColQualList_917(p):
    """ColQualList : """
    p[0] = Expr("""ColQualList""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_ColConstraint_918(p):
    """ColConstraint : CONSTRAINT name ColConstraintElem"""
    p[0] = Expr("""ColConstraint""", """CONSTRAINT name ColConstraintElem""", p[1:] if len(p or []) > 1 else [], p)


def p_ColConstraint_919(p):
    """ColConstraint : ColConstraintElem"""
    p[0] = Expr("""ColConstraint""", """ColConstraintElem""", p[1:] if len(p or []) > 1 else [], p)


def p_ColConstraint_920(p):
    """ColConstraint : ConstraintAttr"""
    p[0] = Expr("""ColConstraint""", """ConstraintAttr""", p[1:] if len(p or []) > 1 else [], p)


def p_ColConstraintElem_921(p):
    """ColConstraintElem : NOT NULL_P"""
    p[0] = Expr("""ColConstraintElem""", """NOT NULL_P""", p[1:] if len(p or []) > 1 else [], p)


def p_ColConstraintElem_922(p):
    """ColConstraintElem : NULL_P"""
    p[0] = Expr("""ColConstraintElem""", """NULL_P""", p[1:] if len(p or []) > 1 else [], p)


def p_ColConstraintElem_923(p):
    """ColConstraintElem : UNIQUE OptConsTableSpace OptConsStatus"""
    p[0] = Expr("""ColConstraintElem""", """UNIQUE OptConsTableSpace OptConsStatus""", p[1:] if len(p or []) > 1 else [], p)


def p_ColConstraintElem_924(p):
    """ColConstraintElem : PRIMARY KEY OptConsTableSpace OptConsStatus"""
    p[0] = Expr("""ColConstraintElem""", """PRIMARY KEY OptConsTableSpace OptConsStatus""", p[1:] if len(p or []) > 1 else [], p)


def p_ColConstraintElem_925(p):
    """ColConstraintElem : CHECK '(' a_expr ')' OptConsStatus"""
    p[0] = Expr("""ColConstraintElem""", """CHECK '(' a_expr ')' OptConsStatus""", p[1:] if len(p or []) > 1 else [], p)


def p_ColConstraintElem_926(p):
    """ColConstraintElem : DEFAULT b_expr"""
    p[0] = Expr("""ColConstraintElem""", """DEFAULT b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ColConstraintElem_927(p):
    """ColConstraintElem : SET USING b_expr"""
    p[0] = Expr("""ColConstraintElem""", """SET USING b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ColConstraintElem_928(p):
    """ColConstraintElem : DEFAULT USING b_expr"""
    p[0] = Expr("""ColConstraintElem""", """DEFAULT USING b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ColConstraintElem_929(p):
    """ColConstraintElem : REFERENCES qualified_name opt_column_list key_match key_actions"""
    p[0] = Expr("""ColConstraintElem""", """REFERENCES qualified_name opt_column_list key_match key_actions""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintAttr_930(p):
    """ConstraintAttr : DEFERRABLE"""
    p[0] = Expr("""ConstraintAttr""", """DEFERRABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintAttr_931(p):
    """ConstraintAttr : NOT DEFERRABLE"""
    p[0] = Expr("""ConstraintAttr""", """NOT DEFERRABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintAttr_932(p):
    """ConstraintAttr : INITIALLY DEFERRED"""
    p[0] = Expr("""ConstraintAttr""", """INITIALLY DEFERRED""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintAttr_933(p):
    """ConstraintAttr : INITIALLY IMMEDIATE"""
    p[0] = Expr("""ConstraintAttr""", """INITIALLY IMMEDIATE""", p[1:] if len(p or []) > 1 else [], p)


def p_TableLikeClause_934(p):
    """TableLikeClause : LIKE qualified_name like_including_projections"""
    p[0] = Expr("""TableLikeClause""", """LIKE qualified_name like_including_projections""", p[1:] if len(p or []) > 1 else [], p)


def p_like_including_projections_935(p):
    """like_including_projections : INCLUDING PROJECTIONS"""
    p[0] = Expr("""like_including_projections""", """INCLUDING PROJECTIONS""", p[1:] if len(p or []) > 1 else [], p)


def p_like_including_projections_936(p):
    """like_including_projections : EXCLUDING PROJECTIONS"""
    p[0] = Expr("""like_including_projections""", """EXCLUDING PROJECTIONS""", p[1:] if len(p or []) > 1 else [], p)


def p_like_including_projections_937(p):
    """like_including_projections : """
    p[0] = Expr("""like_including_projections""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_TableConstraint_938(p):
    """TableConstraint : CONSTRAINT name ConstraintElem"""
    p[0] = Expr("""TableConstraint""", """CONSTRAINT name ConstraintElem""", p[1:] if len(p or []) > 1 else [], p)


def p_TableConstraint_939(p):
    """TableConstraint : ConstraintElem"""
    p[0] = Expr("""TableConstraint""", """ConstraintElem""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintElem_940(p):
    """ConstraintElem : CHECK '(' a_expr ')' OptConsStatus"""
    p[0] = Expr("""ConstraintElem""", """CHECK '(' a_expr ')' OptConsStatus""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintElem_941(p):
    """ConstraintElem : UNIQUE '(' columnList ')' OptConsTableSpace OptConsStatus"""
    p[0] = Expr("""ConstraintElem""", """UNIQUE '(' columnList ')' OptConsTableSpace OptConsStatus""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintElem_942(p):
    """ConstraintElem : PRIMARY KEY '(' columnList ')' OptConsTableSpace OptConsStatus"""
    p[0] = Expr("""ConstraintElem""", """PRIMARY KEY '(' columnList ')' OptConsTableSpace OptConsStatus""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintElem_943(p):
    """ConstraintElem : FOREIGN KEY '(' columnList ')' REFERENCES qualified_name opt_column_list key_match key_actions ConstraintAttributeSpec"""
    p[0] = Expr("""ConstraintElem""", """FOREIGN KEY '(' columnList ')' REFERENCES qualified_name opt_column_list key_match key_actions ConstraintAttributeSpec""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintElem_944(p):
    """ConstraintElem : CORRELATION '(' columnList ')' opt_determines_clause OptionalStrengthValue"""
    p[0] = Expr("""ConstraintElem""", """CORRELATION '(' columnList ')' opt_determines_clause OptionalStrengthValue""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_column_list_945(p):
    """opt_column_list : '(' columnList ')'"""
    p[0] = Expr("""opt_column_list""", """'(' columnList ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_column_list_946(p):
    """opt_column_list : """
    p[0] = Expr("""opt_column_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_columnList_947(p):
    """columnList : columnElem"""
    p[0] = Expr("""columnList""", """columnElem""", p[1:] if len(p or []) > 1 else [], p)


def p_columnList_948(p):
    """columnList : columnList ',' columnElem"""
    p[0] = Expr("""columnList""", """columnList ',' columnElem""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_determines_clause_949(p):
    """opt_determines_clause : DETERMINES '(' columnElem ')'"""
    p[0] = Expr("""opt_determines_clause""", """DETERMINES '(' columnElem ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_determines_clause_950(p):
    """opt_determines_clause : """
    p[0] = Expr("""opt_determines_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptionalStrengthValue_951(p):
    """OptionalStrengthValue : STRENGTH opt_minus FCONST"""
    p[0] = Expr("""OptionalStrengthValue""", """STRENGTH opt_minus FCONST""", p[1:] if len(p or []) > 1 else [], p)


def p_OptionalStrengthValue_952(p):
    """OptionalStrengthValue : STRENGTH opt_minus ICONST"""
    p[0] = Expr("""OptionalStrengthValue""", """STRENGTH opt_minus ICONST""", p[1:] if len(p or []) > 1 else [], p)


def p_OptionalStrengthValue_953(p):
    """OptionalStrengthValue : """
    p[0] = Expr("""OptionalStrengthValue""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_columnElem_954(p):
    """columnElem : ColId"""
    p[0] = Expr("""columnElem""", """ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_key_match_955(p):
    """key_match : MATCH FULL"""
    p[0] = Expr("""key_match""", """MATCH FULL""", p[1:] if len(p or []) > 1 else [], p)


def p_key_match_956(p):
    """key_match : MATCH PARTIAL"""
    p[0] = Expr("""key_match""", """MATCH PARTIAL""", p[1:] if len(p or []) > 1 else [], p)


def p_key_match_957(p):
    """key_match : MATCH SIMPLE"""
    p[0] = Expr("""key_match""", """MATCH SIMPLE""", p[1:] if len(p or []) > 1 else [], p)


def p_key_match_958(p):
    """key_match : """
    p[0] = Expr("""key_match""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_key_actions_959(p):
    """key_actions : key_update"""
    p[0] = Expr("""key_actions""", """key_update""", p[1:] if len(p or []) > 1 else [], p)


def p_key_actions_960(p):
    """key_actions : key_delete"""
    p[0] = Expr("""key_actions""", """key_delete""", p[1:] if len(p or []) > 1 else [], p)


def p_key_actions_961(p):
    """key_actions : key_update key_delete"""
    p[0] = Expr("""key_actions""", """key_update key_delete""", p[1:] if len(p or []) > 1 else [], p)


def p_key_actions_962(p):
    """key_actions : key_delete key_update"""
    p[0] = Expr("""key_actions""", """key_delete key_update""", p[1:] if len(p or []) > 1 else [], p)


def p_key_actions_963(p):
    """key_actions : """
    p[0] = Expr("""key_actions""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_key_update_964(p):
    """key_update : ON UPDATE key_action"""
    p[0] = Expr("""key_update""", """ON UPDATE key_action""", p[1:] if len(p or []) > 1 else [], p)


def p_key_delete_965(p):
    """key_delete : ON DELETE_P key_action"""
    p[0] = Expr("""key_delete""", """ON DELETE_P key_action""", p[1:] if len(p or []) > 1 else [], p)


def p_key_action_966(p):
    """key_action : NO ACTION"""
    p[0] = Expr("""key_action""", """NO ACTION""", p[1:] if len(p or []) > 1 else [], p)


def p_key_action_967(p):
    """key_action : RESTRICT"""
    p[0] = Expr("""key_action""", """RESTRICT""", p[1:] if len(p or []) > 1 else [], p)


def p_key_action_968(p):
    """key_action : CASCADE"""
    p[0] = Expr("""key_action""", """CASCADE""", p[1:] if len(p or []) > 1 else [], p)


def p_key_action_969(p):
    """key_action : SET NULL_P"""
    p[0] = Expr("""key_action""", """SET NULL_P""", p[1:] if len(p or []) > 1 else [], p)


def p_key_action_970(p):
    """key_action : SET DEFAULT"""
    p[0] = Expr("""key_action""", """SET DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_OptInherit_971(p):
    """OptInherit : INHERITS '(' qualified_name_list ')'"""
    p[0] = Expr("""OptInherit""", """INHERITS '(' qualified_name_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_OptInherit_972(p):
    """OptInherit : """
    p[0] = Expr("""OptInherit""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptWithOids_973(p):
    """OptWithOids : WITH OIDS"""
    p[0] = Expr("""OptWithOids""", """WITH OIDS""", p[1:] if len(p or []) > 1 else [], p)


def p_OptWithOids_974(p):
    """OptWithOids : WITHOUT OIDS"""
    p[0] = Expr("""OptWithOids""", """WITHOUT OIDS""", p[1:] if len(p or []) > 1 else [], p)


def p_OptWithOids_975(p):
    """OptWithOids : """
    p[0] = Expr("""OptWithOids""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OnCommitOption_976(p):
    """OnCommitOption : ON COMMIT DROP"""
    p[0] = Expr("""OnCommitOption""", """ON COMMIT DROP""", p[1:] if len(p or []) > 1 else [], p)


def p_OnCommitOption_977(p):
    """OnCommitOption : ON COMMIT DELETE_P ROWS"""
    p[0] = Expr("""OnCommitOption""", """ON COMMIT DELETE_P ROWS""", p[1:] if len(p or []) > 1 else [], p)


def p_OnCommitOption_978(p):
    """OnCommitOption : ON COMMIT PRESERVE ROWS"""
    p[0] = Expr("""OnCommitOption""", """ON COMMIT PRESERVE ROWS""", p[1:] if len(p or []) > 1 else [], p)


def p_OnCommitOption_979(p):
    """OnCommitOption : """
    p[0] = Expr("""OnCommitOption""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTableSpace_980(p):
    """OptTableSpace : TABLESPACE name"""
    p[0] = Expr("""OptTableSpace""", """TABLESPACE name""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTableSpace_981(p):
    """OptTableSpace : """
    p[0] = Expr("""OptTableSpace""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptConsTableSpace_982(p):
    """OptConsTableSpace : USING INDEX TABLESPACE name"""
    p[0] = Expr("""OptConsTableSpace""", """USING INDEX TABLESPACE name""", p[1:] if len(p or []) > 1 else [], p)


def p_OptConsTableSpace_983(p):
    """OptConsTableSpace : """
    p[0] = Expr("""OptConsTableSpace""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptConsStatus_984(p):
    """OptConsStatus : ENABLED"""
    p[0] = Expr("""OptConsStatus""", """ENABLED""", p[1:] if len(p or []) > 1 else [], p)


def p_OptConsStatus_985(p):
    """OptConsStatus : DISABLED"""
    p[0] = Expr("""OptConsStatus""", """DISABLED""", p[1:] if len(p or []) > 1 else [], p)


def p_OptConsStatus_986(p):
    """OptConsStatus : """
    p[0] = Expr("""OptConsStatus""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_987(p):
    """CreateAsStmt : CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_988(p):
    """CreateAsStmt : CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_989(p):
    """CreateAsStmt : CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_990(p):
    """CreateAsStmt : CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_991(p):
    """CreateAsStmt : CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_992(p):
    """CreateAsStmt : CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClausesNoKsafe"""
    p[0] = Expr("""CreateAsStmt""", """CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClausesNoKsafe""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_993(p):
    """CreateAsStmt : CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClausesRequireKsafe VPartition"""
    p[0] = Expr("""CreateAsStmt""", """CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClausesRequireKsafe VPartition""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_994(p):
    """CreateAsStmt : CREATE FLEX OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEX OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_995(p):
    """CreateAsStmt : CREATE FLEX OptTemp TABLE qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEX OptTemp TABLE qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_996(p):
    """CreateAsStmt : CREATE FLEXIBLE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEXIBLE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_997(p):
    """CreateAsStmt : CREATE FLEXIBLE OptTemp TABLE qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEXIBLE OptTemp TABLE qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_998(p):
    """CreateAsStmt : CREATE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_999(p):
    """CreateAsStmt : CREATE MANAGED EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE MANAGED EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1000(p):
    """CreateAsStmt : CREATE FLEX EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEX EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1001(p):
    """CreateAsStmt : CREATE FLEXIBLE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEXIBLE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1002(p):
    """CreateAsStmt : CREATE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1003(p):
    """CreateAsStmt : CREATE MANAGED EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE MANAGED EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1004(p):
    """CreateAsStmt : CREATE FLEX EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEX EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1005(p):
    """CreateAsStmt : CREATE FLEXIBLE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEXIBLE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1006(p):
    """CreateAsStmt : CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1007(p):
    """CreateAsStmt : CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1008(p):
    """CreateAsStmt : CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1009(p):
    """CreateAsStmt : CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1010(p):
    """CreateAsStmt : CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1011(p):
    """CreateAsStmt : CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1012(p):
    """CreateAsStmt : CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClausesNoKsafe"""
    p[0] = Expr("""CreateAsStmt""", """CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClausesNoKsafe""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1013(p):
    """CreateAsStmt : CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClausesNoKsafe"""
    p[0] = Expr("""CreateAsStmt""", """CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClausesNoKsafe""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1014(p):
    """CreateAsStmt : CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClausesRequireKsafe VPartition"""
    p[0] = Expr("""CreateAsStmt""", """CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClausesRequireKsafe VPartition""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1015(p):
    """CreateAsStmt : CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClausesRequireKsafe VPartition"""
    p[0] = Expr("""CreateAsStmt""", """CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClausesRequireKsafe VPartition""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1016(p):
    """CreateAsStmt : CREATE FLEX OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEX OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1017(p):
    """CreateAsStmt : CREATE FLEX OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEX OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1018(p):
    """CreateAsStmt : CREATE FLEXIBLE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEXIBLE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1019(p):
    """CreateAsStmt : CREATE FLEXIBLE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEXIBLE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1020(p):
    """CreateAsStmt : CREATE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1021(p):
    """CreateAsStmt : CREATE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1022(p):
    """CreateAsStmt : CREATE MANAGED EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE MANAGED EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1023(p):
    """CreateAsStmt : CREATE MANAGED EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE MANAGED EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1024(p):
    """CreateAsStmt : CREATE FLEX EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEX EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1025(p):
    """CreateAsStmt : CREATE FLEX EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEX EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1026(p):
    """CreateAsStmt : CREATE FLEXIBLE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEXIBLE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1027(p):
    """CreateAsStmt : CREATE FLEXIBLE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEXIBLE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1028(p):
    """CreateAsStmt : CREATE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1029(p):
    """CreateAsStmt : CREATE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1030(p):
    """CreateAsStmt : CREATE MANAGED EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE MANAGED EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1031(p):
    """CreateAsStmt : CREATE MANAGED EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE MANAGED EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1032(p):
    """CreateAsStmt : CREATE FLEX EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEX EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1033(p):
    """CreateAsStmt : CREATE FLEXIBLE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEXIBLE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAsStmt_1034(p):
    """CreateAsStmt : CREATE FLEXIBLE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt"""
    p[0] = Expr("""CreateAsStmt""", """CREATE FLEXIBLE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_AutoProjectionDef_1035(p):
    """AutoProjectionDef : NO PROJECTION"""
    p[0] = Expr("""AutoProjectionDef""", """NO PROJECTION""", p[1:] if len(p or []) > 1 else [], p)


def p_AutoProjectionDef_1036(p):
    """AutoProjectionDef : opt_sort_clause ProjectionClauses"""
    p[0] = Expr("""AutoProjectionDef""", """opt_sort_clause ProjectionClauses""", p[1:] if len(p or []) > 1 else [], p)


def p_ProjectionClausesRequireKsafe_1037(p):
    """ProjectionClausesRequireKsafe : opt_encode_clause VSegmentation ksafe_num_required"""
    p[0] = Expr("""ProjectionClausesRequireKsafe""", """opt_encode_clause VSegmentation ksafe_num_required""", p[1:] if len(p or []) > 1 else [], p)


def p_ProjectionClausesNoKsafe_1038(p):
    """ProjectionClausesNoKsafe : opt_encode_clause VSegmentation"""
    p[0] = Expr("""ProjectionClausesNoKsafe""", """opt_encode_clause VSegmentation""", p[1:] if len(p or []) > 1 else [], p)


def p_ProjectionClauses_1039(p):
    """ProjectionClauses : opt_encode_clause VSegmentation ksafe_num"""
    p[0] = Expr("""ProjectionClauses""", """opt_encode_clause VSegmentation ksafe_num""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_encode_clause_1040(p):
    """opt_encode_clause : ENCODED BY vt_columnList"""
    p[0] = Expr("""opt_encode_clause""", """ENCODED BY vt_columnList""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_encode_clause_1041(p):
    """opt_encode_clause : """
    p[0] = Expr("""opt_encode_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSchemaKeyword_1042(p):
    """OptSchemaKeyword : SCHEMA"""
    p[0] = Expr("""OptSchemaKeyword""", """SCHEMA""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSchemaKeyword_1043(p):
    """OptSchemaKeyword : """
    p[0] = Expr("""OptSchemaKeyword""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateSeqStmt_1044(p):
    """CreateSeqStmt : CREATE OptTemp SEQUENCE qualified_name OptSeqList"""
    p[0] = Expr("""CreateSeqStmt""", """CREATE OptTemp SEQUENCE qualified_name OptSeqList""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateSeqStmt_1045(p):
    """CreateSeqStmt : CREATE OptTemp SEQUENCE IF_P NOT EXISTS qualified_name OptSeqList"""
    p[0] = Expr("""CreateSeqStmt""", """CREATE OptTemp SEQUENCE IF_P NOT EXISTS qualified_name OptSeqList""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterSeqStmt_1046(p):
    """AlterSeqStmt : ALTER SEQUENCE qualified_name OptSeqList"""
    p[0] = Expr("""AlterSeqStmt""", """ALTER SEQUENCE qualified_name OptSeqList""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterSeqStmt_1047(p):
    """AlterSeqStmt : ALTER SEQUENCE qualified_name SET SCHEMA qualified_schema_name"""
    p[0] = Expr("""AlterSeqStmt""", """ALTER SEQUENCE qualified_name SET SCHEMA qualified_schema_name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterSeqStmt_1048(p):
    """AlterSeqStmt : ALTER SEQUENCE qualified_name OWNER TO name"""
    p[0] = Expr("""AlterSeqStmt""", """ALTER SEQUENCE qualified_name OWNER TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqList_1049(p):
    """OptSeqList : OptSeqList OptSeqElem"""
    p[0] = Expr("""OptSeqList""", """OptSeqList OptSeqElem""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqList_1050(p):
    """OptSeqList : """
    p[0] = Expr("""OptSeqList""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqElem_1051(p):
    """OptSeqElem : CACHE NumericOnly"""
    p[0] = Expr("""OptSeqElem""", """CACHE NumericOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqElem_1052(p):
    """OptSeqElem : NO CACHE"""
    p[0] = Expr("""OptSeqElem""", """NO CACHE""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqElem_1053(p):
    """OptSeqElem : CYCLE"""
    p[0] = Expr("""OptSeqElem""", """CYCLE""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqElem_1054(p):
    """OptSeqElem : NO CYCLE"""
    p[0] = Expr("""OptSeqElem""", """NO CYCLE""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqElem_1055(p):
    """OptSeqElem : ORDER"""
    p[0] = Expr("""OptSeqElem""", """ORDER""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqElem_1056(p):
    """OptSeqElem : NO ORDER"""
    p[0] = Expr("""OptSeqElem""", """NO ORDER""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqElem_1057(p):
    """OptSeqElem : INCREMENT opt_by IntegerOnly"""
    p[0] = Expr("""OptSeqElem""", """INCREMENT opt_by IntegerOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqElem_1058(p):
    """OptSeqElem : MAXVALUE NumericOnly"""
    p[0] = Expr("""OptSeqElem""", """MAXVALUE NumericOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqElem_1059(p):
    """OptSeqElem : MINVALUE NumericOnly"""
    p[0] = Expr("""OptSeqElem""", """MINVALUE NumericOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqElem_1060(p):
    """OptSeqElem : NO MAXVALUE"""
    p[0] = Expr("""OptSeqElem""", """NO MAXVALUE""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqElem_1061(p):
    """OptSeqElem : NO MINVALUE"""
    p[0] = Expr("""OptSeqElem""", """NO MINVALUE""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqElem_1062(p):
    """OptSeqElem : START opt_with IntegerOnly"""
    p[0] = Expr("""OptSeqElem""", """START opt_with IntegerOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSeqElem_1063(p):
    """OptSeqElem : RESTART opt_with IntegerOnly"""
    p[0] = Expr("""OptSeqElem""", """RESTART opt_with IntegerOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_by_1064(p):
    """opt_by : BY"""
    p[0] = Expr("""opt_by""", """BY""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_by_1065(p):
    """opt_by : """
    p[0] = Expr("""opt_by""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_NumericOnly_1066(p):
    """NumericOnly : IntegerOnly"""
    p[0] = Expr("""NumericOnly""", """IntegerOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_NumericOnly_1067(p):
    """NumericOnly : FCONST"""
    p[0] = Expr("""NumericOnly""", """FCONST""", p[1:] if len(p or []) > 1 else [], p)


def p_NumericOnly_1068(p):
    """NumericOnly : '-' FCONST"""
    p[0] = Expr("""NumericOnly""", """'-' FCONST""", p[1:] if len(p or []) > 1 else [], p)


def p_IntegerOnly_1069(p):
    """IntegerOnly : Iconst"""
    p[0] = Expr("""IntegerOnly""", """Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_IntegerOnly_1070(p):
    """IntegerOnly : '-' Iconst"""
    p[0] = Expr("""IntegerOnly""", """'-' Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_RuntimePriorityValue_1071(p):
    """RuntimePriorityValue : HIGH"""
    p[0] = Expr("""RuntimePriorityValue""", """HIGH""", p[1:] if len(p or []) > 1 else [], p)


def p_RuntimePriorityValue_1072(p):
    """RuntimePriorityValue : MEDIUM"""
    p[0] = Expr("""RuntimePriorityValue""", """MEDIUM""", p[1:] if len(p or []) > 1 else [], p)


def p_RuntimePriorityValue_1073(p):
    """RuntimePriorityValue : LOW"""
    p[0] = Expr("""RuntimePriorityValue""", """LOW""", p[1:] if len(p or []) > 1 else [], p)


def p_CreatePLangStmt_1074(p):
    """CreatePLangStmt : CREATE opt_trusted opt_procedural LANGUAGE ColId_or_Sconst HANDLER handler_name opt_validator opt_lancompiler"""
    p[0] = Expr("""CreatePLangStmt""", """CREATE opt_trusted opt_procedural LANGUAGE ColId_or_Sconst HANDLER handler_name opt_validator opt_lancompiler""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_trusted_1075(p):
    """opt_trusted : TRUSTED"""
    p[0] = Expr("""opt_trusted""", """TRUSTED""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_trusted_1076(p):
    """opt_trusted : """
    p[0] = Expr("""opt_trusted""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_handler_name_1077(p):
    """handler_name : name"""
    p[0] = Expr("""handler_name""", """name""", p[1:] if len(p or []) > 1 else [], p)


def p_handler_name_1078(p):
    """handler_name : name attrs"""
    p[0] = Expr("""handler_name""", """name attrs""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_lancompiler_1079(p):
    """opt_lancompiler : LANCOMPILER Sconst"""
    p[0] = Expr("""opt_lancompiler""", """LANCOMPILER Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_lancompiler_1080(p):
    """opt_lancompiler : """
    p[0] = Expr("""opt_lancompiler""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_validator_1081(p):
    """opt_validator : VALIDATOR handler_name"""
    p[0] = Expr("""opt_validator""", """VALIDATOR handler_name""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_validator_1082(p):
    """opt_validator : """
    p[0] = Expr("""opt_validator""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_DropPLangStmt_1083(p):
    """DropPLangStmt : DROP opt_procedural LANGUAGE ColId_or_Sconst opt_drop_behavior"""
    p[0] = Expr("""DropPLangStmt""", """DROP opt_procedural LANGUAGE ColId_or_Sconst opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_procedural_1084(p):
    """opt_procedural : PROCEDURAL"""
    p[0] = Expr("""opt_procedural""", """PROCEDURAL""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_procedural_1085(p):
    """opt_procedural : """
    p[0] = Expr("""opt_procedural""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateTableSpaceStmt_1086(p):
    """CreateTableSpaceStmt : CREATE TABLESPACE name OptTableSpaceOwner LOCATION Sconst"""
    p[0] = Expr("""CreateTableSpaceStmt""", """CREATE TABLESPACE name OptTableSpaceOwner LOCATION Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTableSpaceOwner_1087(p):
    """OptTableSpaceOwner : OWNER name"""
    p[0] = Expr("""OptTableSpaceOwner""", """OWNER name""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTableSpaceOwner_1088(p):
    """OptTableSpaceOwner : """
    p[0] = Expr("""OptTableSpaceOwner""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_DropTableSpaceStmt_1089(p):
    """DropTableSpaceStmt : DROP TABLESPACE name"""
    p[0] = Expr("""DropTableSpaceStmt""", """DROP TABLESPACE name""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateTrigStmt_1090(p):
    """CreateTrigStmt : CREATE TRIGGER name TriggerActionTime TriggerEvents ON qualified_name TriggerForSpec EXECUTE PROCEDURE func_name '(' TriggerFuncArgs ')'"""
    p[0] = Expr("""CreateTrigStmt""", """CREATE TRIGGER name TriggerActionTime TriggerEvents ON qualified_name TriggerForSpec EXECUTE PROCEDURE func_name '(' TriggerFuncArgs ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateTrigStmt_1091(p):
    """CreateTrigStmt : CREATE CONSTRAINT TRIGGER name AFTER TriggerEvents ON qualified_name OptConstrFromTable ConstraintAttributeSpec FOR EACH ROW EXECUTE PROCEDURE func_name '(' TriggerFuncArgs ')'"""
    p[0] = Expr("""CreateTrigStmt""", """CREATE CONSTRAINT TRIGGER name AFTER TriggerEvents ON qualified_name OptConstrFromTable ConstraintAttributeSpec FOR EACH ROW EXECUTE PROCEDURE func_name '(' TriggerFuncArgs ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerActionTime_1092(p):
    """TriggerActionTime : BEFORE"""
    p[0] = Expr("""TriggerActionTime""", """BEFORE""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerActionTime_1093(p):
    """TriggerActionTime : AFTER"""
    p[0] = Expr("""TriggerActionTime""", """AFTER""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerEvents_1094(p):
    """TriggerEvents : TriggerOneEvent"""
    p[0] = Expr("""TriggerEvents""", """TriggerOneEvent""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerEvents_1095(p):
    """TriggerEvents : TriggerOneEvent OR TriggerOneEvent"""
    p[0] = Expr("""TriggerEvents""", """TriggerOneEvent OR TriggerOneEvent""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerEvents_1096(p):
    """TriggerEvents : TriggerOneEvent OR TriggerOneEvent OR TriggerOneEvent"""
    p[0] = Expr("""TriggerEvents""", """TriggerOneEvent OR TriggerOneEvent OR TriggerOneEvent""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerOneEvent_1097(p):
    """TriggerOneEvent : INSERT"""
    p[0] = Expr("""TriggerOneEvent""", """INSERT""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerOneEvent_1098(p):
    """TriggerOneEvent : DELETE_P"""
    p[0] = Expr("""TriggerOneEvent""", """DELETE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerOneEvent_1099(p):
    """TriggerOneEvent : UPDATE"""
    p[0] = Expr("""TriggerOneEvent""", """UPDATE""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerForSpec_1100(p):
    """TriggerForSpec : FOR TriggerForOpt TriggerForType"""
    p[0] = Expr("""TriggerForSpec""", """FOR TriggerForOpt TriggerForType""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerForSpec_1101(p):
    """TriggerForSpec : """
    p[0] = Expr("""TriggerForSpec""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerForOpt_1102(p):
    """TriggerForOpt : EACH"""
    p[0] = Expr("""TriggerForOpt""", """EACH""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerForOpt_1103(p):
    """TriggerForOpt : """
    p[0] = Expr("""TriggerForOpt""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerForType_1104(p):
    """TriggerForType : ROW"""
    p[0] = Expr("""TriggerForType""", """ROW""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerForType_1105(p):
    """TriggerForType : STATEMENT"""
    p[0] = Expr("""TriggerForType""", """STATEMENT""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerFuncArgs_1106(p):
    """TriggerFuncArgs : TriggerFuncArg"""
    p[0] = Expr("""TriggerFuncArgs""", """TriggerFuncArg""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerFuncArgs_1107(p):
    """TriggerFuncArgs : TriggerFuncArgs ',' TriggerFuncArg"""
    p[0] = Expr("""TriggerFuncArgs""", """TriggerFuncArgs ',' TriggerFuncArg""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerFuncArgs_1108(p):
    """TriggerFuncArgs : """
    p[0] = Expr("""TriggerFuncArgs""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerFuncArg_1109(p):
    """TriggerFuncArg : Iconst"""
    p[0] = Expr("""TriggerFuncArg""", """Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerFuncArg_1110(p):
    """TriggerFuncArg : FCONST"""
    p[0] = Expr("""TriggerFuncArg""", """FCONST""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerFuncArg_1111(p):
    """TriggerFuncArg : Sconst"""
    p[0] = Expr("""TriggerFuncArg""", """Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerFuncArg_1112(p):
    """TriggerFuncArg : BCONST"""
    p[0] = Expr("""TriggerFuncArg""", """BCONST""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerFuncArg_1113(p):
    """TriggerFuncArg : XCONST"""
    p[0] = Expr("""TriggerFuncArg""", """XCONST""", p[1:] if len(p or []) > 1 else [], p)


def p_TriggerFuncArg_1114(p):
    """TriggerFuncArg : ColId"""
    p[0] = Expr("""TriggerFuncArg""", """ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_OptConstrFromTable_1115(p):
    """OptConstrFromTable : FROM qualified_name"""
    p[0] = Expr("""OptConstrFromTable""", """FROM qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_OptConstrFromTable_1116(p):
    """OptConstrFromTable : """
    p[0] = Expr("""OptConstrFromTable""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintAttributeSpec_1117(p):
    """ConstraintAttributeSpec : ConstraintDeferrabilitySpec"""
    p[0] = Expr("""ConstraintAttributeSpec""", """ConstraintDeferrabilitySpec""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintAttributeSpec_1118(p):
    """ConstraintAttributeSpec : ConstraintDeferrabilitySpec ConstraintTimeSpec"""
    p[0] = Expr("""ConstraintAttributeSpec""", """ConstraintDeferrabilitySpec ConstraintTimeSpec""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintAttributeSpec_1119(p):
    """ConstraintAttributeSpec : ConstraintTimeSpec"""
    p[0] = Expr("""ConstraintAttributeSpec""", """ConstraintTimeSpec""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintAttributeSpec_1120(p):
    """ConstraintAttributeSpec : ConstraintTimeSpec ConstraintDeferrabilitySpec"""
    p[0] = Expr("""ConstraintAttributeSpec""", """ConstraintTimeSpec ConstraintDeferrabilitySpec""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintAttributeSpec_1121(p):
    """ConstraintAttributeSpec : """
    p[0] = Expr("""ConstraintAttributeSpec""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintDeferrabilitySpec_1122(p):
    """ConstraintDeferrabilitySpec : NOT DEFERRABLE"""
    p[0] = Expr("""ConstraintDeferrabilitySpec""", """NOT DEFERRABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintDeferrabilitySpec_1123(p):
    """ConstraintDeferrabilitySpec : DEFERRABLE"""
    p[0] = Expr("""ConstraintDeferrabilitySpec""", """DEFERRABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintTimeSpec_1124(p):
    """ConstraintTimeSpec : INITIALLY IMMEDIATE"""
    p[0] = Expr("""ConstraintTimeSpec""", """INITIALLY IMMEDIATE""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstraintTimeSpec_1125(p):
    """ConstraintTimeSpec : INITIALLY DEFERRED"""
    p[0] = Expr("""ConstraintTimeSpec""", """INITIALLY DEFERRED""", p[1:] if len(p or []) > 1 else [], p)


def p_DropTrigStmt_1126(p):
    """DropTrigStmt : DROP TRIGGER name ON qualified_name opt_drop_behavior"""
    p[0] = Expr("""DropTrigStmt""", """DROP TRIGGER name ON qualified_name opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateAssertStmt_1127(p):
    """CreateAssertStmt : CREATE ASSERTION name CHECK '(' a_expr ')' ConstraintAttributeSpec"""
    p[0] = Expr("""CreateAssertStmt""", """CREATE ASSERTION name CHECK '(' a_expr ')' ConstraintAttributeSpec""", p[1:] if len(p or []) > 1 else [], p)


def p_DropAssertStmt_1128(p):
    """DropAssertStmt : DROP ASSERTION name opt_drop_behavior"""
    p[0] = Expr("""DropAssertStmt""", """DROP ASSERTION name opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_DefineStmt_1129(p):
    """DefineStmt : CREATE OPERATOR any_operator definition"""
    p[0] = Expr("""DefineStmt""", """CREATE OPERATOR any_operator definition""", p[1:] if len(p or []) > 1 else [], p)


def p_definition_1130(p):
    """definition : '(' def_list ')'"""
    p[0] = Expr("""definition""", """'(' def_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_def_list_1131(p):
    """def_list : def_elem"""
    p[0] = Expr("""def_list""", """def_elem""", p[1:] if len(p or []) > 1 else [], p)


def p_def_list_1132(p):
    """def_list : def_list ',' def_elem"""
    p[0] = Expr("""def_list""", """def_list ',' def_elem""", p[1:] if len(p or []) > 1 else [], p)


def p_def_elem_1133(p):
    """def_elem : ColLabel '=' def_arg"""
    p[0] = Expr("""def_elem""", """ColLabel '=' def_arg""", p[1:] if len(p or []) > 1 else [], p)


def p_def_elem_1134(p):
    """def_elem : ColLabel"""
    p[0] = Expr("""def_elem""", """ColLabel""", p[1:] if len(p or []) > 1 else [], p)


def p_def_arg_1135(p):
    """def_arg : func_return"""
    p[0] = Expr("""def_arg""", """func_return""", p[1:] if len(p or []) > 1 else [], p)


def p_def_arg_1136(p):
    """def_arg : qual_all_Op"""
    p[0] = Expr("""def_arg""", """qual_all_Op""", p[1:] if len(p or []) > 1 else [], p)


def p_def_arg_1137(p):
    """def_arg : NumericOnly"""
    p[0] = Expr("""def_arg""", """NumericOnly""", p[1:] if len(p or []) > 1 else [], p)


def p_def_arg_1138(p):
    """def_arg : Sconst"""
    p[0] = Expr("""def_arg""", """Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateOpClassStmt_1139(p):
    """CreateOpClassStmt : CREATE OPERATOR CLASS any_name opt_default FOR TYPE_P Typename USING access_method AS opclass_item_list"""
    p[0] = Expr("""CreateOpClassStmt""", """CREATE OPERATOR CLASS any_name opt_default FOR TYPE_P Typename USING access_method AS opclass_item_list""", p[1:] if len(p or []) > 1 else [], p)


def p_opclass_item_list_1140(p):
    """opclass_item_list : opclass_item"""
    p[0] = Expr("""opclass_item_list""", """opclass_item""", p[1:] if len(p or []) > 1 else [], p)


def p_opclass_item_list_1141(p):
    """opclass_item_list : opclass_item_list ',' opclass_item"""
    p[0] = Expr("""opclass_item_list""", """opclass_item_list ',' opclass_item""", p[1:] if len(p or []) > 1 else [], p)


def p_opclass_item_1142(p):
    """opclass_item : OPERATOR Iconst any_operator opt_recheck"""
    p[0] = Expr("""opclass_item""", """OPERATOR Iconst any_operator opt_recheck""", p[1:] if len(p or []) > 1 else [], p)


def p_opclass_item_1143(p):
    """opclass_item : OPERATOR Iconst any_operator '(' oper_argtypes ')' opt_recheck"""
    p[0] = Expr("""opclass_item""", """OPERATOR Iconst any_operator '(' oper_argtypes ')' opt_recheck""", p[1:] if len(p or []) > 1 else [], p)


def p_opclass_item_1144(p):
    """opclass_item : FUNCTION Iconst func_name func_args"""
    p[0] = Expr("""opclass_item""", """FUNCTION Iconst func_name func_args""", p[1:] if len(p or []) > 1 else [], p)


def p_opclass_item_1145(p):
    """opclass_item : STORAGE Typename"""
    p[0] = Expr("""opclass_item""", """STORAGE Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_default_1146(p):
    """opt_default : DEFAULT"""
    p[0] = Expr("""opt_default""", """DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_default_1147(p):
    """opt_default : """
    p[0] = Expr("""opt_default""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_recheck_1148(p):
    """opt_recheck : RECHECK"""
    p[0] = Expr("""opt_recheck""", """RECHECK""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_recheck_1149(p):
    """opt_recheck : """
    p[0] = Expr("""opt_recheck""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_DropOpClassStmt_1150(p):
    """DropOpClassStmt : DROP OPERATOR CLASS any_name USING access_method opt_drop_behavior"""
    p[0] = Expr("""DropOpClassStmt""", """DROP OPERATOR CLASS any_name USING access_method opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_DropStmt_1151(p):
    """DropStmt : DROP drop_type IF_P EXISTS any_name_list opt_drop_behavior"""
    p[0] = Expr("""DropStmt""", """DROP drop_type IF_P EXISTS any_name_list opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_DropStmt_1152(p):
    """DropStmt : DROP drop_type any_name_list opt_drop_behavior"""
    p[0] = Expr("""DropStmt""", """DROP drop_type any_name_list opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_DropStmt_1153(p):
    """DropStmt : DROP RESOURCE POOL any_name_list"""
    p[0] = Expr("""DropStmt""", """DROP RESOURCE POOL any_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_DropStmt_1154(p):
    """DropStmt : DROP MODEL IF_P EXISTS any_name_list"""
    p[0] = Expr("""DropStmt""", """DROP MODEL IF_P EXISTS any_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_DropStmt_1155(p):
    """DropStmt : DROP MODEL any_name_list"""
    p[0] = Expr("""DropStmt""", """DROP MODEL any_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_DropStmt_1156(p):
    """DropStmt : DROP Interface_or_address_drop IF_P EXISTS any_name_list opt_drop_behavior"""
    p[0] = Expr("""DropStmt""", """DROP Interface_or_address_drop IF_P EXISTS any_name_list opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_DropStmt_1157(p):
    """DropStmt : DROP Interface_or_address_drop any_name_list opt_drop_behavior"""
    p[0] = Expr("""DropStmt""", """DROP Interface_or_address_drop any_name_list opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1158(p):
    """drop_type : TABLE"""
    p[0] = Expr("""drop_type""", """TABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1159(p):
    """drop_type : SEQUENCE"""
    p[0] = Expr("""drop_type""", """SEQUENCE""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1160(p):
    """drop_type : VIEW"""
    p[0] = Expr("""drop_type""", """VIEW""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1161(p):
    """drop_type : TEXT INDEX"""
    p[0] = Expr("""drop_type""", """TEXT INDEX""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1162(p):
    """drop_type : INDEX"""
    p[0] = Expr("""drop_type""", """INDEX""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1163(p):
    """drop_type : TYPE_P"""
    p[0] = Expr("""drop_type""", """TYPE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1164(p):
    """drop_type : DOMAIN_P"""
    p[0] = Expr("""drop_type""", """DOMAIN_P""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1165(p):
    """drop_type : SCHEMA"""
    p[0] = Expr("""drop_type""", """SCHEMA""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1166(p):
    """drop_type : PROJECTION"""
    p[0] = Expr("""drop_type""", """PROJECTION""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1167(p):
    """drop_type : NODE"""
    p[0] = Expr("""drop_type""", """NODE""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1168(p):
    """drop_type : PROFILE"""
    p[0] = Expr("""drop_type""", """PROFILE""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1169(p):
    """drop_type : ROLE"""
    p[0] = Expr("""drop_type""", """ROLE""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1170(p):
    """drop_type : LIBRARY"""
    p[0] = Expr("""drop_type""", """LIBRARY""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1171(p):
    """drop_type : TUNING RULE"""
    p[0] = Expr("""drop_type""", """TUNING RULE""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1172(p):
    """drop_type : SUBNET"""
    p[0] = Expr("""drop_type""", """SUBNET""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1173(p):
    """drop_type : LOAD BALANCE GROUP_P"""
    p[0] = Expr("""drop_type""", """LOAD BALANCE GROUP_P""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1174(p):
    """drop_type : ROUTING RULE"""
    p[0] = Expr("""drop_type""", """ROUTING RULE""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1175(p):
    """drop_type : FAULT GROUP_P"""
    p[0] = Expr("""drop_type""", """FAULT GROUP_P""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1176(p):
    """drop_type : AUTHENTICATION"""
    p[0] = Expr("""drop_type""", """AUTHENTICATION""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1177(p):
    """drop_type : NOTIFIER"""
    p[0] = Expr("""drop_type""", """NOTIFIER""", p[1:] if len(p or []) > 1 else [], p)


def p_drop_type_1178(p):
    """drop_type : BRANCH"""
    p[0] = Expr("""drop_type""", """BRANCH""", p[1:] if len(p or []) > 1 else [], p)


def p_any_name_list_1179(p):
    """any_name_list : any_name"""
    p[0] = Expr("""any_name_list""", """any_name""", p[1:] if len(p or []) > 1 else [], p)


def p_any_name_list_1180(p):
    """any_name_list : any_name_list ',' any_name"""
    p[0] = Expr("""any_name_list""", """any_name_list ',' any_name""", p[1:] if len(p or []) > 1 else [], p)


def p_any_name_1181(p):
    """any_name : ColId"""
    p[0] = Expr("""any_name""", """ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_any_name_1182(p):
    """any_name : ColId attrs"""
    p[0] = Expr("""any_name""", """ColId attrs""", p[1:] if len(p or []) > 1 else [], p)


def p_attrs_1183(p):
    """attrs : '.' attr_name"""
    p[0] = Expr("""attrs""", """'.' attr_name""", p[1:] if len(p or []) > 1 else [], p)


def p_attrs_1184(p):
    """attrs : attrs '.' attr_name"""
    p[0] = Expr("""attrs""", """attrs '.' attr_name""", p[1:] if len(p or []) > 1 else [], p)


def p_Interface_or_address_drop_1185(p):
    """Interface_or_address_drop : NETWORK INTERFACE"""
    p[0] = Expr("""Interface_or_address_drop""", """NETWORK INTERFACE""", p[1:] if len(p or []) > 1 else [], p)


def p_Interface_or_address_drop_1186(p):
    """Interface_or_address_drop : NETWORK ADDRESS"""
    p[0] = Expr("""Interface_or_address_drop""", """NETWORK ADDRESS""", p[1:] if len(p or []) > 1 else [], p)


def p_TruncateStmt_1187(p):
    """TruncateStmt : TRUNCATE TABLE qualified_name"""
    p[0] = Expr("""TruncateStmt""", """TRUNCATE TABLE qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_CommentStmt_1188(p):
    """CommentStmt : COMMENT ON comment_type any_name IS comment_text"""
    p[0] = Expr("""CommentStmt""", """COMMENT ON comment_type any_name IS comment_text""", p[1:] if len(p or []) > 1 else [], p)


def p_CommentStmt_1189(p):
    """CommentStmt : COMMENT ON FUNCTION func_name func_args IS comment_text"""
    p[0] = Expr("""CommentStmt""", """COMMENT ON FUNCTION func_name func_args IS comment_text""", p[1:] if len(p or []) > 1 else [], p)


def p_CommentStmt_1190(p):
    """CommentStmt : COMMENT ON udx_type FUNCTION func_name func_args IS comment_text"""
    p[0] = Expr("""CommentStmt""", """COMMENT ON udx_type FUNCTION func_name func_args IS comment_text""", p[1:] if len(p or []) > 1 else [], p)


def p_CommentStmt_1191(p):
    """CommentStmt : COMMENT ON OPERATOR any_operator '(' oper_argtypes ')' IS comment_text"""
    p[0] = Expr("""CommentStmt""", """COMMENT ON OPERATOR any_operator '(' oper_argtypes ')' IS comment_text""", p[1:] if len(p or []) > 1 else [], p)


def p_CommentStmt_1192(p):
    """CommentStmt : COMMENT ON CONSTRAINT name ON any_name IS comment_text"""
    p[0] = Expr("""CommentStmt""", """COMMENT ON CONSTRAINT name ON any_name IS comment_text""", p[1:] if len(p or []) > 1 else [], p)


def p_CommentStmt_1193(p):
    """CommentStmt : COMMENT ON RULE name ON any_name IS comment_text"""
    p[0] = Expr("""CommentStmt""", """COMMENT ON RULE name ON any_name IS comment_text""", p[1:] if len(p or []) > 1 else [], p)


def p_CommentStmt_1194(p):
    """CommentStmt : COMMENT ON RULE name IS comment_text"""
    p[0] = Expr("""CommentStmt""", """COMMENT ON RULE name IS comment_text""", p[1:] if len(p or []) > 1 else [], p)


def p_CommentStmt_1195(p):
    """CommentStmt : COMMENT ON TRIGGER name ON any_name IS comment_text"""
    p[0] = Expr("""CommentStmt""", """COMMENT ON TRIGGER name ON any_name IS comment_text""", p[1:] if len(p or []) > 1 else [], p)


def p_CommentStmt_1196(p):
    """CommentStmt : COMMENT ON OPERATOR CLASS any_name USING access_method IS comment_text"""
    p[0] = Expr("""CommentStmt""", """COMMENT ON OPERATOR CLASS any_name USING access_method IS comment_text""", p[1:] if len(p or []) > 1 else [], p)


def p_CommentStmt_1197(p):
    """CommentStmt : COMMENT ON LARGE_P OBJECT_P NumericOnly IS comment_text"""
    p[0] = Expr("""CommentStmt""", """COMMENT ON LARGE_P OBJECT_P NumericOnly IS comment_text""", p[1:] if len(p or []) > 1 else [], p)


def p_CommentStmt_1198(p):
    """CommentStmt : COMMENT ON CAST '(' Typename AS Typename ')' IS comment_text"""
    p[0] = Expr("""CommentStmt""", """COMMENT ON CAST '(' Typename AS Typename ')' IS comment_text""", p[1:] if len(p or []) > 1 else [], p)


def p_CommentStmt_1199(p):
    """CommentStmt : COMMENT ON opt_procedural LANGUAGE any_name IS comment_text"""
    p[0] = Expr("""CommentStmt""", """COMMENT ON opt_procedural LANGUAGE any_name IS comment_text""", p[1:] if len(p or []) > 1 else [], p)


def p_CommentStmt_1200(p):
    """CommentStmt : COMMENT ON LIBRARY func_name IS comment_text"""
    p[0] = Expr("""CommentStmt""", """COMMENT ON LIBRARY func_name IS comment_text""", p[1:] if len(p or []) > 1 else [], p)


def p_comment_type_1201(p):
    """comment_type : COLUMN"""
    p[0] = Expr("""comment_type""", """COLUMN""", p[1:] if len(p or []) > 1 else [], p)


def p_comment_type_1202(p):
    """comment_type : DATABASE"""
    p[0] = Expr("""comment_type""", """DATABASE""", p[1:] if len(p or []) > 1 else [], p)


def p_comment_type_1203(p):
    """comment_type : SCHEMA"""
    p[0] = Expr("""comment_type""", """SCHEMA""", p[1:] if len(p or []) > 1 else [], p)


def p_comment_type_1204(p):
    """comment_type : INDEX"""
    p[0] = Expr("""comment_type""", """INDEX""", p[1:] if len(p or []) > 1 else [], p)


def p_comment_type_1205(p):
    """comment_type : SEQUENCE"""
    p[0] = Expr("""comment_type""", """SEQUENCE""", p[1:] if len(p or []) > 1 else [], p)


def p_comment_type_1206(p):
    """comment_type : TABLE"""
    p[0] = Expr("""comment_type""", """TABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_comment_type_1207(p):
    """comment_type : DOMAIN_P"""
    p[0] = Expr("""comment_type""", """DOMAIN_P""", p[1:] if len(p or []) > 1 else [], p)


def p_comment_type_1208(p):
    """comment_type : TYPE_P"""
    p[0] = Expr("""comment_type""", """TYPE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_comment_type_1209(p):
    """comment_type : VIEW"""
    p[0] = Expr("""comment_type""", """VIEW""", p[1:] if len(p or []) > 1 else [], p)


def p_comment_type_1210(p):
    """comment_type : PROJECTION"""
    p[0] = Expr("""comment_type""", """PROJECTION""", p[1:] if len(p or []) > 1 else [], p)


def p_comment_type_1211(p):
    """comment_type : NODE"""
    p[0] = Expr("""comment_type""", """NODE""", p[1:] if len(p or []) > 1 else [], p)


def p_udx_type_1212(p):
    """udx_type : TRANSFORM"""
    p[0] = Expr("""udx_type""", """TRANSFORM""", p[1:] if len(p or []) > 1 else [], p)


def p_udx_type_1213(p):
    """udx_type : ANALYTIC"""
    p[0] = Expr("""udx_type""", """ANALYTIC""", p[1:] if len(p or []) > 1 else [], p)


def p_udx_type_1214(p):
    """udx_type : AGGREGATE"""
    p[0] = Expr("""udx_type""", """AGGREGATE""", p[1:] if len(p or []) > 1 else [], p)


def p_comment_text_1215(p):
    """comment_text : Sconst"""
    p[0] = Expr("""comment_text""", """Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_comment_text_1216(p):
    """comment_text : NULL_P"""
    p[0] = Expr("""comment_text""", """NULL_P""", p[1:] if len(p or []) > 1 else [], p)


def p_FetchStmt_1217(p):
    """FetchStmt : FETCH fetch_direction from_in name"""
    p[0] = Expr("""FetchStmt""", """FETCH fetch_direction from_in name""", p[1:] if len(p or []) > 1 else [], p)


def p_FetchStmt_1218(p):
    """FetchStmt : FETCH name"""
    p[0] = Expr("""FetchStmt""", """FETCH name""", p[1:] if len(p or []) > 1 else [], p)


def p_FetchStmt_1219(p):
    """FetchStmt : MOVE fetch_direction from_in name"""
    p[0] = Expr("""FetchStmt""", """MOVE fetch_direction from_in name""", p[1:] if len(p or []) > 1 else [], p)


def p_FetchStmt_1220(p):
    """FetchStmt : MOVE name"""
    p[0] = Expr("""FetchStmt""", """MOVE name""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1221(p):
    """fetch_direction : """
    p[0] = Expr("""fetch_direction""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1222(p):
    """fetch_direction : NEXT"""
    p[0] = Expr("""fetch_direction""", """NEXT""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1223(p):
    """fetch_direction : PRIOR"""
    p[0] = Expr("""fetch_direction""", """PRIOR""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1224(p):
    """fetch_direction : FIRST_P"""
    p[0] = Expr("""fetch_direction""", """FIRST_P""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1225(p):
    """fetch_direction : LAST_P"""
    p[0] = Expr("""fetch_direction""", """LAST_P""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1226(p):
    """fetch_direction : ABSOLUTE_P fetch_count"""
    p[0] = Expr("""fetch_direction""", """ABSOLUTE_P fetch_count""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1227(p):
    """fetch_direction : RELATIVE_P fetch_count"""
    p[0] = Expr("""fetch_direction""", """RELATIVE_P fetch_count""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1228(p):
    """fetch_direction : fetch_count"""
    p[0] = Expr("""fetch_direction""", """fetch_count""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1229(p):
    """fetch_direction : ALL"""
    p[0] = Expr("""fetch_direction""", """ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1230(p):
    """fetch_direction : FORWARD"""
    p[0] = Expr("""fetch_direction""", """FORWARD""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1231(p):
    """fetch_direction : FORWARD fetch_count"""
    p[0] = Expr("""fetch_direction""", """FORWARD fetch_count""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1232(p):
    """fetch_direction : FORWARD ALL"""
    p[0] = Expr("""fetch_direction""", """FORWARD ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1233(p):
    """fetch_direction : BACKWARD"""
    p[0] = Expr("""fetch_direction""", """BACKWARD""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1234(p):
    """fetch_direction : BACKWARD fetch_count"""
    p[0] = Expr("""fetch_direction""", """BACKWARD fetch_count""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_direction_1235(p):
    """fetch_direction : BACKWARD ALL"""
    p[0] = Expr("""fetch_direction""", """BACKWARD ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_count_1236(p):
    """fetch_count : Iconst"""
    p[0] = Expr("""fetch_count""", """Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_fetch_count_1237(p):
    """fetch_count : '-' Iconst"""
    p[0] = Expr("""fetch_count""", """'-' Iconst""", p[1:] if len(p or []) > 1 else [], p)


def p_from_in_1238(p):
    """from_in : FROM"""
    p[0] = Expr("""from_in""", """FROM""", p[1:] if len(p or []) > 1 else [], p)


def p_from_in_1239(p):
    """from_in : IN_P"""
    p[0] = Expr("""from_in""", """IN_P""", p[1:] if len(p or []) > 1 else [], p)


def p_GrantStmt_1240(p):
    """GrantStmt : GRANT privileges_or_roles opt_on_target_clause TO grantee_list opt_grant_grantadmin_option"""
    p[0] = Expr("""GrantStmt""", """GRANT privileges_or_roles opt_on_target_clause TO grantee_list opt_grant_grantadmin_option""", p[1:] if len(p or []) > 1 else [], p)


def p_GrantStmt_1241(p):
    """GrantStmt : GRANT AUTHENTICATION auth_list TO grantee_list"""
    p[0] = Expr("""GrantStmt""", """GRANT AUTHENTICATION auth_list TO grantee_list""", p[1:] if len(p or []) > 1 else [], p)


def p_RevokeStmt_1242(p):
    """RevokeStmt : REVOKE revoke_privileges_or_roles opt_on_target_clause FROM grantee_list opt_drop_behavior"""
    p[0] = Expr("""RevokeStmt""", """REVOKE revoke_privileges_or_roles opt_on_target_clause FROM grantee_list opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_RevokeStmt_1243(p):
    """RevokeStmt : REVOKE AUTHENTICATION auth_list FROM grantee_list"""
    p[0] = Expr("""RevokeStmt""", """REVOKE AUTHENTICATION auth_list FROM grantee_list""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_on_target_clause_1244(p):
    """opt_on_target_clause : ON privilege_target"""
    p[0] = Expr("""opt_on_target_clause""", """ON privilege_target""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_on_target_clause_1245(p):
    """opt_on_target_clause : """
    p[0] = Expr("""opt_on_target_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_revoke_privileges_or_roles_1246(p):
    """revoke_privileges_or_roles : privileges_or_roles"""
    p[0] = Expr("""revoke_privileges_or_roles""", """privileges_or_roles""", p[1:] if len(p or []) > 1 else [], p)


def p_revoke_privileges_or_roles_1247(p):
    """revoke_privileges_or_roles : GRANT OPTION FOR privileges_or_roles"""
    p[0] = Expr("""revoke_privileges_or_roles""", """GRANT OPTION FOR privileges_or_roles""", p[1:] if len(p or []) > 1 else [], p)


def p_revoke_privileges_or_roles_1248(p):
    """revoke_privileges_or_roles : ADMIN OPTION FOR privileges_or_roles"""
    p[0] = Expr("""revoke_privileges_or_roles""", """ADMIN OPTION FOR privileges_or_roles""", p[1:] if len(p or []) > 1 else [], p)


def p_privileges_or_roles_1249(p):
    """privileges_or_roles : privilege_or_role_list"""
    p[0] = Expr("""privileges_or_roles""", """privilege_or_role_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privileges_or_roles_1250(p):
    """privileges_or_roles : ALL"""
    p[0] = Expr("""privileges_or_roles""", """ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_privileges_or_roles_1251(p):
    """privileges_or_roles : ALL PRIVILEGES"""
    p[0] = Expr("""privileges_or_roles""", """ALL PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_privileges_or_roles_1252(p):
    """privileges_or_roles : ALL EXTEND"""
    p[0] = Expr("""privileges_or_roles""", """ALL EXTEND""", p[1:] if len(p or []) > 1 else [], p)


def p_privileges_or_roles_1253(p):
    """privileges_or_roles : ALL PRIVILEGES EXTEND"""
    p[0] = Expr("""privileges_or_roles""", """ALL PRIVILEGES EXTEND""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_or_role_list_1254(p):
    """privilege_or_role_list : privilege_or_role"""
    p[0] = Expr("""privilege_or_role_list""", """privilege_or_role""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_or_role_list_1255(p):
    """privilege_or_role_list : privilege_or_role_list ',' privilege_or_role"""
    p[0] = Expr("""privilege_or_role_list""", """privilege_or_role_list ',' privilege_or_role""", p[1:] if len(p or []) > 1 else [], p)


def p_auth_list_1256(p):
    """auth_list : name"""
    p[0] = Expr("""auth_list""", """name""", p[1:] if len(p or []) > 1 else [], p)


def p_auth_list_1257(p):
    """auth_list : auth_list ',' name"""
    p[0] = Expr("""auth_list""", """auth_list ',' name""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_or_role_1258(p):
    """privilege_or_role : SELECT"""
    p[0] = Expr("""privilege_or_role""", """SELECT""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_or_role_1259(p):
    """privilege_or_role : REFERENCES"""
    p[0] = Expr("""privilege_or_role""", """REFERENCES""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_or_role_1260(p):
    """privilege_or_role : CREATE"""
    p[0] = Expr("""privilege_or_role""", """CREATE""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_or_role_1261(p):
    """privilege_or_role : ColId"""
    p[0] = Expr("""privilege_or_role""", """ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1262(p):
    """privilege_target : qualified_name_list"""
    p[0] = Expr("""privilege_target""", """qualified_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1263(p):
    """privilege_target : TABLE qualified_name_list"""
    p[0] = Expr("""privilege_target""", """TABLE qualified_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1264(p):
    """privilege_target : FUNCTION function_with_argtypes_list"""
    p[0] = Expr("""privilege_target""", """FUNCTION function_with_argtypes_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1265(p):
    """privilege_target : TRANSFORM FUNCTION function_with_argtypes_list"""
    p[0] = Expr("""privilege_target""", """TRANSFORM FUNCTION function_with_argtypes_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1266(p):
    """privilege_target : ANALYTIC FUNCTION function_with_argtypes_list"""
    p[0] = Expr("""privilege_target""", """ANALYTIC FUNCTION function_with_argtypes_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1267(p):
    """privilege_target : AGGREGATE FUNCTION function_with_argtypes_list"""
    p[0] = Expr("""privilege_target""", """AGGREGATE FUNCTION function_with_argtypes_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1268(p):
    """privilege_target : SOURCE function_with_argtypes_list"""
    p[0] = Expr("""privilege_target""", """SOURCE function_with_argtypes_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1269(p):
    """privilege_target : FILTER function_with_argtypes_list"""
    p[0] = Expr("""privilege_target""", """FILTER function_with_argtypes_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1270(p):
    """privilege_target : PARSER function_with_argtypes_list"""
    p[0] = Expr("""privilege_target""", """PARSER function_with_argtypes_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1271(p):
    """privilege_target : PROCEDURE proc_with_argtypes_list"""
    p[0] = Expr("""privilege_target""", """PROCEDURE proc_with_argtypes_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1272(p):
    """privilege_target : DATABASE dbname_list"""
    p[0] = Expr("""privilege_target""", """DATABASE dbname_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1273(p):
    """privilege_target : LANGUAGE name_list"""
    p[0] = Expr("""privilege_target""", """LANGUAGE name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1274(p):
    """privilege_target : SCHEMA qualified_schema_name_list"""
    p[0] = Expr("""privilege_target""", """SCHEMA qualified_schema_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1275(p):
    """privilege_target : TABLESPACE name_list"""
    p[0] = Expr("""privilege_target""", """TABLESPACE name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1276(p):
    """privilege_target : SEQUENCE qualified_name_list"""
    p[0] = Expr("""privilege_target""", """SEQUENCE qualified_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1277(p):
    """privilege_target : RESOURCE POOL name_list"""
    p[0] = Expr("""privilege_target""", """RESOURCE POOL name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1278(p):
    """privilege_target : LIBRARY qualified_name_list"""
    p[0] = Expr("""privilege_target""", """LIBRARY qualified_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1279(p):
    """privilege_target : LOCATION copy_file_list"""
    p[0] = Expr("""privilege_target""", """LOCATION copy_file_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1280(p):
    """privilege_target : ALL TABLES IN_P SCHEMA qualified_schema_name_list"""
    p[0] = Expr("""privilege_target""", """ALL TABLES IN_P SCHEMA qualified_schema_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1281(p):
    """privilege_target : ALL FUNCTIONS IN_P SCHEMA qualified_schema_name_list"""
    p[0] = Expr("""privilege_target""", """ALL FUNCTIONS IN_P SCHEMA qualified_schema_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1282(p):
    """privilege_target : ALL SEQUENCES IN_P SCHEMA qualified_schema_name_list"""
    p[0] = Expr("""privilege_target""", """ALL SEQUENCES IN_P SCHEMA qualified_schema_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_privilege_target_1283(p):
    """privilege_target : MODEL qualified_name_list"""
    p[0] = Expr("""privilege_target""", """MODEL qualified_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_grantee_list_1284(p):
    """grantee_list : grantee"""
    p[0] = Expr("""grantee_list""", """grantee""", p[1:] if len(p or []) > 1 else [], p)


def p_grantee_list_1285(p):
    """grantee_list : grantee_list ',' grantee"""
    p[0] = Expr("""grantee_list""", """grantee_list ',' grantee""", p[1:] if len(p or []) > 1 else [], p)


def p_grantee_1286(p):
    """grantee : ColId"""
    p[0] = Expr("""grantee""", """ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_grantee_1287(p):
    """grantee : GROUP_P ColId"""
    p[0] = Expr("""grantee""", """GROUP_P ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_grant_grantadmin_option_1288(p):
    """opt_grant_grantadmin_option : WITH GRANT OPTION"""
    p[0] = Expr("""opt_grant_grantadmin_option""", """WITH GRANT OPTION""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_grant_grantadmin_option_1289(p):
    """opt_grant_grantadmin_option : WITH ADMIN OPTION"""
    p[0] = Expr("""opt_grant_grantadmin_option""", """WITH ADMIN OPTION""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_grant_grantadmin_option_1290(p):
    """opt_grant_grantadmin_option : """
    p[0] = Expr("""opt_grant_grantadmin_option""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_function_with_argtypes_list_1291(p):
    """function_with_argtypes_list : function_with_argtypes"""
    p[0] = Expr("""function_with_argtypes_list""", """function_with_argtypes""", p[1:] if len(p or []) > 1 else [], p)


def p_function_with_argtypes_list_1292(p):
    """function_with_argtypes_list : function_with_argtypes_list ',' function_with_argtypes"""
    p[0] = Expr("""function_with_argtypes_list""", """function_with_argtypes_list ',' function_with_argtypes""", p[1:] if len(p or []) > 1 else [], p)


def p_function_with_argtypes_1293(p):
    """function_with_argtypes : func_name func_args"""
    p[0] = Expr("""function_with_argtypes""", """func_name func_args""", p[1:] if len(p or []) > 1 else [], p)


def p_proc_with_argtypes_list_1294(p):
    """proc_with_argtypes_list : proc_with_argtypes"""
    p[0] = Expr("""proc_with_argtypes_list""", """proc_with_argtypes""", p[1:] if len(p or []) > 1 else [], p)


def p_proc_with_argtypes_list_1295(p):
    """proc_with_argtypes_list : proc_with_argtypes_list ',' proc_with_argtypes"""
    p[0] = Expr("""proc_with_argtypes_list""", """proc_with_argtypes_list ',' proc_with_argtypes""", p[1:] if len(p or []) > 1 else [], p)


def p_proc_with_argtypes_1296(p):
    """proc_with_argtypes : func_name proc_args"""
    p[0] = Expr("""proc_with_argtypes""", """func_name proc_args""", p[1:] if len(p or []) > 1 else [], p)


def p_IndexStmt_1297(p):
    """IndexStmt : CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause tokenizer_clause tokenizer_args stemmer_clause stemmer_args"""
    p[0] = Expr("""IndexStmt""", """CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause tokenizer_clause tokenizer_args stemmer_clause stemmer_args""", p[1:] if len(p or []) > 1 else [], p)


def p_IndexStmt_1298(p):
    """IndexStmt : CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause stemmer_clause stemmer_args tokenizer_clause tokenizer_args"""
    p[0] = Expr("""IndexStmt""", """CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause stemmer_clause stemmer_args tokenizer_clause tokenizer_args""", p[1:] if len(p or []) > 1 else [], p)


def p_IndexStmt_1299(p):
    """IndexStmt : CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause tokenizer_clause tokenizer_args"""
    p[0] = Expr("""IndexStmt""", """CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause tokenizer_clause tokenizer_args""", p[1:] if len(p or []) > 1 else [], p)


def p_IndexStmt_1300(p):
    """IndexStmt : CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause stemmer_clause stemmer_args"""
    p[0] = Expr("""IndexStmt""", """CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause stemmer_clause stemmer_args""", p[1:] if len(p or []) > 1 else [], p)


def p_IndexStmt_1301(p):
    """IndexStmt : CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause"""
    p[0] = Expr("""IndexStmt""", """CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_index_opt_unique_1302(p):
    """index_opt_unique : UNIQUE"""
    p[0] = Expr("""index_opt_unique""", """UNIQUE""", p[1:] if len(p or []) > 1 else [], p)


def p_index_opt_unique_1303(p):
    """index_opt_unique : """
    p[0] = Expr("""index_opt_unique""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_index_opt_text_1304(p):
    """index_opt_text : TEXT"""
    p[0] = Expr("""index_opt_text""", """TEXT""", p[1:] if len(p or []) > 1 else [], p)


def p_index_opt_text_1305(p):
    """index_opt_text : """
    p[0] = Expr("""index_opt_text""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_access_method_clause_1306(p):
    """access_method_clause : USING access_method"""
    p[0] = Expr("""access_method_clause""", """USING access_method""", p[1:] if len(p or []) > 1 else [], p)


def p_access_method_clause_1307(p):
    """access_method_clause : """
    p[0] = Expr("""access_method_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_tokenizer_clause_1308(p):
    """tokenizer_clause : TOKENIZER udx_func_name"""
    p[0] = Expr("""tokenizer_clause""", """TOKENIZER udx_func_name""", p[1:] if len(p or []) > 1 else [], p)


def p_tokenizer_clause_1309(p):
    """tokenizer_clause : TOKENIZER NONE"""
    p[0] = Expr("""tokenizer_clause""", """TOKENIZER NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_stemmer_clause_1310(p):
    """stemmer_clause : STEMMER udx_func_name"""
    p[0] = Expr("""stemmer_clause""", """STEMMER udx_func_name""", p[1:] if len(p or []) > 1 else [], p)


def p_stemmer_clause_1311(p):
    """stemmer_clause : STEMMER NONE"""
    p[0] = Expr("""stemmer_clause""", """STEMMER NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_tokenizer_args_1312(p):
    """tokenizer_args : func_args"""
    p[0] = Expr("""tokenizer_args""", """func_args""", p[1:] if len(p or []) > 1 else [], p)


def p_tokenizer_args_1313(p):
    """tokenizer_args : """
    p[0] = Expr("""tokenizer_args""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_stemmer_args_1314(p):
    """stemmer_args : func_args"""
    p[0] = Expr("""stemmer_args""", """func_args""", p[1:] if len(p or []) > 1 else [], p)


def p_stemmer_args_1315(p):
    """stemmer_args : """
    p[0] = Expr("""stemmer_args""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_index_params_1316(p):
    """index_params : index_elem"""
    p[0] = Expr("""index_params""", """index_elem""", p[1:] if len(p or []) > 1 else [], p)


def p_index_params_1317(p):
    """index_params : index_params ',' index_elem"""
    p[0] = Expr("""index_params""", """index_params ',' index_elem""", p[1:] if len(p or []) > 1 else [], p)


def p_index_elem_1318(p):
    """index_elem : ColId opt_class"""
    p[0] = Expr("""index_elem""", """ColId opt_class""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_class_1319(p):
    """opt_class : any_name"""
    p[0] = Expr("""opt_class""", """any_name""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_class_1320(p):
    """opt_class : USING any_name"""
    p[0] = Expr("""opt_class""", """USING any_name""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_class_1321(p):
    """opt_class : """
    p[0] = Expr("""opt_class""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateUDXStmt_1322(p):
    """CreateUDXStmt : CREATE opt_or_replace TRANSFORM FUNCTION udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name createtransform_opt_list"""
    p[0] = Expr("""CreateUDXStmt""", """CREATE opt_or_replace TRANSFORM FUNCTION udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name createtransform_opt_list""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateUDXStmt_1323(p):
    """CreateUDXStmt : CREATE opt_or_replace ANALYTIC FUNCTION udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name createtransform_opt_list"""
    p[0] = Expr("""CreateUDXStmt""", """CREATE opt_or_replace ANALYTIC FUNCTION udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name createtransform_opt_list""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateUDXStmt_1324(p):
    """CreateUDXStmt : CREATE opt_or_replace SOURCE udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name createtransform_opt_list"""
    p[0] = Expr("""CreateUDXStmt""", """CREATE opt_or_replace SOURCE udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name createtransform_opt_list""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateUDXStmt_1325(p):
    """CreateUDXStmt : CREATE opt_or_replace FILTER udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name createtransform_opt_list"""
    p[0] = Expr("""CreateUDXStmt""", """CREATE opt_or_replace FILTER udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name createtransform_opt_list""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateUDXStmt_1326(p):
    """CreateUDXStmt : CREATE opt_or_replace UNPACKER udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name createtransform_opt_list"""
    p[0] = Expr("""CreateUDXStmt""", """CREATE opt_or_replace UNPACKER udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name createtransform_opt_list""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateUDXStmt_1327(p):
    """CreateUDXStmt : CREATE opt_or_replace PARSER udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name createtransform_opt_list"""
    p[0] = Expr("""CreateUDXStmt""", """CREATE opt_or_replace PARSER udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name createtransform_opt_list""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateUDXStmt_1328(p):
    """CreateUDXStmt : CREATE opt_or_replace AGGREGATE FUNCTION udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name"""
    p[0] = Expr("""CreateUDXStmt""", """CREATE opt_or_replace AGGREGATE FUNCTION udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateUDXStmt_1329(p):
    """CreateUDXStmt : CREATE opt_or_replace TYPE_P udx_func_name definition"""
    p[0] = Expr("""CreateUDXStmt""", """CREATE opt_or_replace TYPE_P udx_func_name definition""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateUDXStmt_1330(p):
    """CreateUDXStmt : CREATE opt_or_replace FILESYSTEM udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name"""
    p[0] = Expr("""CreateUDXStmt""", """CREATE opt_or_replace FILESYSTEM udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_createtransform_opt_list_1331(p):
    """createtransform_opt_list : createtransform_opt_list createtransform_opt_item"""
    p[0] = Expr("""createtransform_opt_list""", """createtransform_opt_list createtransform_opt_item""", p[1:] if len(p or []) > 1 else [], p)


def p_createtransform_opt_list_1332(p):
    """createtransform_opt_list : """
    p[0] = Expr("""createtransform_opt_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_createtransform_opt_item_1333(p):
    """createtransform_opt_item : FENCED"""
    p[0] = Expr("""createtransform_opt_item""", """FENCED""", p[1:] if len(p or []) > 1 else [], p)


def p_createtransform_opt_item_1334(p):
    """createtransform_opt_item : NOT FENCED"""
    p[0] = Expr("""createtransform_opt_item""", """NOT FENCED""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateFunctionStmt_1335(p):
    """CreateFunctionStmt : CREATE opt_or_replace FUNCTION udx_func_name func_args RETURN func_return AS BEGIN_P RETURN a_expr ';' END_P"""
    p[0] = Expr("""CreateFunctionStmt""", """CREATE opt_or_replace FUNCTION udx_func_name func_args RETURN func_return AS BEGIN_P RETURN a_expr ';' END_P""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateFunctionStmt_1336(p):
    """CreateFunctionStmt : CREATE opt_or_replace FUNCTION udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name createfunc_opt_list"""
    p[0] = Expr("""CreateFunctionStmt""", """CREATE opt_or_replace FUNCTION udx_func_name AS Opt_language NAME_P Sconst LIBRARY qualified_name createfunc_opt_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFunctionStmt_1337(p):
    """AlterFunctionStmt : ALTER FUNCTION func_name func_args SET SCHEMA qualified_schema_name"""
    p[0] = Expr("""AlterFunctionStmt""", """ALTER FUNCTION func_name func_args SET SCHEMA qualified_schema_name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFunctionStmt_1338(p):
    """AlterFunctionStmt : ALTER FUNCTION func_name func_args OWNER TO UserId"""
    p[0] = Expr("""AlterFunctionStmt""", """ALTER FUNCTION func_name func_args OWNER TO UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFunctionStmt_1339(p):
    """AlterFunctionStmt : ALTER TRANSFORM FUNCTION func_name func_args SET SCHEMA qualified_schema_name"""
    p[0] = Expr("""AlterFunctionStmt""", """ALTER TRANSFORM FUNCTION func_name func_args SET SCHEMA qualified_schema_name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFunctionStmt_1340(p):
    """AlterFunctionStmt : ALTER TRANSFORM FUNCTION func_name func_args OWNER TO UserId"""
    p[0] = Expr("""AlterFunctionStmt""", """ALTER TRANSFORM FUNCTION func_name func_args OWNER TO UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFunctionStmt_1341(p):
    """AlterFunctionStmt : ALTER AGGREGATE FUNCTION func_name func_args SET SCHEMA qualified_schema_name"""
    p[0] = Expr("""AlterFunctionStmt""", """ALTER AGGREGATE FUNCTION func_name func_args SET SCHEMA qualified_schema_name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFunctionStmt_1342(p):
    """AlterFunctionStmt : ALTER AGGREGATE FUNCTION func_name func_args OWNER TO UserId"""
    p[0] = Expr("""AlterFunctionStmt""", """ALTER AGGREGATE FUNCTION func_name func_args OWNER TO UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFunctionStmt_1343(p):
    """AlterFunctionStmt : ALTER ANALYTIC FUNCTION func_name func_args SET SCHEMA qualified_schema_name"""
    p[0] = Expr("""AlterFunctionStmt""", """ALTER ANALYTIC FUNCTION func_name func_args SET SCHEMA qualified_schema_name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFunctionStmt_1344(p):
    """AlterFunctionStmt : ALTER ANALYTIC FUNCTION func_name func_args OWNER TO UserId"""
    p[0] = Expr("""AlterFunctionStmt""", """ALTER ANALYTIC FUNCTION func_name func_args OWNER TO UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFunctionStmt_1345(p):
    """AlterFunctionStmt : ALTER SOURCE func_name func_args SET SCHEMA qualified_schema_name"""
    p[0] = Expr("""AlterFunctionStmt""", """ALTER SOURCE func_name func_args SET SCHEMA qualified_schema_name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFunctionStmt_1346(p):
    """AlterFunctionStmt : ALTER SOURCE func_name func_args OWNER TO UserId"""
    p[0] = Expr("""AlterFunctionStmt""", """ALTER SOURCE func_name func_args OWNER TO UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFunctionStmt_1347(p):
    """AlterFunctionStmt : ALTER FILTER func_name func_args SET SCHEMA qualified_schema_name"""
    p[0] = Expr("""AlterFunctionStmt""", """ALTER FILTER func_name func_args SET SCHEMA qualified_schema_name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFunctionStmt_1348(p):
    """AlterFunctionStmt : ALTER FILTER func_name func_args OWNER TO UserId"""
    p[0] = Expr("""AlterFunctionStmt""", """ALTER FILTER func_name func_args OWNER TO UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFunctionStmt_1349(p):
    """AlterFunctionStmt : ALTER PARSER func_name func_args SET SCHEMA qualified_schema_name"""
    p[0] = Expr("""AlterFunctionStmt""", """ALTER PARSER func_name func_args SET SCHEMA qualified_schema_name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterFunctionStmt_1350(p):
    """AlterFunctionStmt : ALTER PARSER func_name func_args OWNER TO UserId"""
    p[0] = Expr("""AlterFunctionStmt""", """ALTER PARSER func_name func_args OWNER TO UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterUDxFenceStmt_1351(p):
    """AlterUDxFenceStmt : ALTER FUNCTION func_name func_args SET FENCED fenced_property"""
    p[0] = Expr("""AlterUDxFenceStmt""", """ALTER FUNCTION func_name func_args SET FENCED fenced_property""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterUDxFenceStmt_1352(p):
    """AlterUDxFenceStmt : ALTER TRANSFORM FUNCTION func_name func_args SET FENCED fenced_property"""
    p[0] = Expr("""AlterUDxFenceStmt""", """ALTER TRANSFORM FUNCTION func_name func_args SET FENCED fenced_property""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterUDxFenceStmt_1353(p):
    """AlterUDxFenceStmt : ALTER ANALYTIC FUNCTION func_name func_args SET FENCED fenced_property"""
    p[0] = Expr("""AlterUDxFenceStmt""", """ALTER ANALYTIC FUNCTION func_name func_args SET FENCED fenced_property""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterUDxFenceStmt_1354(p):
    """AlterUDxFenceStmt : ALTER SOURCE func_name func_args SET FENCED fenced_property"""
    p[0] = Expr("""AlterUDxFenceStmt""", """ALTER SOURCE func_name func_args SET FENCED fenced_property""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterUDxFenceStmt_1355(p):
    """AlterUDxFenceStmt : ALTER FILTER func_name func_args SET FENCED fenced_property"""
    p[0] = Expr("""AlterUDxFenceStmt""", """ALTER FILTER func_name func_args SET FENCED fenced_property""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterUDxFenceStmt_1356(p):
    """AlterUDxFenceStmt : ALTER PARSER func_name func_args SET FENCED fenced_property"""
    p[0] = Expr("""AlterUDxFenceStmt""", """ALTER PARSER func_name func_args SET FENCED fenced_property""", p[1:] if len(p or []) > 1 else [], p)


def p_fenced_property_1357(p):
    """fenced_property : TRUE_P"""
    p[0] = Expr("""fenced_property""", """TRUE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_fenced_property_1358(p):
    """fenced_property : FALSE_P"""
    p[0] = Expr("""fenced_property""", """FALSE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_or_replace_1359(p):
    """opt_or_replace : OR REPLACE"""
    p[0] = Expr("""opt_or_replace""", """OR REPLACE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_or_replace_1360(p):
    """opt_or_replace : """
    p[0] = Expr("""opt_or_replace""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_func_args_1361(p):
    """func_args : '(' func_args_list ')'"""
    p[0] = Expr("""func_args""", """'(' func_args_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_func_args_1362(p):
    """func_args : '(' ')'"""
    p[0] = Expr("""func_args""", """'(' ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_func_args_list_1363(p):
    """func_args_list : func_arg"""
    p[0] = Expr("""func_args_list""", """func_arg""", p[1:] if len(p or []) > 1 else [], p)


def p_func_args_list_1364(p):
    """func_args_list : func_args_list ',' func_arg"""
    p[0] = Expr("""func_args_list""", """func_args_list ',' func_arg""", p[1:] if len(p or []) > 1 else [], p)


def p_func_arg_1365(p):
    """func_arg : arg_class param_name func_type"""
    p[0] = Expr("""func_arg""", """arg_class param_name func_type""", p[1:] if len(p or []) > 1 else [], p)


def p_func_arg_1366(p):
    """func_arg : arg_class func_type"""
    p[0] = Expr("""func_arg""", """arg_class func_type""", p[1:] if len(p or []) > 1 else [], p)


def p_arg_class_1367(p):
    """arg_class : IN_P"""
    p[0] = Expr("""arg_class""", """IN_P""", p[1:] if len(p or []) > 1 else [], p)


def p_arg_class_1368(p):
    """arg_class : OUT_P"""
    p[0] = Expr("""arg_class""", """OUT_P""", p[1:] if len(p or []) > 1 else [], p)


def p_arg_class_1369(p):
    """arg_class : INOUT"""
    p[0] = Expr("""arg_class""", """INOUT""", p[1:] if len(p or []) > 1 else [], p)


def p_arg_class_1370(p):
    """arg_class : """
    p[0] = Expr("""arg_class""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_param_name_1371(p):
    """param_name : function_name"""
    p[0] = Expr("""param_name""", """function_name""", p[1:] if len(p or []) > 1 else [], p)


def p_func_return_1372(p):
    """func_return : func_type"""
    p[0] = Expr("""func_return""", """func_type""", p[1:] if len(p or []) > 1 else [], p)


def p_func_type_1373(p):
    """func_type : Typename"""
    p[0] = Expr("""func_type""", """Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_func_type_1374(p):
    """func_type : type_name attrs '%' TYPE_P"""
    p[0] = Expr("""func_type""", """type_name attrs '%' TYPE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_createfunc_opt_list_1375(p):
    """createfunc_opt_list : createfunc_opt_list createfunc_opt_item"""
    p[0] = Expr("""createfunc_opt_list""", """createfunc_opt_list createfunc_opt_item""", p[1:] if len(p or []) > 1 else [], p)


def p_createfunc_opt_list_1376(p):
    """createfunc_opt_list : """
    p[0] = Expr("""createfunc_opt_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_createfunc_opt_item_1377(p):
    """createfunc_opt_item : FENCED"""
    p[0] = Expr("""createfunc_opt_item""", """FENCED""", p[1:] if len(p or []) > 1 else [], p)


def p_createfunc_opt_item_1378(p):
    """createfunc_opt_item : NOT FENCED"""
    p[0] = Expr("""createfunc_opt_item""", """NOT FENCED""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateLibraryStmt_1379(p):
    """CreateLibraryStmt : CREATE opt_or_replace LIBRARY qualified_name AS Sconst Opt_depends Opt_language"""
    p[0] = Expr("""CreateLibraryStmt""", """CREATE opt_or_replace LIBRARY qualified_name AS Sconst Opt_depends Opt_language""", p[1:] if len(p or []) > 1 else [], p)


def p_Opt_depends_1380(p):
    """Opt_depends : DEPENDS Sconst"""
    p[0] = Expr("""Opt_depends""", """DEPENDS Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_Opt_depends_1381(p):
    """Opt_depends : """
    p[0] = Expr("""Opt_depends""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_Opt_language_1382(p):
    """Opt_language : LANGUAGE Sconst"""
    p[0] = Expr("""Opt_language""", """LANGUAGE Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_Opt_language_1383(p):
    """Opt_language : """
    p[0] = Expr("""Opt_language""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterLibraryStmt_1384(p):
    """AlterLibraryStmt : ALTER LIBRARY qualified_name AS Sconst Opt_depends"""
    p[0] = Expr("""AlterLibraryStmt""", """ALTER LIBRARY qualified_name AS Sconst Opt_depends""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateProcStmt_1385(p):
    """CreateProcStmt : CREATE PROCEDURE func_name proc_args createproc_opt_list"""
    p[0] = Expr("""CreateProcStmt""", """CREATE PROCEDURE func_name proc_args createproc_opt_list""", p[1:] if len(p or []) > 1 else [], p)


def p_proc_args_1386(p):
    """proc_args : '(' proc_args_list ')'"""
    p[0] = Expr("""proc_args""", """'(' proc_args_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_proc_args_1387(p):
    """proc_args : '(' ')'"""
    p[0] = Expr("""proc_args""", """'(' ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_proc_args_list_1388(p):
    """proc_args_list : proc_arg"""
    p[0] = Expr("""proc_args_list""", """proc_arg""", p[1:] if len(p or []) > 1 else [], p)


def p_proc_args_list_1389(p):
    """proc_args_list : proc_args_list ',' proc_arg"""
    p[0] = Expr("""proc_args_list""", """proc_args_list ',' proc_arg""", p[1:] if len(p or []) > 1 else [], p)


def p_proc_arg_1390(p):
    """proc_arg : proc_param_name proc_type"""
    p[0] = Expr("""proc_arg""", """proc_param_name proc_type""", p[1:] if len(p or []) > 1 else [], p)


def p_proc_arg_1391(p):
    """proc_arg : proc_type"""
    p[0] = Expr("""proc_arg""", """proc_type""", p[1:] if len(p or []) > 1 else [], p)


def p_proc_param_name_1392(p):
    """proc_param_name : function_name"""
    p[0] = Expr("""proc_param_name""", """function_name""", p[1:] if len(p or []) > 1 else [], p)


def p_proc_type_1393(p):
    """proc_type : Typename"""
    p[0] = Expr("""proc_type""", """Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_createproc_opt_list_1394(p):
    """createproc_opt_list : createproc_opt_item"""
    p[0] = Expr("""createproc_opt_list""", """createproc_opt_item""", p[1:] if len(p or []) > 1 else [], p)


def p_createproc_opt_list_1395(p):
    """createproc_opt_list : createproc_opt_list createproc_opt_item"""
    p[0] = Expr("""createproc_opt_list""", """createproc_opt_list createproc_opt_item""", p[1:] if len(p or []) > 1 else [], p)


def p_createproc_opt_item_1396(p):
    """createproc_opt_item : AS Sconst"""
    p[0] = Expr("""createproc_opt_item""", """AS Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_createproc_opt_item_1397(p):
    """createproc_opt_item : ON Sconst"""
    p[0] = Expr("""createproc_opt_item""", """ON Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_createproc_opt_item_1398(p):
    """createproc_opt_item : LANGUAGE ColId_or_Sconst"""
    p[0] = Expr("""createproc_opt_item""", """LANGUAGE ColId_or_Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_createproc_opt_item_1399(p):
    """createproc_opt_item : USER Sconst"""
    p[0] = Expr("""createproc_opt_item""", """USER Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveFuncStmt_1400(p):
    """RemoveFuncStmt : DROP FUNCTION IF_P EXISTS func_name func_args opt_drop_behavior"""
    p[0] = Expr("""RemoveFuncStmt""", """DROP FUNCTION IF_P EXISTS func_name func_args opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveFuncStmt_1401(p):
    """RemoveFuncStmt : DROP FUNCTION func_name func_args opt_drop_behavior"""
    p[0] = Expr("""RemoveFuncStmt""", """DROP FUNCTION func_name func_args opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveProcStmt_1402(p):
    """RemoveProcStmt : DROP PROCEDURE IF_P EXISTS func_name proc_args opt_drop_behavior"""
    p[0] = Expr("""RemoveProcStmt""", """DROP PROCEDURE IF_P EXISTS func_name proc_args opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveProcStmt_1403(p):
    """RemoveProcStmt : DROP PROCEDURE func_name proc_args opt_drop_behavior"""
    p[0] = Expr("""RemoveProcStmt""", """DROP PROCEDURE func_name proc_args opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveUDXStmt_1404(p):
    """RemoveUDXStmt : DROP TRANSFORM FUNCTION IF_P EXISTS func_name func_args opt_drop_behavior"""
    p[0] = Expr("""RemoveUDXStmt""", """DROP TRANSFORM FUNCTION IF_P EXISTS func_name func_args opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveUDXStmt_1405(p):
    """RemoveUDXStmt : DROP TRANSFORM FUNCTION func_name func_args opt_drop_behavior"""
    p[0] = Expr("""RemoveUDXStmt""", """DROP TRANSFORM FUNCTION func_name func_args opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveUDXStmt_1406(p):
    """RemoveUDXStmt : DROP ANALYTIC FUNCTION IF_P EXISTS func_name func_args"""
    p[0] = Expr("""RemoveUDXStmt""", """DROP ANALYTIC FUNCTION IF_P EXISTS func_name func_args""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveUDXStmt_1407(p):
    """RemoveUDXStmt : DROP ANALYTIC FUNCTION func_name func_args"""
    p[0] = Expr("""RemoveUDXStmt""", """DROP ANALYTIC FUNCTION func_name func_args""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveUDXStmt_1408(p):
    """RemoveUDXStmt : DROP AGGREGATE FUNCTION IF_P EXISTS func_name func_args"""
    p[0] = Expr("""RemoveUDXStmt""", """DROP AGGREGATE FUNCTION IF_P EXISTS func_name func_args""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveUDXStmt_1409(p):
    """RemoveUDXStmt : DROP AGGREGATE FUNCTION func_name func_args"""
    p[0] = Expr("""RemoveUDXStmt""", """DROP AGGREGATE FUNCTION func_name func_args""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveUDXStmt_1410(p):
    """RemoveUDXStmt : DROP PARSER func_name func_args"""
    p[0] = Expr("""RemoveUDXStmt""", """DROP PARSER func_name func_args""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveUDXStmt_1411(p):
    """RemoveUDXStmt : DROP FILTER func_name func_args"""
    p[0] = Expr("""RemoveUDXStmt""", """DROP FILTER func_name func_args""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveUDXStmt_1412(p):
    """RemoveUDXStmt : DROP UNPACKER func_name func_args"""
    p[0] = Expr("""RemoveUDXStmt""", """DROP UNPACKER func_name func_args""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveUDXStmt_1413(p):
    """RemoveUDXStmt : DROP SOURCE func_name func_args"""
    p[0] = Expr("""RemoveUDXStmt""", """DROP SOURCE func_name func_args""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveAggrStmt_1414(p):
    """RemoveAggrStmt : DROP AGGREGATE func_name '(' aggr_argtype ')' opt_drop_behavior"""
    p[0] = Expr("""RemoveAggrStmt""", """DROP AGGREGATE func_name '(' aggr_argtype ')' opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_aggr_argtype_1415(p):
    """aggr_argtype : Typename"""
    p[0] = Expr("""aggr_argtype""", """Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_aggr_argtype_1416(p):
    """aggr_argtype : '*'"""
    p[0] = Expr("""aggr_argtype""", """'*'""", p[1:] if len(p or []) > 1 else [], p)


def p_RemoveOperStmt_1417(p):
    """RemoveOperStmt : DROP OPERATOR any_operator '(' oper_argtypes ')' opt_drop_behavior"""
    p[0] = Expr("""RemoveOperStmt""", """DROP OPERATOR any_operator '(' oper_argtypes ')' opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_oper_argtypes_1418(p):
    """oper_argtypes : Typename"""
    p[0] = Expr("""oper_argtypes""", """Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_oper_argtypes_1419(p):
    """oper_argtypes : Typename ',' Typename"""
    p[0] = Expr("""oper_argtypes""", """Typename ',' Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_oper_argtypes_1420(p):
    """oper_argtypes : NONE ',' Typename"""
    p[0] = Expr("""oper_argtypes""", """NONE ',' Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_oper_argtypes_1421(p):
    """oper_argtypes : Typename ',' NONE"""
    p[0] = Expr("""oper_argtypes""", """Typename ',' NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_any_operator_1422(p):
    """any_operator : all_Op"""
    p[0] = Expr("""any_operator""", """all_Op""", p[1:] if len(p or []) > 1 else [], p)


def p_any_operator_1423(p):
    """any_operator : ColId '.' any_operator"""
    p[0] = Expr("""any_operator""", """ColId '.' any_operator""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateCastStmt_1424(p):
    """CreateCastStmt : CREATE CAST '(' Typename AS Typename ')' WITH FUNCTION function_with_argtypes cast_context"""
    p[0] = Expr("""CreateCastStmt""", """CREATE CAST '(' Typename AS Typename ')' WITH FUNCTION function_with_argtypes cast_context""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateCastStmt_1425(p):
    """CreateCastStmt : CREATE CAST '(' Typename AS Typename ')' WITHOUT FUNCTION cast_context"""
    p[0] = Expr("""CreateCastStmt""", """CREATE CAST '(' Typename AS Typename ')' WITHOUT FUNCTION cast_context""", p[1:] if len(p or []) > 1 else [], p)


def p_cast_context_1426(p):
    """cast_context : AS IMPLICIT_P"""
    p[0] = Expr("""cast_context""", """AS IMPLICIT_P""", p[1:] if len(p or []) > 1 else [], p)


def p_cast_context_1427(p):
    """cast_context : AS ASSIGNMENT"""
    p[0] = Expr("""cast_context""", """AS ASSIGNMENT""", p[1:] if len(p or []) > 1 else [], p)


def p_cast_context_1428(p):
    """cast_context : """
    p[0] = Expr("""cast_context""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_DropCastStmt_1429(p):
    """DropCastStmt : DROP CAST '(' Typename AS Typename ')' opt_drop_behavior"""
    p[0] = Expr("""DropCastStmt""", """DROP CAST '(' Typename AS Typename ')' opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_ReindexStmt_1430(p):
    """ReindexStmt : REINDEX reindex_type qualified_name opt_force"""
    p[0] = Expr("""ReindexStmt""", """REINDEX reindex_type qualified_name opt_force""", p[1:] if len(p or []) > 1 else [], p)


def p_ReindexStmt_1431(p):
    """ReindexStmt : REINDEX DATABASE name opt_force"""
    p[0] = Expr("""ReindexStmt""", """REINDEX DATABASE name opt_force""", p[1:] if len(p or []) > 1 else [], p)


def p_reindex_type_1432(p):
    """reindex_type : INDEX"""
    p[0] = Expr("""reindex_type""", """INDEX""", p[1:] if len(p or []) > 1 else [], p)


def p_reindex_type_1433(p):
    """reindex_type : TABLE"""
    p[0] = Expr("""reindex_type""", """TABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_force_1434(p):
    """opt_force : FORCE"""
    p[0] = Expr("""opt_force""", """FORCE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_force_1435(p):
    """opt_force : """
    p[0] = Expr("""opt_force""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1436(p):
    """RenameStmt : ALTER AGGREGATE func_name '(' aggr_argtype ')' RENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER AGGREGATE func_name '(' aggr_argtype ')' RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1437(p):
    """RenameStmt : ALTER DATABASE database_name RENAME TO database_name"""
    p[0] = Expr("""RenameStmt""", """ALTER DATABASE database_name RENAME TO database_name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1438(p):
    """RenameStmt : ALTER FUNCTION func_name func_args RENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER FUNCTION func_name func_args RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1439(p):
    """RenameStmt : ALTER GROUP_P UserId RENAME TO UserId"""
    p[0] = Expr("""RenameStmt""", """ALTER GROUP_P UserId RENAME TO UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1440(p):
    """RenameStmt : ALTER LANGUAGE name RENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER LANGUAGE name RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1441(p):
    """RenameStmt : ALTER OPERATOR CLASS any_name USING access_method RENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER OPERATOR CLASS any_name USING access_method RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1442(p):
    """RenameStmt : ALTER SCHEMA qualified_schema_name_list RENAME TO name_list"""
    p[0] = Expr("""RenameStmt""", """ALTER SCHEMA qualified_schema_name_list RENAME TO name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1443(p):
    """RenameStmt : ALTER TABLE qualified_name_list ',' qualified_name RENAME TO name_list"""
    p[0] = Expr("""RenameStmt""", """ALTER TABLE qualified_name_list ',' qualified_name RENAME TO name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1444(p):
    """RenameStmt : ALTER TABLE relation_expr RENAME TO name_list"""
    p[0] = Expr("""RenameStmt""", """ALTER TABLE relation_expr RENAME TO name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1445(p):
    """RenameStmt : ALTER VIEW qualified_name_list RENAME TO name_list"""
    p[0] = Expr("""RenameStmt""", """ALTER VIEW qualified_name_list RENAME TO name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1446(p):
    """RenameStmt : ALTER TABLE relation_expr RENAME opt_column name TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER TABLE relation_expr RENAME opt_column name TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1447(p):
    """RenameStmt : ALTER TABLE relation_expr RENAME CONSTRAINT name TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER TABLE relation_expr RENAME CONSTRAINT name TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1448(p):
    """RenameStmt : ALTER INDEX relation_expr RENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER INDEX relation_expr RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1449(p):
    """RenameStmt : ALTER MODEL relation_expr RENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER MODEL relation_expr RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1450(p):
    """RenameStmt : ALTER TRIGGER name ON relation_expr RENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER TRIGGER name ON relation_expr RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1451(p):
    """RenameStmt : ALTER USER UserId RENAME TO UserId"""
    p[0] = Expr("""RenameStmt""", """ALTER USER UserId RENAME TO UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1452(p):
    """RenameStmt : ALTER ROLE UserId RENAME TO UserId"""
    p[0] = Expr("""RenameStmt""", """ALTER ROLE UserId RENAME TO UserId""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1453(p):
    """RenameStmt : ALTER TABLESPACE name RENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER TABLESPACE name RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1454(p):
    """RenameStmt : ALTER PROJECTION qualified_name RENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER PROJECTION qualified_name RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1455(p):
    """RenameStmt : ALTER PROJECTION qualified_name SET BASENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER PROJECTION qualified_name SET BASENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1456(p):
    """RenameStmt : ALTER SEQUENCE qualified_name RENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER SEQUENCE qualified_name RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1457(p):
    """RenameStmt : ALTER PROFILE qualified_name RENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER PROFILE qualified_name RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1458(p):
    """RenameStmt : ALTER SUBNET qualified_name RENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER SUBNET qualified_name RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1459(p):
    """RenameStmt : ALTER NETWORK INTERFACE qualified_name RENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER NETWORK INTERFACE qualified_name RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_RenameStmt_1460(p):
    """RenameStmt : ALTER AUTHENTICATION qualified_name RENAME TO name"""
    p[0] = Expr("""RenameStmt""", """ALTER AUTHENTICATION qualified_name RENAME TO name""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_column_1461(p):
    """opt_column : COLUMN"""
    p[0] = Expr("""opt_column""", """COLUMN""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_column_1462(p):
    """opt_column : """
    p[0] = Expr("""opt_column""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_RuleStmt_1463(p):
    """RuleStmt : CREATE opt_or_replace RULE name AS _embed0_RuleStmt ON event TO qualified_name where_clause DO opt_instead RuleActionList"""
    p[0] = Expr("""RuleStmt""", """CREATE opt_or_replace RULE name AS _embed0_RuleStmt ON event TO qualified_name where_clause DO opt_instead RuleActionList""", p[1:] if len(p or []) > 1 else [], p)


def p__embed0_RuleStmt(p):
    '''_embed0_RuleStmt : '''


def p_RuleActionList_1464(p):
    """RuleActionList : NOTHING"""
    p[0] = Expr("""RuleActionList""", """NOTHING""", p[1:] if len(p or []) > 1 else [], p)


def p_RuleActionList_1465(p):
    """RuleActionList : RuleActionStmt"""
    p[0] = Expr("""RuleActionList""", """RuleActionStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_RuleActionList_1466(p):
    """RuleActionList : '(' RuleActionMulti ')'"""
    p[0] = Expr("""RuleActionList""", """'(' RuleActionMulti ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_RuleActionMulti_1467(p):
    """RuleActionMulti : RuleActionMulti ';' RuleActionStmtOrEmpty"""
    p[0] = Expr("""RuleActionMulti""", """RuleActionMulti ';' RuleActionStmtOrEmpty""", p[1:] if len(p or []) > 1 else [], p)


def p_RuleActionMulti_1468(p):
    """RuleActionMulti : RuleActionStmtOrEmpty"""
    p[0] = Expr("""RuleActionMulti""", """RuleActionStmtOrEmpty""", p[1:] if len(p or []) > 1 else [], p)


def p_RuleActionStmt_1469(p):
    """RuleActionStmt : SelectStmt"""
    p[0] = Expr("""RuleActionStmt""", """SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_RuleActionStmt_1470(p):
    """RuleActionStmt : InsertStmt"""
    p[0] = Expr("""RuleActionStmt""", """InsertStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_RuleActionStmt_1471(p):
    """RuleActionStmt : UpdateStmt"""
    p[0] = Expr("""RuleActionStmt""", """UpdateStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_RuleActionStmt_1472(p):
    """RuleActionStmt : DeleteStmt"""
    p[0] = Expr("""RuleActionStmt""", """DeleteStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_RuleActionStmt_1473(p):
    """RuleActionStmt : NotifyStmt"""
    p[0] = Expr("""RuleActionStmt""", """NotifyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_RuleActionStmt_1474(p):
    """RuleActionStmt : ExportStmt"""
    p[0] = Expr("""RuleActionStmt""", """ExportStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_RuleActionStmt_1475(p):
    """RuleActionStmt : VMergeStmt"""
    p[0] = Expr("""RuleActionStmt""", """VMergeStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_RuleActionStmtOrEmpty_1476(p):
    """RuleActionStmtOrEmpty : RuleActionStmt"""
    p[0] = Expr("""RuleActionStmtOrEmpty""", """RuleActionStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_RuleActionStmtOrEmpty_1477(p):
    """RuleActionStmtOrEmpty : """
    p[0] = Expr("""RuleActionStmtOrEmpty""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_event_1478(p):
    """event : SELECT"""
    p[0] = Expr("""event""", """SELECT""", p[1:] if len(p or []) > 1 else [], p)


def p_event_1479(p):
    """event : UPDATE"""
    p[0] = Expr("""event""", """UPDATE""", p[1:] if len(p or []) > 1 else [], p)


def p_event_1480(p):
    """event : DELETE_P"""
    p[0] = Expr("""event""", """DELETE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_event_1481(p):
    """event : INSERT"""
    p[0] = Expr("""event""", """INSERT""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_instead_1482(p):
    """opt_instead : INSTEAD"""
    p[0] = Expr("""opt_instead""", """INSTEAD""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_instead_1483(p):
    """opt_instead : ALSO"""
    p[0] = Expr("""opt_instead""", """ALSO""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_instead_1484(p):
    """opt_instead : """
    p[0] = Expr("""opt_instead""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_DropRuleStmt_1485(p):
    """DropRuleStmt : DROP RULE name ON qualified_name opt_drop_behavior"""
    p[0] = Expr("""DropRuleStmt""", """DROP RULE name ON qualified_name opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_NotifyStmt_1486(p):
    """NotifyStmt : NOTIFY qualified_name"""
    p[0] = Expr("""NotifyStmt""", """NOTIFY qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_ListenStmt_1487(p):
    """ListenStmt : LISTEN qualified_name"""
    p[0] = Expr("""ListenStmt""", """LISTEN qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_UnlistenStmt_1488(p):
    """UnlistenStmt : UNLISTEN qualified_name"""
    p[0] = Expr("""UnlistenStmt""", """UNLISTEN qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_UnlistenStmt_1489(p):
    """UnlistenStmt : UNLISTEN '*'"""
    p[0] = Expr("""UnlistenStmt""", """UNLISTEN '*'""", p[1:] if len(p or []) > 1 else [], p)


def p_TransactionStmt_1490(p):
    """TransactionStmt : ABORT_P opt_transaction"""
    p[0] = Expr("""TransactionStmt""", """ABORT_P opt_transaction""", p[1:] if len(p or []) > 1 else [], p)


def p_TransactionStmt_1491(p):
    """TransactionStmt : BEGIN_P opt_transaction transaction_mode_list_or_empty"""
    p[0] = Expr("""TransactionStmt""", """BEGIN_P opt_transaction transaction_mode_list_or_empty""", p[1:] if len(p or []) > 1 else [], p)


def p_TransactionStmt_1492(p):
    """TransactionStmt : START TRANSACTION transaction_mode_list_or_empty"""
    p[0] = Expr("""TransactionStmt""", """START TRANSACTION transaction_mode_list_or_empty""", p[1:] if len(p or []) > 1 else [], p)


def p_TransactionStmt_1493(p):
    """TransactionStmt : COMMIT opt_transaction opt_durable"""
    p[0] = Expr("""TransactionStmt""", """COMMIT opt_transaction opt_durable""", p[1:] if len(p or []) > 1 else [], p)


def p_TransactionStmt_1494(p):
    """TransactionStmt : END_P opt_transaction"""
    p[0] = Expr("""TransactionStmt""", """END_P opt_transaction""", p[1:] if len(p or []) > 1 else [], p)


def p_TransactionStmt_1495(p):
    """TransactionStmt : ROLLBACK_P opt_transaction"""
    p[0] = Expr("""TransactionStmt""", """ROLLBACK_P opt_transaction""", p[1:] if len(p or []) > 1 else [], p)


def p_TransactionStmt_1496(p):
    """TransactionStmt : SAVEPOINT ColId"""
    p[0] = Expr("""TransactionStmt""", """SAVEPOINT ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_TransactionStmt_1497(p):
    """TransactionStmt : RELEASE SAVEPOINT ColId"""
    p[0] = Expr("""TransactionStmt""", """RELEASE SAVEPOINT ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_TransactionStmt_1498(p):
    """TransactionStmt : RELEASE ColId"""
    p[0] = Expr("""TransactionStmt""", """RELEASE ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_TransactionStmt_1499(p):
    """TransactionStmt : ROLLBACK_P opt_transaction TO SAVEPOINT ColId"""
    p[0] = Expr("""TransactionStmt""", """ROLLBACK_P opt_transaction TO SAVEPOINT ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_TransactionStmt_1500(p):
    """TransactionStmt : ROLLBACK_P opt_transaction TO ColId"""
    p[0] = Expr("""TransactionStmt""", """ROLLBACK_P opt_transaction TO ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_transaction_1501(p):
    """opt_transaction : WORK"""
    p[0] = Expr("""opt_transaction""", """WORK""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_transaction_1502(p):
    """opt_transaction : TRANSACTION"""
    p[0] = Expr("""opt_transaction""", """TRANSACTION""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_transaction_1503(p):
    """opt_transaction : """
    p[0] = Expr("""opt_transaction""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_transaction_mode_item_1504(p):
    """transaction_mode_item : ISOLATION LEVEL iso_level"""
    p[0] = Expr("""transaction_mode_item""", """ISOLATION LEVEL iso_level""", p[1:] if len(p or []) > 1 else [], p)


def p_transaction_mode_item_1505(p):
    """transaction_mode_item : READ ONLY"""
    p[0] = Expr("""transaction_mode_item""", """READ ONLY""", p[1:] if len(p or []) > 1 else [], p)


def p_transaction_mode_item_1506(p):
    """transaction_mode_item : READ WRITE"""
    p[0] = Expr("""transaction_mode_item""", """READ WRITE""", p[1:] if len(p or []) > 1 else [], p)


def p_transaction_mode_list_1507(p):
    """transaction_mode_list : transaction_mode_item"""
    p[0] = Expr("""transaction_mode_list""", """transaction_mode_item""", p[1:] if len(p or []) > 1 else [], p)


def p_transaction_mode_list_1508(p):
    """transaction_mode_list : transaction_mode_list ',' transaction_mode_item"""
    p[0] = Expr("""transaction_mode_list""", """transaction_mode_list ',' transaction_mode_item""", p[1:] if len(p or []) > 1 else [], p)


def p_transaction_mode_list_1509(p):
    """transaction_mode_list : transaction_mode_list transaction_mode_item"""
    p[0] = Expr("""transaction_mode_list""", """transaction_mode_list transaction_mode_item""", p[1:] if len(p or []) > 1 else [], p)


def p_transaction_mode_list_or_empty_1510(p):
    """transaction_mode_list_or_empty : transaction_mode_list"""
    p[0] = Expr("""transaction_mode_list_or_empty""", """transaction_mode_list""", p[1:] if len(p or []) > 1 else [], p)


def p_transaction_mode_list_or_empty_1511(p):
    """transaction_mode_list_or_empty : """
    p[0] = Expr("""transaction_mode_list_or_empty""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_durable_1512(p):
    """opt_durable : DURABLE"""
    p[0] = Expr("""opt_durable""", """DURABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_durable_1513(p):
    """opt_durable : """
    p[0] = Expr("""opt_durable""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_ViewStmt_1514(p):
    """ViewStmt : CREATE OptLocalTempOnly VIEW qualified_name opt_column_list AS SelectStmt"""
    p[0] = Expr("""ViewStmt""", """CREATE OptLocalTempOnly VIEW qualified_name opt_column_list AS SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ViewStmt_1515(p):
    """ViewStmt : CREATE OptLocalTempOnly VIEW qualified_name opt_column_list INCLUDE SCHEMA PRIVILEGES AS SelectStmt"""
    p[0] = Expr("""ViewStmt""", """CREATE OptLocalTempOnly VIEW qualified_name opt_column_list INCLUDE SCHEMA PRIVILEGES AS SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ViewStmt_1516(p):
    """ViewStmt : CREATE OptLocalTempOnly VIEW qualified_name opt_column_list INCLUDE PRIVILEGES AS SelectStmt"""
    p[0] = Expr("""ViewStmt""", """CREATE OptLocalTempOnly VIEW qualified_name opt_column_list INCLUDE PRIVILEGES AS SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ViewStmt_1517(p):
    """ViewStmt : CREATE OptLocalTempOnly VIEW qualified_name opt_column_list EXCLUDE SCHEMA PRIVILEGES AS SelectStmt"""
    p[0] = Expr("""ViewStmt""", """CREATE OptLocalTempOnly VIEW qualified_name opt_column_list EXCLUDE SCHEMA PRIVILEGES AS SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ViewStmt_1518(p):
    """ViewStmt : CREATE OptLocalTempOnly VIEW qualified_name opt_column_list EXCLUDE PRIVILEGES AS SelectStmt"""
    p[0] = Expr("""ViewStmt""", """CREATE OptLocalTempOnly VIEW qualified_name opt_column_list EXCLUDE PRIVILEGES AS SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ViewStmt_1519(p):
    """ViewStmt : CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list AS SelectStmt"""
    p[0] = Expr("""ViewStmt""", """CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list AS SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ViewStmt_1520(p):
    """ViewStmt : CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list INCLUDE SCHEMA PRIVILEGES AS SelectStmt"""
    p[0] = Expr("""ViewStmt""", """CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list INCLUDE SCHEMA PRIVILEGES AS SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ViewStmt_1521(p):
    """ViewStmt : CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list INCLUDE PRIVILEGES AS SelectStmt"""
    p[0] = Expr("""ViewStmt""", """CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list INCLUDE PRIVILEGES AS SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ViewStmt_1522(p):
    """ViewStmt : CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list EXCLUDE SCHEMA PRIVILEGES AS SelectStmt"""
    p[0] = Expr("""ViewStmt""", """CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list EXCLUDE SCHEMA PRIVILEGES AS SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ViewStmt_1523(p):
    """ViewStmt : CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list EXCLUDE PRIVILEGES AS SelectStmt"""
    p[0] = Expr("""ViewStmt""", """CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list EXCLUDE PRIVILEGES AS SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_LoadStmt_1524(p):
    """LoadStmt : LOAD file_name"""
    p[0] = Expr("""LoadStmt""", """LOAD file_name""", p[1:] if len(p or []) > 1 else [], p)


def p_CreatedbStmt_1525(p):
    """CreatedbStmt : CREATE DATABASE database_name opt_with createdb_opt_list"""
    p[0] = Expr("""CreatedbStmt""", """CREATE DATABASE database_name opt_with createdb_opt_list""", p[1:] if len(p or []) > 1 else [], p)


def p_createdb_opt_list_1526(p):
    """createdb_opt_list : createdb_opt_list createdb_opt_item"""
    p[0] = Expr("""createdb_opt_list""", """createdb_opt_list createdb_opt_item""", p[1:] if len(p or []) > 1 else [], p)


def p_createdb_opt_list_1527(p):
    """createdb_opt_list : """
    p[0] = Expr("""createdb_opt_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_createdb_opt_item_1528(p):
    """createdb_opt_item : TABLESPACE opt_equal name"""
    p[0] = Expr("""createdb_opt_item""", """TABLESPACE opt_equal name""", p[1:] if len(p or []) > 1 else [], p)


def p_createdb_opt_item_1529(p):
    """createdb_opt_item : TABLESPACE opt_equal DEFAULT"""
    p[0] = Expr("""createdb_opt_item""", """TABLESPACE opt_equal DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_createdb_opt_item_1530(p):
    """createdb_opt_item : LOCATION opt_equal Sconst"""
    p[0] = Expr("""createdb_opt_item""", """LOCATION opt_equal Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_createdb_opt_item_1531(p):
    """createdb_opt_item : LOCATION opt_equal DEFAULT"""
    p[0] = Expr("""createdb_opt_item""", """LOCATION opt_equal DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_createdb_opt_item_1532(p):
    """createdb_opt_item : TEMPLATE opt_equal name"""
    p[0] = Expr("""createdb_opt_item""", """TEMPLATE opt_equal name""", p[1:] if len(p or []) > 1 else [], p)


def p_createdb_opt_item_1533(p):
    """createdb_opt_item : TEMPLATE opt_equal DEFAULT"""
    p[0] = Expr("""createdb_opt_item""", """TEMPLATE opt_equal DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_createdb_opt_item_1534(p):
    """createdb_opt_item : OWNER opt_equal name"""
    p[0] = Expr("""createdb_opt_item""", """OWNER opt_equal name""", p[1:] if len(p or []) > 1 else [], p)


def p_createdb_opt_item_1535(p):
    """createdb_opt_item : OWNER opt_equal DEFAULT"""
    p[0] = Expr("""createdb_opt_item""", """OWNER opt_equal DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_equal_1536(p):
    """opt_equal : '='"""
    p[0] = Expr("""opt_equal""", """'='""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_equal_1537(p):
    """opt_equal : """
    p[0] = Expr("""opt_equal""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_knob_list_1538(p):
    """knob_list : name"""
    p[0] = Expr("""knob_list""", """name""", p[1:] if len(p or []) > 1 else [], p)


def p_knob_list_1539(p):
    """knob_list : knob_list ',' name"""
    p[0] = Expr("""knob_list""", """knob_list ',' name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterDatabaseSetStmt_1540(p):
    """AlterDatabaseSetStmt : ALTER DATABASE database_name EXPORT ON name"""
    p[0] = Expr("""AlterDatabaseSetStmt""", """ALTER DATABASE database_name EXPORT ON name""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterDatabaseSetStmt_1541(p):
    """AlterDatabaseSetStmt : ALTER DATABASE database_name EXPORT ON DEFAULT"""
    p[0] = Expr("""AlterDatabaseSetStmt""", """ALTER DATABASE database_name EXPORT ON DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterDatabaseSetStmt_1542(p):
    """AlterDatabaseSetStmt : ALTER DATABASE database_name DROP ALL FAULT GROUP_P"""
    p[0] = Expr("""AlterDatabaseSetStmt""", """ALTER DATABASE database_name DROP ALL FAULT GROUP_P""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterDatabaseSetStmt_1543(p):
    """AlterDatabaseSetStmt : ALTER DATABASE database_name DROP ALL AUTO FAULT GROUP_P"""
    p[0] = Expr("""AlterDatabaseSetStmt""", """ALTER DATABASE database_name DROP ALL AUTO FAULT GROUP_P""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterDatabaseSetStmt_1544(p):
    """AlterDatabaseSetStmt : ALTER DATABASE database_name SET PARAMETER paramarg_list"""
    p[0] = Expr("""AlterDatabaseSetStmt""", """ALTER DATABASE database_name SET PARAMETER paramarg_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterDatabaseSetStmt_1545(p):
    """AlterDatabaseSetStmt : ALTER DATABASE database_name SET paramarg_list"""
    p[0] = Expr("""AlterDatabaseSetStmt""", """ALTER DATABASE database_name SET paramarg_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterDatabaseSetStmt_1546(p):
    """AlterDatabaseSetStmt : ALTER DATABASE database_name CLEAR PARAMETER knob_list"""
    p[0] = Expr("""AlterDatabaseSetStmt""", """ALTER DATABASE database_name CLEAR PARAMETER knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterDatabaseSetStmt_1547(p):
    """AlterDatabaseSetStmt : ALTER DATABASE database_name CLEAR knob_list"""
    p[0] = Expr("""AlterDatabaseSetStmt""", """ALTER DATABASE database_name CLEAR knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterDatabaseSetStmt_1548(p):
    """AlterDatabaseSetStmt : ALTER DATABASE database_name RESET STANDBY"""
    p[0] = Expr("""AlterDatabaseSetStmt""", """ALTER DATABASE database_name RESET STANDBY""", p[1:] if len(p or []) > 1 else [], p)


def p_ShowDatabaseStmt_1549(p):
    """ShowDatabaseStmt : SHOW DATABASE database_name knob_list"""
    p[0] = Expr("""ShowDatabaseStmt""", """SHOW DATABASE database_name knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_ShowDatabaseStmt_1550(p):
    """ShowDatabaseStmt : SHOW DATABASE database_name PARAMETER knob_list"""
    p[0] = Expr("""ShowDatabaseStmt""", """SHOW DATABASE database_name PARAMETER knob_list""", p[1:] if len(p or []) > 1 else [], p)


def p_ShowDatabaseStmt_1551(p):
    """ShowDatabaseStmt : SHOW DATABASE database_name ALL"""
    p[0] = Expr("""ShowDatabaseStmt""", """SHOW DATABASE database_name ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_ShowDatabaseStmt_1552(p):
    """ShowDatabaseStmt : SHOW DATABASE database_name PARAMETER ALL"""
    p[0] = Expr("""ShowDatabaseStmt""", """SHOW DATABASE database_name PARAMETER ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_DropdbStmt_1553(p):
    """DropdbStmt : DROP DATABASE database_name"""
    p[0] = Expr("""DropdbStmt""", """DROP DATABASE database_name""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateSubnetStmt_1554(p):
    """CreateSubnetStmt : CREATE SUBNET name opt_with Sconst opt_force"""
    p[0] = Expr("""CreateSubnetStmt""", """CREATE SUBNET name opt_with Sconst opt_force""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateDomainStmt_1555(p):
    """CreateDomainStmt : CREATE DOMAIN_P any_name opt_as Typename ColQualList"""
    p[0] = Expr("""CreateDomainStmt""", """CREATE DOMAIN_P any_name opt_as Typename ColQualList""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterDomainStmt_1556(p):
    """AlterDomainStmt : ALTER DOMAIN_P any_name alter_column_default"""
    p[0] = Expr("""AlterDomainStmt""", """ALTER DOMAIN_P any_name alter_column_default""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterDomainStmt_1557(p):
    """AlterDomainStmt : ALTER DOMAIN_P any_name DROP NOT NULL_P"""
    p[0] = Expr("""AlterDomainStmt""", """ALTER DOMAIN_P any_name DROP NOT NULL_P""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterDomainStmt_1558(p):
    """AlterDomainStmt : ALTER DOMAIN_P any_name SET NOT NULL_P"""
    p[0] = Expr("""AlterDomainStmt""", """ALTER DOMAIN_P any_name SET NOT NULL_P""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterDomainStmt_1559(p):
    """AlterDomainStmt : ALTER DOMAIN_P any_name ADD TableConstraint"""
    p[0] = Expr("""AlterDomainStmt""", """ALTER DOMAIN_P any_name ADD TableConstraint""", p[1:] if len(p or []) > 1 else [], p)


def p_AlterDomainStmt_1560(p):
    """AlterDomainStmt : ALTER DOMAIN_P any_name DROP CONSTRAINT name opt_drop_behavior"""
    p[0] = Expr("""AlterDomainStmt""", """ALTER DOMAIN_P any_name DROP CONSTRAINT name opt_drop_behavior""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_as_1561(p):
    """opt_as : AS"""
    p[0] = Expr("""opt_as""", """AS""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_as_1562(p):
    """opt_as : """
    p[0] = Expr("""opt_as""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_CreateLocationStmt_1563(p):
    """CreateLocationStmt : CREATE LOCATION Sconst OptNodes OptShared OptUsage OptLabel OptSize"""
    p[0] = Expr("""CreateLocationStmt""", """CREATE LOCATION Sconst OptNodes OptShared OptUsage OptLabel OptSize""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUsage_1564(p):
    """OptUsage : USAGE Sconst"""
    p[0] = Expr("""OptUsage""", """USAGE Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptUsage_1565(p):
    """OptUsage : """
    p[0] = Expr("""OptUsage""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptNodes_1566(p):
    """OptNodes : ALL NODES"""
    p[0] = Expr("""OptNodes""", """ALL NODES""", p[1:] if len(p or []) > 1 else [], p)


def p_OptNodes_1567(p):
    """OptNodes : NODE Sconst"""
    p[0] = Expr("""OptNodes""", """NODE Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptNodes_1568(p):
    """OptNodes : """
    p[0] = Expr("""OptNodes""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptShared_1569(p):
    """OptShared : SHARED"""
    p[0] = Expr("""OptShared""", """SHARED""", p[1:] if len(p or []) > 1 else [], p)


def p_OptShared_1570(p):
    """OptShared : COMMUNAL"""
    p[0] = Expr("""OptShared""", """COMMUNAL""", p[1:] if len(p or []) > 1 else [], p)


def p_OptShared_1571(p):
    """OptShared : """
    p[0] = Expr("""OptShared""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptLabel_1572(p):
    """OptLabel : LABEL Sconst"""
    p[0] = Expr("""OptLabel""", """LABEL Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptLabel_1573(p):
    """OptLabel : """
    p[0] = Expr("""OptLabel""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSize_1574(p):
    """OptSize : LIMIT Sconst"""
    p[0] = Expr("""OptSize""", """LIMIT Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptSize_1575(p):
    """OptSize : """
    p[0] = Expr("""OptSize""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_ClusterStmt_1576(p):
    """ClusterStmt : CLUSTER index_name ON qualified_name"""
    p[0] = Expr("""ClusterStmt""", """CLUSTER index_name ON qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_ClusterStmt_1577(p):
    """ClusterStmt : CLUSTER qualified_name"""
    p[0] = Expr("""ClusterStmt""", """CLUSTER qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_ClusterStmt_1578(p):
    """ClusterStmt : CLUSTER"""
    p[0] = Expr("""ClusterStmt""", """CLUSTER""", p[1:] if len(p or []) > 1 else [], p)


def p_AnalyzeStmt_1579(p):
    """AnalyzeStmt : analyze_keyword"""
    p[0] = Expr("""AnalyzeStmt""", """analyze_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_AnalyzeStmt_1580(p):
    """AnalyzeStmt : analyze_keyword qualified_name opt_name_list"""
    p[0] = Expr("""AnalyzeStmt""", """analyze_keyword qualified_name opt_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AnalyzeStmt_1581(p):
    """AnalyzeStmt : analyze_keyword CONSTRAINT qualified_name opt_name_list"""
    p[0] = Expr("""AnalyzeStmt""", """analyze_keyword CONSTRAINT qualified_name opt_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_AnalyzeStmt_1582(p):
    """AnalyzeStmt : analyze_keyword ALL CONSTRAINT"""
    p[0] = Expr("""AnalyzeStmt""", """analyze_keyword ALL CONSTRAINT""", p[1:] if len(p or []) > 1 else [], p)


def p_analyze_keyword_1583(p):
    """analyze_keyword : ANALYZE"""
    p[0] = Expr("""analyze_keyword""", """ANALYZE""", p[1:] if len(p or []) > 1 else [], p)


def p_analyze_keyword_1584(p):
    """analyze_keyword : ANALYSE"""
    p[0] = Expr("""analyze_keyword""", """ANALYSE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_json_1585(p):
    """opt_json : JSON"""
    p[0] = Expr("""opt_json""", """JSON""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_json_1586(p):
    """opt_json : """
    p[0] = Expr("""opt_json""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_verbose_1587(p):
    """opt_verbose : VERBOSE"""
    p[0] = Expr("""opt_verbose""", """VERBOSE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_verbose_1588(p):
    """opt_verbose : """
    p[0] = Expr("""opt_verbose""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_name_list_1589(p):
    """opt_name_list : '(' name_list ')'"""
    p[0] = Expr("""opt_name_list""", """'(' name_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_name_list_1590(p):
    """opt_name_list : """
    p[0] = Expr("""opt_name_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_local_1591(p):
    """opt_local : LOCAL"""
    p[0] = Expr("""opt_local""", """LOCAL""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_local_1592(p):
    """opt_local : """
    p[0] = Expr("""opt_local""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_hint_list_1593(p):
    """opt_hint_list : '(' hint_list ')'"""
    p[0] = Expr("""opt_hint_list""", """'(' hint_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_hint_list_1594(p):
    """opt_hint_list : """
    p[0] = Expr("""opt_hint_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanStabilitySavePlanStmt_1595(p):
    """PlanStabilitySavePlanStmt : SAVE QUERY PlanStabilitySupportedStmt"""
    p[0] = Expr("""PlanStabilitySavePlanStmt""", """SAVE QUERY PlanStabilitySupportedStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanStabilityAssociatePlanStmt_1596(p):
    """PlanStabilityAssociatePlanStmt : CREATE DIRECTED QUERY OptPlan PlanIdentifier PlanDescription OptimizerVersion DirectedQueryCreationDate PlanStabilitySupportedStmt"""
    p[0] = Expr("""PlanStabilityAssociatePlanStmt""", """CREATE DIRECTED QUERY OptPlan PlanIdentifier PlanDescription OptimizerVersion DirectedQueryCreationDate PlanStabilitySupportedStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanStabilityAssociatePlanStmt_1597(p):
    """PlanStabilityAssociatePlanStmt : CREATE DIRECTED QUERY CUSTOM PlanIdentifier PlanDescription OptimizerVersion DirectedQueryCreationDate PlanStabilitySupportedStmt"""
    p[0] = Expr("""PlanStabilityAssociatePlanStmt""", """CREATE DIRECTED QUERY CUSTOM PlanIdentifier PlanDescription OptimizerVersion DirectedQueryCreationDate PlanStabilitySupportedStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanStabilityRemovePlanStmt_1598(p):
    """PlanStabilityRemovePlanStmt : DROP DIRECTED QUERY PlanIdentifierList"""
    p[0] = Expr("""PlanStabilityRemovePlanStmt""", """DROP DIRECTED QUERY PlanIdentifierList""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanStabilityGetPlanStmt_1599(p):
    """PlanStabilityGetPlanStmt : GET DIRECTED QUERY PlanStabilitySupportedStmt"""
    p[0] = Expr("""PlanStabilityGetPlanStmt""", """GET DIRECTED QUERY PlanStabilitySupportedStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanStabilityGetPlanStmt_1600(p):
    """PlanStabilityGetPlanStmt : GET UNINDEXED DIRECTED QUERY"""
    p[0] = Expr("""PlanStabilityGetPlanStmt""", """GET UNINDEXED DIRECTED QUERY""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanStabilityActivatePlanStmt_1601(p):
    """PlanStabilityActivatePlanStmt : ACTIVATE DIRECTED QUERY PlanIdentifier"""
    p[0] = Expr("""PlanStabilityActivatePlanStmt""", """ACTIVATE DIRECTED QUERY PlanIdentifier""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanStabilityActivatePlanStmt_1602(p):
    """PlanStabilityActivatePlanStmt : DEACTIVATE DIRECTED QUERY PlanIdentifier"""
    p[0] = Expr("""PlanStabilityActivatePlanStmt""", """DEACTIVATE DIRECTED QUERY PlanIdentifier""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanStabilityActivatePlanStmt_1603(p):
    """PlanStabilityActivatePlanStmt : DEACTIVATE DIRECTED QUERY PlanStabilitySupportedStmt"""
    p[0] = Expr("""PlanStabilityActivatePlanStmt""", """DEACTIVATE DIRECTED QUERY PlanStabilitySupportedStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanStabilitySupportedStmt_1604(p):
    """PlanStabilitySupportedStmt : VSelectStmt"""
    p[0] = Expr("""PlanStabilitySupportedStmt""", """VSelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanIdentifier_1605(p):
    """PlanIdentifier : ColLabel"""
    p[0] = Expr("""PlanIdentifier""", """ColLabel""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanIdentifierList_1606(p):
    """PlanIdentifierList : PlanIdentifierList ',' PlanIdentifier"""
    p[0] = Expr("""PlanIdentifierList""", """PlanIdentifierList ',' PlanIdentifier""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanIdentifierList_1607(p):
    """PlanIdentifierList : PlanIdentifier"""
    p[0] = Expr("""PlanIdentifierList""", """PlanIdentifier""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanDescription_1608(p):
    """PlanDescription : COMMENT Sconst"""
    p[0] = Expr("""PlanDescription""", """COMMENT Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_PlanDescription_1609(p):
    """PlanDescription : """
    p[0] = Expr("""PlanDescription""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptimizerVersion_1610(p):
    """OptimizerVersion : OPTVER Sconst"""
    p[0] = Expr("""OptimizerVersion""", """OPTVER Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_OptimizerVersion_1611(p):
    """OptimizerVersion : """
    p[0] = Expr("""OptimizerVersion""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_DirectedQueryCreationDate_1612(p):
    """DirectedQueryCreationDate : PSDATE Sconst"""
    p[0] = Expr("""DirectedQueryCreationDate""", """PSDATE Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_DirectedQueryCreationDate_1613(p):
    """DirectedQueryCreationDate : """
    p[0] = Expr("""DirectedQueryCreationDate""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_OptPlan_1614(p):
    """OptPlan : OPTIMIZER"""
    p[0] = Expr("""OptPlan""", """OPTIMIZER""", p[1:] if len(p or []) > 1 else [], p)


def p_OptPlan_1615(p):
    """OptPlan : OPT"""
    p[0] = Expr("""OptPlan""", """OPT""", p[1:] if len(p or []) > 1 else [], p)


def p_ExplainStmt_1616(p):
    """ExplainStmt : EXPLAIN hint_clause opt_analyze opt_local opt_verbose opt_json opt_annotated ExplainableStmt"""
    p[0] = Expr("""ExplainStmt""", """EXPLAIN hint_clause opt_analyze opt_local opt_verbose opt_json opt_annotated ExplainableStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ExplainableStmt_1617(p):
    """ExplainableStmt : VSelectStmt"""
    p[0] = Expr("""ExplainableStmt""", """VSelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ExplainableStmt_1618(p):
    """ExplainableStmt : InsertStmt"""
    p[0] = Expr("""ExplainableStmt""", """InsertStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ExplainableStmt_1619(p):
    """ExplainableStmt : UpdateStmt"""
    p[0] = Expr("""ExplainableStmt""", """UpdateStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ExplainableStmt_1620(p):
    """ExplainableStmt : DeleteStmt"""
    p[0] = Expr("""ExplainableStmt""", """DeleteStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ExplainableStmt_1621(p):
    """ExplainableStmt : CopyStmt"""
    p[0] = Expr("""ExplainableStmt""", """CopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ExplainableStmt_1622(p):
    """ExplainableStmt : DeclareCursorStmt"""
    p[0] = Expr("""ExplainableStmt""", """DeclareCursorStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ExplainableStmt_1623(p):
    """ExplainableStmt : ExecuteStmt"""
    p[0] = Expr("""ExplainableStmt""", """ExecuteStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ExplainableStmt_1624(p):
    """ExplainableStmt : ExportStmt"""
    p[0] = Expr("""ExplainableStmt""", """ExportStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ExplainableStmt_1625(p):
    """ExplainableStmt : VMergeStmt"""
    p[0] = Expr("""ExplainableStmt""", """VMergeStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_analyze_1626(p):
    """opt_analyze : analyze_keyword"""
    p[0] = Expr("""opt_analyze""", """analyze_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_analyze_1627(p):
    """opt_analyze : """
    p[0] = Expr("""opt_analyze""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_annotated_1628(p):
    """opt_annotated : ANNOTATED"""
    p[0] = Expr("""opt_annotated""", """ANNOTATED""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_annotated_1629(p):
    """opt_annotated : """
    p[0] = Expr("""opt_annotated""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_ProfileStmt_1630(p):
    """ProfileStmt : PROFILE ProfileableStmt"""
    p[0] = Expr("""ProfileStmt""", """PROFILE ProfileableStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ProfileableStmt_1631(p):
    """ProfileableStmt : VSelectStmt"""
    p[0] = Expr("""ProfileableStmt""", """VSelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ProfileableStmt_1632(p):
    """ProfileableStmt : InsertStmt"""
    p[0] = Expr("""ProfileableStmt""", """InsertStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ProfileableStmt_1633(p):
    """ProfileableStmt : UpdateStmt"""
    p[0] = Expr("""ProfileableStmt""", """UpdateStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ProfileableStmt_1634(p):
    """ProfileableStmt : DeleteStmt"""
    p[0] = Expr("""ProfileableStmt""", """DeleteStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ProfileableStmt_1635(p):
    """ProfileableStmt : CopyStmt"""
    p[0] = Expr("""ProfileableStmt""", """CopyStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ProfileableStmt_1636(p):
    """ProfileableStmt : ExportStmt"""
    p[0] = Expr("""ProfileableStmt""", """ExportStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ProfileableStmt_1637(p):
    """ProfileableStmt : VMergeStmt"""
    p[0] = Expr("""ProfileableStmt""", """VMergeStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_PrepareStmt_1638(p):
    """PrepareStmt : PREPARE name prep_type_clause AS PreparableStmt"""
    p[0] = Expr("""PrepareStmt""", """PREPARE name prep_type_clause AS PreparableStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_prep_type_clause_1639(p):
    """prep_type_clause : '(' prep_type_list ')'"""
    p[0] = Expr("""prep_type_clause""", """'(' prep_type_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_prep_type_clause_1640(p):
    """prep_type_clause : """
    p[0] = Expr("""prep_type_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_prep_type_list_1641(p):
    """prep_type_list : Typename"""
    p[0] = Expr("""prep_type_list""", """Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_prep_type_list_1642(p):
    """prep_type_list : IDENT '(' Iconst ')'"""
    p[0] = Expr("""prep_type_list""", """IDENT '(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_prep_type_list_1643(p):
    """prep_type_list : prep_type_list ',' Typename"""
    p[0] = Expr("""prep_type_list""", """prep_type_list ',' Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_prep_type_list_1644(p):
    """prep_type_list : prep_type_list ',' IDENT '(' Iconst ')'"""
    p[0] = Expr("""prep_type_list""", """prep_type_list ',' IDENT '(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_PreparableStmt_1645(p):
    """PreparableStmt : SelectStmt"""
    p[0] = Expr("""PreparableStmt""", """SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_PreparableStmt_1646(p):
    """PreparableStmt : InsertStmt"""
    p[0] = Expr("""PreparableStmt""", """InsertStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_PreparableStmt_1647(p):
    """PreparableStmt : UpdateStmt"""
    p[0] = Expr("""PreparableStmt""", """UpdateStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_PreparableStmt_1648(p):
    """PreparableStmt : DeleteStmt"""
    p[0] = Expr("""PreparableStmt""", """DeleteStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_PreparableStmt_1649(p):
    """PreparableStmt : ExportStmt"""
    p[0] = Expr("""PreparableStmt""", """ExportStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_PreparableStmt_1650(p):
    """PreparableStmt : VMergeStmt"""
    p[0] = Expr("""PreparableStmt""", """VMergeStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_ExecuteStmt_1651(p):
    """ExecuteStmt : EXECUTE name execute_param_clause"""
    p[0] = Expr("""ExecuteStmt""", """EXECUTE name execute_param_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_ExecuteStmt_1652(p):
    """ExecuteStmt : CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS EXECUTE name execute_param_clause"""
    p[0] = Expr("""ExecuteStmt""", """CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS EXECUTE name execute_param_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_execute_param_clause_1653(p):
    """execute_param_clause : '(' expr_list ')'"""
    p[0] = Expr("""execute_param_clause""", """'(' expr_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_execute_param_clause_1654(p):
    """execute_param_clause : """
    p[0] = Expr("""execute_param_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_DeallocateStmt_1655(p):
    """DeallocateStmt : DEALLOCATE name"""
    p[0] = Expr("""DeallocateStmt""", """DEALLOCATE name""", p[1:] if len(p or []) > 1 else [], p)


def p_DeallocateStmt_1656(p):
    """DeallocateStmt : DEALLOCATE PREPARE name"""
    p[0] = Expr("""DeallocateStmt""", """DEALLOCATE PREPARE name""", p[1:] if len(p or []) > 1 else [], p)


def p_VMergeStmt_1657(p):
    """VMergeStmt : MERGE hint_clause INTO merge_table_tgt_ref USING merge_table_src_ref ON a_expr merge_clause_list"""
    p[0] = Expr("""VMergeStmt""", """MERGE hint_clause INTO merge_table_tgt_ref USING merge_table_src_ref ON a_expr merge_clause_list""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_clause_list_1658(p):
    """merge_clause_list : merge_clause"""
    p[0] = Expr("""merge_clause_list""", """merge_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_clause_list_1659(p):
    """merge_clause_list : merge_clause_list merge_clause"""
    p[0] = Expr("""merge_clause_list""", """merge_clause_list merge_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_clause_1660(p):
    """merge_clause : merge_update_clause"""
    p[0] = Expr("""merge_clause""", """merge_update_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_clause_1661(p):
    """merge_clause : merge_insert_clause"""
    p[0] = Expr("""merge_clause""", """merge_insert_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_update_clause_1662(p):
    """merge_update_clause : WHEN MATCHED THEN UPDATE SET update_target_list where_clause"""
    p[0] = Expr("""merge_update_clause""", """WHEN MATCHED THEN UPDATE SET update_target_list where_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_update_clause_1663(p):
    """merge_update_clause : WHEN MATCHED AND a_expr THEN UPDATE SET update_target_list"""
    p[0] = Expr("""merge_update_clause""", """WHEN MATCHED AND a_expr THEN UPDATE SET update_target_list""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_insert_clause_1664(p):
    """merge_insert_clause : WHEN NOT MATCHED THEN INSERT merge_insert_target_list where_clause"""
    p[0] = Expr("""merge_insert_clause""", """WHEN NOT MATCHED THEN INSERT merge_insert_target_list where_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_insert_clause_1665(p):
    """merge_insert_clause : WHEN NOT MATCHED AND a_expr THEN INSERT merge_insert_target_list"""
    p[0] = Expr("""merge_insert_clause""", """WHEN NOT MATCHED AND a_expr THEN INSERT merge_insert_target_list""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_insert_target_list_1666(p):
    """merge_insert_target_list : VALUES '(' insert_target_list ')'"""
    p[0] = Expr("""merge_insert_target_list""", """VALUES '(' insert_target_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_insert_target_list_1667(p):
    """merge_insert_target_list : DEFAULT VALUES"""
    p[0] = Expr("""merge_insert_target_list""", """DEFAULT VALUES""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_insert_target_list_1668(p):
    """merge_insert_target_list : select_with_parens"""
    p[0] = Expr("""merge_insert_target_list""", """select_with_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_insert_target_list_1669(p):
    """merge_insert_target_list : '(' insert_column_list ')' VALUES '(' insert_target_list ')'"""
    p[0] = Expr("""merge_insert_target_list""", """'(' insert_column_list ')' VALUES '(' insert_target_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_insert_target_list_1670(p):
    """merge_insert_target_list : '(' insert_column_list ')' select_with_parens"""
    p[0] = Expr("""merge_insert_target_list""", """'(' insert_column_list ')' select_with_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_table_tgt_ref_1671(p):
    """merge_table_tgt_ref : relation_expr"""
    p[0] = Expr("""merge_table_tgt_ref""", """relation_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_table_tgt_ref_1672(p):
    """merge_table_tgt_ref : relation_expr alias_clause"""
    p[0] = Expr("""merge_table_tgt_ref""", """relation_expr alias_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_table_tgt_ref_1673(p):
    """merge_table_tgt_ref : select_with_parens"""
    p[0] = Expr("""merge_table_tgt_ref""", """select_with_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_table_tgt_ref_1674(p):
    """merge_table_tgt_ref : select_with_parens alias_clause"""
    p[0] = Expr("""merge_table_tgt_ref""", """select_with_parens alias_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_table_src_ref_1675(p):
    """merge_table_src_ref : relation_expr"""
    p[0] = Expr("""merge_table_src_ref""", """relation_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_table_src_ref_1676(p):
    """merge_table_src_ref : relation_expr alias_clause"""
    p[0] = Expr("""merge_table_src_ref""", """relation_expr alias_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_table_src_ref_1677(p):
    """merge_table_src_ref : select_with_parens"""
    p[0] = Expr("""merge_table_src_ref""", """select_with_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_merge_table_src_ref_1678(p):
    """merge_table_src_ref : select_with_parens alias_clause"""
    p[0] = Expr("""merge_table_src_ref""", """select_with_parens alias_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_InsertStmt_1679(p):
    """InsertStmt : INSERT hint_clause INTO qualified_name insert_rest"""
    p[0] = Expr("""InsertStmt""", """INSERT hint_clause INTO qualified_name insert_rest""", p[1:] if len(p or []) > 1 else [], p)


def p_insert_rest_1680(p):
    """insert_rest : VALUES '(' insert_target_list ')'"""
    p[0] = Expr("""insert_rest""", """VALUES '(' insert_target_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_insert_rest_1681(p):
    """insert_rest : DEFAULT VALUES"""
    p[0] = Expr("""insert_rest""", """DEFAULT VALUES""", p[1:] if len(p or []) > 1 else [], p)


def p_insert_rest_1682(p):
    """insert_rest : VSelectStmt"""
    p[0] = Expr("""insert_rest""", """VSelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_insert_rest_1683(p):
    """insert_rest : '(' insert_column_list ')' VALUES '(' insert_target_list ')'"""
    p[0] = Expr("""insert_rest""", """'(' insert_column_list ')' VALUES '(' insert_target_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_insert_rest_1684(p):
    """insert_rest : '(' insert_column_list ')' VSelectStmt"""
    p[0] = Expr("""insert_rest""", """'(' insert_column_list ')' VSelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_insert_column_list_1685(p):
    """insert_column_list : insert_column_item"""
    p[0] = Expr("""insert_column_list""", """insert_column_item""", p[1:] if len(p or []) > 1 else [], p)


def p_insert_column_list_1686(p):
    """insert_column_list : insert_column_list ',' insert_column_item"""
    p[0] = Expr("""insert_column_list""", """insert_column_list ',' insert_column_item""", p[1:] if len(p or []) > 1 else [], p)


def p_insert_column_item_1687(p):
    """insert_column_item : ColId opt_indirection"""
    p[0] = Expr("""insert_column_item""", """ColId opt_indirection""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_connect_addr_family_1688(p):
    """opt_connect_addr_family : ',' Sconst"""
    p[0] = Expr("""opt_connect_addr_family""", """',' Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_connect_addr_family_1689(p):
    """opt_connect_addr_family : """
    p[0] = Expr("""opt_connect_addr_family""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_connect_tls_mode_1690(p):
    """opt_connect_tls_mode : TLSMODE PREFER"""
    p[0] = Expr("""opt_connect_tls_mode""", """TLSMODE PREFER""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_connect_tls_mode_1691(p):
    """opt_connect_tls_mode : """
    p[0] = Expr("""opt_connect_tls_mode""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_ConnectStmt_1692(p):
    """ConnectStmt : CONNECT TO VERTICA database_name USER UserId PASSWORD Sconst ON Sconst ',' Iconst opt_connect_addr_family opt_connect_tls_mode"""
    p[0] = Expr("""ConnectStmt""", """CONNECT TO VERTICA database_name USER UserId PASSWORD Sconst ON Sconst ',' Iconst opt_connect_addr_family opt_connect_tls_mode""", p[1:] if len(p or []) > 1 else [], p)


def p_DisconnectStmt_1693(p):
    """DisconnectStmt : DISCONNECT database_name"""
    p[0] = Expr("""DisconnectStmt""", """DISCONNECT database_name""", p[1:] if len(p or []) > 1 else [], p)


def p_ExportStmt_1694(p):
    """ExportStmt : EXPORT TO VERTICA export_relation opt_export_column_list export_select export_segmentation"""
    p[0] = Expr("""ExportStmt""", """EXPORT TO VERTICA export_relation opt_export_column_list export_select export_segmentation""", p[1:] if len(p or []) > 1 else [], p)


def p_ExportStmt_1695(p):
    """ExportStmt : EXPORT TO STDOUT export_select"""
    p[0] = Expr("""ExportStmt""", """EXPORT TO STDOUT export_select""", p[1:] if len(p or []) > 1 else [], p)


def p_ExportStmt_1696(p):
    """ExportStmt : EXPORT TO PARQUET '(' paramarg_list ')' opt_export_over_clause AS SelectStmt"""
    p[0] = Expr("""ExportStmt""", """EXPORT TO PARQUET '(' paramarg_list ')' opt_export_over_clause AS SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_export_over_clause_1697(p):
    """opt_export_over_clause : over_clause"""
    p[0] = Expr("""opt_export_over_clause""", """over_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_export_over_clause_1698(p):
    """opt_export_over_clause : """
    p[0] = Expr("""opt_export_over_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_export_column_list_1699(p):
    """opt_export_column_list : '(' export_column_list ')'"""
    p[0] = Expr("""opt_export_column_list""", """'(' export_column_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_export_column_list_1700(p):
    """opt_export_column_list : """
    p[0] = Expr("""opt_export_column_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_export_column_list_1701(p):
    """export_column_list : columnref"""
    p[0] = Expr("""export_column_list""", """columnref""", p[1:] if len(p or []) > 1 else [], p)


def p_export_column_list_1702(p):
    """export_column_list : export_column_list ',' columnref"""
    p[0] = Expr("""export_column_list""", """export_column_list ',' columnref""", p[1:] if len(p or []) > 1 else [], p)


def p_export_segmentation_1703(p):
    """export_segmentation : SEGMENTED BY b_expr"""
    p[0] = Expr("""export_segmentation""", """SEGMENTED BY b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_export_segmentation_1704(p):
    """export_segmentation : """
    p[0] = Expr("""export_segmentation""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_export_target_list_1705(p):
    """opt_export_target_list : '(' target_list ')'"""
    p[0] = Expr("""opt_export_target_list""", """'(' target_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_export_target_list_1706(p):
    """opt_export_target_list : """
    p[0] = Expr("""opt_export_target_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_export_select_1707(p):
    """export_select : AS SelectStmt"""
    p[0] = Expr("""export_select""", """AS SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_export_select_1708(p):
    """export_select : AS VHistoricalSelectStmt"""
    p[0] = Expr("""export_select""", """AS VHistoricalSelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_export_select_1709(p):
    """export_select : FROM qualified_name opt_export_target_list"""
    p[0] = Expr("""export_select""", """FROM qualified_name opt_export_target_list""", p[1:] if len(p or []) > 1 else [], p)


def p_export_relation_1710(p):
    """export_relation : any_name"""
    p[0] = Expr("""export_relation""", """any_name""", p[1:] if len(p or []) > 1 else [], p)


def p_DeleteStmt_1711(p):
    """DeleteStmt : DELETE_P hint_clause FROM relation_expr where_clause"""
    p[0] = Expr("""DeleteStmt""", """DELETE_P hint_clause FROM relation_expr where_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_LockStmt_1712(p):
    """LockStmt : LOCK_P opt_table qualified_name_list opt_lock opt_nowait"""
    p[0] = Expr("""LockStmt""", """LOCK_P opt_table qualified_name_list opt_lock opt_nowait""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_lock_1713(p):
    """opt_lock : IN_P lock_type MODE"""
    p[0] = Expr("""opt_lock""", """IN_P lock_type MODE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_lock_1714(p):
    """opt_lock : """
    p[0] = Expr("""opt_lock""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_lock_type_1715(p):
    """lock_type : SHARE"""
    p[0] = Expr("""lock_type""", """SHARE""", p[1:] if len(p or []) > 1 else [], p)


def p_lock_type_1716(p):
    """lock_type : INSERT"""
    p[0] = Expr("""lock_type""", """INSERT""", p[1:] if len(p or []) > 1 else [], p)


def p_lock_type_1717(p):
    """lock_type : INSERT VALIDATE"""
    p[0] = Expr("""lock_type""", """INSERT VALIDATE""", p[1:] if len(p or []) > 1 else [], p)


def p_lock_type_1718(p):
    """lock_type : SHARE INSERT"""
    p[0] = Expr("""lock_type""", """SHARE INSERT""", p[1:] if len(p or []) > 1 else [], p)


def p_lock_type_1719(p):
    """lock_type : EXCLUSIVE"""
    p[0] = Expr("""lock_type""", """EXCLUSIVE""", p[1:] if len(p or []) > 1 else [], p)


def p_lock_type_1720(p):
    """lock_type : NOT DELETE_P"""
    p[0] = Expr("""lock_type""", """NOT DELETE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_lock_type_1721(p):
    """lock_type : USAGE"""
    p[0] = Expr("""lock_type""", """USAGE""", p[1:] if len(p or []) > 1 else [], p)


def p_lock_type_1722(p):
    """lock_type : OWNER"""
    p[0] = Expr("""lock_type""", """OWNER""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_nowait_1723(p):
    """opt_nowait : NOWAIT"""
    p[0] = Expr("""opt_nowait""", """NOWAIT""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_nowait_1724(p):
    """opt_nowait : """
    p[0] = Expr("""opt_nowait""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_UpdateStmt_1725(p):
    """UpdateStmt : UPDATE hint_clause relation_expr_opt_alias SET update_target_list from_clause where_clause"""
    p[0] = Expr("""UpdateStmt""", """UPDATE hint_clause relation_expr_opt_alias SET update_target_list from_clause where_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_DeclareCursorStmt_1726(p):
    """DeclareCursorStmt : DECLARE name cursor_options CURSOR opt_hold FOR SelectStmt"""
    p[0] = Expr("""DeclareCursorStmt""", """DECLARE name cursor_options CURSOR opt_hold FOR SelectStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_cursor_options_1727(p):
    """cursor_options : """
    p[0] = Expr("""cursor_options""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_cursor_options_1728(p):
    """cursor_options : cursor_options NO SCROLL"""
    p[0] = Expr("""cursor_options""", """cursor_options NO SCROLL""", p[1:] if len(p or []) > 1 else [], p)


def p_cursor_options_1729(p):
    """cursor_options : cursor_options SCROLL"""
    p[0] = Expr("""cursor_options""", """cursor_options SCROLL""", p[1:] if len(p or []) > 1 else [], p)


def p_cursor_options_1730(p):
    """cursor_options : cursor_options BINARY"""
    p[0] = Expr("""cursor_options""", """cursor_options BINARY""", p[1:] if len(p or []) > 1 else [], p)


def p_cursor_options_1731(p):
    """cursor_options : cursor_options INSENSITIVE"""
    p[0] = Expr("""cursor_options""", """cursor_options INSENSITIVE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_hold_1732(p):
    """opt_hold : """
    p[0] = Expr("""opt_hold""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_hold_1733(p):
    """opt_hold : WITH HOLD"""
    p[0] = Expr("""opt_hold""", """WITH HOLD""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_hold_1734(p):
    """opt_hold : WITHOUT HOLD"""
    p[0] = Expr("""opt_hold""", """WITHOUT HOLD""", p[1:] if len(p or []) > 1 else [], p)


def p_SelectStmt_1735(p):
    """SelectStmt : select_no_parens %prec UMINUS"""
    p[0] = Expr("""SelectStmt""", """select_no_parens %prec UMINUS""", p[1:] if len(p or []) > 1 else [], p)


def p_SelectStmt_1736(p):
    """SelectStmt : select_with_parens %prec UMINUS"""
    p[0] = Expr("""SelectStmt""", """select_with_parens %prec UMINUS""", p[1:] if len(p or []) > 1 else [], p)


def p_select_with_parens_1737(p):
    """select_with_parens : '(' select_no_parens ')'"""
    p[0] = Expr("""select_with_parens""", """'(' select_no_parens ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_select_with_parens_1738(p):
    """select_with_parens : '(' select_with_parens ')'"""
    p[0] = Expr("""select_with_parens""", """'(' select_with_parens ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_select_no_parens_1739(p):
    """select_no_parens : simple_select"""
    p[0] = Expr("""select_no_parens""", """simple_select""", p[1:] if len(p or []) > 1 else [], p)


def p_select_no_parens_1740(p):
    """select_no_parens : select_clause sort_clause"""
    p[0] = Expr("""select_no_parens""", """select_clause sort_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_select_no_parens_1741(p):
    """select_no_parens : select_clause opt_sort_clause for_update_clause opt_select_limit"""
    p[0] = Expr("""select_no_parens""", """select_clause opt_sort_clause for_update_clause opt_select_limit""", p[1:] if len(p or []) > 1 else [], p)


def p_select_no_parens_1742(p):
    """select_no_parens : select_clause opt_sort_clause select_limit opt_for_update_clause"""
    p[0] = Expr("""select_no_parens""", """select_clause opt_sort_clause select_limit opt_for_update_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_select_no_parens_1743(p):
    """select_no_parens : with_clause select_clause"""
    p[0] = Expr("""select_no_parens""", """with_clause select_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_select_no_parens_1744(p):
    """select_no_parens : with_clause select_clause select_limit"""
    p[0] = Expr("""select_no_parens""", """with_clause select_clause select_limit""", p[1:] if len(p or []) > 1 else [], p)


def p_select_no_parens_1745(p):
    """select_no_parens : with_clause select_clause sort_clause"""
    p[0] = Expr("""select_no_parens""", """with_clause select_clause sort_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_select_no_parens_1746(p):
    """select_no_parens : with_clause select_clause sort_clause select_limit"""
    p[0] = Expr("""select_no_parens""", """with_clause select_clause sort_clause select_limit""", p[1:] if len(p or []) > 1 else [], p)


def p_select_clause_1747(p):
    """select_clause : simple_select"""
    p[0] = Expr("""select_clause""", """simple_select""", p[1:] if len(p or []) > 1 else [], p)


def p_select_clause_1748(p):
    """select_clause : select_with_parens"""
    p[0] = Expr("""select_clause""", """select_with_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_simple_select_1749(p):
    """simple_select : SELECT hint_clause opt_distinct target_list select_clauses"""
    p[0] = Expr("""simple_select""", """SELECT hint_clause opt_distinct target_list select_clauses""", p[1:] if len(p or []) > 1 else [], p)


def p_simple_select_1750(p):
    """simple_select : select_clause UNION opt_all hint_clause select_clause"""
    p[0] = Expr("""simple_select""", """select_clause UNION opt_all hint_clause select_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_simple_select_1751(p):
    """simple_select : select_clause INTERSECT opt_all hint_clause select_clause"""
    p[0] = Expr("""simple_select""", """select_clause INTERSECT opt_all hint_clause select_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_simple_select_1752(p):
    """simple_select : select_clause EXCEPT opt_all hint_clause select_clause"""
    p[0] = Expr("""simple_select""", """select_clause EXCEPT opt_all hint_clause select_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_simple_select_1753(p):
    """simple_select : select_clause MINUS opt_all hint_clause select_clause"""
    p[0] = Expr("""simple_select""", """select_clause MINUS opt_all hint_clause select_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_with_clause_1754(p):
    """with_clause : WITH hint_clause RECURSIVE cte_list"""
    p[0] = Expr("""with_clause""", """WITH hint_clause RECURSIVE cte_list""", p[1:] if len(p or []) > 1 else [], p)


def p_with_clause_1755(p):
    """with_clause : WITH hint_clause cte_list"""
    p[0] = Expr("""with_clause""", """WITH hint_clause cte_list""", p[1:] if len(p or []) > 1 else [], p)


def p_cte_list_1756(p):
    """cte_list : common_table_expr"""
    p[0] = Expr("""cte_list""", """common_table_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_cte_list_1757(p):
    """cte_list : cte_list ',' common_table_expr"""
    p[0] = Expr("""cte_list""", """cte_list ',' common_table_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_common_table_expr_1758(p):
    """common_table_expr : name opt_name_list AS '(' SelectStmt ')'"""
    p[0] = Expr("""common_table_expr""", """name opt_name_list AS '(' SelectStmt ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_select_clauses_1759(p):
    """select_clauses : from_clause where_clause timeseries_clause group_clause having_clause window_clause pattern_clause"""
    p[0] = Expr("""select_clauses""", """from_clause where_clause timeseries_clause group_clause having_clause window_clause pattern_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_VSelectIntoStmt_1760(p):
    """VSelectIntoStmt : SelectIntoStmt"""
    p[0] = Expr("""VSelectIntoStmt""", """SelectIntoStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_VSelectIntoStmt_1761(p):
    """VSelectIntoStmt : EpochOrTime SelectIntoStmt"""
    p[0] = Expr("""VSelectIntoStmt""", """EpochOrTime SelectIntoStmt""", p[1:] if len(p or []) > 1 else [], p)


def p_SelectIntoStmt_1762(p):
    """SelectIntoStmt : simple_select_into"""
    p[0] = Expr("""SelectIntoStmt""", """simple_select_into""", p[1:] if len(p or []) > 1 else [], p)


def p_SelectIntoStmt_1763(p):
    """SelectIntoStmt : simple_select_into sort_clause"""
    p[0] = Expr("""SelectIntoStmt""", """simple_select_into sort_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_SelectIntoStmt_1764(p):
    """SelectIntoStmt : simple_select_into opt_sort_clause for_update_clause opt_select_limit"""
    p[0] = Expr("""SelectIntoStmt""", """simple_select_into opt_sort_clause for_update_clause opt_select_limit""", p[1:] if len(p or []) > 1 else [], p)


def p_SelectIntoStmt_1765(p):
    """SelectIntoStmt : simple_select_into opt_sort_clause select_limit opt_for_update_clause"""
    p[0] = Expr("""SelectIntoStmt""", """simple_select_into opt_sort_clause select_limit opt_for_update_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_simple_select_into_1766(p):
    """simple_select_into : SELECT hint_clause opt_distinct target_list INTO OptTempTableName OnCommitOption select_clauses"""
    p[0] = Expr("""simple_select_into""", """SELECT hint_clause opt_distinct target_list INTO OptTempTableName OnCommitOption select_clauses""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTempTableName_1767(p):
    """OptTempTableName : TEMPORARY opt_table qualified_name"""
    p[0] = Expr("""OptTempTableName""", """TEMPORARY opt_table qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTempTableName_1768(p):
    """OptTempTableName : TEMP opt_table qualified_name"""
    p[0] = Expr("""OptTempTableName""", """TEMP opt_table qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTempTableName_1769(p):
    """OptTempTableName : LOCAL TEMPORARY opt_table qualified_name"""
    p[0] = Expr("""OptTempTableName""", """LOCAL TEMPORARY opt_table qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTempTableName_1770(p):
    """OptTempTableName : LOCAL TEMP opt_table qualified_name"""
    p[0] = Expr("""OptTempTableName""", """LOCAL TEMP opt_table qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTempTableName_1771(p):
    """OptTempTableName : GLOBAL TEMPORARY opt_table qualified_name"""
    p[0] = Expr("""OptTempTableName""", """GLOBAL TEMPORARY opt_table qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTempTableName_1772(p):
    """OptTempTableName : GLOBAL TEMP opt_table qualified_name"""
    p[0] = Expr("""OptTempTableName""", """GLOBAL TEMP opt_table qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTempTableName_1773(p):
    """OptTempTableName : TABLE qualified_name"""
    p[0] = Expr("""OptTempTableName""", """TABLE qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_OptTempTableName_1774(p):
    """OptTempTableName : qualified_name"""
    p[0] = Expr("""OptTempTableName""", """qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_table_1775(p):
    """opt_table : TABLE"""
    p[0] = Expr("""opt_table""", """TABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_table_1776(p):
    """opt_table : """
    p[0] = Expr("""opt_table""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_all_1777(p):
    """opt_all : ALL"""
    p[0] = Expr("""opt_all""", """ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_all_1778(p):
    """opt_all : DISTINCT"""
    p[0] = Expr("""opt_all""", """DISTINCT""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_all_1779(p):
    """opt_all : """
    p[0] = Expr("""opt_all""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_distinct_1780(p):
    """opt_distinct : DISTINCT"""
    p[0] = Expr("""opt_distinct""", """DISTINCT""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_distinct_1781(p):
    """opt_distinct : DISTINCT ON '(' expr_list ')'"""
    p[0] = Expr("""opt_distinct""", """DISTINCT ON '(' expr_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_distinct_1782(p):
    """opt_distinct : ALL"""
    p[0] = Expr("""opt_distinct""", """ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_distinct_1783(p):
    """opt_distinct : """
    p[0] = Expr("""opt_distinct""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_sort_clause_1784(p):
    """opt_sort_clause : sort_clause"""
    p[0] = Expr("""opt_sort_clause""", """sort_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_sort_clause_1785(p):
    """opt_sort_clause : """
    p[0] = Expr("""opt_sort_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_sort_clause_1786(p):
    """sort_clause : ORDER BY sortby_list"""
    p[0] = Expr("""sort_clause""", """ORDER BY sortby_list""", p[1:] if len(p or []) > 1 else [], p)


def p_sortby_list_1787(p):
    """sortby_list : sortby"""
    p[0] = Expr("""sortby_list""", """sortby""", p[1:] if len(p or []) > 1 else [], p)


def p_sortby_list_1788(p):
    """sortby_list : sortby_list ',' sortby"""
    p[0] = Expr("""sortby_list""", """sortby_list ',' sortby""", p[1:] if len(p or []) > 1 else [], p)


def p_sortby_1789(p):
    """sortby : a_expr USING qual_all_Op"""
    p[0] = Expr("""sortby""", """a_expr USING qual_all_Op""", p[1:] if len(p or []) > 1 else [], p)


def p_sortby_1790(p):
    """sortby : a_expr asc_desc"""
    p[0] = Expr("""sortby""", """a_expr asc_desc""", p[1:] if len(p or []) > 1 else [], p)


def p_asc_desc_1791(p):
    """asc_desc : ASC"""
    p[0] = Expr("""asc_desc""", """ASC""", p[1:] if len(p or []) > 1 else [], p)


def p_asc_desc_1792(p):
    """asc_desc : DESC"""
    p[0] = Expr("""asc_desc""", """DESC""", p[1:] if len(p or []) > 1 else [], p)


def p_asc_desc_1793(p):
    """asc_desc : """
    p[0] = Expr("""asc_desc""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_select_limit_1794(p):
    """select_limit : LIMIT select_limit_value OFFSET select_offset_value"""
    p[0] = Expr("""select_limit""", """LIMIT select_limit_value OFFSET select_offset_value""", p[1:] if len(p or []) > 1 else [], p)


def p_select_limit_1795(p):
    """select_limit : OFFSET select_offset_value LIMIT select_limit_value"""
    p[0] = Expr("""select_limit""", """OFFSET select_offset_value LIMIT select_limit_value""", p[1:] if len(p or []) > 1 else [], p)


def p_select_limit_1796(p):
    """select_limit : LIMIT select_limit_value"""
    p[0] = Expr("""select_limit""", """LIMIT select_limit_value""", p[1:] if len(p or []) > 1 else [], p)


def p_select_limit_1797(p):
    """select_limit : OFFSET select_offset_value"""
    p[0] = Expr("""select_limit""", """OFFSET select_offset_value""", p[1:] if len(p or []) > 1 else [], p)


def p_select_limit_1798(p):
    """select_limit : LIMIT select_limit_value ',' select_offset_value"""
    p[0] = Expr("""select_limit""", """LIMIT select_limit_value ',' select_offset_value""", p[1:] if len(p or []) > 1 else [], p)


def p_select_limit_1799(p):
    """select_limit : LIMIT IntegerOnly OVER '(' partition_clause orderby_clause ')'"""
    p[0] = Expr("""select_limit""", """LIMIT IntegerOnly OVER '(' partition_clause orderby_clause ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_select_limit_1800(p):
    """opt_select_limit : select_limit"""
    p[0] = Expr("""opt_select_limit""", """select_limit""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_select_limit_1801(p):
    """opt_select_limit : """
    p[0] = Expr("""opt_select_limit""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_select_limit_value_1802(p):
    """select_limit_value : a_expr"""
    p[0] = Expr("""select_limit_value""", """a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_select_limit_value_1803(p):
    """select_limit_value : ALL"""
    p[0] = Expr("""select_limit_value""", """ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_select_offset_value_1804(p):
    """select_offset_value : a_expr"""
    p[0] = Expr("""select_offset_value""", """a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_group_clause_1805(p):
    """group_clause : GROUP_P BY hint_clause groupby_expr_list"""
    p[0] = Expr("""group_clause""", """GROUP_P BY hint_clause groupby_expr_list""", p[1:] if len(p or []) > 1 else [], p)


def p_group_clause_1806(p):
    """group_clause : """
    p[0] = Expr("""group_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_having_clause_1807(p):
    """having_clause : HAVING a_expr"""
    p[0] = Expr("""having_clause""", """HAVING a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_having_clause_1808(p):
    """having_clause : """
    p[0] = Expr("""having_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_for_update_clause_1809(p):
    """for_update_clause : FOR UPDATE update_list"""
    p[0] = Expr("""for_update_clause""", """FOR UPDATE update_list""", p[1:] if len(p or []) > 1 else [], p)


def p_for_update_clause_1810(p):
    """for_update_clause : FOR READ ONLY"""
    p[0] = Expr("""for_update_clause""", """FOR READ ONLY""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_for_update_clause_1811(p):
    """opt_for_update_clause : for_update_clause"""
    p[0] = Expr("""opt_for_update_clause""", """for_update_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_for_update_clause_1812(p):
    """opt_for_update_clause : """
    p[0] = Expr("""opt_for_update_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_update_list_1813(p):
    """update_list : OF qualified_name_list"""
    p[0] = Expr("""update_list""", """OF qualified_name_list""", p[1:] if len(p or []) > 1 else [], p)


def p_update_list_1814(p):
    """update_list : """
    p[0] = Expr("""update_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_hint_clause_1815(p):
    """hint_clause : HINT_BEGIN hint_rest"""
    p[0] = Expr("""hint_clause""", """HINT_BEGIN hint_rest""", p[1:] if len(p or []) > 1 else [], p)


def p_hint_clause_1816(p):
    """hint_clause : """
    p[0] = Expr("""hint_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_hint_rest_1817(p):
    """hint_rest : hints HINT_END"""
    p[0] = Expr("""hint_rest""", """hints HINT_END""", p[1:] if len(p or []) > 1 else [], p)


def p_hint_rest_1818(p):
    """hint_rest : error HINT_END"""
    p[0] = Expr("""hint_rest""", """error HINT_END""", p[1:] if len(p or []) > 1 else [], p)


def p_hints_1819(p):
    """hints : hint"""
    p[0] = Expr("""hints""", """hint""", p[1:] if len(p or []) > 1 else [], p)


def p_hints_1820(p):
    """hints : hints ',' hint"""
    p[0] = Expr("""hints""", """hints ',' hint""", p[1:] if len(p or []) > 1 else [], p)


def p_hint_1821(p):
    """hint : hint_name opt_hint_list"""
    p[0] = Expr("""hint""", """hint_name opt_hint_list""", p[1:] if len(p or []) > 1 else [], p)


def p_hint_1822(p):
    """hint : """
    p[0] = Expr("""hint""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_groupby_expr_list_1823(p):
    """groupby_expr_list : groupby_expr"""
    p[0] = Expr("""groupby_expr_list""", """groupby_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_groupby_expr_list_1824(p):
    """groupby_expr_list : groupby_expr_list ',' groupby_expr"""
    p[0] = Expr("""groupby_expr_list""", """groupby_expr_list ',' groupby_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_groupby_expr_1825(p):
    """groupby_expr : a_expr"""
    p[0] = Expr("""groupby_expr""", """a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_groupby_expr_1826(p):
    """groupby_expr : rollup_clause"""
    p[0] = Expr("""groupby_expr""", """rollup_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_groupby_expr_1827(p):
    """groupby_expr : cube_clause"""
    p[0] = Expr("""groupby_expr""", """cube_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_groupby_expr_1828(p):
    """groupby_expr : grouping_sets_clause"""
    p[0] = Expr("""groupby_expr""", """grouping_sets_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_rollup_clause_1829(p):
    """rollup_clause : ROLLUP '(' grouping_expr_list ')'"""
    p[0] = Expr("""rollup_clause""", """ROLLUP '(' grouping_expr_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_cube_clause_1830(p):
    """cube_clause : CUBE '(' grouping_expr_list ')'"""
    p[0] = Expr("""cube_clause""", """CUBE '(' grouping_expr_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_grouping_sets_clause_1831(p):
    """grouping_sets_clause : GROUPING SETS '(' grouping_set_expr_list ')'"""
    p[0] = Expr("""grouping_sets_clause""", """GROUPING SETS '(' grouping_set_expr_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_grouping_expr_list_1832(p):
    """grouping_expr_list : grouping_expr"""
    p[0] = Expr("""grouping_expr_list""", """grouping_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_grouping_expr_list_1833(p):
    """grouping_expr_list : grouping_expr_list ',' grouping_expr"""
    p[0] = Expr("""grouping_expr_list""", """grouping_expr_list ',' grouping_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_grouping_expr_1834(p):
    """grouping_expr : ad_expr"""
    p[0] = Expr("""grouping_expr""", """ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_grouping_expr_1835(p):
    """grouping_expr : '(' expr_list ')' _embed0_grouping_expr %prec IS"""
    p[0] = Expr("""grouping_expr""", """'(' expr_list ')' _embed0_grouping_expr %prec IS""", p[1:] if len(p or []) > 1 else [], p)


def p__embed0_grouping_expr(p):
    '''_embed0_grouping_expr : '''


def p_grouping_set_expr_list_1836(p):
    """grouping_set_expr_list : grouping_set_expr"""
    p[0] = Expr("""grouping_set_expr_list""", """grouping_set_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_grouping_set_expr_list_1837(p):
    """grouping_set_expr_list : grouping_set_expr_list ',' grouping_set_expr"""
    p[0] = Expr("""grouping_set_expr_list""", """grouping_set_expr_list ',' grouping_set_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_grouping_set_expr_1838(p):
    """grouping_set_expr : ad_expr"""
    p[0] = Expr("""grouping_set_expr""", """ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_grouping_set_expr_1839(p):
    """grouping_set_expr : rollup_clause"""
    p[0] = Expr("""grouping_set_expr""", """rollup_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_grouping_set_expr_1840(p):
    """grouping_set_expr : cube_clause"""
    p[0] = Expr("""grouping_set_expr""", """cube_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_grouping_set_expr_1841(p):
    """grouping_set_expr : '(' ')'"""
    p[0] = Expr("""grouping_set_expr""", """'(' ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_grouping_set_expr_1842(p):
    """grouping_set_expr : '(' expr_list ')' _embed0_grouping_set_expr %prec IS"""
    p[0] = Expr("""grouping_set_expr""", """'(' expr_list ')' _embed0_grouping_set_expr %prec IS""", p[1:] if len(p or []) > 1 else [], p)


def p__embed0_grouping_set_expr(p):
    '''_embed0_grouping_set_expr : '''


def p_from_clause_1843(p):
    """from_clause : FROM from_list"""
    p[0] = Expr("""from_clause""", """FROM from_list""", p[1:] if len(p or []) > 1 else [], p)


def p_from_clause_1844(p):
    """from_clause : """
    p[0] = Expr("""from_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_from_list_1845(p):
    """from_list : table_ref"""
    p[0] = Expr("""from_list""", """table_ref""", p[1:] if len(p or []) > 1 else [], p)


def p_from_list_1846(p):
    """from_list : from_list ',' table_ref"""
    p[0] = Expr("""from_list""", """from_list ',' table_ref""", p[1:] if len(p or []) > 1 else [], p)


def p_table_ref_1847(p):
    """table_ref : relation_expr hint_clause"""
    p[0] = Expr("""table_ref""", """relation_expr hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_table_ref_1848(p):
    """table_ref : relation_expr table_sample hint_clause"""
    p[0] = Expr("""table_ref""", """relation_expr table_sample hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_table_ref_1849(p):
    """table_ref : relation_expr alias_clause hint_clause"""
    p[0] = Expr("""table_ref""", """relation_expr alias_clause hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_table_ref_1850(p):
    """table_ref : relation_expr table_sample alias_clause hint_clause"""
    p[0] = Expr("""table_ref""", """relation_expr table_sample alias_clause hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_table_ref_1851(p):
    """table_ref : func_table"""
    p[0] = Expr("""table_ref""", """func_table""", p[1:] if len(p or []) > 1 else [], p)


def p_table_ref_1852(p):
    """table_ref : func_table alias_clause"""
    p[0] = Expr("""table_ref""", """func_table alias_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_table_ref_1853(p):
    """table_ref : func_table AS '(' TableFuncElementList ')'"""
    p[0] = Expr("""table_ref""", """func_table AS '(' TableFuncElementList ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_table_ref_1854(p):
    """table_ref : func_table AS ColId '(' TableFuncElementList ')'"""
    p[0] = Expr("""table_ref""", """func_table AS ColId '(' TableFuncElementList ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_table_ref_1855(p):
    """table_ref : func_table AliasColId '(' TableFuncElementList ')'"""
    p[0] = Expr("""table_ref""", """func_table AliasColId '(' TableFuncElementList ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_table_ref_1856(p):
    """table_ref : select_with_parens"""
    p[0] = Expr("""table_ref""", """select_with_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_table_ref_1857(p):
    """table_ref : select_with_parens alias_clause"""
    p[0] = Expr("""table_ref""", """select_with_parens alias_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_table_ref_1858(p):
    """table_ref : joined_table"""
    p[0] = Expr("""table_ref""", """joined_table""", p[1:] if len(p or []) > 1 else [], p)


def p_table_ref_1859(p):
    """table_ref : '(' joined_table ')' alias_clause"""
    p[0] = Expr("""table_ref""", """'(' joined_table ')' alias_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_table_sample_1860(p):
    """table_sample : TABLESAMPLE '(' FCONST ')'"""
    p[0] = Expr("""table_sample""", """TABLESAMPLE '(' FCONST ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_table_sample_1861(p):
    """table_sample : TABLESAMPLE '(' Iconst ')'"""
    p[0] = Expr("""table_sample""", """TABLESAMPLE '(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_joined_table_1862(p):
    """joined_table : '(' joined_table ')'"""
    p[0] = Expr("""joined_table""", """'(' joined_table ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_joined_table_1863(p):
    """joined_table : table_ref CROSS JOIN hint_clause table_ref"""
    p[0] = Expr("""joined_table""", """table_ref CROSS JOIN hint_clause table_ref""", p[1:] if len(p or []) > 1 else [], p)


def p_joined_table_1864(p):
    """joined_table : table_ref CROSS COMPLEX JOIN hint_clause table_ref"""
    p[0] = Expr("""joined_table""", """table_ref CROSS COMPLEX JOIN hint_clause table_ref""", p[1:] if len(p or []) > 1 else [], p)


def p_joined_table_1865(p):
    """joined_table : table_ref UNIONJOIN hint_clause table_ref"""
    p[0] = Expr("""joined_table""", """table_ref UNIONJOIN hint_clause table_ref""", p[1:] if len(p or []) > 1 else [], p)


def p_joined_table_1866(p):
    """joined_table : table_ref join_type JOIN hint_clause table_ref join_qual"""
    p[0] = Expr("""joined_table""", """table_ref join_type JOIN hint_clause table_ref join_qual""", p[1:] if len(p or []) > 1 else [], p)


def p_joined_table_1867(p):
    """joined_table : table_ref JOIN hint_clause table_ref join_qual"""
    p[0] = Expr("""joined_table""", """table_ref JOIN hint_clause table_ref join_qual""", p[1:] if len(p or []) > 1 else [], p)


def p_joined_table_1868(p):
    """joined_table : table_ref COMPLEX JOIN hint_clause table_ref join_qual"""
    p[0] = Expr("""joined_table""", """table_ref COMPLEX JOIN hint_clause table_ref join_qual""", p[1:] if len(p or []) > 1 else [], p)


def p_joined_table_1869(p):
    """joined_table : table_ref NATURAL join_type JOIN hint_clause table_ref"""
    p[0] = Expr("""joined_table""", """table_ref NATURAL join_type JOIN hint_clause table_ref""", p[1:] if len(p or []) > 1 else [], p)


def p_joined_table_1870(p):
    """joined_table : table_ref NATURAL JOIN hint_clause table_ref"""
    p[0] = Expr("""joined_table""", """table_ref NATURAL JOIN hint_clause table_ref""", p[1:] if len(p or []) > 1 else [], p)


def p_joined_table_1871(p):
    """joined_table : table_ref join_type_ext JOIN hint_clause table_ref join_qual"""
    p[0] = Expr("""joined_table""", """table_ref join_type_ext JOIN hint_clause table_ref join_qual""", p[1:] if len(p or []) > 1 else [], p)


def p_joined_table_1872(p):
    """joined_table : table_ref join_type_ext COMPLEX JOIN hint_clause table_ref join_qual"""
    p[0] = Expr("""joined_table""", """table_ref join_type_ext COMPLEX JOIN hint_clause table_ref join_qual""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_clause_1873(p):
    """alias_clause : AS ColId '(' name_list ')'"""
    p[0] = Expr("""alias_clause""", """AS ColId '(' name_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_clause_1874(p):
    """alias_clause : AS ColId"""
    p[0] = Expr("""alias_clause""", """AS ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_clause_1875(p):
    """alias_clause : AliasColId '(' name_list ')'"""
    p[0] = Expr("""alias_clause""", """AliasColId '(' name_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_clause_1876(p):
    """alias_clause : AliasColId"""
    p[0] = Expr("""alias_clause""", """AliasColId""", p[1:] if len(p or []) > 1 else [], p)


def p_join_type_1877(p):
    """join_type : FULL join_outer"""
    p[0] = Expr("""join_type""", """FULL join_outer""", p[1:] if len(p or []) > 1 else [], p)


def p_join_type_1878(p):
    """join_type : LEFT join_outer"""
    p[0] = Expr("""join_type""", """LEFT join_outer""", p[1:] if len(p or []) > 1 else [], p)


def p_join_type_1879(p):
    """join_type : RIGHT join_outer"""
    p[0] = Expr("""join_type""", """RIGHT join_outer""", p[1:] if len(p or []) > 1 else [], p)


def p_join_type_1880(p):
    """join_type : INNER_P"""
    p[0] = Expr("""join_type""", """INNER_P""", p[1:] if len(p or []) > 1 else [], p)


def p_join_outer_1881(p):
    """join_outer : OUTER_P"""
    p[0] = Expr("""join_outer""", """OUTER_P""", p[1:] if len(p or []) > 1 else [], p)


def p_join_outer_1882(p):
    """join_outer : """
    p[0] = Expr("""join_outer""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_join_type_ext_1883(p):
    """join_type_ext : SEMI"""
    p[0] = Expr("""join_type_ext""", """SEMI""", p[1:] if len(p or []) > 1 else [], p)


def p_join_type_ext_1884(p):
    """join_type_ext : LEFT SEMI"""
    p[0] = Expr("""join_type_ext""", """LEFT SEMI""", p[1:] if len(p or []) > 1 else [], p)


def p_join_type_ext_1885(p):
    """join_type_ext : ANTI"""
    p[0] = Expr("""join_type_ext""", """ANTI""", p[1:] if len(p or []) > 1 else [], p)


def p_join_type_ext_1886(p):
    """join_type_ext : LEFT ANTI"""
    p[0] = Expr("""join_type_ext""", """LEFT ANTI""", p[1:] if len(p or []) > 1 else [], p)


def p_join_type_ext_1887(p):
    """join_type_ext : SEMIALL"""
    p[0] = Expr("""join_type_ext""", """SEMIALL""", p[1:] if len(p or []) > 1 else [], p)


def p_join_type_ext_1888(p):
    """join_type_ext : LEFT SEMIALL"""
    p[0] = Expr("""join_type_ext""", """LEFT SEMIALL""", p[1:] if len(p or []) > 1 else [], p)


def p_join_type_ext_1889(p):
    """join_type_ext : NULLAWARE ANTI"""
    p[0] = Expr("""join_type_ext""", """NULLAWARE ANTI""", p[1:] if len(p or []) > 1 else [], p)


def p_join_type_ext_1890(p):
    """join_type_ext : LEFT NULLAWARE ANTI"""
    p[0] = Expr("""join_type_ext""", """LEFT NULLAWARE ANTI""", p[1:] if len(p or []) > 1 else [], p)


def p_join_type_ext_1891(p):
    """join_type_ext : UNI"""
    p[0] = Expr("""join_type_ext""", """UNI""", p[1:] if len(p or []) > 1 else [], p)


def p_join_qual_1892(p):
    """join_qual : USING '(' name_list ')'"""
    p[0] = Expr("""join_qual""", """USING '(' name_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_join_qual_1893(p):
    """join_qual : ON a_expr"""
    p[0] = Expr("""join_qual""", """ON a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_relation_expr_1894(p):
    """relation_expr : qualified_name"""
    p[0] = Expr("""relation_expr""", """qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_relation_expr_1895(p):
    """relation_expr : qualified_name '*'"""
    p[0] = Expr("""relation_expr""", """qualified_name '*'""", p[1:] if len(p or []) > 1 else [], p)


def p_relation_expr_1896(p):
    """relation_expr : ONLY qualified_name"""
    p[0] = Expr("""relation_expr""", """ONLY qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_relation_expr_1897(p):
    """relation_expr : ONLY '(' qualified_name ')'"""
    p[0] = Expr("""relation_expr""", """ONLY '(' qualified_name ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_relation_expr_opt_alias_1898(p):
    """relation_expr_opt_alias : relation_expr %prec UMINUS"""
    p[0] = Expr("""relation_expr_opt_alias""", """relation_expr %prec UMINUS""", p[1:] if len(p or []) > 1 else [], p)


def p_relation_expr_opt_alias_1899(p):
    """relation_expr_opt_alias : relation_expr ColId"""
    p[0] = Expr("""relation_expr_opt_alias""", """relation_expr ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_relation_expr_opt_alias_1900(p):
    """relation_expr_opt_alias : relation_expr AS ColId"""
    p[0] = Expr("""relation_expr_opt_alias""", """relation_expr AS ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_func_table_1901(p):
    """func_table : func_expr"""
    p[0] = Expr("""func_table""", """func_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_where_clause_1902(p):
    """where_clause : WHERE a_expr"""
    p[0] = Expr("""where_clause""", """WHERE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_where_clause_1903(p):
    """where_clause : """
    p[0] = Expr("""where_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_TableFuncElementList_1904(p):
    """TableFuncElementList : TableFuncElement"""
    p[0] = Expr("""TableFuncElementList""", """TableFuncElement""", p[1:] if len(p or []) > 1 else [], p)


def p_TableFuncElementList_1905(p):
    """TableFuncElementList : TableFuncElementList ',' TableFuncElement"""
    p[0] = Expr("""TableFuncElementList""", """TableFuncElementList ',' TableFuncElement""", p[1:] if len(p or []) > 1 else [], p)


def p_TableFuncElement_1906(p):
    """TableFuncElement : ColId Typename"""
    p[0] = Expr("""TableFuncElement""", """ColId Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_TypenameWithTypmod_1907(p):
    """TypenameWithTypmod : Typename"""
    p[0] = Expr("""TypenameWithTypmod""", """Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_TypenameWithTypmod_1908(p):
    """TypenameWithTypmod : sequencetype"""
    p[0] = Expr("""TypenameWithTypmod""", """sequencetype""", p[1:] if len(p or []) > 1 else [], p)


def p_TypenameWithTypmod_1909(p):
    """TypenameWithTypmod : sequencetype '(' IntegerOnly ')'"""
    p[0] = Expr("""TypenameWithTypmod""", """sequencetype '(' IntegerOnly ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_TypenameWithTypmod_1910(p):
    """TypenameWithTypmod : sequencetype '(' IntegerOnly ',' IntegerOnly ',' IntegerOnly ')'"""
    p[0] = Expr("""TypenameWithTypmod""", """sequencetype '(' IntegerOnly ',' IntegerOnly ',' IntegerOnly ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_TypenameWithTypmod_1911(p):
    """TypenameWithTypmod : sequencetype '(' IntegerOnly ',' IntegerOnly ')'"""
    p[0] = Expr("""TypenameWithTypmod""", """sequencetype '(' IntegerOnly ',' IntegerOnly ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_Typename_1912(p):
    """Typename : SimpleTypename opt_array_bounds"""
    p[0] = Expr("""Typename""", """SimpleTypename opt_array_bounds""", p[1:] if len(p or []) > 1 else [], p)


def p_Typename_1913(p):
    """Typename : SETOF SimpleTypename opt_array_bounds"""
    p[0] = Expr("""Typename""", """SETOF SimpleTypename opt_array_bounds""", p[1:] if len(p or []) > 1 else [], p)


def p_Typename_1914(p):
    """Typename : SimpleTypename ARRAY '[' Iconst ']'"""
    p[0] = Expr("""Typename""", """SimpleTypename ARRAY '[' Iconst ']'""", p[1:] if len(p or []) > 1 else [], p)


def p_Typename_1915(p):
    """Typename : SETOF SimpleTypename ARRAY '[' Iconst ']'"""
    p[0] = Expr("""Typename""", """SETOF SimpleTypename ARRAY '[' Iconst ']'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_array_bounds_1916(p):
    """opt_array_bounds : opt_array_bounds '[' ']'"""
    p[0] = Expr("""opt_array_bounds""", """opt_array_bounds '[' ']'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_array_bounds_1917(p):
    """opt_array_bounds : opt_array_bounds '[' Iconst ']'"""
    p[0] = Expr("""opt_array_bounds""", """opt_array_bounds '[' Iconst ']'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_array_bounds_1918(p):
    """opt_array_bounds : """
    p[0] = Expr("""opt_array_bounds""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_SimpleTypename_1919(p):
    """SimpleTypename : GenericType"""
    p[0] = Expr("""SimpleTypename""", """GenericType""", p[1:] if len(p or []) > 1 else [], p)


def p_SimpleTypename_1920(p):
    """SimpleTypename : Numeric"""
    p[0] = Expr("""SimpleTypename""", """Numeric""", p[1:] if len(p or []) > 1 else [], p)


def p_SimpleTypename_1921(p):
    """SimpleTypename : Binary"""
    p[0] = Expr("""SimpleTypename""", """Binary""", p[1:] if len(p or []) > 1 else [], p)


def p_SimpleTypename_1922(p):
    """SimpleTypename : Bit"""
    p[0] = Expr("""SimpleTypename""", """Bit""", p[1:] if len(p or []) > 1 else [], p)


def p_SimpleTypename_1923(p):
    """SimpleTypename : Character"""
    p[0] = Expr("""SimpleTypename""", """Character""", p[1:] if len(p or []) > 1 else [], p)


def p_SimpleTypename_1924(p):
    """SimpleTypename : ConstDatetime"""
    p[0] = Expr("""SimpleTypename""", """ConstDatetime""", p[1:] if len(p or []) > 1 else [], p)


def p_SimpleTypename_1925(p):
    """SimpleTypename : ConstInterval interval_qualifier"""
    p[0] = Expr("""SimpleTypename""", """ConstInterval interval_qualifier""", p[1:] if len(p or []) > 1 else [], p)


def p_SimpleTypename_1926(p):
    """SimpleTypename : ConstIntervalYM interval_qualifier"""
    p[0] = Expr("""SimpleTypename""", """ConstIntervalYM interval_qualifier""", p[1:] if len(p or []) > 1 else [], p)


def p_SimpleTypename_1927(p):
    """SimpleTypename : type_name attrs"""
    p[0] = Expr("""SimpleTypename""", """type_name attrs""", p[1:] if len(p or []) > 1 else [], p)


def p_SimpleTypename_1928(p):
    """SimpleTypename : Uuid"""
    p[0] = Expr("""SimpleTypename""", """Uuid""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstTypename_1929(p):
    """ConstTypename : GenericTypeWithoutLength"""
    p[0] = Expr("""ConstTypename""", """GenericTypeWithoutLength""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstTypename_1930(p):
    """ConstTypename : Numeric"""
    p[0] = Expr("""ConstTypename""", """Numeric""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstTypename_1931(p):
    """ConstTypename : ConstBinary"""
    p[0] = Expr("""ConstTypename""", """ConstBinary""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstTypename_1932(p):
    """ConstTypename : ConstBit"""
    p[0] = Expr("""ConstTypename""", """ConstBit""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstTypename_1933(p):
    """ConstTypename : ConstCharacter"""
    p[0] = Expr("""ConstTypename""", """ConstCharacter""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstTypename_1934(p):
    """ConstTypename : ConstDatetime"""
    p[0] = Expr("""ConstTypename""", """ConstDatetime""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstTypename_1935(p):
    """ConstTypename : Uuid"""
    p[0] = Expr("""ConstTypename""", """Uuid""", p[1:] if len(p or []) > 1 else [], p)


def p_GenericType_1936(p):
    """GenericType : GenericTypeWithLength"""
    p[0] = Expr("""GenericType""", """GenericTypeWithLength""", p[1:] if len(p or []) > 1 else [], p)


def p_GenericType_1937(p):
    """GenericType : GenericTypeWithoutLength"""
    p[0] = Expr("""GenericType""", """GenericTypeWithoutLength""", p[1:] if len(p or []) > 1 else [], p)


def p_GenericTypeWithLength_1938(p):
    """GenericTypeWithLength : type_name '(' Iconst ')'"""
    p[0] = Expr("""GenericTypeWithLength""", """type_name '(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_GenericTypeWithoutLength_1939(p):
    """GenericTypeWithoutLength : type_name"""
    p[0] = Expr("""GenericTypeWithoutLength""", """type_name""", p[1:] if len(p or []) > 1 else [], p)


def p_Numeric_1940(p):
    """Numeric : INT_P"""
    p[0] = Expr("""Numeric""", """INT_P""", p[1:] if len(p or []) > 1 else [], p)


def p_Numeric_1941(p):
    """Numeric : INTEGER"""
    p[0] = Expr("""Numeric""", """INTEGER""", p[1:] if len(p or []) > 1 else [], p)


def p_Numeric_1942(p):
    """Numeric : SMALLINT"""
    p[0] = Expr("""Numeric""", """SMALLINT""", p[1:] if len(p or []) > 1 else [], p)


def p_Numeric_1943(p):
    """Numeric : TINYINT"""
    p[0] = Expr("""Numeric""", """TINYINT""", p[1:] if len(p or []) > 1 else [], p)


def p_Numeric_1944(p):
    """Numeric : BIGINT"""
    p[0] = Expr("""Numeric""", """BIGINT""", p[1:] if len(p or []) > 1 else [], p)


def p_Numeric_1945(p):
    """Numeric : REAL"""
    p[0] = Expr("""Numeric""", """REAL""", p[1:] if len(p or []) > 1 else [], p)


def p_Numeric_1946(p):
    """Numeric : FLOAT_P opt_float"""
    p[0] = Expr("""Numeric""", """FLOAT_P opt_float""", p[1:] if len(p or []) > 1 else [], p)


def p_Numeric_1947(p):
    """Numeric : DOUBLE_P PRECISION"""
    p[0] = Expr("""Numeric""", """DOUBLE_P PRECISION""", p[1:] if len(p or []) > 1 else [], p)


def p_Numeric_1948(p):
    """Numeric : DECIMAL_P opt_decimal"""
    p[0] = Expr("""Numeric""", """DECIMAL_P opt_decimal""", p[1:] if len(p or []) > 1 else [], p)


def p_Numeric_1949(p):
    """Numeric : DEC opt_decimal"""
    p[0] = Expr("""Numeric""", """DEC opt_decimal""", p[1:] if len(p or []) > 1 else [], p)


def p_Numeric_1950(p):
    """Numeric : NUMERIC opt_numeric"""
    p[0] = Expr("""Numeric""", """NUMERIC opt_numeric""", p[1:] if len(p or []) > 1 else [], p)


def p_Numeric_1951(p):
    """Numeric : MONEY opt_numeric"""
    p[0] = Expr("""Numeric""", """MONEY opt_numeric""", p[1:] if len(p or []) > 1 else [], p)


def p_Numeric_1952(p):
    """Numeric : NUMBER_P opt_numeric"""
    p[0] = Expr("""Numeric""", """NUMBER_P opt_numeric""", p[1:] if len(p or []) > 1 else [], p)


def p_Numeric_1953(p):
    """Numeric : BOOLEAN_P"""
    p[0] = Expr("""Numeric""", """BOOLEAN_P""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_float_1954(p):
    """opt_float : '(' Iconst ')'"""
    p[0] = Expr("""opt_float""", """'(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_float_1955(p):
    """opt_float : """
    p[0] = Expr("""opt_float""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_numeric_1956(p):
    """opt_numeric : '(' Iconst ',' Iconst ')'"""
    p[0] = Expr("""opt_numeric""", """'(' Iconst ',' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_numeric_1957(p):
    """opt_numeric : '(' Iconst ')'"""
    p[0] = Expr("""opt_numeric""", """'(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_numeric_1958(p):
    """opt_numeric : """
    p[0] = Expr("""opt_numeric""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_decimal_1959(p):
    """opt_decimal : '(' Iconst ',' Iconst ')'"""
    p[0] = Expr("""opt_decimal""", """'(' Iconst ',' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_decimal_1960(p):
    """opt_decimal : '(' Iconst ')'"""
    p[0] = Expr("""opt_decimal""", """'(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_decimal_1961(p):
    """opt_decimal : """
    p[0] = Expr("""opt_decimal""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_Binary_1962(p):
    """Binary : BinaryWithLength"""
    p[0] = Expr("""Binary""", """BinaryWithLength""", p[1:] if len(p or []) > 1 else [], p)


def p_Binary_1963(p):
    """Binary : BinaryWithoutLength"""
    p[0] = Expr("""Binary""", """BinaryWithoutLength""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstBinary_1964(p):
    """ConstBinary : BinaryWithLength"""
    p[0] = Expr("""ConstBinary""", """BinaryWithLength""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstBinary_1965(p):
    """ConstBinary : BinaryWithoutLength"""
    p[0] = Expr("""ConstBinary""", """BinaryWithoutLength""", p[1:] if len(p or []) > 1 else [], p)


def p_BinaryWithLength_1966(p):
    """BinaryWithLength : binary '(' Iconst ')'"""
    p[0] = Expr("""BinaryWithLength""", """binary '(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_BinaryWithoutLength_1967(p):
    """BinaryWithoutLength : binary"""
    p[0] = Expr("""BinaryWithoutLength""", """binary""", p[1:] if len(p or []) > 1 else [], p)


def p_binary_1968(p):
    """binary : BINARY opt_varying"""
    p[0] = Expr("""binary""", """BINARY opt_varying""", p[1:] if len(p or []) > 1 else [], p)


def p_binary_1969(p):
    """binary : VARBINARY"""
    p[0] = Expr("""binary""", """VARBINARY""", p[1:] if len(p or []) > 1 else [], p)


def p_binary_1970(p):
    """binary : RAW"""
    p[0] = Expr("""binary""", """RAW""", p[1:] if len(p or []) > 1 else [], p)


def p_binary_1971(p):
    """binary : BYTEA"""
    p[0] = Expr("""binary""", """BYTEA""", p[1:] if len(p or []) > 1 else [], p)


def p_binary_1972(p):
    """binary : LONG VARBINARY"""
    p[0] = Expr("""binary""", """LONG VARBINARY""", p[1:] if len(p or []) > 1 else [], p)


def p_Bit_1973(p):
    """Bit : BitWithLength"""
    p[0] = Expr("""Bit""", """BitWithLength""", p[1:] if len(p or []) > 1 else [], p)


def p_Bit_1974(p):
    """Bit : BitWithoutLength"""
    p[0] = Expr("""Bit""", """BitWithoutLength""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstBit_1975(p):
    """ConstBit : BitWithLength"""
    p[0] = Expr("""ConstBit""", """BitWithLength""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstBit_1976(p):
    """ConstBit : BitWithoutLength"""
    p[0] = Expr("""ConstBit""", """BitWithoutLength""", p[1:] if len(p or []) > 1 else [], p)


def p_BitWithLength_1977(p):
    """BitWithLength : BIT opt_varying '(' Iconst ')'"""
    p[0] = Expr("""BitWithLength""", """BIT opt_varying '(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_BitWithoutLength_1978(p):
    """BitWithoutLength : BIT opt_varying"""
    p[0] = Expr("""BitWithoutLength""", """BIT opt_varying""", p[1:] if len(p or []) > 1 else [], p)


def p_Character_1979(p):
    """Character : CharacterWithLength"""
    p[0] = Expr("""Character""", """CharacterWithLength""", p[1:] if len(p or []) > 1 else [], p)


def p_Character_1980(p):
    """Character : CharacterWithoutLength"""
    p[0] = Expr("""Character""", """CharacterWithoutLength""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstCharacter_1981(p):
    """ConstCharacter : CharacterWithLength"""
    p[0] = Expr("""ConstCharacter""", """CharacterWithLength""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstCharacter_1982(p):
    """ConstCharacter : CharacterWithoutLength"""
    p[0] = Expr("""ConstCharacter""", """CharacterWithoutLength""", p[1:] if len(p or []) > 1 else [], p)


def p_CharacterWithLength_1983(p):
    """CharacterWithLength : character '(' Iconst ')'"""
    p[0] = Expr("""CharacterWithLength""", """character '(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_CharacterWithoutLength_1984(p):
    """CharacterWithoutLength : character"""
    p[0] = Expr("""CharacterWithoutLength""", """character""", p[1:] if len(p or []) > 1 else [], p)


def p_character_1985(p):
    """character : CHARACTER opt_varying"""
    p[0] = Expr("""character""", """CHARACTER opt_varying""", p[1:] if len(p or []) > 1 else [], p)


def p_character_1986(p):
    """character : CHAR_P opt_varying"""
    p[0] = Expr("""character""", """CHAR_P opt_varying""", p[1:] if len(p or []) > 1 else [], p)


def p_character_1987(p):
    """character : VARCHAR"""
    p[0] = Expr("""character""", """VARCHAR""", p[1:] if len(p or []) > 1 else [], p)


def p_character_1988(p):
    """character : VARCHAR2"""
    p[0] = Expr("""character""", """VARCHAR2""", p[1:] if len(p or []) > 1 else [], p)


def p_character_1989(p):
    """character : NCHAR opt_varying"""
    p[0] = Expr("""character""", """NCHAR opt_varying""", p[1:] if len(p or []) > 1 else [], p)


def p_character_1990(p):
    """character : LONG VARCHAR"""
    p[0] = Expr("""character""", """LONG VARCHAR""", p[1:] if len(p or []) > 1 else [], p)


def p_sequencetype_1991(p):
    """sequencetype : IDENTITY_P"""
    p[0] = Expr("""sequencetype""", """IDENTITY_P""", p[1:] if len(p or []) > 1 else [], p)


def p_sequencetype_1992(p):
    """sequencetype : AUTO_INC"""
    p[0] = Expr("""sequencetype""", """AUTO_INC""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_varying_1993(p):
    """opt_varying : VARYING"""
    p[0] = Expr("""opt_varying""", """VARYING""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_varying_1994(p):
    """opt_varying : """
    p[0] = Expr("""opt_varying""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstDatetime_1995(p):
    """ConstDatetime : TIMESTAMP '(' Iconst ')' opt_timezone"""
    p[0] = Expr("""ConstDatetime""", """TIMESTAMP '(' Iconst ')' opt_timezone""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstDatetime_1996(p):
    """ConstDatetime : TIMESTAMP opt_timezone"""
    p[0] = Expr("""ConstDatetime""", """TIMESTAMP opt_timezone""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstDatetime_1997(p):
    """ConstDatetime : DATETIME"""
    p[0] = Expr("""ConstDatetime""", """DATETIME""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstDatetime_1998(p):
    """ConstDatetime : SMALLDATETIME"""
    p[0] = Expr("""ConstDatetime""", """SMALLDATETIME""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstDatetime_1999(p):
    """ConstDatetime : TIMESTAMPTZ '(' Iconst ')'"""
    p[0] = Expr("""ConstDatetime""", """TIMESTAMPTZ '(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstDatetime_2000(p):
    """ConstDatetime : TIMESTAMPTZ"""
    p[0] = Expr("""ConstDatetime""", """TIMESTAMPTZ""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstDatetime_2001(p):
    """ConstDatetime : TIME '(' Iconst ')' opt_timezone"""
    p[0] = Expr("""ConstDatetime""", """TIME '(' Iconst ')' opt_timezone""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstDatetime_2002(p):
    """ConstDatetime : TIME opt_timezone"""
    p[0] = Expr("""ConstDatetime""", """TIME opt_timezone""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstDatetime_2003(p):
    """ConstDatetime : TIMETZ '(' Iconst ')'"""
    p[0] = Expr("""ConstDatetime""", """TIMETZ '(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstDatetime_2004(p):
    """ConstDatetime : TIMETZ"""
    p[0] = Expr("""ConstDatetime""", """TIMETZ""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstInterval_2005(p):
    """ConstInterval : INTERVAL"""
    p[0] = Expr("""ConstInterval""", """INTERVAL""", p[1:] if len(p or []) > 1 else [], p)


def p_ConstIntervalYM_2006(p):
    """ConstIntervalYM : INTERVALYM"""
    p[0] = Expr("""ConstIntervalYM""", """INTERVALYM""", p[1:] if len(p or []) > 1 else [], p)


def p_Uuid_2007(p):
    """Uuid : UUID"""
    p[0] = Expr("""Uuid""", """UUID""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_timezone_2008(p):
    """opt_timezone : WITH timezone"""
    p[0] = Expr("""opt_timezone""", """WITH timezone""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_timezone_2009(p):
    """opt_timezone : WITHOUT timezone"""
    p[0] = Expr("""opt_timezone""", """WITHOUT timezone""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_timezone_2010(p):
    """opt_timezone : """
    p[0] = Expr("""opt_timezone""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_minus_2011(p):
    """opt_minus : '-'"""
    p[0] = Expr("""opt_minus""", """'-'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_minus_2012(p):
    """opt_minus : '+'"""
    p[0] = Expr("""opt_minus""", """'+'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_minus_2013(p):
    """opt_minus : """
    p[0] = Expr("""opt_minus""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_leading_precision_2014(p):
    """leading_precision : '(' Iconst ')'"""
    p[0] = Expr("""leading_precision""", """'(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_leading_precision_2015(p):
    """leading_precision : """
    p[0] = Expr("""leading_precision""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_seconds_precision_2016(p):
    """seconds_precision : '(' Iconst ')'"""
    p[0] = Expr("""seconds_precision""", """'(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_seconds_precision_2017(p):
    """seconds_precision : """
    p[0] = Expr("""seconds_precision""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_interval_qualifier_2018(p):
    """interval_qualifier : YEAR_P leading_precision"""
    p[0] = Expr("""interval_qualifier""", """YEAR_P leading_precision""", p[1:] if len(p or []) > 1 else [], p)


def p_interval_qualifier_2019(p):
    """interval_qualifier : MONTH_P leading_precision"""
    p[0] = Expr("""interval_qualifier""", """MONTH_P leading_precision""", p[1:] if len(p or []) > 1 else [], p)


def p_interval_qualifier_2020(p):
    """interval_qualifier : DAY_P leading_precision"""
    p[0] = Expr("""interval_qualifier""", """DAY_P leading_precision""", p[1:] if len(p or []) > 1 else [], p)


def p_interval_qualifier_2021(p):
    """interval_qualifier : HOUR_P leading_precision"""
    p[0] = Expr("""interval_qualifier""", """HOUR_P leading_precision""", p[1:] if len(p or []) > 1 else [], p)


def p_interval_qualifier_2022(p):
    """interval_qualifier : MINUTE_P leading_precision"""
    p[0] = Expr("""interval_qualifier""", """MINUTE_P leading_precision""", p[1:] if len(p or []) > 1 else [], p)


def p_interval_qualifier_2023(p):
    """interval_qualifier : SECOND_P seconds_precision"""
    p[0] = Expr("""interval_qualifier""", """SECOND_P seconds_precision""", p[1:] if len(p or []) > 1 else [], p)


def p_interval_qualifier_2024(p):
    """interval_qualifier : YEAR_P leading_precision TO MONTH_P"""
    p[0] = Expr("""interval_qualifier""", """YEAR_P leading_precision TO MONTH_P""", p[1:] if len(p or []) > 1 else [], p)


def p_interval_qualifier_2025(p):
    """interval_qualifier : DAY_P leading_precision TO HOUR_P"""
    p[0] = Expr("""interval_qualifier""", """DAY_P leading_precision TO HOUR_P""", p[1:] if len(p or []) > 1 else [], p)


def p_interval_qualifier_2026(p):
    """interval_qualifier : DAY_P leading_precision TO MINUTE_P"""
    p[0] = Expr("""interval_qualifier""", """DAY_P leading_precision TO MINUTE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_interval_qualifier_2027(p):
    """interval_qualifier : DAY_P leading_precision TO SECOND_P seconds_precision"""
    p[0] = Expr("""interval_qualifier""", """DAY_P leading_precision TO SECOND_P seconds_precision""", p[1:] if len(p or []) > 1 else [], p)


def p_interval_qualifier_2028(p):
    """interval_qualifier : HOUR_P leading_precision TO MINUTE_P"""
    p[0] = Expr("""interval_qualifier""", """HOUR_P leading_precision TO MINUTE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_interval_qualifier_2029(p):
    """interval_qualifier : HOUR_P leading_precision TO SECOND_P seconds_precision"""
    p[0] = Expr("""interval_qualifier""", """HOUR_P leading_precision TO SECOND_P seconds_precision""", p[1:] if len(p or []) > 1 else [], p)


def p_interval_qualifier_2030(p):
    """interval_qualifier : MINUTE_P leading_precision TO SECOND_P seconds_precision"""
    p[0] = Expr("""interval_qualifier""", """MINUTE_P leading_precision TO SECOND_P seconds_precision""", p[1:] if len(p or []) > 1 else [], p)


def p_interval_qualifier_2031(p):
    """interval_qualifier : seconds_precision"""
    p[0] = Expr("""interval_qualifier""", """seconds_precision""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2032(p):
    """a_expr : c_expr"""
    p[0] = Expr("""a_expr""", """c_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2033(p):
    """a_expr : interpolate_expr"""
    p[0] = Expr("""a_expr""", """interpolate_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2034(p):
    """a_expr : a_expr TYPECAST Typename hint_clause"""
    p[0] = Expr("""a_expr""", """a_expr TYPECAST Typename hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2035(p):
    """a_expr : a_expr SOFTTYPECAST Typename hint_clause"""
    p[0] = Expr("""a_expr""", """a_expr SOFTTYPECAST Typename hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2036(p):
    """a_expr : a_expr AT timezone c_expr"""
    p[0] = Expr("""a_expr""", """a_expr AT timezone c_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2037(p):
    """a_expr : a_expr AT LOCAL"""
    p[0] = Expr("""a_expr""", """a_expr AT LOCAL""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2038(p):
    """a_expr : '+' a_expr %prec UMINUS"""
    p[0] = Expr("""a_expr""", """'+' a_expr %prec UMINUS""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2039(p):
    """a_expr : '-' a_expr %prec UMINUS"""
    p[0] = Expr("""a_expr""", """'-' a_expr %prec UMINUS""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2040(p):
    """a_expr : a_expr '+' a_expr"""
    p[0] = Expr("""a_expr""", """a_expr '+' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2041(p):
    """a_expr : a_expr '-' a_expr"""
    p[0] = Expr("""a_expr""", """a_expr '-' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2042(p):
    """a_expr : a_expr '*' a_expr"""
    p[0] = Expr("""a_expr""", """a_expr '*' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2043(p):
    """a_expr : a_expr '/' a_expr"""
    p[0] = Expr("""a_expr""", """a_expr '/' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2044(p):
    """a_expr : a_expr Op_SS a_expr"""
    p[0] = Expr("""a_expr""", """a_expr Op_SS a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2045(p):
    """a_expr : a_expr '%' a_expr"""
    p[0] = Expr("""a_expr""", """a_expr '%' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2046(p):
    """a_expr : a_expr '^' a_expr"""
    p[0] = Expr("""a_expr""", """a_expr '^' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2047(p):
    """a_expr : a_expr '<' a_expr"""
    p[0] = Expr("""a_expr""", """a_expr '<' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2048(p):
    """a_expr : a_expr '>' a_expr"""
    p[0] = Expr("""a_expr""", """a_expr '>' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2049(p):
    """a_expr : a_expr '=' a_expr"""
    p[0] = Expr("""a_expr""", """a_expr '=' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2050(p):
    """a_expr : a_expr Op_Cmp a_expr"""
    p[0] = Expr("""a_expr""", """a_expr Op_Cmp a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2051(p):
    """a_expr : a_expr '|' a_expr"""
    p[0] = Expr("""a_expr""", """a_expr '|' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2052(p):
    """a_expr : a_expr qual_Op a_expr %prec Op"""
    p[0] = Expr("""a_expr""", """a_expr qual_Op a_expr %prec Op""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2053(p):
    """a_expr : qual_Op a_expr %prec Op"""
    p[0] = Expr("""a_expr""", """qual_Op a_expr %prec Op""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2054(p):
    """a_expr : a_expr '!'"""
    p[0] = Expr("""a_expr""", """a_expr '!'""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2055(p):
    """a_expr : a_expr AND a_expr"""
    p[0] = Expr("""a_expr""", """a_expr AND a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2056(p):
    """a_expr : a_expr OR a_expr"""
    p[0] = Expr("""a_expr""", """a_expr OR a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2057(p):
    """a_expr : NOT a_expr"""
    p[0] = Expr("""a_expr""", """NOT a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2058(p):
    """a_expr : a_expr LIKE a_expr"""
    p[0] = Expr("""a_expr""", """a_expr LIKE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2059(p):
    """a_expr : a_expr NOT LIKE a_expr"""
    p[0] = Expr("""a_expr""", """a_expr NOT LIKE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2060(p):
    """a_expr : a_expr ILIKE a_expr"""
    p[0] = Expr("""a_expr""", """a_expr ILIKE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2061(p):
    """a_expr : a_expr NOT ILIKE a_expr"""
    p[0] = Expr("""a_expr""", """a_expr NOT ILIKE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2062(p):
    """a_expr : a_expr LIKE a_expr ESCAPE a_expr"""
    p[0] = Expr("""a_expr""", """a_expr LIKE a_expr ESCAPE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2063(p):
    """a_expr : a_expr NOT LIKE a_expr ESCAPE a_expr"""
    p[0] = Expr("""a_expr""", """a_expr NOT LIKE a_expr ESCAPE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2064(p):
    """a_expr : a_expr ILIKE a_expr ESCAPE a_expr"""
    p[0] = Expr("""a_expr""", """a_expr ILIKE a_expr ESCAPE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2065(p):
    """a_expr : a_expr NOT ILIKE a_expr ESCAPE a_expr"""
    p[0] = Expr("""a_expr""", """a_expr NOT ILIKE a_expr ESCAPE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2066(p):
    """a_expr : a_expr LIKEB a_expr"""
    p[0] = Expr("""a_expr""", """a_expr LIKEB a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2067(p):
    """a_expr : a_expr NOT LIKEB a_expr"""
    p[0] = Expr("""a_expr""", """a_expr NOT LIKEB a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2068(p):
    """a_expr : a_expr ILIKEB a_expr"""
    p[0] = Expr("""a_expr""", """a_expr ILIKEB a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2069(p):
    """a_expr : a_expr NOT ILIKEB a_expr"""
    p[0] = Expr("""a_expr""", """a_expr NOT ILIKEB a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2070(p):
    """a_expr : a_expr LIKEB a_expr ESCAPE a_expr"""
    p[0] = Expr("""a_expr""", """a_expr LIKEB a_expr ESCAPE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2071(p):
    """a_expr : a_expr NOT LIKEB a_expr ESCAPE a_expr"""
    p[0] = Expr("""a_expr""", """a_expr NOT LIKEB a_expr ESCAPE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2072(p):
    """a_expr : a_expr ILIKEB a_expr ESCAPE a_expr"""
    p[0] = Expr("""a_expr""", """a_expr ILIKEB a_expr ESCAPE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2073(p):
    """a_expr : a_expr NOT ILIKEB a_expr ESCAPE a_expr"""
    p[0] = Expr("""a_expr""", """a_expr NOT ILIKEB a_expr ESCAPE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2074(p):
    """a_expr : a_expr SIMILAR TO a_expr %prec SIMILAR"""
    p[0] = Expr("""a_expr""", """a_expr SIMILAR TO a_expr %prec SIMILAR""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2075(p):
    """a_expr : a_expr SIMILAR TO a_expr ESCAPE a_expr"""
    p[0] = Expr("""a_expr""", """a_expr SIMILAR TO a_expr ESCAPE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2076(p):
    """a_expr : a_expr NOT SIMILAR TO a_expr %prec SIMILAR"""
    p[0] = Expr("""a_expr""", """a_expr NOT SIMILAR TO a_expr %prec SIMILAR""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2077(p):
    """a_expr : a_expr NOT SIMILAR TO a_expr ESCAPE a_expr"""
    p[0] = Expr("""a_expr""", """a_expr NOT SIMILAR TO a_expr ESCAPE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2078(p):
    """a_expr : a_expr ISNULL"""
    p[0] = Expr("""a_expr""", """a_expr ISNULL""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2079(p):
    """a_expr : a_expr IS NULL_P"""
    p[0] = Expr("""a_expr""", """a_expr IS NULL_P""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2080(p):
    """a_expr : a_expr NOTNULL"""
    p[0] = Expr("""a_expr""", """a_expr NOTNULL""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2081(p):
    """a_expr : a_expr IS NOT NULL_P"""
    p[0] = Expr("""a_expr""", """a_expr IS NOT NULL_P""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2082(p):
    """a_expr : row OVERLAPS row"""
    p[0] = Expr("""a_expr""", """row OVERLAPS row""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2083(p):
    """a_expr : a_expr IS TRUE_P"""
    p[0] = Expr("""a_expr""", """a_expr IS TRUE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2084(p):
    """a_expr : a_expr IS NOT TRUE_P"""
    p[0] = Expr("""a_expr""", """a_expr IS NOT TRUE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2085(p):
    """a_expr : a_expr IS FALSE_P"""
    p[0] = Expr("""a_expr""", """a_expr IS FALSE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2086(p):
    """a_expr : a_expr IS NOT FALSE_P"""
    p[0] = Expr("""a_expr""", """a_expr IS NOT FALSE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2087(p):
    """a_expr : a_expr IS UNKNOWN"""
    p[0] = Expr("""a_expr""", """a_expr IS UNKNOWN""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2088(p):
    """a_expr : a_expr IS NOT UNKNOWN"""
    p[0] = Expr("""a_expr""", """a_expr IS NOT UNKNOWN""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2089(p):
    """a_expr : a_expr IS DISTINCT FROM a_expr %prec IS"""
    p[0] = Expr("""a_expr""", """a_expr IS DISTINCT FROM a_expr %prec IS""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2090(p):
    """a_expr : a_expr IS OF '(' type_list ')' %prec IS"""
    p[0] = Expr("""a_expr""", """a_expr IS OF '(' type_list ')' %prec IS""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2091(p):
    """a_expr : a_expr IS NOT OF '(' type_list ')' %prec IS"""
    p[0] = Expr("""a_expr""", """a_expr IS NOT OF '(' type_list ')' %prec IS""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2092(p):
    """a_expr : a_expr BETWEEN b_expr AND b_expr %prec BETWEEN"""
    p[0] = Expr("""a_expr""", """a_expr BETWEEN b_expr AND b_expr %prec BETWEEN""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2093(p):
    """a_expr : a_expr NOT BETWEEN b_expr AND b_expr %prec BETWEEN"""
    p[0] = Expr("""a_expr""", """a_expr NOT BETWEEN b_expr AND b_expr %prec BETWEEN""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2094(p):
    """a_expr : a_expr IN_P in_expr"""
    p[0] = Expr("""a_expr""", """a_expr IN_P in_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2095(p):
    """a_expr : a_expr NOT IN_P in_expr"""
    p[0] = Expr("""a_expr""", """a_expr NOT IN_P in_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2096(p):
    """a_expr : a_expr subquery_Op sub_type select_with_parens %prec Op"""
    p[0] = Expr("""a_expr""", """a_expr subquery_Op sub_type select_with_parens %prec Op""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2097(p):
    """a_expr : a_expr subquery_Op sub_type '(' a_expr ')' %prec Op"""
    p[0] = Expr("""a_expr""", """a_expr subquery_Op sub_type '(' a_expr ')' %prec Op""", p[1:] if len(p or []) > 1 else [], p)


def p_a_expr_2098(p):
    """a_expr : UNIQUE select_with_parens %prec Op"""
    p[0] = Expr("""a_expr""", """UNIQUE select_with_parens %prec Op""", p[1:] if len(p or []) > 1 else [], p)


def p_interpolate_expr_2099(p):
    """interpolate_expr : columnref INTERPOLATE PREVIOUS_P VALUE_P columnref"""
    p[0] = Expr("""interpolate_expr""", """columnref INTERPOLATE PREVIOUS_P VALUE_P columnref""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2100(p):
    """ad_expr : d_expr"""
    p[0] = Expr("""ad_expr""", """d_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2101(p):
    """ad_expr : interpolate_expr"""
    p[0] = Expr("""ad_expr""", """interpolate_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2102(p):
    """ad_expr : ad_expr TYPECAST Typename"""
    p[0] = Expr("""ad_expr""", """ad_expr TYPECAST Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2103(p):
    """ad_expr : ad_expr SOFTTYPECAST Typename"""
    p[0] = Expr("""ad_expr""", """ad_expr SOFTTYPECAST Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2104(p):
    """ad_expr : ad_expr AT timezone d_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr AT timezone d_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2105(p):
    """ad_expr : ad_expr AT LOCAL"""
    p[0] = Expr("""ad_expr""", """ad_expr AT LOCAL""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2106(p):
    """ad_expr : '+' ad_expr %prec UMINUS"""
    p[0] = Expr("""ad_expr""", """'+' ad_expr %prec UMINUS""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2107(p):
    """ad_expr : '-' ad_expr %prec UMINUS"""
    p[0] = Expr("""ad_expr""", """'-' ad_expr %prec UMINUS""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2108(p):
    """ad_expr : ad_expr '+' ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr '+' ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2109(p):
    """ad_expr : ad_expr '-' ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr '-' ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2110(p):
    """ad_expr : ad_expr '*' ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr '*' ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2111(p):
    """ad_expr : ad_expr '/' ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr '/' ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2112(p):
    """ad_expr : ad_expr Op_SS ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr Op_SS ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2113(p):
    """ad_expr : ad_expr '%' ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr '%' ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2114(p):
    """ad_expr : ad_expr '^' ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr '^' ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2115(p):
    """ad_expr : ad_expr '<' ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr '<' ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2116(p):
    """ad_expr : ad_expr '>' ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr '>' ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2117(p):
    """ad_expr : ad_expr '=' ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr '=' ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2118(p):
    """ad_expr : ad_expr Op_Cmp ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr Op_Cmp ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2119(p):
    """ad_expr : ad_expr '|' ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr '|' ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2120(p):
    """ad_expr : ad_expr qual_Op ad_expr %prec Op"""
    p[0] = Expr("""ad_expr""", """ad_expr qual_Op ad_expr %prec Op""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2121(p):
    """ad_expr : qual_Op ad_expr %prec Op"""
    p[0] = Expr("""ad_expr""", """qual_Op ad_expr %prec Op""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2122(p):
    """ad_expr : ad_expr '!'"""
    p[0] = Expr("""ad_expr""", """ad_expr '!'""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2123(p):
    """ad_expr : ad_expr AND ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr AND ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2124(p):
    """ad_expr : ad_expr OR ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr OR ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2125(p):
    """ad_expr : NOT ad_expr"""
    p[0] = Expr("""ad_expr""", """NOT ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2126(p):
    """ad_expr : ad_expr LIKE ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr LIKE ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2127(p):
    """ad_expr : ad_expr NOT LIKE ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr NOT LIKE ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2128(p):
    """ad_expr : ad_expr ILIKE ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr ILIKE ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2129(p):
    """ad_expr : ad_expr NOT ILIKE ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr NOT ILIKE ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2130(p):
    """ad_expr : ad_expr LIKE ad_expr ESCAPE ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr LIKE ad_expr ESCAPE ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2131(p):
    """ad_expr : ad_expr NOT LIKE ad_expr ESCAPE ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr NOT LIKE ad_expr ESCAPE ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2132(p):
    """ad_expr : ad_expr ILIKE ad_expr ESCAPE ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr ILIKE ad_expr ESCAPE ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2133(p):
    """ad_expr : ad_expr NOT ILIKE ad_expr ESCAPE ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr NOT ILIKE ad_expr ESCAPE ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2134(p):
    """ad_expr : ad_expr LIKEB ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr LIKEB ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2135(p):
    """ad_expr : ad_expr NOT LIKEB ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr NOT LIKEB ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2136(p):
    """ad_expr : ad_expr ILIKEB ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr ILIKEB ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2137(p):
    """ad_expr : ad_expr NOT ILIKEB ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr NOT ILIKEB ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2138(p):
    """ad_expr : ad_expr LIKEB ad_expr ESCAPE ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr LIKEB ad_expr ESCAPE ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2139(p):
    """ad_expr : ad_expr NOT LIKEB ad_expr ESCAPE ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr NOT LIKEB ad_expr ESCAPE ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2140(p):
    """ad_expr : ad_expr ILIKEB ad_expr ESCAPE ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr ILIKEB ad_expr ESCAPE ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2141(p):
    """ad_expr : ad_expr NOT ILIKEB ad_expr ESCAPE ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr NOT ILIKEB ad_expr ESCAPE ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2142(p):
    """ad_expr : ad_expr SIMILAR TO ad_expr %prec SIMILAR"""
    p[0] = Expr("""ad_expr""", """ad_expr SIMILAR TO ad_expr %prec SIMILAR""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2143(p):
    """ad_expr : ad_expr SIMILAR TO ad_expr ESCAPE ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr SIMILAR TO ad_expr ESCAPE ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2144(p):
    """ad_expr : ad_expr NOT SIMILAR TO ad_expr %prec SIMILAR"""
    p[0] = Expr("""ad_expr""", """ad_expr NOT SIMILAR TO ad_expr %prec SIMILAR""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2145(p):
    """ad_expr : ad_expr NOT SIMILAR TO ad_expr ESCAPE ad_expr"""
    p[0] = Expr("""ad_expr""", """ad_expr NOT SIMILAR TO ad_expr ESCAPE ad_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2146(p):
    """ad_expr : ad_expr ISNULL"""
    p[0] = Expr("""ad_expr""", """ad_expr ISNULL""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2147(p):
    """ad_expr : ad_expr IS NULL_P"""
    p[0] = Expr("""ad_expr""", """ad_expr IS NULL_P""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2148(p):
    """ad_expr : ad_expr NOTNULL"""
    p[0] = Expr("""ad_expr""", """ad_expr NOTNULL""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2149(p):
    """ad_expr : ad_expr IS NOT NULL_P"""
    p[0] = Expr("""ad_expr""", """ad_expr IS NOT NULL_P""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2150(p):
    """ad_expr : ad_expr IS TRUE_P"""
    p[0] = Expr("""ad_expr""", """ad_expr IS TRUE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2151(p):
    """ad_expr : ad_expr IS NOT TRUE_P"""
    p[0] = Expr("""ad_expr""", """ad_expr IS NOT TRUE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2152(p):
    """ad_expr : ad_expr IS FALSE_P"""
    p[0] = Expr("""ad_expr""", """ad_expr IS FALSE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2153(p):
    """ad_expr : ad_expr IS NOT FALSE_P"""
    p[0] = Expr("""ad_expr""", """ad_expr IS NOT FALSE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2154(p):
    """ad_expr : ad_expr IS UNKNOWN"""
    p[0] = Expr("""ad_expr""", """ad_expr IS UNKNOWN""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2155(p):
    """ad_expr : ad_expr IS NOT UNKNOWN"""
    p[0] = Expr("""ad_expr""", """ad_expr IS NOT UNKNOWN""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2156(p):
    """ad_expr : ad_expr IS DISTINCT FROM ad_expr %prec IS"""
    p[0] = Expr("""ad_expr""", """ad_expr IS DISTINCT FROM ad_expr %prec IS""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2157(p):
    """ad_expr : ad_expr IS OF '(' type_list ')' %prec IS"""
    p[0] = Expr("""ad_expr""", """ad_expr IS OF '(' type_list ')' %prec IS""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2158(p):
    """ad_expr : ad_expr IS NOT OF '(' type_list ')' %prec IS"""
    p[0] = Expr("""ad_expr""", """ad_expr IS NOT OF '(' type_list ')' %prec IS""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2159(p):
    """ad_expr : ad_expr BETWEEN bd_expr AND bd_expr %prec BETWEEN"""
    p[0] = Expr("""ad_expr""", """ad_expr BETWEEN bd_expr AND bd_expr %prec BETWEEN""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2160(p):
    """ad_expr : ad_expr NOT BETWEEN bd_expr AND bd_expr %prec BETWEEN"""
    p[0] = Expr("""ad_expr""", """ad_expr NOT BETWEEN bd_expr AND bd_expr %prec BETWEEN""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2161(p):
    """ad_expr : ad_expr subquery_Op sub_type select_with_parens %prec Op"""
    p[0] = Expr("""ad_expr""", """ad_expr subquery_Op sub_type select_with_parens %prec Op""", p[1:] if len(p or []) > 1 else [], p)


def p_ad_expr_2162(p):
    """ad_expr : ad_expr subquery_Op sub_type '(' ad_expr ')' %prec Op"""
    p[0] = Expr("""ad_expr""", """ad_expr subquery_Op sub_type '(' ad_expr ')' %prec Op""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2163(p):
    """b_expr : c_expr"""
    p[0] = Expr("""b_expr""", """c_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2164(p):
    """b_expr : b_expr TYPECAST Typename"""
    p[0] = Expr("""b_expr""", """b_expr TYPECAST Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2165(p):
    """b_expr : b_expr SOFTTYPECAST Typename"""
    p[0] = Expr("""b_expr""", """b_expr SOFTTYPECAST Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2166(p):
    """b_expr : '+' b_expr %prec UMINUS"""
    p[0] = Expr("""b_expr""", """'+' b_expr %prec UMINUS""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2167(p):
    """b_expr : '-' b_expr %prec UMINUS"""
    p[0] = Expr("""b_expr""", """'-' b_expr %prec UMINUS""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2168(p):
    """b_expr : b_expr '+' b_expr"""
    p[0] = Expr("""b_expr""", """b_expr '+' b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2169(p):
    """b_expr : b_expr '-' b_expr"""
    p[0] = Expr("""b_expr""", """b_expr '-' b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2170(p):
    """b_expr : b_expr '*' b_expr"""
    p[0] = Expr("""b_expr""", """b_expr '*' b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2171(p):
    """b_expr : b_expr '/' b_expr"""
    p[0] = Expr("""b_expr""", """b_expr '/' b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2172(p):
    """b_expr : b_expr Op_SS b_expr"""
    p[0] = Expr("""b_expr""", """b_expr Op_SS b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2173(p):
    """b_expr : b_expr '%' b_expr"""
    p[0] = Expr("""b_expr""", """b_expr '%' b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2174(p):
    """b_expr : b_expr '^' b_expr"""
    p[0] = Expr("""b_expr""", """b_expr '^' b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2175(p):
    """b_expr : b_expr '<' b_expr"""
    p[0] = Expr("""b_expr""", """b_expr '<' b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2176(p):
    """b_expr : b_expr '>' b_expr"""
    p[0] = Expr("""b_expr""", """b_expr '>' b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2177(p):
    """b_expr : b_expr '=' b_expr"""
    p[0] = Expr("""b_expr""", """b_expr '=' b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2178(p):
    """b_expr : b_expr Op_Cmp b_expr"""
    p[0] = Expr("""b_expr""", """b_expr Op_Cmp b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2179(p):
    """b_expr : b_expr '|' b_expr"""
    p[0] = Expr("""b_expr""", """b_expr '|' b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2180(p):
    """b_expr : b_expr qual_Op b_expr %prec Op"""
    p[0] = Expr("""b_expr""", """b_expr qual_Op b_expr %prec Op""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2181(p):
    """b_expr : qual_Op b_expr %prec Op"""
    p[0] = Expr("""b_expr""", """qual_Op b_expr %prec Op""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2182(p):
    """b_expr : b_expr '!'"""
    p[0] = Expr("""b_expr""", """b_expr '!'""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2183(p):
    """b_expr : b_expr IS DISTINCT FROM b_expr %prec IS"""
    p[0] = Expr("""b_expr""", """b_expr IS DISTINCT FROM b_expr %prec IS""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2184(p):
    """b_expr : b_expr IS OF '(' type_list ')' %prec IS"""
    p[0] = Expr("""b_expr""", """b_expr IS OF '(' type_list ')' %prec IS""", p[1:] if len(p or []) > 1 else [], p)


def p_b_expr_2185(p):
    """b_expr : b_expr IS NOT OF '(' type_list ')' %prec IS"""
    p[0] = Expr("""b_expr""", """b_expr IS NOT OF '(' type_list ')' %prec IS""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2186(p):
    """bd_expr : d_expr"""
    p[0] = Expr("""bd_expr""", """d_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2187(p):
    """bd_expr : bd_expr TYPECAST Typename"""
    p[0] = Expr("""bd_expr""", """bd_expr TYPECAST Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2188(p):
    """bd_expr : bd_expr SOFTTYPECAST Typename"""
    p[0] = Expr("""bd_expr""", """bd_expr SOFTTYPECAST Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2189(p):
    """bd_expr : '+' bd_expr %prec UMINUS"""
    p[0] = Expr("""bd_expr""", """'+' bd_expr %prec UMINUS""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2190(p):
    """bd_expr : '-' bd_expr %prec UMINUS"""
    p[0] = Expr("""bd_expr""", """'-' bd_expr %prec UMINUS""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2191(p):
    """bd_expr : bd_expr '+' bd_expr"""
    p[0] = Expr("""bd_expr""", """bd_expr '+' bd_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2192(p):
    """bd_expr : bd_expr '-' bd_expr"""
    p[0] = Expr("""bd_expr""", """bd_expr '-' bd_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2193(p):
    """bd_expr : bd_expr '*' bd_expr"""
    p[0] = Expr("""bd_expr""", """bd_expr '*' bd_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2194(p):
    """bd_expr : bd_expr '/' bd_expr"""
    p[0] = Expr("""bd_expr""", """bd_expr '/' bd_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2195(p):
    """bd_expr : bd_expr Op_SS bd_expr"""
    p[0] = Expr("""bd_expr""", """bd_expr Op_SS bd_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2196(p):
    """bd_expr : bd_expr '%' bd_expr"""
    p[0] = Expr("""bd_expr""", """bd_expr '%' bd_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2197(p):
    """bd_expr : bd_expr '^' bd_expr"""
    p[0] = Expr("""bd_expr""", """bd_expr '^' bd_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2198(p):
    """bd_expr : bd_expr '<' bd_expr"""
    p[0] = Expr("""bd_expr""", """bd_expr '<' bd_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2199(p):
    """bd_expr : bd_expr '>' bd_expr"""
    p[0] = Expr("""bd_expr""", """bd_expr '>' bd_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2200(p):
    """bd_expr : bd_expr '=' bd_expr"""
    p[0] = Expr("""bd_expr""", """bd_expr '=' bd_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2201(p):
    """bd_expr : bd_expr Op_Cmp bd_expr"""
    p[0] = Expr("""bd_expr""", """bd_expr Op_Cmp bd_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2202(p):
    """bd_expr : bd_expr '|' bd_expr"""
    p[0] = Expr("""bd_expr""", """bd_expr '|' bd_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2203(p):
    """bd_expr : bd_expr qual_Op bd_expr %prec Op"""
    p[0] = Expr("""bd_expr""", """bd_expr qual_Op bd_expr %prec Op""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2204(p):
    """bd_expr : qual_Op bd_expr %prec Op"""
    p[0] = Expr("""bd_expr""", """qual_Op bd_expr %prec Op""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2205(p):
    """bd_expr : bd_expr '!'"""
    p[0] = Expr("""bd_expr""", """bd_expr '!'""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2206(p):
    """bd_expr : bd_expr IS DISTINCT FROM bd_expr %prec IS"""
    p[0] = Expr("""bd_expr""", """bd_expr IS DISTINCT FROM bd_expr %prec IS""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2207(p):
    """bd_expr : bd_expr IS OF '(' type_list ')' %prec IS"""
    p[0] = Expr("""bd_expr""", """bd_expr IS OF '(' type_list ')' %prec IS""", p[1:] if len(p or []) > 1 else [], p)


def p_bd_expr_2208(p):
    """bd_expr : bd_expr IS NOT OF '(' type_list ')' %prec IS"""
    p[0] = Expr("""bd_expr""", """bd_expr IS NOT OF '(' type_list ')' %prec IS""", p[1:] if len(p or []) > 1 else [], p)


def p_c_expr_2209(p):
    """c_expr : columnref"""
    p[0] = Expr("""c_expr""", """columnref""", p[1:] if len(p or []) > 1 else [], p)


def p_c_expr_2210(p):
    """c_expr : AexprConst"""
    p[0] = Expr("""c_expr""", """AexprConst""", p[1:] if len(p or []) > 1 else [], p)


def p_c_expr_2211(p):
    """c_expr : PARAM opt_indirection"""
    p[0] = Expr("""c_expr""", """PARAM opt_indirection""", p[1:] if len(p or []) > 1 else [], p)


def p_c_expr_2212(p):
    """c_expr : '(' a_expr ')' indirection"""
    p[0] = Expr("""c_expr""", """'(' a_expr ')' indirection""", p[1:] if len(p or []) > 1 else [], p)


def p_c_expr_2213(p):
    """c_expr : '(' a_expr ')'"""
    p[0] = Expr("""c_expr""", """'(' a_expr ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_c_expr_2214(p):
    """c_expr : '(' a_expr '-' a_expr ')' interval_qualifier"""
    p[0] = Expr("""c_expr""", """'(' a_expr '-' a_expr ')' interval_qualifier""", p[1:] if len(p or []) > 1 else [], p)


def p_c_expr_2215(p):
    """c_expr : case_expr"""
    p[0] = Expr("""c_expr""", """case_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_c_expr_2216(p):
    """c_expr : func_expr"""
    p[0] = Expr("""c_expr""", """func_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_c_expr_2217(p):
    """c_expr : select_with_parens %prec UMINUS"""
    p[0] = Expr("""c_expr""", """select_with_parens %prec UMINUS""", p[1:] if len(p or []) > 1 else [], p)


def p_c_expr_2218(p):
    """c_expr : EXISTS select_with_parens"""
    p[0] = Expr("""c_expr""", """EXISTS select_with_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_c_expr_2219(p):
    """c_expr : ARRAY select_with_parens"""
    p[0] = Expr("""c_expr""", """ARRAY select_with_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_c_expr_2220(p):
    """c_expr : ARRAY array_expr"""
    p[0] = Expr("""c_expr""", """ARRAY array_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_c_expr_2221(p):
    """c_expr : row"""
    p[0] = Expr("""c_expr""", """row""", p[1:] if len(p or []) > 1 else [], p)


def p_d_expr_2222(p):
    """d_expr : columnref"""
    p[0] = Expr("""d_expr""", """columnref""", p[1:] if len(p or []) > 1 else [], p)


def p_d_expr_2223(p):
    """d_expr : AexprConst"""
    p[0] = Expr("""d_expr""", """AexprConst""", p[1:] if len(p or []) > 1 else [], p)


def p_d_expr_2224(p):
    """d_expr : PARAM opt_indirection"""
    p[0] = Expr("""d_expr""", """PARAM opt_indirection""", p[1:] if len(p or []) > 1 else [], p)


def p_d_expr_2225(p):
    """d_expr : '(' a_expr '-' a_expr ')' interval_qualifier"""
    p[0] = Expr("""d_expr""", """'(' a_expr '-' a_expr ')' interval_qualifier""", p[1:] if len(p or []) > 1 else [], p)


def p_d_expr_2226(p):
    """d_expr : case_expr"""
    p[0] = Expr("""d_expr""", """case_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_d_expr_2227(p):
    """d_expr : func_expr"""
    p[0] = Expr("""d_expr""", """func_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_d_expr_2228(p):
    """d_expr : select_with_parens %prec UMINUS"""
    p[0] = Expr("""d_expr""", """select_with_parens %prec UMINUS""", p[1:] if len(p or []) > 1 else [], p)


def p_d_expr_2229(p):
    """d_expr : EXISTS select_with_parens"""
    p[0] = Expr("""d_expr""", """EXISTS select_with_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_d_expr_2230(p):
    """d_expr : ARRAY select_with_parens"""
    p[0] = Expr("""d_expr""", """ARRAY select_with_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_d_expr_2231(p):
    """d_expr : ARRAY array_expr"""
    p[0] = Expr("""d_expr""", """ARRAY array_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_func_expr_2232(p):
    """func_expr : non_analytic_function"""
    p[0] = Expr("""func_expr""", """non_analytic_function""", p[1:] if len(p or []) > 1 else [], p)


def p_func_expr_2233(p):
    """func_expr : analytic_function"""
    p[0] = Expr("""func_expr""", """analytic_function""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2234(p):
    """non_analytic_function : func_name '(' ')'"""
    p[0] = Expr("""non_analytic_function""", """func_name '(' ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2235(p):
    """non_analytic_function : func_name '(' expr_list ')'"""
    p[0] = Expr("""non_analytic_function""", """func_name '(' expr_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2236(p):
    """non_analytic_function : func_name '(' ALL expr_list ')'"""
    p[0] = Expr("""non_analytic_function""", """func_name '(' ALL expr_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2237(p):
    """non_analytic_function : func_name '(' USING PARAMETERS paramarg_list ')'"""
    p[0] = Expr("""non_analytic_function""", """func_name '(' USING PARAMETERS paramarg_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2238(p):
    """non_analytic_function : func_name '(' expr_list USING PARAMETERS paramarg_list ')'"""
    p[0] = Expr("""non_analytic_function""", """func_name '(' expr_list USING PARAMETERS paramarg_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2239(p):
    """non_analytic_function : func_name '(' DISTINCT expr_list USING PARAMETERS paramarg_list ')'"""
    p[0] = Expr("""non_analytic_function""", """func_name '(' DISTINCT expr_list USING PARAMETERS paramarg_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2240(p):
    """non_analytic_function : func_name '(' '*' USING PARAMETERS paramarg_list ')'"""
    p[0] = Expr("""non_analytic_function""", """func_name '(' '*' USING PARAMETERS paramarg_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2241(p):
    """non_analytic_function : func_name '(' DISTINCT expr_list ')'"""
    p[0] = Expr("""non_analytic_function""", """func_name '(' DISTINCT expr_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2242(p):
    """non_analytic_function : func_name '(' expr_list IGNORE NULLS ')'"""
    p[0] = Expr("""non_analytic_function""", """func_name '(' expr_list IGNORE NULLS ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2243(p):
    """non_analytic_function : func_name '(' expr_list IGNORE NULLS ',' a_expr ')'"""
    p[0] = Expr("""non_analytic_function""", """func_name '(' expr_list IGNORE NULLS ',' a_expr ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2244(p):
    """non_analytic_function : func_name '(' '*' ')'"""
    p[0] = Expr("""non_analytic_function""", """func_name '(' '*' ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2245(p):
    """non_analytic_function : CURRENT_DATE opt_parens"""
    p[0] = Expr("""non_analytic_function""", """CURRENT_DATE opt_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2246(p):
    """non_analytic_function : CURRENT_TIME"""
    p[0] = Expr("""non_analytic_function""", """CURRENT_TIME""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2247(p):
    """non_analytic_function : CURRENT_TIME '(' Iconst ')'"""
    p[0] = Expr("""non_analytic_function""", """CURRENT_TIME '(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2248(p):
    """non_analytic_function : CURRENT_TIMESTAMP"""
    p[0] = Expr("""non_analytic_function""", """CURRENT_TIMESTAMP""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2249(p):
    """non_analytic_function : CURRENT_TIMESTAMP '(' Iconst ')'"""
    p[0] = Expr("""non_analytic_function""", """CURRENT_TIMESTAMP '(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2250(p):
    """non_analytic_function : LOCALTIME"""
    p[0] = Expr("""non_analytic_function""", """LOCALTIME""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2251(p):
    """non_analytic_function : LOCALTIME '(' Iconst ')'"""
    p[0] = Expr("""non_analytic_function""", """LOCALTIME '(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2252(p):
    """non_analytic_function : LOCALTIMESTAMP"""
    p[0] = Expr("""non_analytic_function""", """LOCALTIMESTAMP""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2253(p):
    """non_analytic_function : LOCALTIMESTAMP '(' Iconst ')'"""
    p[0] = Expr("""non_analytic_function""", """LOCALTIMESTAMP '(' Iconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2254(p):
    """non_analytic_function : CURRENT_DATABASE opt_parens"""
    p[0] = Expr("""non_analytic_function""", """CURRENT_DATABASE opt_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2255(p):
    """non_analytic_function : CURRENT_SCHEMA opt_parens"""
    p[0] = Expr("""non_analytic_function""", """CURRENT_SCHEMA opt_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2256(p):
    """non_analytic_function : CURRENT_USER opt_parens"""
    p[0] = Expr("""non_analytic_function""", """CURRENT_USER opt_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2257(p):
    """non_analytic_function : SESSION_USER opt_parens"""
    p[0] = Expr("""non_analytic_function""", """SESSION_USER opt_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2258(p):
    """non_analytic_function : SYSDATE opt_parens"""
    p[0] = Expr("""non_analytic_function""", """SYSDATE opt_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2259(p):
    """non_analytic_function : USER opt_parens"""
    p[0] = Expr("""non_analytic_function""", """USER opt_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2260(p):
    """non_analytic_function : CAST '(' a_expr AS Typename ')'"""
    p[0] = Expr("""non_analytic_function""", """CAST '(' a_expr AS Typename ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2261(p):
    """non_analytic_function : DATEDIFF '(' datediff_list ')'"""
    p[0] = Expr("""non_analytic_function""", """DATEDIFF '(' datediff_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2262(p):
    """non_analytic_function : EXTRACT '(' extract_list ')'"""
    p[0] = Expr("""non_analytic_function""", """EXTRACT '(' extract_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2263(p):
    """non_analytic_function : CHAR_LENGTH '(' a_expr using_octets ')'"""
    p[0] = Expr("""non_analytic_function""", """CHAR_LENGTH '(' a_expr using_octets ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2264(p):
    """non_analytic_function : CHARACTER_LENGTH '(' a_expr using_octets ')'"""
    p[0] = Expr("""non_analytic_function""", """CHARACTER_LENGTH '(' a_expr using_octets ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2265(p):
    """non_analytic_function : OVERLAY '(' overlay_list using_octets ')'"""
    p[0] = Expr("""non_analytic_function""", """OVERLAY '(' overlay_list using_octets ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2266(p):
    """non_analytic_function : POSITION '(' position_list using_octets ')'"""
    p[0] = Expr("""non_analytic_function""", """POSITION '(' position_list using_octets ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2267(p):
    """non_analytic_function : SUBSTRING '(' substr_list using_octets ')'"""
    p[0] = Expr("""non_analytic_function""", """SUBSTRING '(' substr_list using_octets ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2268(p):
    """non_analytic_function : TIMESTAMPADD '(' datediff_list ')'"""
    p[0] = Expr("""non_analytic_function""", """TIMESTAMPADD '(' datediff_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2269(p):
    """non_analytic_function : TIMESTAMPDIFF '(' datediff_list ')'"""
    p[0] = Expr("""non_analytic_function""", """TIMESTAMPDIFF '(' datediff_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2270(p):
    """non_analytic_function : TREAT '(' a_expr AS Typename ')'"""
    p[0] = Expr("""non_analytic_function""", """TREAT '(' a_expr AS Typename ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2271(p):
    """non_analytic_function : TRIM '(' BOTH trim_list ')'"""
    p[0] = Expr("""non_analytic_function""", """TRIM '(' BOTH trim_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2272(p):
    """non_analytic_function : TRIM '(' LEADING trim_list ')'"""
    p[0] = Expr("""non_analytic_function""", """TRIM '(' LEADING trim_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2273(p):
    """non_analytic_function : TRIM '(' TRAILING trim_list ')'"""
    p[0] = Expr("""non_analytic_function""", """TRIM '(' TRAILING trim_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2274(p):
    """non_analytic_function : TRIM '(' trim_list ')'"""
    p[0] = Expr("""non_analytic_function""", """TRIM '(' trim_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_non_analytic_function_2275(p):
    """non_analytic_function : DECODE '(' a_expr ',' decode_search_result_list decode_default ')'"""
    p[0] = Expr("""non_analytic_function""", """DECODE '(' a_expr ',' decode_search_result_list decode_default ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_parens_2276(p):
    """opt_parens : '(' ')'"""
    p[0] = Expr("""opt_parens""", """'(' ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_parens_2277(p):
    """opt_parens : """
    p[0] = Expr("""opt_parens""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_paramarg_2278(p):
    """paramarg : name '=' a_expr"""
    p[0] = Expr("""paramarg""", """name '=' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_paramarg_list_2279(p):
    """paramarg_list : paramarg"""
    p[0] = Expr("""paramarg_list""", """paramarg""", p[1:] if len(p or []) > 1 else [], p)


def p_paramarg_list_2280(p):
    """paramarg_list : paramarg_list ',' paramarg"""
    p[0] = Expr("""paramarg_list""", """paramarg_list ',' paramarg""", p[1:] if len(p or []) > 1 else [], p)


def p_load_function_2281(p):
    """load_function : func_name '(' PARAMETERS Sconst ')'"""
    p[0] = Expr("""load_function""", """func_name '(' PARAMETERS Sconst ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_load_function_2282(p):
    """load_function : func_name '(' paramarg_list ')'"""
    p[0] = Expr("""load_function""", """func_name '(' paramarg_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_load_function_2283(p):
    """load_function : func_name '(' ')'"""
    p[0] = Expr("""load_function""", """func_name '(' ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_row_2284(p):
    """row : ROW '(' expr_list ')'"""
    p[0] = Expr("""row""", """ROW '(' expr_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_row_2285(p):
    """row : ROW '(' ')'"""
    p[0] = Expr("""row""", """ROW '(' ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_row_2286(p):
    """row : '(' expr_list ',' a_expr ')'"""
    p[0] = Expr("""row""", """'(' expr_list ',' a_expr ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_sub_type_2287(p):
    """sub_type : ANY"""
    p[0] = Expr("""sub_type""", """ANY""", p[1:] if len(p or []) > 1 else [], p)


def p_sub_type_2288(p):
    """sub_type : SOME"""
    p[0] = Expr("""sub_type""", """SOME""", p[1:] if len(p or []) > 1 else [], p)


def p_sub_type_2289(p):
    """sub_type : ALL"""
    p[0] = Expr("""sub_type""", """ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_all_Op_2290(p):
    """all_Op : Op"""
    p[0] = Expr("""all_Op""", """Op""", p[1:] if len(p or []) > 1 else [], p)


def p_all_Op_2291(p):
    """all_Op : MathOp"""
    p[0] = Expr("""all_Op""", """MathOp""", p[1:] if len(p or []) > 1 else [], p)


def p_MathOp_2292(p):
    """MathOp : '+'"""
    p[0] = Expr("""MathOp""", """'+'""", p[1:] if len(p or []) > 1 else [], p)


def p_MathOp_2293(p):
    """MathOp : '-'"""
    p[0] = Expr("""MathOp""", """'-'""", p[1:] if len(p or []) > 1 else [], p)


def p_MathOp_2294(p):
    """MathOp : '*'"""
    p[0] = Expr("""MathOp""", """'*'""", p[1:] if len(p or []) > 1 else [], p)


def p_MathOp_2295(p):
    """MathOp : '/'"""
    p[0] = Expr("""MathOp""", """'/'""", p[1:] if len(p or []) > 1 else [], p)


def p_MathOp_2296(p):
    """MathOp : Op_SS"""
    p[0] = Expr("""MathOp""", """Op_SS""", p[1:] if len(p or []) > 1 else [], p)


def p_MathOp_2297(p):
    """MathOp : '%'"""
    p[0] = Expr("""MathOp""", """'%'""", p[1:] if len(p or []) > 1 else [], p)


def p_MathOp_2298(p):
    """MathOp : '^'"""
    p[0] = Expr("""MathOp""", """'^'""", p[1:] if len(p or []) > 1 else [], p)


def p_MathOp_2299(p):
    """MathOp : '<'"""
    p[0] = Expr("""MathOp""", """'<'""", p[1:] if len(p or []) > 1 else [], p)


def p_MathOp_2300(p):
    """MathOp : '>'"""
    p[0] = Expr("""MathOp""", """'>'""", p[1:] if len(p or []) > 1 else [], p)


def p_MathOp_2301(p):
    """MathOp : '='"""
    p[0] = Expr("""MathOp""", """'='""", p[1:] if len(p or []) > 1 else [], p)


def p_MathOp_2302(p):
    """MathOp : Op_Cmp"""
    p[0] = Expr("""MathOp""", """Op_Cmp""", p[1:] if len(p or []) > 1 else [], p)


def p_qual_Op_2303(p):
    """qual_Op : Op"""
    p[0] = Expr("""qual_Op""", """Op""", p[1:] if len(p or []) > 1 else [], p)


def p_qual_Op_2304(p):
    """qual_Op : OPERATOR '(' any_operator ')'"""
    p[0] = Expr("""qual_Op""", """OPERATOR '(' any_operator ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_qual_all_Op_2305(p):
    """qual_all_Op : all_Op"""
    p[0] = Expr("""qual_all_Op""", """all_Op""", p[1:] if len(p or []) > 1 else [], p)


def p_qual_all_Op_2306(p):
    """qual_all_Op : OPERATOR '(' any_operator ')'"""
    p[0] = Expr("""qual_all_Op""", """OPERATOR '(' any_operator ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_subquery_Op_2307(p):
    """subquery_Op : all_Op"""
    p[0] = Expr("""subquery_Op""", """all_Op""", p[1:] if len(p or []) > 1 else [], p)


def p_subquery_Op_2308(p):
    """subquery_Op : OPERATOR '(' any_operator ')'"""
    p[0] = Expr("""subquery_Op""", """OPERATOR '(' any_operator ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_subquery_Op_2309(p):
    """subquery_Op : LIKE"""
    p[0] = Expr("""subquery_Op""", """LIKE""", p[1:] if len(p or []) > 1 else [], p)


def p_subquery_Op_2310(p):
    """subquery_Op : NOT LIKE"""
    p[0] = Expr("""subquery_Op""", """NOT LIKE""", p[1:] if len(p or []) > 1 else [], p)


def p_subquery_Op_2311(p):
    """subquery_Op : ILIKE"""
    p[0] = Expr("""subquery_Op""", """ILIKE""", p[1:] if len(p or []) > 1 else [], p)


def p_subquery_Op_2312(p):
    """subquery_Op : NOT ILIKE"""
    p[0] = Expr("""subquery_Op""", """NOT ILIKE""", p[1:] if len(p or []) > 1 else [], p)


def p_subquery_Op_2313(p):
    """subquery_Op : LIKEB"""
    p[0] = Expr("""subquery_Op""", """LIKEB""", p[1:] if len(p or []) > 1 else [], p)


def p_subquery_Op_2314(p):
    """subquery_Op : NOT LIKEB"""
    p[0] = Expr("""subquery_Op""", """NOT LIKEB""", p[1:] if len(p or []) > 1 else [], p)


def p_subquery_Op_2315(p):
    """subquery_Op : ILIKEB"""
    p[0] = Expr("""subquery_Op""", """ILIKEB""", p[1:] if len(p or []) > 1 else [], p)


def p_subquery_Op_2316(p):
    """subquery_Op : NOT ILIKEB"""
    p[0] = Expr("""subquery_Op""", """NOT ILIKEB""", p[1:] if len(p or []) > 1 else [], p)


def p_expr_list_2317(p):
    """expr_list : a_expr"""
    p[0] = Expr("""expr_list""", """a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_expr_list_2318(p):
    """expr_list : expr_list ',' a_expr"""
    p[0] = Expr("""expr_list""", """expr_list ',' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_datediff_list_2319(p):
    """datediff_list : extract_arg ',' expr_list"""
    p[0] = Expr("""datediff_list""", """extract_arg ',' expr_list""", p[1:] if len(p or []) > 1 else [], p)


def p_datediff_list_2320(p):
    """datediff_list : '(' a_expr ')' ',' expr_list"""
    p[0] = Expr("""datediff_list""", """'(' a_expr ')' ',' expr_list""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_list_2321(p):
    """extract_list : extract_arg FROM a_expr"""
    p[0] = Expr("""extract_list""", """extract_arg FROM a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_type_list_2322(p):
    """type_list : type_list ',' Typename"""
    p[0] = Expr("""type_list""", """type_list ',' Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_type_list_2323(p):
    """type_list : Typename"""
    p[0] = Expr("""type_list""", """Typename""", p[1:] if len(p or []) > 1 else [], p)


def p_array_expr_list_2324(p):
    """array_expr_list : array_expr"""
    p[0] = Expr("""array_expr_list""", """array_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_array_expr_list_2325(p):
    """array_expr_list : array_expr_list ',' array_expr"""
    p[0] = Expr("""array_expr_list""", """array_expr_list ',' array_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_array_expr_2326(p):
    """array_expr : '[' expr_list ']'"""
    p[0] = Expr("""array_expr""", """'[' expr_list ']'""", p[1:] if len(p or []) > 1 else [], p)


def p_array_expr_2327(p):
    """array_expr : '[' array_expr_list ']'"""
    p[0] = Expr("""array_expr""", """'[' array_expr_list ']'""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2328(p):
    """extract_arg : IDENT"""
    p[0] = Expr("""extract_arg""", """IDENT""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2329(p):
    """extract_arg : DAY_P"""
    p[0] = Expr("""extract_arg""", """DAY_P""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2330(p):
    """extract_arg : DEC"""
    p[0] = Expr("""extract_arg""", """DEC""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2331(p):
    """extract_arg : EPOCH_P"""
    p[0] = Expr("""extract_arg""", """EPOCH_P""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2332(p):
    """extract_arg : HOUR_P"""
    p[0] = Expr("""extract_arg""", """HOUR_P""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2333(p):
    """extract_arg : HOURS_P"""
    p[0] = Expr("""extract_arg""", """HOURS_P""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2334(p):
    """extract_arg : MICROSECONDS_P"""
    p[0] = Expr("""extract_arg""", """MICROSECONDS_P""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2335(p):
    """extract_arg : MILLISECONDS_P"""
    p[0] = Expr("""extract_arg""", """MILLISECONDS_P""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2336(p):
    """extract_arg : MINUTE_P"""
    p[0] = Expr("""extract_arg""", """MINUTE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2337(p):
    """extract_arg : MINUTES_P"""
    p[0] = Expr("""extract_arg""", """MINUTES_P""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2338(p):
    """extract_arg : MONTH_P"""
    p[0] = Expr("""extract_arg""", """MONTH_P""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2339(p):
    """extract_arg : SECOND_P"""
    p[0] = Expr("""extract_arg""", """SECOND_P""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2340(p):
    """extract_arg : SECONDS_P"""
    p[0] = Expr("""extract_arg""", """SECONDS_P""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2341(p):
    """extract_arg : timezone"""
    p[0] = Expr("""extract_arg""", """timezone""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2342(p):
    """extract_arg : YEAR_P"""
    p[0] = Expr("""extract_arg""", """YEAR_P""", p[1:] if len(p or []) > 1 else [], p)


def p_extract_arg_2343(p):
    """extract_arg : SCONST"""
    p[0] = Expr("""extract_arg""", """SCONST""", p[1:] if len(p or []) > 1 else [], p)


def p_overlay_list_2344(p):
    """overlay_list : a_expr overlay_placing substr_from substr_for"""
    p[0] = Expr("""overlay_list""", """a_expr overlay_placing substr_from substr_for""", p[1:] if len(p or []) > 1 else [], p)


def p_overlay_list_2345(p):
    """overlay_list : a_expr overlay_placing substr_from"""
    p[0] = Expr("""overlay_list""", """a_expr overlay_placing substr_from""", p[1:] if len(p or []) > 1 else [], p)


def p_overlay_placing_2346(p):
    """overlay_placing : PLACING a_expr"""
    p[0] = Expr("""overlay_placing""", """PLACING a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_position_list_2347(p):
    """position_list : b_expr IN_P b_expr"""
    p[0] = Expr("""position_list""", """b_expr IN_P b_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_position_list_2348(p):
    """position_list : """
    p[0] = Expr("""position_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_decode_search_result_list_2349(p):
    """decode_search_result_list : decode_search_result"""
    p[0] = Expr("""decode_search_result_list""", """decode_search_result""", p[1:] if len(p or []) > 1 else [], p)


def p_decode_search_result_list_2350(p):
    """decode_search_result_list : decode_search_result_list ',' decode_search_result"""
    p[0] = Expr("""decode_search_result_list""", """decode_search_result_list ',' decode_search_result""", p[1:] if len(p or []) > 1 else [], p)


def p_decode_search_result_2351(p):
    """decode_search_result : a_expr ',' a_expr"""
    p[0] = Expr("""decode_search_result""", """a_expr ',' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_decode_default_2352(p):
    """decode_default : ',' a_expr"""
    p[0] = Expr("""decode_default""", """',' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_decode_default_2353(p):
    """decode_default : """
    p[0] = Expr("""decode_default""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_substr_list_2354(p):
    """substr_list : a_expr substr_from substr_for"""
    p[0] = Expr("""substr_list""", """a_expr substr_from substr_for""", p[1:] if len(p or []) > 1 else [], p)


def p_substr_list_2355(p):
    """substr_list : a_expr substr_for substr_from"""
    p[0] = Expr("""substr_list""", """a_expr substr_for substr_from""", p[1:] if len(p or []) > 1 else [], p)


def p_substr_list_2356(p):
    """substr_list : a_expr substr_from"""
    p[0] = Expr("""substr_list""", """a_expr substr_from""", p[1:] if len(p or []) > 1 else [], p)


def p_substr_list_2357(p):
    """substr_list : a_expr substr_for"""
    p[0] = Expr("""substr_list""", """a_expr substr_for""", p[1:] if len(p or []) > 1 else [], p)


def p_substr_list_2358(p):
    """substr_list : expr_list"""
    p[0] = Expr("""substr_list""", """expr_list""", p[1:] if len(p or []) > 1 else [], p)


def p_substr_list_2359(p):
    """substr_list : """
    p[0] = Expr("""substr_list""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_substr_from_2360(p):
    """substr_from : FROM a_expr"""
    p[0] = Expr("""substr_from""", """FROM a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_substr_for_2361(p):
    """substr_for : FOR a_expr"""
    p[0] = Expr("""substr_for""", """FOR a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_using_octets_2362(p):
    """using_octets : USING OCTETS"""
    p[0] = Expr("""using_octets""", """USING OCTETS""", p[1:] if len(p or []) > 1 else [], p)


def p_using_octets_2363(p):
    """using_octets : USING CHARACTERS"""
    p[0] = Expr("""using_octets""", """USING CHARACTERS""", p[1:] if len(p or []) > 1 else [], p)


def p_using_octets_2364(p):
    """using_octets : """
    p[0] = Expr("""using_octets""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_trim_list_2365(p):
    """trim_list : a_expr FROM expr_list"""
    p[0] = Expr("""trim_list""", """a_expr FROM expr_list""", p[1:] if len(p or []) > 1 else [], p)


def p_trim_list_2366(p):
    """trim_list : FROM expr_list"""
    p[0] = Expr("""trim_list""", """FROM expr_list""", p[1:] if len(p or []) > 1 else [], p)


def p_trim_list_2367(p):
    """trim_list : a_expr"""
    p[0] = Expr("""trim_list""", """a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_in_expr_2368(p):
    """in_expr : select_with_parens"""
    p[0] = Expr("""in_expr""", """select_with_parens""", p[1:] if len(p or []) > 1 else [], p)


def p_in_expr_2369(p):
    """in_expr : '(' expr_list ')'"""
    p[0] = Expr("""in_expr""", """'(' expr_list ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_case_expr_2370(p):
    """case_expr : CASE case_arg when_clause_list case_default END_P"""
    p[0] = Expr("""case_expr""", """CASE case_arg when_clause_list case_default END_P""", p[1:] if len(p or []) > 1 else [], p)


def p_when_clause_list_2371(p):
    """when_clause_list : when_clause"""
    p[0] = Expr("""when_clause_list""", """when_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_when_clause_list_2372(p):
    """when_clause_list : when_clause_list when_clause"""
    p[0] = Expr("""when_clause_list""", """when_clause_list when_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_when_clause_2373(p):
    """when_clause : WHEN nullsequal a_expr THEN a_expr"""
    p[0] = Expr("""when_clause""", """WHEN nullsequal a_expr THEN a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_case_default_2374(p):
    """case_default : ELSE a_expr"""
    p[0] = Expr("""case_default""", """ELSE a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_case_default_2375(p):
    """case_default : """
    p[0] = Expr("""case_default""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_case_arg_2376(p):
    """case_arg : a_expr"""
    p[0] = Expr("""case_arg""", """a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_case_arg_2377(p):
    """case_arg : """
    p[0] = Expr("""case_arg""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_nullsequal_2378(p):
    """nullsequal : NULLSEQUAL"""
    p[0] = Expr("""nullsequal""", """NULLSEQUAL""", p[1:] if len(p or []) > 1 else [], p)


def p_nullsequal_2379(p):
    """nullsequal : """
    p[0] = Expr("""nullsequal""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_columnref_2380(p):
    """columnref : relation_name"""
    p[0] = Expr("""columnref""", """relation_name""", p[1:] if len(p or []) > 1 else [], p)


def p_columnref_2381(p):
    """columnref : relation_name indirection"""
    p[0] = Expr("""columnref""", """relation_name indirection""", p[1:] if len(p or []) > 1 else [], p)


def p_indirection_el_2382(p):
    """indirection_el : '.' attr_name"""
    p[0] = Expr("""indirection_el""", """'.' attr_name""", p[1:] if len(p or []) > 1 else [], p)


def p_indirection_el_2383(p):
    """indirection_el : '.' '*'"""
    p[0] = Expr("""indirection_el""", """'.' '*'""", p[1:] if len(p or []) > 1 else [], p)


def p_indirection_el_2384(p):
    """indirection_el : '[' a_expr ']'"""
    p[0] = Expr("""indirection_el""", """'[' a_expr ']'""", p[1:] if len(p or []) > 1 else [], p)


def p_indirection_el_2385(p):
    """indirection_el : '[' a_expr ':' a_expr ']'"""
    p[0] = Expr("""indirection_el""", """'[' a_expr ':' a_expr ']'""", p[1:] if len(p or []) > 1 else [], p)


def p_indirection_2386(p):
    """indirection : indirection_el"""
    p[0] = Expr("""indirection""", """indirection_el""", p[1:] if len(p or []) > 1 else [], p)


def p_indirection_2387(p):
    """indirection : indirection indirection_el"""
    p[0] = Expr("""indirection""", """indirection indirection_el""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_indirection_2388(p):
    """opt_indirection : """
    p[0] = Expr("""opt_indirection""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_indirection_2389(p):
    """opt_indirection : opt_indirection indirection_el"""
    p[0] = Expr("""opt_indirection""", """opt_indirection indirection_el""", p[1:] if len(p or []) > 1 else [], p)


def p_target_list_2390(p):
    """target_list : target_el"""
    p[0] = Expr("""target_list""", """target_el""", p[1:] if len(p or []) > 1 else [], p)


def p_target_list_2391(p):
    """target_list : target_list ',' target_el"""
    p[0] = Expr("""target_list""", """target_list ',' target_el""", p[1:] if len(p or []) > 1 else [], p)


def p_target_el_2392(p):
    """target_el : a_expr AS ColLabel"""
    p[0] = Expr("""target_el""", """a_expr AS ColLabel""", p[1:] if len(p or []) > 1 else [], p)


def p_target_el_2393(p):
    """target_el : a_expr BareColLabel"""
    p[0] = Expr("""target_el""", """a_expr BareColLabel""", p[1:] if len(p or []) > 1 else [], p)


def p_target_el_2394(p):
    """target_el : a_expr"""
    p[0] = Expr("""target_el""", """a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_target_el_2395(p):
    """target_el : '*'"""
    p[0] = Expr("""target_el""", """'*'""", p[1:] if len(p or []) > 1 else [], p)


def p_target_el_2396(p):
    """target_el : a_expr AS '(' columnList ')'"""
    p[0] = Expr("""target_el""", """a_expr AS '(' columnList ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_timeseries_clause_2397(p):
    """timeseries_clause : TIMESERIES ColId AS AexprConst OVER '(' opt_partition_clause ORDER BY a_expr ')'"""
    p[0] = Expr("""timeseries_clause""", """TIMESERIES ColId AS AexprConst OVER '(' opt_partition_clause ORDER BY a_expr ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_timeseries_clause_2398(p):
    """timeseries_clause : """
    p[0] = Expr("""timeseries_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_clause_2399(p):
    """pattern_clause : MATCH '(' opt_partition_clause orderby_clause pattern_define_clause pattern_in_clause pattern_match_options_clause pattern_results_clause ')'"""
    p[0] = Expr("""pattern_clause""", """MATCH '(' opt_partition_clause orderby_clause pattern_define_clause pattern_in_clause pattern_match_options_clause pattern_results_clause ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_clause_2400(p):
    """pattern_clause : """
    p[0] = Expr("""pattern_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_define_clause_2401(p):
    """pattern_define_clause : DEFINE event_definition_list"""
    p[0] = Expr("""pattern_define_clause""", """DEFINE event_definition_list""", p[1:] if len(p or []) > 1 else [], p)


def p_event_definition_list_2402(p):
    """event_definition_list : event_definition"""
    p[0] = Expr("""event_definition_list""", """event_definition""", p[1:] if len(p or []) > 1 else [], p)


def p_event_definition_list_2403(p):
    """event_definition_list : event_definition_list ',' event_definition"""
    p[0] = Expr("""event_definition_list""", """event_definition_list ',' event_definition""", p[1:] if len(p or []) > 1 else [], p)


def p_event_definition_2404(p):
    """event_definition : ColId AS a_expr"""
    p[0] = Expr("""event_definition""", """ColId AS a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_in_clause_2405(p):
    """pattern_in_clause : PATTERN pattern_list"""
    p[0] = Expr("""pattern_in_clause""", """PATTERN pattern_list""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_list_2406(p):
    """pattern_list : pattern"""
    p[0] = Expr("""pattern_list""", """pattern""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_list_2407(p):
    """pattern_list : pattern_list ',' pattern"""
    p[0] = Expr("""pattern_list""", """pattern_list ',' pattern""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_2408(p):
    """pattern : ColId AS '(' regexp ')'"""
    p[0] = Expr("""pattern""", """ColId AS '(' regexp ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_regexp_2409(p):
    """regexp : regexp regexpprime"""
    p[0] = Expr("""regexp""", """regexp regexpprime""", p[1:] if len(p or []) > 1 else [], p)


def p_regexp_2410(p):
    """regexp : regexp '|' regexpprime"""
    p[0] = Expr("""regexp""", """regexp '|' regexpprime""", p[1:] if len(p or []) > 1 else [], p)


def p_regexp_2411(p):
    """regexp : regexpprime"""
    p[0] = Expr("""regexp""", """regexpprime""", p[1:] if len(p or []) > 1 else [], p)


def p_regexpprime_2412(p):
    """regexpprime : '(' regexp ')' pattern_quantifier"""
    p[0] = Expr("""regexpprime""", """'(' regexp ')' pattern_quantifier""", p[1:] if len(p or []) > 1 else [], p)


def p_regexpprime_2413(p):
    """regexpprime : ColId pattern_quantifier"""
    p[0] = Expr("""regexpprime""", """ColId pattern_quantifier""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_quantifier_2414(p):
    """pattern_quantifier : all_Op"""
    p[0] = Expr("""pattern_quantifier""", """all_Op""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_quantifier_2415(p):
    """pattern_quantifier : """
    p[0] = Expr("""pattern_quantifier""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_results_clause_2416(p):
    """pattern_results_clause : RESULTS GROUPED BY MATCH"""
    p[0] = Expr("""pattern_results_clause""", """RESULTS GROUPED BY MATCH""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_results_clause_2417(p):
    """pattern_results_clause : RESULTS ALL ROWS"""
    p[0] = Expr("""pattern_results_clause""", """RESULTS ALL ROWS""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_results_clause_2418(p):
    """pattern_results_clause : """
    p[0] = Expr("""pattern_results_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_match_options_clause_2419(p):
    """pattern_match_options_clause : ROWS MATCH FIRST_P EVENT_P"""
    p[0] = Expr("""pattern_match_options_clause""", """ROWS MATCH FIRST_P EVENT_P""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_match_options_clause_2420(p):
    """pattern_match_options_clause : ROWS MATCH ALL EVENTS_P"""
    p[0] = Expr("""pattern_match_options_clause""", """ROWS MATCH ALL EVENTS_P""", p[1:] if len(p or []) > 1 else [], p)


def p_pattern_match_options_clause_2421(p):
    """pattern_match_options_clause : """
    p[0] = Expr("""pattern_match_options_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_window_clause_2422(p):
    """window_clause : WINDOW window_definition_list"""
    p[0] = Expr("""window_clause""", """WINDOW window_definition_list""", p[1:] if len(p or []) > 1 else [], p)


def p_window_clause_2423(p):
    """window_clause : """
    p[0] = Expr("""window_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_window_definition_list_2424(p):
    """window_definition_list : window_definition"""
    p[0] = Expr("""window_definition_list""", """window_definition""", p[1:] if len(p or []) > 1 else [], p)


def p_window_definition_list_2425(p):
    """window_definition_list : window_definition_list ',' window_definition"""
    p[0] = Expr("""window_definition_list""", """window_definition_list ',' window_definition""", p[1:] if len(p or []) > 1 else [], p)


def p_window_definition_2426(p):
    """window_definition : ColId AS window_specification"""
    p[0] = Expr("""window_definition""", """ColId AS window_specification""", p[1:] if len(p or []) > 1 else [], p)


def p_over_clause_2427(p):
    """over_clause : OVER window_specification"""
    p[0] = Expr("""over_clause""", """OVER window_specification""", p[1:] if len(p or []) > 1 else [], p)


def p_over_clause_2428(p):
    """over_clause : OVER ColId"""
    p[0] = Expr("""over_clause""", """OVER ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_within_clause_2429(p):
    """within_clause : WITHIN GROUP_P '(' orderby_clause ')'"""
    p[0] = Expr("""within_clause""", """WITHIN GROUP_P '(' orderby_clause ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_within_clause_2430(p):
    """within_clause : """
    p[0] = Expr("""within_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_window_specification_2431(p):
    """window_specification : '(' opt_existing_window_name opt_partition_clause opt_orderby_clause opt_frame_clause ')'"""
    p[0] = Expr("""window_specification""", """'(' opt_existing_window_name opt_partition_clause opt_orderby_clause opt_frame_clause ')'""", p[1:] if len(p or []) > 1 else [], p)


def p_analytic_function_2432(p):
    """analytic_function : non_analytic_function within_clause over_clause"""
    p[0] = Expr("""analytic_function""", """non_analytic_function within_clause over_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_existing_window_name_2433(p):
    """opt_existing_window_name : ColId"""
    p[0] = Expr("""opt_existing_window_name""", """ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_existing_window_name_2434(p):
    """opt_existing_window_name : %prec Op"""
    p[0] = Expr("""opt_existing_window_name""", """%prec Op""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_frame_clause_2435(p):
    """opt_frame_clause : RANGE frame_extent frame_exclusion"""
    p[0] = Expr("""opt_frame_clause""", """RANGE frame_extent frame_exclusion""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_frame_clause_2436(p):
    """opt_frame_clause : ROWS frame_extent frame_exclusion"""
    p[0] = Expr("""opt_frame_clause""", """ROWS frame_extent frame_exclusion""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_frame_clause_2437(p):
    """opt_frame_clause : """
    p[0] = Expr("""opt_frame_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_extent_2438(p):
    """frame_extent : frame_bound1"""
    p[0] = Expr("""frame_extent""", """frame_bound1""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_extent_2439(p):
    """frame_extent : BETWEEN frame_bound1 AND frame_bound2"""
    p[0] = Expr("""frame_extent""", """BETWEEN frame_bound1 AND frame_bound2""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_exclusion_2440(p):
    """frame_exclusion : EXCLUDE CURRENT_P ROW"""
    p[0] = Expr("""frame_exclusion""", """EXCLUDE CURRENT_P ROW""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_exclusion_2441(p):
    """frame_exclusion : EXCLUDE GROUP_P"""
    p[0] = Expr("""frame_exclusion""", """EXCLUDE GROUP_P""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_exclusion_2442(p):
    """frame_exclusion : EXCLUDE TIES"""
    p[0] = Expr("""frame_exclusion""", """EXCLUDE TIES""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_exclusion_2443(p):
    """frame_exclusion : EXCLUDE NO OTHERS"""
    p[0] = Expr("""frame_exclusion""", """EXCLUDE NO OTHERS""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_exclusion_2444(p):
    """frame_exclusion : """
    p[0] = Expr("""frame_exclusion""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_bound1_2445(p):
    """frame_bound1 : UNBOUNDED PRECEDING"""
    p[0] = Expr("""frame_bound1""", """UNBOUNDED PRECEDING""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_bound1_2446(p):
    """frame_bound1 : UNBOUNDED FOLLOWING"""
    p[0] = Expr("""frame_bound1""", """UNBOUNDED FOLLOWING""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_bound1_2447(p):
    """frame_bound1 : a_expr PRECEDING"""
    p[0] = Expr("""frame_bound1""", """a_expr PRECEDING""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_bound1_2448(p):
    """frame_bound1 : a_expr FOLLOWING"""
    p[0] = Expr("""frame_bound1""", """a_expr FOLLOWING""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_bound1_2449(p):
    """frame_bound1 : CURRENT_P ROW"""
    p[0] = Expr("""frame_bound1""", """CURRENT_P ROW""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_bound2_2450(p):
    """frame_bound2 : UNBOUNDED PRECEDING"""
    p[0] = Expr("""frame_bound2""", """UNBOUNDED PRECEDING""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_bound2_2451(p):
    """frame_bound2 : UNBOUNDED FOLLOWING"""
    p[0] = Expr("""frame_bound2""", """UNBOUNDED FOLLOWING""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_bound2_2452(p):
    """frame_bound2 : a_expr PRECEDING"""
    p[0] = Expr("""frame_bound2""", """a_expr PRECEDING""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_bound2_2453(p):
    """frame_bound2 : a_expr FOLLOWING"""
    p[0] = Expr("""frame_bound2""", """a_expr FOLLOWING""", p[1:] if len(p or []) > 1 else [], p)


def p_frame_bound2_2454(p):
    """frame_bound2 : CURRENT_P ROW"""
    p[0] = Expr("""frame_bound2""", """CURRENT_P ROW""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_partition_clause_2455(p):
    """opt_partition_clause : partition_clause"""
    p[0] = Expr("""opt_partition_clause""", """partition_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_partition_clause_2456(p):
    """opt_partition_clause : """
    p[0] = Expr("""opt_partition_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_partition_clause_2457(p):
    """partition_clause : PARTITION BY expr_list"""
    p[0] = Expr("""partition_clause""", """PARTITION BY expr_list""", p[1:] if len(p or []) > 1 else [], p)


def p_partition_clause_2458(p):
    """partition_clause : PARTITION BATCH BY expr_list"""
    p[0] = Expr("""partition_clause""", """PARTITION BATCH BY expr_list""", p[1:] if len(p or []) > 1 else [], p)


def p_partition_clause_2459(p):
    """partition_clause : PARTITION PREPASS BY expr_list"""
    p[0] = Expr("""partition_clause""", """PARTITION PREPASS BY expr_list""", p[1:] if len(p or []) > 1 else [], p)


def p_partition_clause_2460(p):
    """partition_clause : PARTITION AUTO"""
    p[0] = Expr("""partition_clause""", """PARTITION AUTO""", p[1:] if len(p or []) > 1 else [], p)


def p_partition_clause_2461(p):
    """partition_clause : PARTITION NODES"""
    p[0] = Expr("""partition_clause""", """PARTITION NODES""", p[1:] if len(p or []) > 1 else [], p)


def p_partition_clause_2462(p):
    """partition_clause : PARTITION BEST"""
    p[0] = Expr("""partition_clause""", """PARTITION BEST""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_orderby_clause_2463(p):
    """opt_orderby_clause : orderby_clause"""
    p[0] = Expr("""opt_orderby_clause""", """orderby_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_orderby_clause_2464(p):
    """opt_orderby_clause : """
    p[0] = Expr("""opt_orderby_clause""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_orderby_clause_2465(p):
    """orderby_clause : ORDER BY orderby_list"""
    p[0] = Expr("""orderby_clause""", """ORDER BY orderby_list""", p[1:] if len(p or []) > 1 else [], p)


def p_orderby_list_2466(p):
    """orderby_list : orderby"""
    p[0] = Expr("""orderby_list""", """orderby""", p[1:] if len(p or []) > 1 else [], p)


def p_orderby_list_2467(p):
    """orderby_list : orderby_list ',' orderby"""
    p[0] = Expr("""orderby_list""", """orderby_list ',' orderby""", p[1:] if len(p or []) > 1 else [], p)


def p_orderby_2468(p):
    """orderby : a_expr asc_desc_sort opt_nulls_order"""
    p[0] = Expr("""orderby""", """a_expr asc_desc_sort opt_nulls_order""", p[1:] if len(p or []) > 1 else [], p)


def p_asc_desc_sort_2469(p):
    """asc_desc_sort : ASC"""
    p[0] = Expr("""asc_desc_sort""", """ASC""", p[1:] if len(p or []) > 1 else [], p)


def p_asc_desc_sort_2470(p):
    """asc_desc_sort : DESC"""
    p[0] = Expr("""asc_desc_sort""", """DESC""", p[1:] if len(p or []) > 1 else [], p)


def p_asc_desc_sort_2471(p):
    """asc_desc_sort : """
    p[0] = Expr("""asc_desc_sort""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_nulls_order_2472(p):
    """opt_nulls_order : NULLS FIRST_P"""
    p[0] = Expr("""opt_nulls_order""", """NULLS FIRST_P""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_nulls_order_2473(p):
    """opt_nulls_order : NULLS LAST_P"""
    p[0] = Expr("""opt_nulls_order""", """NULLS LAST_P""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_nulls_order_2474(p):
    """opt_nulls_order : NULLS AUTO"""
    p[0] = Expr("""opt_nulls_order""", """NULLS AUTO""", p[1:] if len(p or []) > 1 else [], p)


def p_opt_nulls_order_2475(p):
    """opt_nulls_order : """
    p[0] = Expr("""opt_nulls_order""", """""", p[1:] if len(p or []) > 1 else [], p)


def p_update_target_list_2476(p):
    """update_target_list : update_target_el"""
    p[0] = Expr("""update_target_list""", """update_target_el""", p[1:] if len(p or []) > 1 else [], p)


def p_update_target_list_2477(p):
    """update_target_list : update_target_list ',' update_target_el"""
    p[0] = Expr("""update_target_list""", """update_target_list ',' update_target_el""", p[1:] if len(p or []) > 1 else [], p)


def p_update_target_el_2478(p):
    """update_target_el : ColId opt_indirection '=' a_expr"""
    p[0] = Expr("""update_target_el""", """ColId opt_indirection '=' a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_update_target_el_2479(p):
    """update_target_el : ColId opt_indirection '=' DEFAULT"""
    p[0] = Expr("""update_target_el""", """ColId opt_indirection '=' DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_insert_target_list_2480(p):
    """insert_target_list : insert_target_el"""
    p[0] = Expr("""insert_target_list""", """insert_target_el""", p[1:] if len(p or []) > 1 else [], p)


def p_insert_target_list_2481(p):
    """insert_target_list : insert_target_list ',' insert_target_el"""
    p[0] = Expr("""insert_target_list""", """insert_target_list ',' insert_target_el""", p[1:] if len(p or []) > 1 else [], p)


def p_insert_target_el_2482(p):
    """insert_target_el : a_expr"""
    p[0] = Expr("""insert_target_el""", """a_expr""", p[1:] if len(p or []) > 1 else [], p)


def p_insert_target_el_2483(p):
    """insert_target_el : DEFAULT"""
    p[0] = Expr("""insert_target_el""", """DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_qualified_schema_name_list_2484(p):
    """qualified_schema_name_list : qualified_schema_name"""
    p[0] = Expr("""qualified_schema_name_list""", """qualified_schema_name""", p[1:] if len(p or []) > 1 else [], p)


def p_qualified_schema_name_list_2485(p):
    """qualified_schema_name_list : qualified_schema_name_list ',' qualified_schema_name"""
    p[0] = Expr("""qualified_schema_name_list""", """qualified_schema_name_list ',' qualified_schema_name""", p[1:] if len(p or []) > 1 else [], p)


def p_qualified_schema_name_2486(p):
    """qualified_schema_name : ColId"""
    p[0] = Expr("""qualified_schema_name""", """ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_qualified_schema_name_2487(p):
    """qualified_schema_name : ColId '.' ColId"""
    p[0] = Expr("""qualified_schema_name""", """ColId '.' ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_relation_name_2488(p):
    """relation_name : SpecialRuleRelation"""
    p[0] = Expr("""relation_name""", """SpecialRuleRelation""", p[1:] if len(p or []) > 1 else [], p)


def p_relation_name_2489(p):
    """relation_name : ColId"""
    p[0] = Expr("""relation_name""", """ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_qualified_name_list_2490(p):
    """qualified_name_list : qualified_name"""
    p[0] = Expr("""qualified_name_list""", """qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_qualified_name_list_2491(p):
    """qualified_name_list : qualified_name_list ',' qualified_name"""
    p[0] = Expr("""qualified_name_list""", """qualified_name_list ',' qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_relname_w_indirection_2492(p):
    """relname_w_indirection : relation_name indirection"""
    p[0] = Expr("""relname_w_indirection""", """relation_name indirection""", p[1:] if len(p or []) > 1 else [], p)


def p_hint_list_2493(p):
    """hint_list : hint_name"""
    p[0] = Expr("""hint_list""", """hint_name""", p[1:] if len(p or []) > 1 else [], p)


def p_hint_list_2494(p):
    """hint_list : hint_list ',' hint_name"""
    p[0] = Expr("""hint_list""", """hint_list ',' hint_name""", p[1:] if len(p or []) > 1 else [], p)


def p_udx_func_name_2495(p):
    """udx_func_name : udx_function_name"""
    p[0] = Expr("""udx_func_name""", """udx_function_name""", p[1:] if len(p or []) > 1 else [], p)


def p_udx_func_name_2496(p):
    """udx_func_name : relname_w_indirection"""
    p[0] = Expr("""udx_func_name""", """relname_w_indirection""", p[1:] if len(p or []) > 1 else [], p)


def p_qualified_name_2497(p):
    """qualified_name : relation_name"""
    p[0] = Expr("""qualified_name""", """relation_name""", p[1:] if len(p or []) > 1 else [], p)


def p_qualified_name_2498(p):
    """qualified_name : relname_w_indirection"""
    p[0] = Expr("""qualified_name""", """relname_w_indirection""", p[1:] if len(p or []) > 1 else [], p)


def p_name_list_2499(p):
    """name_list : name"""
    p[0] = Expr("""name_list""", """name""", p[1:] if len(p or []) > 1 else [], p)


def p_name_list_2500(p):
    """name_list : name_list ',' name"""
    p[0] = Expr("""name_list""", """name_list ',' name""", p[1:] if len(p or []) > 1 else [], p)


def p_name_list_2501(p):
    """name_list : name_list AND name"""
    p[0] = Expr("""name_list""", """name_list AND name""", p[1:] if len(p or []) > 1 else [], p)


def p_name_2502(p):
    """name : ColId"""
    p[0] = Expr("""name""", """ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_database_name_2503(p):
    """database_name : ColId"""
    p[0] = Expr("""database_name""", """ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_database_name_2504(p):
    """database_name : DEFAULT"""
    p[0] = Expr("""database_name""", """DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_dbname_list_2505(p):
    """dbname_list : database_name"""
    p[0] = Expr("""dbname_list""", """database_name""", p[1:] if len(p or []) > 1 else [], p)


def p_dbname_list_2506(p):
    """dbname_list : dbname_list ',' database_name"""
    p[0] = Expr("""dbname_list""", """dbname_list ',' database_name""", p[1:] if len(p or []) > 1 else [], p)


def p_access_method_2507(p):
    """access_method : ColId"""
    p[0] = Expr("""access_method""", """ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_attr_name_2508(p):
    """attr_name : ColLabel"""
    p[0] = Expr("""attr_name""", """ColLabel""", p[1:] if len(p or []) > 1 else [], p)


def p_index_name_2509(p):
    """index_name : qualified_name"""
    p[0] = Expr("""index_name""", """qualified_name""", p[1:] if len(p or []) > 1 else [], p)


def p_file_name_2510(p):
    """file_name : Sconst"""
    p[0] = Expr("""file_name""", """Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_func_name_2511(p):
    """func_name : function_name"""
    p[0] = Expr("""func_name""", """function_name""", p[1:] if len(p or []) > 1 else [], p)


def p_func_name_2512(p):
    """func_name : relation_name indirection"""
    p[0] = Expr("""func_name""", """relation_name indirection""", p[1:] if len(p or []) > 1 else [], p)


def p_AexprConst_2513(p):
    """AexprConst : Iconst hint_clause"""
    p[0] = Expr("""AexprConst""", """Iconst hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_AexprConst_2514(p):
    """AexprConst : FCONST hint_clause"""
    p[0] = Expr("""AexprConst""", """FCONST hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_AexprConst_2515(p):
    """AexprConst : Sconst hint_clause"""
    p[0] = Expr("""AexprConst""", """Sconst hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_AexprConst_2516(p):
    """AexprConst : BCONST hint_clause"""
    p[0] = Expr("""AexprConst""", """BCONST hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_AexprConst_2517(p):
    """AexprConst : XCONST hint_clause"""
    p[0] = Expr("""AexprConst""", """XCONST hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_AexprConst_2518(p):
    """AexprConst : ConstTypename Sconst hint_clause"""
    p[0] = Expr("""AexprConst""", """ConstTypename Sconst hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_AexprConst_2519(p):
    """AexprConst : ConstInterval seconds_precision opt_minus Sconst hint_clause interval_qualifier"""
    p[0] = Expr("""AexprConst""", """ConstInterval seconds_precision opt_minus Sconst hint_clause interval_qualifier""", p[1:] if len(p or []) > 1 else [], p)


def p_AexprConst_2520(p):
    """AexprConst : ConstIntervalYM opt_minus Sconst hint_clause interval_qualifier"""
    p[0] = Expr("""AexprConst""", """ConstIntervalYM opt_minus Sconst hint_clause interval_qualifier""", p[1:] if len(p or []) > 1 else [], p)


def p_AexprConst_2521(p):
    """AexprConst : TRUE_P hint_clause"""
    p[0] = Expr("""AexprConst""", """TRUE_P hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_AexprConst_2522(p):
    """AexprConst : FALSE_P hint_clause"""
    p[0] = Expr("""AexprConst""", """FALSE_P hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_AexprConst_2523(p):
    """AexprConst : NULL_P hint_clause"""
    p[0] = Expr("""AexprConst""", """NULL_P hint_clause""", p[1:] if len(p or []) > 1 else [], p)


def p_Iconst_2524(p):
    """Iconst : ICONST"""
    p[0] = Expr("""Iconst""", """ICONST""", p[1:] if len(p or []) > 1 else [], p)


def p_Sconst_2525(p):
    """Sconst : SCONST"""
    p[0] = Expr("""Sconst""", """SCONST""", p[1:] if len(p or []) > 1 else [], p)


def p_UserId_2526(p):
    """UserId : ColId"""
    p[0] = Expr("""UserId""", """ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_ProfileId_2527(p):
    """ProfileId : ColId"""
    p[0] = Expr("""ProfileId""", """ColId""", p[1:] if len(p or []) > 1 else [], p)


def p_ProfileId_2528(p):
    """ProfileId : DEFAULT"""
    p[0] = Expr("""ProfileId""", """DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_ColId_2529(p):
    """ColId : IDENT"""
    p[0] = Expr("""ColId""", """IDENT""", p[1:] if len(p or []) > 1 else [], p)


def p_ColId_2530(p):
    """ColId : unreserved_keyword"""
    p[0] = Expr("""ColId""", """unreserved_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColId_2531(p):
    """ColId : bare_col_alias_excluded_keyword"""
    p[0] = Expr("""ColId""", """bare_col_alias_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColId_2532(p):
    """ColId : bare_col_rel_alias_excl_keyword"""
    p[0] = Expr("""ColId""", """bare_col_rel_alias_excl_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColId_2533(p):
    """ColId : alias_excluded_keyword"""
    p[0] = Expr("""ColId""", """alias_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColId_2534(p):
    """ColId : col_name_keyword"""
    p[0] = Expr("""ColId""", """col_name_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColId_2535(p):
    """ColId : type_excluded_keyword"""
    p[0] = Expr("""ColId""", """type_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColId_2536(p):
    """ColId : func_excluded_keyword"""
    p[0] = Expr("""ColId""", """func_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_AliasColId_2537(p):
    """AliasColId : IDENT"""
    p[0] = Expr("""AliasColId""", """IDENT""", p[1:] if len(p or []) > 1 else [], p)


def p_AliasColId_2538(p):
    """AliasColId : unreserved_keyword"""
    p[0] = Expr("""AliasColId""", """unreserved_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_AliasColId_2539(p):
    """AliasColId : bare_col_alias_excluded_keyword"""
    p[0] = Expr("""AliasColId""", """bare_col_alias_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_AliasColId_2540(p):
    """AliasColId : col_name_keyword"""
    p[0] = Expr("""AliasColId""", """col_name_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_AliasColId_2541(p):
    """AliasColId : type_excluded_keyword"""
    p[0] = Expr("""AliasColId""", """type_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_AliasColId_2542(p):
    """AliasColId : func_excluded_keyword"""
    p[0] = Expr("""AliasColId""", """func_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_type_name_2543(p):
    """type_name : IDENT"""
    p[0] = Expr("""type_name""", """IDENT""", p[1:] if len(p or []) > 1 else [], p)


def p_type_name_2544(p):
    """type_name : unreserved_keyword"""
    p[0] = Expr("""type_name""", """unreserved_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_type_name_2545(p):
    """type_name : bare_col_alias_excluded_keyword"""
    p[0] = Expr("""type_name""", """bare_col_alias_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_type_name_2546(p):
    """type_name : bare_col_rel_alias_excl_keyword"""
    p[0] = Expr("""type_name""", """bare_col_rel_alias_excl_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_type_name_2547(p):
    """type_name : alias_excluded_keyword"""
    p[0] = Expr("""type_name""", """alias_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_type_name_2548(p):
    """type_name : func_excluded_keyword"""
    p[0] = Expr("""type_name""", """func_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_function_name_2549(p):
    """function_name : IDENT"""
    p[0] = Expr("""function_name""", """IDENT""", p[1:] if len(p or []) > 1 else [], p)


def p_function_name_2550(p):
    """function_name : unreserved_keyword"""
    p[0] = Expr("""function_name""", """unreserved_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_function_name_2551(p):
    """function_name : bare_col_alias_excluded_keyword"""
    p[0] = Expr("""function_name""", """bare_col_alias_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_function_name_2552(p):
    """function_name : bare_col_rel_alias_excl_keyword"""
    p[0] = Expr("""function_name""", """bare_col_rel_alias_excl_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_function_name_2553(p):
    """function_name : alias_excluded_keyword"""
    p[0] = Expr("""function_name""", """alias_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_function_name_2554(p):
    """function_name : func_name_keyword"""
    p[0] = Expr("""function_name""", """func_name_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_udx_function_name_2555(p):
    """udx_function_name : IDENT"""
    p[0] = Expr("""udx_function_name""", """IDENT""", p[1:] if len(p or []) > 1 else [], p)


def p_udx_function_name_2556(p):
    """udx_function_name : unreserved_keyword"""
    p[0] = Expr("""udx_function_name""", """unreserved_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_udx_function_name_2557(p):
    """udx_function_name : bare_col_alias_excluded_keyword"""
    p[0] = Expr("""udx_function_name""", """bare_col_alias_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_udx_function_name_2558(p):
    """udx_function_name : bare_col_rel_alias_excl_keyword"""
    p[0] = Expr("""udx_function_name""", """bare_col_rel_alias_excl_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_udx_function_name_2559(p):
    """udx_function_name : alias_excluded_keyword"""
    p[0] = Expr("""udx_function_name""", """alias_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_udx_function_name_2560(p):
    """udx_function_name : func_name_keyword"""
    p[0] = Expr("""udx_function_name""", """func_name_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_udx_function_name_2561(p):
    """udx_function_name : type_excluded_keyword"""
    p[0] = Expr("""udx_function_name""", """type_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_hint_name_2562(p):
    """hint_name : ColLabel"""
    p[0] = Expr("""hint_name""", """ColLabel""", p[1:] if len(p or []) > 1 else [], p)


def p_hive_arg_name_2563(p):
    """hive_arg_name : ColLabel"""
    p[0] = Expr("""hive_arg_name""", """ColLabel""", p[1:] if len(p or []) > 1 else [], p)


def p_ColLabel_2564(p):
    """ColLabel : IDENT"""
    p[0] = Expr("""ColLabel""", """IDENT""", p[1:] if len(p or []) > 1 else [], p)


def p_ColLabel_2565(p):
    """ColLabel : unreserved_keyword"""
    p[0] = Expr("""ColLabel""", """unreserved_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColLabel_2566(p):
    """ColLabel : bare_col_alias_excluded_keyword"""
    p[0] = Expr("""ColLabel""", """bare_col_alias_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColLabel_2567(p):
    """ColLabel : bare_col_rel_alias_excl_keyword"""
    p[0] = Expr("""ColLabel""", """bare_col_rel_alias_excl_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColLabel_2568(p):
    """ColLabel : alias_excluded_keyword"""
    p[0] = Expr("""ColLabel""", """alias_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColLabel_2569(p):
    """ColLabel : col_name_keyword"""
    p[0] = Expr("""ColLabel""", """col_name_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColLabel_2570(p):
    """ColLabel : type_excluded_keyword"""
    p[0] = Expr("""ColLabel""", """type_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColLabel_2571(p):
    """ColLabel : func_excluded_keyword"""
    p[0] = Expr("""ColLabel""", """func_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColLabel_2572(p):
    """ColLabel : func_name_keyword"""
    p[0] = Expr("""ColLabel""", """func_name_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColLabel_2573(p):
    """ColLabel : reserved_keyword"""
    p[0] = Expr("""ColLabel""", """reserved_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_ColLabel_2574(p):
    """ColLabel : Sconst"""
    p[0] = Expr("""ColLabel""", """Sconst""", p[1:] if len(p or []) > 1 else [], p)


def p_BareColLabel_2575(p):
    """BareColLabel : IDENT"""
    p[0] = Expr("""BareColLabel""", """IDENT""", p[1:] if len(p or []) > 1 else [], p)


def p_BareColLabel_2576(p):
    """BareColLabel : alias_excluded_keyword"""
    p[0] = Expr("""BareColLabel""", """alias_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_BareColLabel_2577(p):
    """BareColLabel : type_excluded_keyword"""
    p[0] = Expr("""BareColLabel""", """type_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_BareColLabel_2578(p):
    """BareColLabel : func_excluded_keyword"""
    p[0] = Expr("""BareColLabel""", """func_excluded_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_BareColLabel_2579(p):
    """BareColLabel : unreserved_keyword"""
    p[0] = Expr("""BareColLabel""", """unreserved_keyword""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_excluded_keyword_2580(p):
    """alias_excluded_keyword : ANTI"""
    p[0] = Expr("""alias_excluded_keyword""", """ANTI""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_excluded_keyword_2581(p):
    """alias_excluded_keyword : COMPLEX"""
    p[0] = Expr("""alias_excluded_keyword""", """COMPLEX""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_excluded_keyword_2582(p):
    """alias_excluded_keyword : CROSS"""
    p[0] = Expr("""alias_excluded_keyword""", """CROSS""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_excluded_keyword_2583(p):
    """alias_excluded_keyword : FULL"""
    p[0] = Expr("""alias_excluded_keyword""", """FULL""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_excluded_keyword_2584(p):
    """alias_excluded_keyword : INNER_P"""
    p[0] = Expr("""alias_excluded_keyword""", """INNER_P""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_excluded_keyword_2585(p):
    """alias_excluded_keyword : JOIN"""
    p[0] = Expr("""alias_excluded_keyword""", """JOIN""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_excluded_keyword_2586(p):
    """alias_excluded_keyword : LEFT"""
    p[0] = Expr("""alias_excluded_keyword""", """LEFT""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_excluded_keyword_2587(p):
    """alias_excluded_keyword : NATURAL"""
    p[0] = Expr("""alias_excluded_keyword""", """NATURAL""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_excluded_keyword_2588(p):
    """alias_excluded_keyword : NULLAWARE"""
    p[0] = Expr("""alias_excluded_keyword""", """NULLAWARE""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_excluded_keyword_2589(p):
    """alias_excluded_keyword : OUTER_P"""
    p[0] = Expr("""alias_excluded_keyword""", """OUTER_P""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_excluded_keyword_2590(p):
    """alias_excluded_keyword : RIGHT"""
    p[0] = Expr("""alias_excluded_keyword""", """RIGHT""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_excluded_keyword_2591(p):
    """alias_excluded_keyword : SEMI"""
    p[0] = Expr("""alias_excluded_keyword""", """SEMI""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_excluded_keyword_2592(p):
    """alias_excluded_keyword : SEMIALL"""
    p[0] = Expr("""alias_excluded_keyword""", """SEMIALL""", p[1:] if len(p or []) > 1 else [], p)


def p_alias_excluded_keyword_2593(p):
    """alias_excluded_keyword : UNI"""
    p[0] = Expr("""alias_excluded_keyword""", """UNI""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2594(p):
    """unreserved_keyword : ABORT_P"""
    p[0] = Expr("""unreserved_keyword""", """ABORT_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2595(p):
    """unreserved_keyword : ABSOLUTE_P"""
    p[0] = Expr("""unreserved_keyword""", """ABSOLUTE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2596(p):
    """unreserved_keyword : ACCESS"""
    p[0] = Expr("""unreserved_keyword""", """ACCESS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2597(p):
    """unreserved_keyword : ACCOUNT"""
    p[0] = Expr("""unreserved_keyword""", """ACCOUNT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2598(p):
    """unreserved_keyword : ACTION"""
    p[0] = Expr("""unreserved_keyword""", """ACTION""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2599(p):
    """unreserved_keyword : ACTIVATE"""
    p[0] = Expr("""unreserved_keyword""", """ACTIVATE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2600(p):
    """unreserved_keyword : ACTIVEPARTITIONCOUNT"""
    p[0] = Expr("""unreserved_keyword""", """ACTIVEPARTITIONCOUNT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2601(p):
    """unreserved_keyword : ADD"""
    p[0] = Expr("""unreserved_keyword""", """ADD""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2602(p):
    """unreserved_keyword : ADDRESS"""
    p[0] = Expr("""unreserved_keyword""", """ADDRESS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2603(p):
    """unreserved_keyword : ADMIN"""
    p[0] = Expr("""unreserved_keyword""", """ADMIN""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2604(p):
    """unreserved_keyword : AFTER"""
    p[0] = Expr("""unreserved_keyword""", """AFTER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2605(p):
    """unreserved_keyword : AGGREGATE"""
    p[0] = Expr("""unreserved_keyword""", """AGGREGATE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2606(p):
    """unreserved_keyword : ALSO"""
    p[0] = Expr("""unreserved_keyword""", """ALSO""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2607(p):
    """unreserved_keyword : ALTER"""
    p[0] = Expr("""unreserved_keyword""", """ALTER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2608(p):
    """unreserved_keyword : ANALYSE"""
    p[0] = Expr("""unreserved_keyword""", """ANALYSE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2609(p):
    """unreserved_keyword : ANALYTIC"""
    p[0] = Expr("""unreserved_keyword""", """ANALYTIC""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2610(p):
    """unreserved_keyword : ANALYZE"""
    p[0] = Expr("""unreserved_keyword""", """ANALYZE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2611(p):
    """unreserved_keyword : ANNOTATED"""
    p[0] = Expr("""unreserved_keyword""", """ANNOTATED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2612(p):
    """unreserved_keyword : ASSIGNMENT"""
    p[0] = Expr("""unreserved_keyword""", """ASSIGNMENT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2613(p):
    """unreserved_keyword : AT"""
    p[0] = Expr("""unreserved_keyword""", """AT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2614(p):
    """unreserved_keyword : AUTO"""
    p[0] = Expr("""unreserved_keyword""", """AUTO""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2615(p):
    """unreserved_keyword : AUTHENTICATION"""
    p[0] = Expr("""unreserved_keyword""", """AUTHENTICATION""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2616(p):
    """unreserved_keyword : AVAILABLE"""
    p[0] = Expr("""unreserved_keyword""", """AVAILABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2617(p):
    """unreserved_keyword : BACKWARD"""
    p[0] = Expr("""unreserved_keyword""", """BACKWARD""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2618(p):
    """unreserved_keyword : BALANCE"""
    p[0] = Expr("""unreserved_keyword""", """BALANCE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2619(p):
    """unreserved_keyword : BASENAME"""
    p[0] = Expr("""unreserved_keyword""", """BASENAME""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2620(p):
    """unreserved_keyword : BATCH"""
    p[0] = Expr("""unreserved_keyword""", """BATCH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2621(p):
    """unreserved_keyword : BEFORE"""
    p[0] = Expr("""unreserved_keyword""", """BEFORE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2622(p):
    """unreserved_keyword : BEGIN_P"""
    p[0] = Expr("""unreserved_keyword""", """BEGIN_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2623(p):
    """unreserved_keyword : BEST"""
    p[0] = Expr("""unreserved_keyword""", """BEST""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2624(p):
    """unreserved_keyword : BLOCK"""
    p[0] = Expr("""unreserved_keyword""", """BLOCK""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2625(p):
    """unreserved_keyword : BLOCK_DICT"""
    p[0] = Expr("""unreserved_keyword""", """BLOCK_DICT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2626(p):
    """unreserved_keyword : BLOCKDICT_COMP"""
    p[0] = Expr("""unreserved_keyword""", """BLOCKDICT_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2627(p):
    """unreserved_keyword : BRANCH"""
    p[0] = Expr("""unreserved_keyword""", """BRANCH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2628(p):
    """unreserved_keyword : BROADCAST"""
    p[0] = Expr("""unreserved_keyword""", """BROADCAST""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2629(p):
    """unreserved_keyword : BY"""
    p[0] = Expr("""unreserved_keyword""", """BY""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2630(p):
    """unreserved_keyword : BYTES"""
    p[0] = Expr("""unreserved_keyword""", """BYTES""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2631(p):
    """unreserved_keyword : BZIP"""
    p[0] = Expr("""unreserved_keyword""", """BZIP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2632(p):
    """unreserved_keyword : BZIP_COMP"""
    p[0] = Expr("""unreserved_keyword""", """BZIP_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2633(p):
    """unreserved_keyword : CACHE"""
    p[0] = Expr("""unreserved_keyword""", """CACHE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2634(p):
    """unreserved_keyword : CALLED"""
    p[0] = Expr("""unreserved_keyword""", """CALLED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2635(p):
    """unreserved_keyword : CASCADE"""
    p[0] = Expr("""unreserved_keyword""", """CASCADE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2636(p):
    """unreserved_keyword : CATALOGPATH"""
    p[0] = Expr("""unreserved_keyword""", """CATALOGPATH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2637(p):
    """unreserved_keyword : CHAIN"""
    p[0] = Expr("""unreserved_keyword""", """CHAIN""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2638(p):
    """unreserved_keyword : CHARACTERISTICS"""
    p[0] = Expr("""unreserved_keyword""", """CHARACTERISTICS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2639(p):
    """unreserved_keyword : CHARACTERS"""
    p[0] = Expr("""unreserved_keyword""", """CHARACTERS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2640(p):
    """unreserved_keyword : CHECKPOINT"""
    p[0] = Expr("""unreserved_keyword""", """CHECKPOINT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2641(p):
    """unreserved_keyword : CLASS"""
    p[0] = Expr("""unreserved_keyword""", """CLASS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2642(p):
    """unreserved_keyword : CLEAR"""
    p[0] = Expr("""unreserved_keyword""", """CLEAR""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2643(p):
    """unreserved_keyword : CLOSE"""
    p[0] = Expr("""unreserved_keyword""", """CLOSE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2644(p):
    """unreserved_keyword : CLUSTER"""
    p[0] = Expr("""unreserved_keyword""", """CLUSTER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2645(p):
    """unreserved_keyword : COLSIZES"""
    p[0] = Expr("""unreserved_keyword""", """COLSIZES""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2646(p):
    """unreserved_keyword : COLUMNS_COUNT"""
    p[0] = Expr("""unreserved_keyword""", """COLUMNS_COUNT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2647(p):
    """unreserved_keyword : COMMENT"""
    p[0] = Expr("""unreserved_keyword""", """COMMENT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2648(p):
    """unreserved_keyword : COMMIT"""
    p[0] = Expr("""unreserved_keyword""", """COMMIT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2649(p):
    """unreserved_keyword : COMMITTED"""
    p[0] = Expr("""unreserved_keyword""", """COMMITTED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2650(p):
    """unreserved_keyword : COMMONDELTA_COMP"""
    p[0] = Expr("""unreserved_keyword""", """COMMONDELTA_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2651(p):
    """unreserved_keyword : COMMUNAL"""
    p[0] = Expr("""unreserved_keyword""", """COMMUNAL""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2652(p):
    """unreserved_keyword : CONNECT"""
    p[0] = Expr("""unreserved_keyword""", """CONNECT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2653(p):
    """unreserved_keyword : CONSTRAINTS"""
    p[0] = Expr("""unreserved_keyword""", """CONSTRAINTS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2654(p):
    """unreserved_keyword : CONTROL"""
    p[0] = Expr("""unreserved_keyword""", """CONTROL""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2655(p):
    """unreserved_keyword : COPY"""
    p[0] = Expr("""unreserved_keyword""", """COPY""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2656(p):
    """unreserved_keyword : CPUAFFINITYMODE"""
    p[0] = Expr("""unreserved_keyword""", """CPUAFFINITYMODE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2657(p):
    """unreserved_keyword : CPUAFFINITYSET"""
    p[0] = Expr("""unreserved_keyword""", """CPUAFFINITYSET""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2658(p):
    """unreserved_keyword : CREATEDB"""
    p[0] = Expr("""unreserved_keyword""", """CREATEDB""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2659(p):
    """unreserved_keyword : CREATEUSER"""
    p[0] = Expr("""unreserved_keyword""", """CREATEUSER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2660(p):
    """unreserved_keyword : CSV"""
    p[0] = Expr("""unreserved_keyword""", """CSV""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2661(p):
    """unreserved_keyword : CUBE"""
    p[0] = Expr("""unreserved_keyword""", """CUBE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2662(p):
    """unreserved_keyword : CURRENT_P"""
    p[0] = Expr("""unreserved_keyword""", """CURRENT_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2663(p):
    """unreserved_keyword : CURSOR"""
    p[0] = Expr("""unreserved_keyword""", """CURSOR""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2664(p):
    """unreserved_keyword : CUSTOM"""
    p[0] = Expr("""unreserved_keyword""", """CUSTOM""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2665(p):
    """unreserved_keyword : CUSTOM_PARTITIONS"""
    p[0] = Expr("""unreserved_keyword""", """CUSTOM_PARTITIONS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2666(p):
    """unreserved_keyword : CYCLE"""
    p[0] = Expr("""unreserved_keyword""", """CYCLE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2667(p):
    """unreserved_keyword : DATA_P"""
    p[0] = Expr("""unreserved_keyword""", """DATA_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2668(p):
    """unreserved_keyword : DATABASE"""
    p[0] = Expr("""unreserved_keyword""", """DATABASE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2669(p):
    """unreserved_keyword : DATAPATH"""
    p[0] = Expr("""unreserved_keyword""", """DATAPATH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2670(p):
    """unreserved_keyword : DEACTIVATE"""
    p[0] = Expr("""unreserved_keyword""", """DEACTIVATE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2671(p):
    """unreserved_keyword : DEALLOCATE"""
    p[0] = Expr("""unreserved_keyword""", """DEALLOCATE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2672(p):
    """unreserved_keyword : DECLARE"""
    p[0] = Expr("""unreserved_keyword""", """DECLARE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2673(p):
    """unreserved_keyword : DEFAULTS"""
    p[0] = Expr("""unreserved_keyword""", """DEFAULTS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2674(p):
    """unreserved_keyword : DEFERRED"""
    p[0] = Expr("""unreserved_keyword""", """DEFERRED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2675(p):
    """unreserved_keyword : DEFINE"""
    p[0] = Expr("""unreserved_keyword""", """DEFINE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2676(p):
    """unreserved_keyword : DEFINER"""
    p[0] = Expr("""unreserved_keyword""", """DEFINER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2677(p):
    """unreserved_keyword : DELETE_P"""
    p[0] = Expr("""unreserved_keyword""", """DELETE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2678(p):
    """unreserved_keyword : DELIMITER"""
    p[0] = Expr("""unreserved_keyword""", """DELIMITER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2679(p):
    """unreserved_keyword : DELIMITERS"""
    p[0] = Expr("""unreserved_keyword""", """DELIMITERS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2680(p):
    """unreserved_keyword : DELTARANGE_COMP"""
    p[0] = Expr("""unreserved_keyword""", """DELTARANGE_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2681(p):
    """unreserved_keyword : DELTARANGE_COMP_SP"""
    p[0] = Expr("""unreserved_keyword""", """DELTARANGE_COMP_SP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2682(p):
    """unreserved_keyword : DELTAVAL"""
    p[0] = Expr("""unreserved_keyword""", """DELTAVAL""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2683(p):
    """unreserved_keyword : DEPENDS"""
    p[0] = Expr("""unreserved_keyword""", """DEPENDS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2684(p):
    """unreserved_keyword : DETERMINES"""
    p[0] = Expr("""unreserved_keyword""", """DETERMINES""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2685(p):
    """unreserved_keyword : DIRECT"""
    p[0] = Expr("""unreserved_keyword""", """DIRECT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2686(p):
    """unreserved_keyword : DIRECTCOLS"""
    p[0] = Expr("""unreserved_keyword""", """DIRECTCOLS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2687(p):
    """unreserved_keyword : DIRECTED"""
    p[0] = Expr("""unreserved_keyword""", """DIRECTED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2688(p):
    """unreserved_keyword : DIRECTGROUPED"""
    p[0] = Expr("""unreserved_keyword""", """DIRECTGROUPED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2689(p):
    """unreserved_keyword : DIRECTPROJ"""
    p[0] = Expr("""unreserved_keyword""", """DIRECTPROJ""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2690(p):
    """unreserved_keyword : DISABLE"""
    p[0] = Expr("""unreserved_keyword""", """DISABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2691(p):
    """unreserved_keyword : DISABLED"""
    p[0] = Expr("""unreserved_keyword""", """DISABLED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2692(p):
    """unreserved_keyword : DISCONNECT"""
    p[0] = Expr("""unreserved_keyword""", """DISCONNECT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2693(p):
    """unreserved_keyword : DISTVALINDEX"""
    p[0] = Expr("""unreserved_keyword""", """DISTVALINDEX""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2694(p):
    """unreserved_keyword : DO"""
    p[0] = Expr("""unreserved_keyword""", """DO""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2695(p):
    """unreserved_keyword : DOMAIN_P"""
    p[0] = Expr("""unreserved_keyword""", """DOMAIN_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2696(p):
    """unreserved_keyword : DOUBLE_P"""
    p[0] = Expr("""unreserved_keyword""", """DOUBLE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2697(p):
    """unreserved_keyword : DROP"""
    p[0] = Expr("""unreserved_keyword""", """DROP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2698(p):
    """unreserved_keyword : DURABLE"""
    p[0] = Expr("""unreserved_keyword""", """DURABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2699(p):
    """unreserved_keyword : EACH"""
    p[0] = Expr("""unreserved_keyword""", """EACH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2700(p):
    """unreserved_keyword : ENABLE"""
    p[0] = Expr("""unreserved_keyword""", """ENABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2701(p):
    """unreserved_keyword : ENABLED"""
    p[0] = Expr("""unreserved_keyword""", """ENABLED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2702(p):
    """unreserved_keyword : ENCLOSED"""
    p[0] = Expr("""unreserved_keyword""", """ENCLOSED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2703(p):
    """unreserved_keyword : ENCODING"""
    p[0] = Expr("""unreserved_keyword""", """ENCODING""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2704(p):
    """unreserved_keyword : ENCRYPTED"""
    p[0] = Expr("""unreserved_keyword""", """ENCRYPTED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2705(p):
    """unreserved_keyword : ENFORCELENGTH"""
    p[0] = Expr("""unreserved_keyword""", """ENFORCELENGTH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2706(p):
    """unreserved_keyword : EPHEMERAL"""
    p[0] = Expr("""unreserved_keyword""", """EPHEMERAL""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2707(p):
    """unreserved_keyword : EPOCH_P"""
    p[0] = Expr("""unreserved_keyword""", """EPOCH_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2708(p):
    """unreserved_keyword : ERROR_P"""
    p[0] = Expr("""unreserved_keyword""", """ERROR_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2709(p):
    """unreserved_keyword : ESCAPE"""
    p[0] = Expr("""unreserved_keyword""", """ESCAPE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2710(p):
    """unreserved_keyword : EVENT_P"""
    p[0] = Expr("""unreserved_keyword""", """EVENT_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2711(p):
    """unreserved_keyword : EVENTS_P"""
    p[0] = Expr("""unreserved_keyword""", """EVENTS_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2712(p):
    """unreserved_keyword : EXCEPTION"""
    p[0] = Expr("""unreserved_keyword""", """EXCEPTION""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2713(p):
    """unreserved_keyword : EXCEPTIONS"""
    p[0] = Expr("""unreserved_keyword""", """EXCEPTIONS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2714(p):
    """unreserved_keyword : EXCLUDE"""
    p[0] = Expr("""unreserved_keyword""", """EXCLUDE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2715(p):
    """unreserved_keyword : EXCLUDING"""
    p[0] = Expr("""unreserved_keyword""", """EXCLUDING""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2716(p):
    """unreserved_keyword : EXCLUSIVE"""
    p[0] = Expr("""unreserved_keyword""", """EXCLUSIVE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2717(p):
    """unreserved_keyword : EXECUTE"""
    p[0] = Expr("""unreserved_keyword""", """EXECUTE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2718(p):
    """unreserved_keyword : EXECUTIONPARALLELISM"""
    p[0] = Expr("""unreserved_keyword""", """EXECUTIONPARALLELISM""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2719(p):
    """unreserved_keyword : EXPIRE"""
    p[0] = Expr("""unreserved_keyword""", """EXPIRE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2720(p):
    """unreserved_keyword : EXPLAIN"""
    p[0] = Expr("""unreserved_keyword""", """EXPLAIN""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2721(p):
    """unreserved_keyword : EXPORT"""
    p[0] = Expr("""unreserved_keyword""", """EXPORT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2722(p):
    """unreserved_keyword : EXTEND"""
    p[0] = Expr("""unreserved_keyword""", """EXTEND""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2723(p):
    """unreserved_keyword : EXTERNAL"""
    p[0] = Expr("""unreserved_keyword""", """EXTERNAL""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2724(p):
    """unreserved_keyword : FAILED_LOGIN_ATTEMPTS"""
    p[0] = Expr("""unreserved_keyword""", """FAILED_LOGIN_ATTEMPTS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2725(p):
    """unreserved_keyword : FAULT"""
    p[0] = Expr("""unreserved_keyword""", """FAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2726(p):
    """unreserved_keyword : FENCED"""
    p[0] = Expr("""unreserved_keyword""", """FENCED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2727(p):
    """unreserved_keyword : FETCH"""
    p[0] = Expr("""unreserved_keyword""", """FETCH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2728(p):
    """unreserved_keyword : FILESYSTEM"""
    p[0] = Expr("""unreserved_keyword""", """FILESYSTEM""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2729(p):
    """unreserved_keyword : FILLER"""
    p[0] = Expr("""unreserved_keyword""", """FILLER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2730(p):
    """unreserved_keyword : FILTER"""
    p[0] = Expr("""unreserved_keyword""", """FILTER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2731(p):
    """unreserved_keyword : FIXEDWIDTH"""
    p[0] = Expr("""unreserved_keyword""", """FIXEDWIDTH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2732(p):
    """unreserved_keyword : FIRST_P"""
    p[0] = Expr("""unreserved_keyword""", """FIRST_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2733(p):
    """unreserved_keyword : FLEX"""
    p[0] = Expr("""unreserved_keyword""", """FLEX""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2734(p):
    """unreserved_keyword : FLEXIBLE"""
    p[0] = Expr("""unreserved_keyword""", """FLEXIBLE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2735(p):
    """unreserved_keyword : FOLLOWING"""
    p[0] = Expr("""unreserved_keyword""", """FOLLOWING""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2736(p):
    """unreserved_keyword : FORCE"""
    p[0] = Expr("""unreserved_keyword""", """FORCE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2737(p):
    """unreserved_keyword : FORMAT"""
    p[0] = Expr("""unreserved_keyword""", """FORMAT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2738(p):
    """unreserved_keyword : FORWARD"""
    p[0] = Expr("""unreserved_keyword""", """FORWARD""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2739(p):
    """unreserved_keyword : FREEZE"""
    p[0] = Expr("""unreserved_keyword""", """FREEZE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2740(p):
    """unreserved_keyword : FUNCTION"""
    p[0] = Expr("""unreserved_keyword""", """FUNCTION""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2741(p):
    """unreserved_keyword : FUNCTIONS"""
    p[0] = Expr("""unreserved_keyword""", """FUNCTIONS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2742(p):
    """unreserved_keyword : GCDDELTA"""
    p[0] = Expr("""unreserved_keyword""", """GCDDELTA""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2743(p):
    """unreserved_keyword : GET"""
    p[0] = Expr("""unreserved_keyword""", """GET""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2744(p):
    """unreserved_keyword : GLOBAL"""
    p[0] = Expr("""unreserved_keyword""", """GLOBAL""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2745(p):
    """unreserved_keyword : GRACEPERIOD"""
    p[0] = Expr("""unreserved_keyword""", """GRACEPERIOD""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2746(p):
    """unreserved_keyword : GROUPED"""
    p[0] = Expr("""unreserved_keyword""", """GROUPED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2747(p):
    """unreserved_keyword : GROUPING"""
    p[0] = Expr("""unreserved_keyword""", """GROUPING""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2748(p):
    """unreserved_keyword : GZIP"""
    p[0] = Expr("""unreserved_keyword""", """GZIP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2749(p):
    """unreserved_keyword : GZIP_COMP"""
    p[0] = Expr("""unreserved_keyword""", """GZIP_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2750(p):
    """unreserved_keyword : HANDLER"""
    p[0] = Expr("""unreserved_keyword""", """HANDLER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2751(p):
    """unreserved_keyword : HCATALOG"""
    p[0] = Expr("""unreserved_keyword""", """HCATALOG""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2752(p):
    """unreserved_keyword : HCATALOG_CONNECTION_TIMEOUT"""
    p[0] = Expr("""unreserved_keyword""", """HCATALOG_CONNECTION_TIMEOUT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2753(p):
    """unreserved_keyword : HCATALOG_DB"""
    p[0] = Expr("""unreserved_keyword""", """HCATALOG_DB""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2754(p):
    """unreserved_keyword : HCATALOG_SCHEMA"""
    p[0] = Expr("""unreserved_keyword""", """HCATALOG_SCHEMA""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2755(p):
    """unreserved_keyword : HCATALOG_SLOW_TRANSFER_LIMIT"""
    p[0] = Expr("""unreserved_keyword""", """HCATALOG_SLOW_TRANSFER_LIMIT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2756(p):
    """unreserved_keyword : HCATALOG_SLOW_TRANSFER_TIME"""
    p[0] = Expr("""unreserved_keyword""", """HCATALOG_SLOW_TRANSFER_TIME""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2757(p):
    """unreserved_keyword : HCATALOG_USER"""
    p[0] = Expr("""unreserved_keyword""", """HCATALOG_USER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2758(p):
    """unreserved_keyword : HIGH"""
    p[0] = Expr("""unreserved_keyword""", """HIGH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2759(p):
    """unreserved_keyword : HIVESERVER2_HOSTNAME"""
    p[0] = Expr("""unreserved_keyword""", """HIVESERVER2_HOSTNAME""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2760(p):
    """unreserved_keyword : HOLD"""
    p[0] = Expr("""unreserved_keyword""", """HOLD""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2761(p):
    """unreserved_keyword : HOST"""
    p[0] = Expr("""unreserved_keyword""", """HOST""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2762(p):
    """unreserved_keyword : HOSTNAME"""
    p[0] = Expr("""unreserved_keyword""", """HOSTNAME""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2763(p):
    """unreserved_keyword : HOURS_P"""
    p[0] = Expr("""unreserved_keyword""", """HOURS_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2764(p):
    """unreserved_keyword : IDENTIFIED"""
    p[0] = Expr("""unreserved_keyword""", """IDENTIFIED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2765(p):
    """unreserved_keyword : IDLESESSIONTIMEOUT"""
    p[0] = Expr("""unreserved_keyword""", """IDLESESSIONTIMEOUT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2766(p):
    """unreserved_keyword : IF_P"""
    p[0] = Expr("""unreserved_keyword""", """IF_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2767(p):
    """unreserved_keyword : IGNORE"""
    p[0] = Expr("""unreserved_keyword""", """IGNORE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2768(p):
    """unreserved_keyword : IMMEDIATE"""
    p[0] = Expr("""unreserved_keyword""", """IMMEDIATE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2769(p):
    """unreserved_keyword : IMMUTABLE"""
    p[0] = Expr("""unreserved_keyword""", """IMMUTABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2770(p):
    """unreserved_keyword : IMPLICIT_P"""
    p[0] = Expr("""unreserved_keyword""", """IMPLICIT_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2771(p):
    """unreserved_keyword : INCLUDE"""
    p[0] = Expr("""unreserved_keyword""", """INCLUDE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2772(p):
    """unreserved_keyword : INCLUDING"""
    p[0] = Expr("""unreserved_keyword""", """INCLUDING""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2773(p):
    """unreserved_keyword : INCREMENT"""
    p[0] = Expr("""unreserved_keyword""", """INCREMENT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2774(p):
    """unreserved_keyword : INDEX"""
    p[0] = Expr("""unreserved_keyword""", """INDEX""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2775(p):
    """unreserved_keyword : INHERITS"""
    p[0] = Expr("""unreserved_keyword""", """INHERITS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2776(p):
    """unreserved_keyword : INPUT_P"""
    p[0] = Expr("""unreserved_keyword""", """INPUT_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2777(p):
    """unreserved_keyword : INSENSITIVE"""
    p[0] = Expr("""unreserved_keyword""", """INSENSITIVE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2778(p):
    """unreserved_keyword : INSERT"""
    p[0] = Expr("""unreserved_keyword""", """INSERT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2779(p):
    """unreserved_keyword : INSTEAD"""
    p[0] = Expr("""unreserved_keyword""", """INSTEAD""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2780(p):
    """unreserved_keyword : INTERFACE"""
    p[0] = Expr("""unreserved_keyword""", """INTERFACE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2781(p):
    """unreserved_keyword : INVOKER"""
    p[0] = Expr("""unreserved_keyword""", """INVOKER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2782(p):
    """unreserved_keyword : ISOLATION"""
    p[0] = Expr("""unreserved_keyword""", """ISOLATION""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2783(p):
    """unreserved_keyword : JSON"""
    p[0] = Expr("""unreserved_keyword""", """JSON""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2784(p):
    """unreserved_keyword : KEY"""
    p[0] = Expr("""unreserved_keyword""", """KEY""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2785(p):
    """unreserved_keyword : LABEL"""
    p[0] = Expr("""unreserved_keyword""", """LABEL""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2786(p):
    """unreserved_keyword : LANCOMPILER"""
    p[0] = Expr("""unreserved_keyword""", """LANCOMPILER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2787(p):
    """unreserved_keyword : LANGUAGE"""
    p[0] = Expr("""unreserved_keyword""", """LANGUAGE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2788(p):
    """unreserved_keyword : LARGE_P"""
    p[0] = Expr("""unreserved_keyword""", """LARGE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2789(p):
    """unreserved_keyword : LAST_P"""
    p[0] = Expr("""unreserved_keyword""", """LAST_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2790(p):
    """unreserved_keyword : LATEST"""
    p[0] = Expr("""unreserved_keyword""", """LATEST""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2791(p):
    """unreserved_keyword : LESS"""
    p[0] = Expr("""unreserved_keyword""", """LESS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2792(p):
    """unreserved_keyword : LEVEL"""
    p[0] = Expr("""unreserved_keyword""", """LEVEL""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2793(p):
    """unreserved_keyword : LIBRARY"""
    p[0] = Expr("""unreserved_keyword""", """LIBRARY""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2794(p):
    """unreserved_keyword : LISTEN"""
    p[0] = Expr("""unreserved_keyword""", """LISTEN""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2795(p):
    """unreserved_keyword : LOAD"""
    p[0] = Expr("""unreserved_keyword""", """LOAD""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2796(p):
    """unreserved_keyword : LOCAL"""
    p[0] = Expr("""unreserved_keyword""", """LOCAL""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2797(p):
    """unreserved_keyword : LOCATION"""
    p[0] = Expr("""unreserved_keyword""", """LOCATION""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2798(p):
    """unreserved_keyword : LOCK_P"""
    p[0] = Expr("""unreserved_keyword""", """LOCK_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2799(p):
    """unreserved_keyword : LOW"""
    p[0] = Expr("""unreserved_keyword""", """LOW""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2800(p):
    """unreserved_keyword : LZO"""
    p[0] = Expr("""unreserved_keyword""", """LZO""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2801(p):
    """unreserved_keyword : MANAGED"""
    p[0] = Expr("""unreserved_keyword""", """MANAGED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2802(p):
    """unreserved_keyword : MASK"""
    p[0] = Expr("""unreserved_keyword""", """MASK""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2803(p):
    """unreserved_keyword : MATCHED"""
    p[0] = Expr("""unreserved_keyword""", """MATCHED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2804(p):
    """unreserved_keyword : MATERIALIZE"""
    p[0] = Expr("""unreserved_keyword""", """MATERIALIZE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2805(p):
    """unreserved_keyword : MAXCONCURRENCY"""
    p[0] = Expr("""unreserved_keyword""", """MAXCONCURRENCY""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2806(p):
    """unreserved_keyword : MAXCONCURRENCYGRACE"""
    p[0] = Expr("""unreserved_keyword""", """MAXCONCURRENCYGRACE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2807(p):
    """unreserved_keyword : MAXCONNECTIONS"""
    p[0] = Expr("""unreserved_keyword""", """MAXCONNECTIONS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2808(p):
    """unreserved_keyword : MAXMEMORYSIZE"""
    p[0] = Expr("""unreserved_keyword""", """MAXMEMORYSIZE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2809(p):
    """unreserved_keyword : MAXPAYLOAD"""
    p[0] = Expr("""unreserved_keyword""", """MAXPAYLOAD""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2810(p):
    """unreserved_keyword : MAXQUERYMEMORYSIZE"""
    p[0] = Expr("""unreserved_keyword""", """MAXQUERYMEMORYSIZE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2811(p):
    """unreserved_keyword : MAXVALUE"""
    p[0] = Expr("""unreserved_keyword""", """MAXVALUE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2812(p):
    """unreserved_keyword : MEDIUM"""
    p[0] = Expr("""unreserved_keyword""", """MEDIUM""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2813(p):
    """unreserved_keyword : METHOD"""
    p[0] = Expr("""unreserved_keyword""", """METHOD""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2814(p):
    """unreserved_keyword : MEMORYCAP"""
    p[0] = Expr("""unreserved_keyword""", """MEMORYCAP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2815(p):
    """unreserved_keyword : MEMORYSIZE"""
    p[0] = Expr("""unreserved_keyword""", """MEMORYSIZE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2816(p):
    """unreserved_keyword : MERGE"""
    p[0] = Expr("""unreserved_keyword""", """MERGE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2817(p):
    """unreserved_keyword : MERGEOUT"""
    p[0] = Expr("""unreserved_keyword""", """MERGEOUT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2818(p):
    """unreserved_keyword : MICROSECONDS_P"""
    p[0] = Expr("""unreserved_keyword""", """MICROSECONDS_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2819(p):
    """unreserved_keyword : MILLISECONDS_P"""
    p[0] = Expr("""unreserved_keyword""", """MILLISECONDS_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2820(p):
    """unreserved_keyword : MINUTES_P"""
    p[0] = Expr("""unreserved_keyword""", """MINUTES_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2821(p):
    """unreserved_keyword : MINVALUE"""
    p[0] = Expr("""unreserved_keyword""", """MINVALUE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2822(p):
    """unreserved_keyword : MODE"""
    p[0] = Expr("""unreserved_keyword""", """MODE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2823(p):
    """unreserved_keyword : MODEL"""
    p[0] = Expr("""unreserved_keyword""", """MODEL""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2824(p):
    """unreserved_keyword : MOVE"""
    p[0] = Expr("""unreserved_keyword""", """MOVE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2825(p):
    """unreserved_keyword : MOVEOUT"""
    p[0] = Expr("""unreserved_keyword""", """MOVEOUT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2826(p):
    """unreserved_keyword : NAME_P"""
    p[0] = Expr("""unreserved_keyword""", """NAME_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2827(p):
    """unreserved_keyword : NATIVE"""
    p[0] = Expr("""unreserved_keyword""", """NATIVE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2828(p):
    """unreserved_keyword : NETWORK"""
    p[0] = Expr("""unreserved_keyword""", """NETWORK""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2829(p):
    """unreserved_keyword : NEXT"""
    p[0] = Expr("""unreserved_keyword""", """NEXT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2830(p):
    """unreserved_keyword : NO"""
    p[0] = Expr("""unreserved_keyword""", """NO""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2831(p):
    """unreserved_keyword : NOCREATEDB"""
    p[0] = Expr("""unreserved_keyword""", """NOCREATEDB""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2832(p):
    """unreserved_keyword : NOCREATEUSER"""
    p[0] = Expr("""unreserved_keyword""", """NOCREATEUSER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2833(p):
    """unreserved_keyword : NODE"""
    p[0] = Expr("""unreserved_keyword""", """NODE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2834(p):
    """unreserved_keyword : NODES"""
    p[0] = Expr("""unreserved_keyword""", """NODES""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2835(p):
    """unreserved_keyword : NOTHING"""
    p[0] = Expr("""unreserved_keyword""", """NOTHING""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2836(p):
    """unreserved_keyword : NOTIFIER"""
    p[0] = Expr("""unreserved_keyword""", """NOTIFIER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2837(p):
    """unreserved_keyword : NOTIFY"""
    p[0] = Expr("""unreserved_keyword""", """NOTIFY""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2838(p):
    """unreserved_keyword : NOWAIT"""
    p[0] = Expr("""unreserved_keyword""", """NOWAIT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2839(p):
    """unreserved_keyword : NULLCOLS"""
    p[0] = Expr("""unreserved_keyword""", """NULLCOLS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2840(p):
    """unreserved_keyword : NULLS"""
    p[0] = Expr("""unreserved_keyword""", """NULLS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2841(p):
    """unreserved_keyword : OBJECT_P"""
    p[0] = Expr("""unreserved_keyword""", """OBJECT_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2842(p):
    """unreserved_keyword : OCTETS"""
    p[0] = Expr("""unreserved_keyword""", """OCTETS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2843(p):
    """unreserved_keyword : OF"""
    p[0] = Expr("""unreserved_keyword""", """OF""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2844(p):
    """unreserved_keyword : OFF"""
    p[0] = Expr("""unreserved_keyword""", """OFF""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2845(p):
    """unreserved_keyword : OIDS"""
    p[0] = Expr("""unreserved_keyword""", """OIDS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2846(p):
    """unreserved_keyword : OPERATOR"""
    p[0] = Expr("""unreserved_keyword""", """OPERATOR""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2847(p):
    """unreserved_keyword : OPT"""
    p[0] = Expr("""unreserved_keyword""", """OPT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2848(p):
    """unreserved_keyword : OPTIMIZER"""
    p[0] = Expr("""unreserved_keyword""", """OPTIMIZER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2849(p):
    """unreserved_keyword : OPTION"""
    p[0] = Expr("""unreserved_keyword""", """OPTION""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2850(p):
    """unreserved_keyword : OPTVER"""
    p[0] = Expr("""unreserved_keyword""", """OPTVER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2851(p):
    """unreserved_keyword : ORC"""
    p[0] = Expr("""unreserved_keyword""", """ORC""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2852(p):
    """unreserved_keyword : OTHERS"""
    p[0] = Expr("""unreserved_keyword""", """OTHERS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2853(p):
    """unreserved_keyword : OWNER"""
    p[0] = Expr("""unreserved_keyword""", """OWNER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2854(p):
    """unreserved_keyword : PARAMETER"""
    p[0] = Expr("""unreserved_keyword""", """PARAMETER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2855(p):
    """unreserved_keyword : PARAMETERS"""
    p[0] = Expr("""unreserved_keyword""", """PARAMETERS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2856(p):
    """unreserved_keyword : PARQUET"""
    p[0] = Expr("""unreserved_keyword""", """PARQUET""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2857(p):
    """unreserved_keyword : PARSER"""
    p[0] = Expr("""unreserved_keyword""", """PARSER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2858(p):
    """unreserved_keyword : PARTIAL"""
    p[0] = Expr("""unreserved_keyword""", """PARTIAL""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2859(p):
    """unreserved_keyword : PARTITION"""
    p[0] = Expr("""unreserved_keyword""", """PARTITION""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2860(p):
    """unreserved_keyword : PARTITIONING"""
    p[0] = Expr("""unreserved_keyword""", """PARTITIONING""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2861(p):
    """unreserved_keyword : PASSWORD"""
    p[0] = Expr("""unreserved_keyword""", """PASSWORD""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2862(p):
    """unreserved_keyword : PASSWORD_GRACE_TIME"""
    p[0] = Expr("""unreserved_keyword""", """PASSWORD_GRACE_TIME""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2863(p):
    """unreserved_keyword : PASSWORD_LIFE_TIME"""
    p[0] = Expr("""unreserved_keyword""", """PASSWORD_LIFE_TIME""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2864(p):
    """unreserved_keyword : PASSWORD_LOCK_TIME"""
    p[0] = Expr("""unreserved_keyword""", """PASSWORD_LOCK_TIME""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2865(p):
    """unreserved_keyword : PASSWORD_REUSE_TIME"""
    p[0] = Expr("""unreserved_keyword""", """PASSWORD_REUSE_TIME""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2866(p):
    """unreserved_keyword : PASSWORD_MAX_LENGTH"""
    p[0] = Expr("""unreserved_keyword""", """PASSWORD_MAX_LENGTH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2867(p):
    """unreserved_keyword : PASSWORD_MIN_DIGITS"""
    p[0] = Expr("""unreserved_keyword""", """PASSWORD_MIN_DIGITS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2868(p):
    """unreserved_keyword : PASSWORD_MIN_LENGTH"""
    p[0] = Expr("""unreserved_keyword""", """PASSWORD_MIN_LENGTH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2869(p):
    """unreserved_keyword : PASSWORD_MIN_LETTERS"""
    p[0] = Expr("""unreserved_keyword""", """PASSWORD_MIN_LETTERS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2870(p):
    """unreserved_keyword : PASSWORD_MIN_LOWERCASE_LETTERS"""
    p[0] = Expr("""unreserved_keyword""", """PASSWORD_MIN_LOWERCASE_LETTERS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2871(p):
    """unreserved_keyword : PASSWORD_MIN_SYMBOLS"""
    p[0] = Expr("""unreserved_keyword""", """PASSWORD_MIN_SYMBOLS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2872(p):
    """unreserved_keyword : PASSWORD_MIN_UPPERCASE_LETTERS"""
    p[0] = Expr("""unreserved_keyword""", """PASSWORD_MIN_UPPERCASE_LETTERS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2873(p):
    """unreserved_keyword : PASSWORD_REUSE_MAX"""
    p[0] = Expr("""unreserved_keyword""", """PASSWORD_REUSE_MAX""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2874(p):
    """unreserved_keyword : PATH"""
    p[0] = Expr("""unreserved_keyword""", """PATH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2875(p):
    """unreserved_keyword : PATTERN"""
    p[0] = Expr("""unreserved_keyword""", """PATTERN""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2876(p):
    """unreserved_keyword : PERCENT"""
    p[0] = Expr("""unreserved_keyword""", """PERCENT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2877(p):
    """unreserved_keyword : PERMANENT"""
    p[0] = Expr("""unreserved_keyword""", """PERMANENT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2878(p):
    """unreserved_keyword : PLACING"""
    p[0] = Expr("""unreserved_keyword""", """PLACING""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2879(p):
    """unreserved_keyword : PLANNEDCONCURRENCY"""
    p[0] = Expr("""unreserved_keyword""", """PLANNEDCONCURRENCY""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2880(p):
    """unreserved_keyword : POLICY"""
    p[0] = Expr("""unreserved_keyword""", """POLICY""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2881(p):
    """unreserved_keyword : POOL"""
    p[0] = Expr("""unreserved_keyword""", """POOL""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2882(p):
    """unreserved_keyword : PORT"""
    p[0] = Expr("""unreserved_keyword""", """PORT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2883(p):
    """unreserved_keyword : PRECEDING"""
    p[0] = Expr("""unreserved_keyword""", """PRECEDING""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2884(p):
    """unreserved_keyword : PREFER"""
    p[0] = Expr("""unreserved_keyword""", """PREFER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2885(p):
    """unreserved_keyword : PREPARE"""
    p[0] = Expr("""unreserved_keyword""", """PREPARE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2886(p):
    """unreserved_keyword : PREPASS"""
    p[0] = Expr("""unreserved_keyword""", """PREPASS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2887(p):
    """unreserved_keyword : PRESERVE"""
    p[0] = Expr("""unreserved_keyword""", """PRESERVE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2888(p):
    """unreserved_keyword : PREVIOUS_P"""
    p[0] = Expr("""unreserved_keyword""", """PREVIOUS_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2889(p):
    """unreserved_keyword : PRIOR"""
    p[0] = Expr("""unreserved_keyword""", """PRIOR""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2890(p):
    """unreserved_keyword : PRIORITY"""
    p[0] = Expr("""unreserved_keyword""", """PRIORITY""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2891(p):
    """unreserved_keyword : PRIVILEGES"""
    p[0] = Expr("""unreserved_keyword""", """PRIVILEGES""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2892(p):
    """unreserved_keyword : PROCEDURAL"""
    p[0] = Expr("""unreserved_keyword""", """PROCEDURAL""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2893(p):
    """unreserved_keyword : PROCEDURE"""
    p[0] = Expr("""unreserved_keyword""", """PROCEDURE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2894(p):
    """unreserved_keyword : PROFILE"""
    p[0] = Expr("""unreserved_keyword""", """PROFILE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2895(p):
    """unreserved_keyword : PROJECTION"""
    p[0] = Expr("""unreserved_keyword""", """PROJECTION""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2896(p):
    """unreserved_keyword : PROJECTIONS"""
    p[0] = Expr("""unreserved_keyword""", """PROJECTIONS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2897(p):
    """unreserved_keyword : PSDATE"""
    p[0] = Expr("""unreserved_keyword""", """PSDATE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2898(p):
    """unreserved_keyword : QUERY"""
    p[0] = Expr("""unreserved_keyword""", """QUERY""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2899(p):
    """unreserved_keyword : QUEUETIMEOUT"""
    p[0] = Expr("""unreserved_keyword""", """QUEUETIMEOUT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2900(p):
    """unreserved_keyword : QUOTE"""
    p[0] = Expr("""unreserved_keyword""", """QUOTE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2901(p):
    """unreserved_keyword : RANDOM"""
    p[0] = Expr("""unreserved_keyword""", """RANDOM""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2902(p):
    """unreserved_keyword : RANGE"""
    p[0] = Expr("""unreserved_keyword""", """RANGE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2903(p):
    """unreserved_keyword : READ"""
    p[0] = Expr("""unreserved_keyword""", """READ""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2904(p):
    """unreserved_keyword : RECHECK"""
    p[0] = Expr("""unreserved_keyword""", """RECHECK""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2905(p):
    """unreserved_keyword : RECORD_P"""
    p[0] = Expr("""unreserved_keyword""", """RECORD_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2906(p):
    """unreserved_keyword : RECOVER"""
    p[0] = Expr("""unreserved_keyword""", """RECOVER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2907(p):
    """unreserved_keyword : RECURSIVE"""
    p[0] = Expr("""unreserved_keyword""", """RECURSIVE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2908(p):
    """unreserved_keyword : REFRESH"""
    p[0] = Expr("""unreserved_keyword""", """REFRESH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2909(p):
    """unreserved_keyword : REINDEX"""
    p[0] = Expr("""unreserved_keyword""", """REINDEX""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2910(p):
    """unreserved_keyword : REJECTED_P"""
    p[0] = Expr("""unreserved_keyword""", """REJECTED_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2911(p):
    """unreserved_keyword : REJECTMAX"""
    p[0] = Expr("""unreserved_keyword""", """REJECTMAX""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2912(p):
    """unreserved_keyword : RELATIVE_P"""
    p[0] = Expr("""unreserved_keyword""", """RELATIVE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2913(p):
    """unreserved_keyword : RELEASE"""
    p[0] = Expr("""unreserved_keyword""", """RELEASE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2914(p):
    """unreserved_keyword : REMOVE"""
    p[0] = Expr("""unreserved_keyword""", """REMOVE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2915(p):
    """unreserved_keyword : RENAME"""
    p[0] = Expr("""unreserved_keyword""", """RENAME""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2916(p):
    """unreserved_keyword : REORGANIZE"""
    p[0] = Expr("""unreserved_keyword""", """REORGANIZE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2917(p):
    """unreserved_keyword : REPEATABLE"""
    p[0] = Expr("""unreserved_keyword""", """REPEATABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2918(p):
    """unreserved_keyword : REPLACE"""
    p[0] = Expr("""unreserved_keyword""", """REPLACE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2919(p):
    """unreserved_keyword : RESET"""
    p[0] = Expr("""unreserved_keyword""", """RESET""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2920(p):
    """unreserved_keyword : RESOURCE"""
    p[0] = Expr("""unreserved_keyword""", """RESOURCE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2921(p):
    """unreserved_keyword : RESTART"""
    p[0] = Expr("""unreserved_keyword""", """RESTART""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2922(p):
    """unreserved_keyword : RESTRICT"""
    p[0] = Expr("""unreserved_keyword""", """RESTRICT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2923(p):
    """unreserved_keyword : RESULTS"""
    p[0] = Expr("""unreserved_keyword""", """RESULTS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2924(p):
    """unreserved_keyword : RETURN"""
    p[0] = Expr("""unreserved_keyword""", """RETURN""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2925(p):
    """unreserved_keyword : RETURNREJECTED"""
    p[0] = Expr("""unreserved_keyword""", """RETURNREJECTED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2926(p):
    """unreserved_keyword : REVOKE"""
    p[0] = Expr("""unreserved_keyword""", """REVOKE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2927(p):
    """unreserved_keyword : RLE"""
    p[0] = Expr("""unreserved_keyword""", """RLE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2928(p):
    """unreserved_keyword : ROLE"""
    p[0] = Expr("""unreserved_keyword""", """ROLE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2929(p):
    """unreserved_keyword : ROLES"""
    p[0] = Expr("""unreserved_keyword""", """ROLES""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2930(p):
    """unreserved_keyword : ROLLBACK_P"""
    p[0] = Expr("""unreserved_keyword""", """ROLLBACK_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2931(p):
    """unreserved_keyword : ROLLUP"""
    p[0] = Expr("""unreserved_keyword""", """ROLLUP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2932(p):
    """unreserved_keyword : ROUTE"""
    p[0] = Expr("""unreserved_keyword""", """ROUTE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2933(p):
    """unreserved_keyword : ROUTING"""
    p[0] = Expr("""unreserved_keyword""", """ROUTING""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2934(p):
    """unreserved_keyword : ROWS"""
    p[0] = Expr("""unreserved_keyword""", """ROWS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2935(p):
    """unreserved_keyword : RULE"""
    p[0] = Expr("""unreserved_keyword""", """RULE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2936(p):
    """unreserved_keyword : RUNTIMECAP"""
    p[0] = Expr("""unreserved_keyword""", """RUNTIMECAP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2937(p):
    """unreserved_keyword : RUNTIMEPRIORITY"""
    p[0] = Expr("""unreserved_keyword""", """RUNTIMEPRIORITY""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2938(p):
    """unreserved_keyword : RUNTIMETHRESHOLD"""
    p[0] = Expr("""unreserved_keyword""", """RUNTIMETHRESHOLD""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2939(p):
    """unreserved_keyword : SAVE"""
    p[0] = Expr("""unreserved_keyword""", """SAVE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2940(p):
    """unreserved_keyword : SAVEPOINT"""
    p[0] = Expr("""unreserved_keyword""", """SAVEPOINT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2941(p):
    """unreserved_keyword : SCROLL"""
    p[0] = Expr("""unreserved_keyword""", """SCROLL""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2942(p):
    """unreserved_keyword : SEARCH_PATH"""
    p[0] = Expr("""unreserved_keyword""", """SEARCH_PATH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2943(p):
    """unreserved_keyword : SECONDS_P"""
    p[0] = Expr("""unreserved_keyword""", """SECONDS_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2944(p):
    """unreserved_keyword : SECURITY"""
    p[0] = Expr("""unreserved_keyword""", """SECURITY""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2945(p):
    """unreserved_keyword : SECURITY_ALGORITHM"""
    p[0] = Expr("""unreserved_keyword""", """SECURITY_ALGORITHM""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2946(p):
    """unreserved_keyword : SEQUENCE"""
    p[0] = Expr("""unreserved_keyword""", """SEQUENCE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2947(p):
    """unreserved_keyword : SEQUENCES"""
    p[0] = Expr("""unreserved_keyword""", """SEQUENCES""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2948(p):
    """unreserved_keyword : SERIALIZABLE"""
    p[0] = Expr("""unreserved_keyword""", """SERIALIZABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2949(p):
    """unreserved_keyword : SESSION"""
    p[0] = Expr("""unreserved_keyword""", """SESSION""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2950(p):
    """unreserved_keyword : SET"""
    p[0] = Expr("""unreserved_keyword""", """SET""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2951(p):
    """unreserved_keyword : SETS"""
    p[0] = Expr("""unreserved_keyword""", """SETS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2952(p):
    """unreserved_keyword : SHARE"""
    p[0] = Expr("""unreserved_keyword""", """SHARE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2953(p):
    """unreserved_keyword : SHARED"""
    p[0] = Expr("""unreserved_keyword""", """SHARED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2954(p):
    """unreserved_keyword : SHOW"""
    p[0] = Expr("""unreserved_keyword""", """SHOW""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2955(p):
    """unreserved_keyword : SIMPLE"""
    p[0] = Expr("""unreserved_keyword""", """SIMPLE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2956(p):
    """unreserved_keyword : SINGLEINITIATOR"""
    p[0] = Expr("""unreserved_keyword""", """SINGLEINITIATOR""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2957(p):
    """unreserved_keyword : SKIP"""
    p[0] = Expr("""unreserved_keyword""", """SKIP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2958(p):
    """unreserved_keyword : SOURCE"""
    p[0] = Expr("""unreserved_keyword""", """SOURCE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2959(p):
    """unreserved_keyword : SPLIT"""
    p[0] = Expr("""unreserved_keyword""", """SPLIT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2960(p):
    """unreserved_keyword : SSL_CONFIG"""
    p[0] = Expr("""unreserved_keyword""", """SSL_CONFIG""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2961(p):
    """unreserved_keyword : STABLE"""
    p[0] = Expr("""unreserved_keyword""", """STABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2962(p):
    """unreserved_keyword : STANDBY"""
    p[0] = Expr("""unreserved_keyword""", """STANDBY""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2963(p):
    """unreserved_keyword : START"""
    p[0] = Expr("""unreserved_keyword""", """START""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2964(p):
    """unreserved_keyword : STATEMENT"""
    p[0] = Expr("""unreserved_keyword""", """STATEMENT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2965(p):
    """unreserved_keyword : STATISTICS"""
    p[0] = Expr("""unreserved_keyword""", """STATISTICS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2966(p):
    """unreserved_keyword : STDIN"""
    p[0] = Expr("""unreserved_keyword""", """STDIN""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2967(p):
    """unreserved_keyword : STDOUT"""
    p[0] = Expr("""unreserved_keyword""", """STDOUT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2968(p):
    """unreserved_keyword : STEMMER"""
    p[0] = Expr("""unreserved_keyword""", """STEMMER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2969(p):
    """unreserved_keyword : STORAGE"""
    p[0] = Expr("""unreserved_keyword""", """STORAGE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2970(p):
    """unreserved_keyword : STREAM_P"""
    p[0] = Expr("""unreserved_keyword""", """STREAM_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2971(p):
    """unreserved_keyword : STRENGTH"""
    p[0] = Expr("""unreserved_keyword""", """STRENGTH""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2972(p):
    """unreserved_keyword : STRICT_P"""
    p[0] = Expr("""unreserved_keyword""", """STRICT_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2973(p):
    """unreserved_keyword : SUBNET"""
    p[0] = Expr("""unreserved_keyword""", """SUBNET""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2974(p):
    """unreserved_keyword : SYSID"""
    p[0] = Expr("""unreserved_keyword""", """SYSID""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2975(p):
    """unreserved_keyword : SYSTEM"""
    p[0] = Expr("""unreserved_keyword""", """SYSTEM""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2976(p):
    """unreserved_keyword : TABLES"""
    p[0] = Expr("""unreserved_keyword""", """TABLES""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2977(p):
    """unreserved_keyword : TABLESPACE"""
    p[0] = Expr("""unreserved_keyword""", """TABLESPACE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2978(p):
    """unreserved_keyword : TEMP"""
    p[0] = Expr("""unreserved_keyword""", """TEMP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2979(p):
    """unreserved_keyword : TEMPLATE"""
    p[0] = Expr("""unreserved_keyword""", """TEMPLATE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2980(p):
    """unreserved_keyword : TEMPORARY"""
    p[0] = Expr("""unreserved_keyword""", """TEMPORARY""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2981(p):
    """unreserved_keyword : TEMPSPACECAP"""
    p[0] = Expr("""unreserved_keyword""", """TEMPSPACECAP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2982(p):
    """unreserved_keyword : TERMINATOR_P"""
    p[0] = Expr("""unreserved_keyword""", """TERMINATOR_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2983(p):
    """unreserved_keyword : TEXT"""
    p[0] = Expr("""unreserved_keyword""", """TEXT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2984(p):
    """unreserved_keyword : THAN"""
    p[0] = Expr("""unreserved_keyword""", """THAN""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2985(p):
    """unreserved_keyword : TIES"""
    p[0] = Expr("""unreserved_keyword""", """TIES""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2986(p):
    """unreserved_keyword : TLS"""
    p[0] = Expr("""unreserved_keyword""", """TLS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2987(p):
    """unreserved_keyword : TLSMODE"""
    p[0] = Expr("""unreserved_keyword""", """TLSMODE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2988(p):
    """unreserved_keyword : TOAST"""
    p[0] = Expr("""unreserved_keyword""", """TOAST""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2989(p):
    """unreserved_keyword : TOLERANCE"""
    p[0] = Expr("""unreserved_keyword""", """TOLERANCE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2990(p):
    """unreserved_keyword : TOKENIZER"""
    p[0] = Expr("""unreserved_keyword""", """TOKENIZER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2991(p):
    """unreserved_keyword : TRANSACTION"""
    p[0] = Expr("""unreserved_keyword""", """TRANSACTION""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2992(p):
    """unreserved_keyword : TRANSFORM"""
    p[0] = Expr("""unreserved_keyword""", """TRANSFORM""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2993(p):
    """unreserved_keyword : TRICKLE"""
    p[0] = Expr("""unreserved_keyword""", """TRICKLE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2994(p):
    """unreserved_keyword : TRIGGER"""
    p[0] = Expr("""unreserved_keyword""", """TRIGGER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2995(p):
    """unreserved_keyword : TRUNCATE"""
    p[0] = Expr("""unreserved_keyword""", """TRUNCATE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2996(p):
    """unreserved_keyword : TRUSTED"""
    p[0] = Expr("""unreserved_keyword""", """TRUSTED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2997(p):
    """unreserved_keyword : TUNING"""
    p[0] = Expr("""unreserved_keyword""", """TUNING""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2998(p):
    """unreserved_keyword : TYPE_P"""
    p[0] = Expr("""unreserved_keyword""", """TYPE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_2999(p):
    """unreserved_keyword : UDPARAMETER"""
    p[0] = Expr("""unreserved_keyword""", """UDPARAMETER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3000(p):
    """unreserved_keyword : UNCOMMITTED"""
    p[0] = Expr("""unreserved_keyword""", """UNCOMMITTED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3001(p):
    """unreserved_keyword : UNCOMPRESSED"""
    p[0] = Expr("""unreserved_keyword""", """UNCOMPRESSED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3002(p):
    """unreserved_keyword : UNINDEXED"""
    p[0] = Expr("""unreserved_keyword""", """UNINDEXED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3003(p):
    """unreserved_keyword : UNKNOWN"""
    p[0] = Expr("""unreserved_keyword""", """UNKNOWN""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3004(p):
    """unreserved_keyword : UNLIMITED"""
    p[0] = Expr("""unreserved_keyword""", """UNLIMITED""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3005(p):
    """unreserved_keyword : UNLISTEN"""
    p[0] = Expr("""unreserved_keyword""", """UNLISTEN""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3006(p):
    """unreserved_keyword : UNLOCK_P"""
    p[0] = Expr("""unreserved_keyword""", """UNLOCK_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3007(p):
    """unreserved_keyword : UNPACKER"""
    p[0] = Expr("""unreserved_keyword""", """UNPACKER""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3008(p):
    """unreserved_keyword : UPDATE"""
    p[0] = Expr("""unreserved_keyword""", """UPDATE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3009(p):
    """unreserved_keyword : USAGE"""
    p[0] = Expr("""unreserved_keyword""", """USAGE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3010(p):
    """unreserved_keyword : VACUUM"""
    p[0] = Expr("""unreserved_keyword""", """VACUUM""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3011(p):
    """unreserved_keyword : VALIDATE"""
    p[0] = Expr("""unreserved_keyword""", """VALIDATE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3012(p):
    """unreserved_keyword : VALIDATOR"""
    p[0] = Expr("""unreserved_keyword""", """VALIDATOR""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3013(p):
    """unreserved_keyword : VALUE_P"""
    p[0] = Expr("""unreserved_keyword""", """VALUE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3014(p):
    """unreserved_keyword : VALUES"""
    p[0] = Expr("""unreserved_keyword""", """VALUES""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3015(p):
    """unreserved_keyword : VERBOSE"""
    p[0] = Expr("""unreserved_keyword""", """VERBOSE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3016(p):
    """unreserved_keyword : VERTICA"""
    p[0] = Expr("""unreserved_keyword""", """VERTICA""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3017(p):
    """unreserved_keyword : VIEW"""
    p[0] = Expr("""unreserved_keyword""", """VIEW""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3018(p):
    """unreserved_keyword : VOLATILE"""
    p[0] = Expr("""unreserved_keyword""", """VOLATILE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3019(p):
    """unreserved_keyword : WAIT"""
    p[0] = Expr("""unreserved_keyword""", """WAIT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3020(p):
    """unreserved_keyword : WEBHDFS_ADDRESS"""
    p[0] = Expr("""unreserved_keyword""", """WEBHDFS_ADDRESS""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3021(p):
    """unreserved_keyword : WEBSERVICE_HOSTNAME"""
    p[0] = Expr("""unreserved_keyword""", """WEBSERVICE_HOSTNAME""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3022(p):
    """unreserved_keyword : WEBSERVICE_PORT"""
    p[0] = Expr("""unreserved_keyword""", """WEBSERVICE_PORT""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3023(p):
    """unreserved_keyword : WORK"""
    p[0] = Expr("""unreserved_keyword""", """WORK""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3024(p):
    """unreserved_keyword : WRITE"""
    p[0] = Expr("""unreserved_keyword""", """WRITE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3025(p):
    """unreserved_keyword : ZONE"""
    p[0] = Expr("""unreserved_keyword""", """ZONE""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3026(p):
    """unreserved_keyword : ZSTD"""
    p[0] = Expr("""unreserved_keyword""", """ZSTD""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3027(p):
    """unreserved_keyword : ZSTD_COMP"""
    p[0] = Expr("""unreserved_keyword""", """ZSTD_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3028(p):
    """unreserved_keyword : ZSTD_FAST_COMP"""
    p[0] = Expr("""unreserved_keyword""", """ZSTD_FAST_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_unreserved_keyword_3029(p):
    """unreserved_keyword : ZSTD_HIGH_COMP"""
    p[0] = Expr("""unreserved_keyword""", """ZSTD_HIGH_COMP""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3030(p):
    """bare_col_alias_excluded_keyword : ASSERTION"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """ASSERTION""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3031(p):
    """bare_col_alias_excluded_keyword : DAY_P"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """DAY_P""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3032(p):
    """bare_col_alias_excluded_keyword : HOUR_P"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """HOUR_P""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3033(p):
    """bare_col_alias_excluded_keyword : ILIKE"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """ILIKE""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3034(p):
    """bare_col_alias_excluded_keyword : ILIKEB"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """ILIKEB""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3035(p):
    """bare_col_alias_excluded_keyword : INTERPOLATE"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """INTERPOLATE""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3036(p):
    """bare_col_alias_excluded_keyword : ISNULL"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """ISNULL""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3037(p):
    """bare_col_alias_excluded_keyword : LIKEB"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """LIKEB""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3038(p):
    """bare_col_alias_excluded_keyword : MINUTE_P"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """MINUTE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3039(p):
    """bare_col_alias_excluded_keyword : MONTH_P"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """MONTH_P""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3040(p):
    """bare_col_alias_excluded_keyword : NOTNULL"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """NOTNULL""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3041(p):
    """bare_col_alias_excluded_keyword : SECOND_P"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """SECOND_P""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3042(p):
    """bare_col_alias_excluded_keyword : VARYING"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """VARYING""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3043(p):
    """bare_col_alias_excluded_keyword : WITHOUT"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """WITHOUT""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_alias_excluded_keyword_3044(p):
    """bare_col_alias_excluded_keyword : YEAR_P"""
    p[0] = Expr("""bare_col_alias_excluded_keyword""", """YEAR_P""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_rel_alias_excl_keyword_3045(p):
    """bare_col_rel_alias_excl_keyword : ENCODED"""
    p[0] = Expr("""bare_col_rel_alias_excl_keyword""", """ENCODED""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_rel_alias_excl_keyword_3046(p):
    """bare_col_rel_alias_excl_keyword : KSAFE"""
    p[0] = Expr("""bare_col_rel_alias_excl_keyword""", """KSAFE""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_rel_alias_excl_keyword_3047(p):
    """bare_col_rel_alias_excl_keyword : MINUS"""
    p[0] = Expr("""bare_col_rel_alias_excl_keyword""", """MINUS""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_rel_alias_excl_keyword_3048(p):
    """bare_col_rel_alias_excl_keyword : PINNED"""
    p[0] = Expr("""bare_col_rel_alias_excl_keyword""", """PINNED""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_rel_alias_excl_keyword_3049(p):
    """bare_col_rel_alias_excl_keyword : SEGMENTED"""
    p[0] = Expr("""bare_col_rel_alias_excl_keyword""", """SEGMENTED""", p[1:] if len(p or []) > 1 else [], p)


def p_bare_col_rel_alias_excl_keyword_3050(p):
    """bare_col_rel_alias_excl_keyword : UNSEGMENTED"""
    p[0] = Expr("""bare_col_rel_alias_excl_keyword""", """UNSEGMENTED""", p[1:] if len(p or []) > 1 else [], p)


def p_func_excluded_keyword_3051(p):
    """func_excluded_keyword : DATEDIFF"""
    p[0] = Expr("""func_excluded_keyword""", """DATEDIFF""", p[1:] if len(p or []) > 1 else [], p)


def p_func_excluded_keyword_3052(p):
    """func_excluded_keyword : DECODE"""
    p[0] = Expr("""func_excluded_keyword""", """DECODE""", p[1:] if len(p or []) > 1 else [], p)


def p_func_excluded_keyword_3053(p):
    """func_excluded_keyword : TIMESTAMPADD"""
    p[0] = Expr("""func_excluded_keyword""", """TIMESTAMPADD""", p[1:] if len(p or []) > 1 else [], p)


def p_func_excluded_keyword_3054(p):
    """func_excluded_keyword : TIMESTAMPDIFF"""
    p[0] = Expr("""func_excluded_keyword""", """TIMESTAMPDIFF""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3055(p):
    """type_excluded_keyword : ACCESSRANK"""
    p[0] = Expr("""type_excluded_keyword""", """ACCESSRANK""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3056(p):
    """type_excluded_keyword : AUTO_INC"""
    p[0] = Expr("""type_excluded_keyword""", """AUTO_INC""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3057(p):
    """type_excluded_keyword : BIGINT"""
    p[0] = Expr("""type_excluded_keyword""", """BIGINT""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3058(p):
    """type_excluded_keyword : BIT"""
    p[0] = Expr("""type_excluded_keyword""", """BIT""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3059(p):
    """type_excluded_keyword : BYTEA"""
    p[0] = Expr("""type_excluded_keyword""", """BYTEA""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3060(p):
    """type_excluded_keyword : BOOLEAN_P"""
    p[0] = Expr("""type_excluded_keyword""", """BOOLEAN_P""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3061(p):
    """type_excluded_keyword : CHAR_P"""
    p[0] = Expr("""type_excluded_keyword""", """CHAR_P""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3062(p):
    """type_excluded_keyword : CHARACTER"""
    p[0] = Expr("""type_excluded_keyword""", """CHARACTER""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3063(p):
    """type_excluded_keyword : DATETIME"""
    p[0] = Expr("""type_excluded_keyword""", """DATETIME""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3064(p):
    """type_excluded_keyword : DEC"""
    p[0] = Expr("""type_excluded_keyword""", """DEC""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3065(p):
    """type_excluded_keyword : DECIMAL_P"""
    p[0] = Expr("""type_excluded_keyword""", """DECIMAL_P""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3066(p):
    """type_excluded_keyword : FLOAT_P"""
    p[0] = Expr("""type_excluded_keyword""", """FLOAT_P""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3067(p):
    """type_excluded_keyword : IDENTITY_P"""
    p[0] = Expr("""type_excluded_keyword""", """IDENTITY_P""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3068(p):
    """type_excluded_keyword : INT_P"""
    p[0] = Expr("""type_excluded_keyword""", """INT_P""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3069(p):
    """type_excluded_keyword : INTEGER"""
    p[0] = Expr("""type_excluded_keyword""", """INTEGER""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3070(p):
    """type_excluded_keyword : LONG"""
    p[0] = Expr("""type_excluded_keyword""", """LONG""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3071(p):
    """type_excluded_keyword : MONEY"""
    p[0] = Expr("""type_excluded_keyword""", """MONEY""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3072(p):
    """type_excluded_keyword : NATIONAL"""
    p[0] = Expr("""type_excluded_keyword""", """NATIONAL""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3073(p):
    """type_excluded_keyword : NCHAR"""
    p[0] = Expr("""type_excluded_keyword""", """NCHAR""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3074(p):
    """type_excluded_keyword : NUMBER_P"""
    p[0] = Expr("""type_excluded_keyword""", """NUMBER_P""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3075(p):
    """type_excluded_keyword : NUMERIC"""
    p[0] = Expr("""type_excluded_keyword""", """NUMERIC""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3076(p):
    """type_excluded_keyword : RAW"""
    p[0] = Expr("""type_excluded_keyword""", """RAW""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3077(p):
    """type_excluded_keyword : REAL"""
    p[0] = Expr("""type_excluded_keyword""", """REAL""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3078(p):
    """type_excluded_keyword : SETOF"""
    p[0] = Expr("""type_excluded_keyword""", """SETOF""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3079(p):
    """type_excluded_keyword : SMALLDATETIME"""
    p[0] = Expr("""type_excluded_keyword""", """SMALLDATETIME""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3080(p):
    """type_excluded_keyword : SMALLINT"""
    p[0] = Expr("""type_excluded_keyword""", """SMALLINT""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3081(p):
    """type_excluded_keyword : TIME"""
    p[0] = Expr("""type_excluded_keyword""", """TIME""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3082(p):
    """type_excluded_keyword : TIMESTAMP"""
    p[0] = Expr("""type_excluded_keyword""", """TIMESTAMP""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3083(p):
    """type_excluded_keyword : TIMESTAMPTZ"""
    p[0] = Expr("""type_excluded_keyword""", """TIMESTAMPTZ""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3084(p):
    """type_excluded_keyword : TIMETZ"""
    p[0] = Expr("""type_excluded_keyword""", """TIMETZ""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3085(p):
    """type_excluded_keyword : TINYINT"""
    p[0] = Expr("""type_excluded_keyword""", """TINYINT""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3086(p):
    """type_excluded_keyword : UUID"""
    p[0] = Expr("""type_excluded_keyword""", """UUID""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3087(p):
    """type_excluded_keyword : VALINDEX"""
    p[0] = Expr("""type_excluded_keyword""", """VALINDEX""", p[1:] if len(p or []) > 1 else [], p)


def p_type_excluded_keyword_3088(p):
    """type_excluded_keyword : VARCHAR2"""
    p[0] = Expr("""type_excluded_keyword""", """VARCHAR2""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3089(p):
    """col_name_keyword : CHAR_LENGTH"""
    p[0] = Expr("""col_name_keyword""", """CHAR_LENGTH""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3090(p):
    """col_name_keyword : CHARACTER_LENGTH"""
    p[0] = Expr("""col_name_keyword""", """CHARACTER_LENGTH""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3091(p):
    """col_name_keyword : EXISTS"""
    p[0] = Expr("""col_name_keyword""", """EXISTS""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3092(p):
    """col_name_keyword : EXTRACT"""
    p[0] = Expr("""col_name_keyword""", """EXTRACT""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3093(p):
    """col_name_keyword : INOUT"""
    p[0] = Expr("""col_name_keyword""", """INOUT""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3094(p):
    """col_name_keyword : NONE"""
    p[0] = Expr("""col_name_keyword""", """NONE""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3095(p):
    """col_name_keyword : OUT_P"""
    p[0] = Expr("""col_name_keyword""", """OUT_P""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3096(p):
    """col_name_keyword : OVERLAY"""
    p[0] = Expr("""col_name_keyword""", """OVERLAY""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3097(p):
    """col_name_keyword : POSITION"""
    p[0] = Expr("""col_name_keyword""", """POSITION""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3098(p):
    """col_name_keyword : PRECISION"""
    p[0] = Expr("""col_name_keyword""", """PRECISION""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3099(p):
    """col_name_keyword : ROW"""
    p[0] = Expr("""col_name_keyword""", """ROW""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3100(p):
    """col_name_keyword : SUBSTRING"""
    p[0] = Expr("""col_name_keyword""", """SUBSTRING""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3101(p):
    """col_name_keyword : TIMEZONE"""
    p[0] = Expr("""col_name_keyword""", """TIMEZONE""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3102(p):
    """col_name_keyword : TREAT"""
    p[0] = Expr("""col_name_keyword""", """TREAT""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3103(p):
    """col_name_keyword : TRIM"""
    p[0] = Expr("""col_name_keyword""", """TRIM""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3104(p):
    """col_name_keyword : VARBINARY"""
    p[0] = Expr("""col_name_keyword""", """VARBINARY""", p[1:] if len(p or []) > 1 else [], p)


def p_col_name_keyword_3105(p):
    """col_name_keyword : VARCHAR"""
    p[0] = Expr("""col_name_keyword""", """VARCHAR""", p[1:] if len(p or []) > 1 else [], p)


def p_func_name_keyword_3106(p):
    """func_name_keyword : AUTHORIZATION"""
    p[0] = Expr("""func_name_keyword""", """AUTHORIZATION""", p[1:] if len(p or []) > 1 else [], p)


def p_func_name_keyword_3107(p):
    """func_name_keyword : BETWEEN"""
    p[0] = Expr("""func_name_keyword""", """BETWEEN""", p[1:] if len(p or []) > 1 else [], p)


def p_func_name_keyword_3108(p):
    """func_name_keyword : CORRELATION"""
    p[0] = Expr("""func_name_keyword""", """CORRELATION""", p[1:] if len(p or []) > 1 else [], p)


def p_func_name_keyword_3109(p):
    """func_name_keyword : IS"""
    p[0] = Expr("""func_name_keyword""", """IS""", p[1:] if len(p or []) > 1 else [], p)


def p_func_name_keyword_3110(p):
    """func_name_keyword : LIKE"""
    p[0] = Expr("""func_name_keyword""", """LIKE""", p[1:] if len(p or []) > 1 else [], p)


def p_func_name_keyword_3111(p):
    """func_name_keyword : LIMIT"""
    p[0] = Expr("""func_name_keyword""", """LIMIT""", p[1:] if len(p or []) > 1 else [], p)


def p_func_name_keyword_3112(p):
    """func_name_keyword : OVER"""
    p[0] = Expr("""func_name_keyword""", """OVER""", p[1:] if len(p or []) > 1 else [], p)


def p_func_name_keyword_3113(p):
    """func_name_keyword : OVERLAPS"""
    p[0] = Expr("""func_name_keyword""", """OVERLAPS""", p[1:] if len(p or []) > 1 else [], p)


def p_func_name_keyword_3114(p):
    """func_name_keyword : SIMILAR"""
    p[0] = Expr("""func_name_keyword""", """SIMILAR""", p[1:] if len(p or []) > 1 else [], p)


def p_func_name_keyword_3115(p):
    """func_name_keyword : TIMESERIES"""
    p[0] = Expr("""func_name_keyword""", """TIMESERIES""", p[1:] if len(p or []) > 1 else [], p)


def p_func_name_keyword_3116(p):
    """func_name_keyword : UNBOUNDED"""
    p[0] = Expr("""func_name_keyword""", """UNBOUNDED""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3117(p):
    """reserved_keyword : ALL"""
    p[0] = Expr("""reserved_keyword""", """ALL""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3118(p):
    """reserved_keyword : AND"""
    p[0] = Expr("""reserved_keyword""", """AND""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3119(p):
    """reserved_keyword : ANY"""
    p[0] = Expr("""reserved_keyword""", """ANY""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3120(p):
    """reserved_keyword : ARRAY"""
    p[0] = Expr("""reserved_keyword""", """ARRAY""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3121(p):
    """reserved_keyword : AS"""
    p[0] = Expr("""reserved_keyword""", """AS""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3122(p):
    """reserved_keyword : ASC"""
    p[0] = Expr("""reserved_keyword""", """ASC""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3123(p):
    """reserved_keyword : BINARY"""
    p[0] = Expr("""reserved_keyword""", """BINARY""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3124(p):
    """reserved_keyword : BOTH"""
    p[0] = Expr("""reserved_keyword""", """BOTH""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3125(p):
    """reserved_keyword : CASE"""
    p[0] = Expr("""reserved_keyword""", """CASE""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3126(p):
    """reserved_keyword : CAST"""
    p[0] = Expr("""reserved_keyword""", """CAST""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3127(p):
    """reserved_keyword : CHECK"""
    p[0] = Expr("""reserved_keyword""", """CHECK""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3128(p):
    """reserved_keyword : COLLATE"""
    p[0] = Expr("""reserved_keyword""", """COLLATE""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3129(p):
    """reserved_keyword : COLUMN"""
    p[0] = Expr("""reserved_keyword""", """COLUMN""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3130(p):
    """reserved_keyword : CONSTRAINT"""
    p[0] = Expr("""reserved_keyword""", """CONSTRAINT""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3131(p):
    """reserved_keyword : CREATE"""
    p[0] = Expr("""reserved_keyword""", """CREATE""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3132(p):
    """reserved_keyword : CURRENT_DATABASE"""
    p[0] = Expr("""reserved_keyword""", """CURRENT_DATABASE""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3133(p):
    """reserved_keyword : CURRENT_DATE"""
    p[0] = Expr("""reserved_keyword""", """CURRENT_DATE""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3134(p):
    """reserved_keyword : CURRENT_SCHEMA"""
    p[0] = Expr("""reserved_keyword""", """CURRENT_SCHEMA""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3135(p):
    """reserved_keyword : CURRENT_TIME"""
    p[0] = Expr("""reserved_keyword""", """CURRENT_TIME""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3136(p):
    """reserved_keyword : CURRENT_TIMESTAMP"""
    p[0] = Expr("""reserved_keyword""", """CURRENT_TIMESTAMP""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3137(p):
    """reserved_keyword : CURRENT_USER"""
    p[0] = Expr("""reserved_keyword""", """CURRENT_USER""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3138(p):
    """reserved_keyword : DEFAULT"""
    p[0] = Expr("""reserved_keyword""", """DEFAULT""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3139(p):
    """reserved_keyword : DEFERRABLE"""
    p[0] = Expr("""reserved_keyword""", """DEFERRABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3140(p):
    """reserved_keyword : DESC"""
    p[0] = Expr("""reserved_keyword""", """DESC""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3141(p):
    """reserved_keyword : DISTINCT"""
    p[0] = Expr("""reserved_keyword""", """DISTINCT""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3142(p):
    """reserved_keyword : ELSE"""
    p[0] = Expr("""reserved_keyword""", """ELSE""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3143(p):
    """reserved_keyword : END_P"""
    p[0] = Expr("""reserved_keyword""", """END_P""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3144(p):
    """reserved_keyword : EXCEPT"""
    p[0] = Expr("""reserved_keyword""", """EXCEPT""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3145(p):
    """reserved_keyword : FALSE_P"""
    p[0] = Expr("""reserved_keyword""", """FALSE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3146(p):
    """reserved_keyword : FOR"""
    p[0] = Expr("""reserved_keyword""", """FOR""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3147(p):
    """reserved_keyword : FOREIGN"""
    p[0] = Expr("""reserved_keyword""", """FOREIGN""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3148(p):
    """reserved_keyword : FROM"""
    p[0] = Expr("""reserved_keyword""", """FROM""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3149(p):
    """reserved_keyword : GRANT"""
    p[0] = Expr("""reserved_keyword""", """GRANT""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3150(p):
    """reserved_keyword : GROUP_P"""
    p[0] = Expr("""reserved_keyword""", """GROUP_P""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3151(p):
    """reserved_keyword : HAVING"""
    p[0] = Expr("""reserved_keyword""", """HAVING""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3152(p):
    """reserved_keyword : IN_P"""
    p[0] = Expr("""reserved_keyword""", """IN_P""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3153(p):
    """reserved_keyword : INITIALLY"""
    p[0] = Expr("""reserved_keyword""", """INITIALLY""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3154(p):
    """reserved_keyword : INTERSECT"""
    p[0] = Expr("""reserved_keyword""", """INTERSECT""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3155(p):
    """reserved_keyword : INTERVAL"""
    p[0] = Expr("""reserved_keyword""", """INTERVAL""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3156(p):
    """reserved_keyword : INTERVALYM"""
    p[0] = Expr("""reserved_keyword""", """INTERVALYM""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3157(p):
    """reserved_keyword : INTO"""
    p[0] = Expr("""reserved_keyword""", """INTO""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3158(p):
    """reserved_keyword : LEADING"""
    p[0] = Expr("""reserved_keyword""", """LEADING""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3159(p):
    """reserved_keyword : LOCALTIME"""
    p[0] = Expr("""reserved_keyword""", """LOCALTIME""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3160(p):
    """reserved_keyword : LOCALTIMESTAMP"""
    p[0] = Expr("""reserved_keyword""", """LOCALTIMESTAMP""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3161(p):
    """reserved_keyword : MATCH"""
    p[0] = Expr("""reserved_keyword""", """MATCH""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3162(p):
    """reserved_keyword : NEW"""
    p[0] = Expr("""reserved_keyword""", """NEW""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3163(p):
    """reserved_keyword : NOT"""
    p[0] = Expr("""reserved_keyword""", """NOT""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3164(p):
    """reserved_keyword : NULL_P"""
    p[0] = Expr("""reserved_keyword""", """NULL_P""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3165(p):
    """reserved_keyword : NULLSEQUAL"""
    p[0] = Expr("""reserved_keyword""", """NULLSEQUAL""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3166(p):
    """reserved_keyword : OFFSET"""
    p[0] = Expr("""reserved_keyword""", """OFFSET""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3167(p):
    """reserved_keyword : OLD"""
    p[0] = Expr("""reserved_keyword""", """OLD""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3168(p):
    """reserved_keyword : ON"""
    p[0] = Expr("""reserved_keyword""", """ON""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3169(p):
    """reserved_keyword : ONLY"""
    p[0] = Expr("""reserved_keyword""", """ONLY""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3170(p):
    """reserved_keyword : OR"""
    p[0] = Expr("""reserved_keyword""", """OR""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3171(p):
    """reserved_keyword : ORDER"""
    p[0] = Expr("""reserved_keyword""", """ORDER""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3172(p):
    """reserved_keyword : PRIMARY"""
    p[0] = Expr("""reserved_keyword""", """PRIMARY""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3173(p):
    """reserved_keyword : REFERENCES"""
    p[0] = Expr("""reserved_keyword""", """REFERENCES""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3174(p):
    """reserved_keyword : SCHEMA"""
    p[0] = Expr("""reserved_keyword""", """SCHEMA""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3175(p):
    """reserved_keyword : SELECT"""
    p[0] = Expr("""reserved_keyword""", """SELECT""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3176(p):
    """reserved_keyword : SESSION_USER"""
    p[0] = Expr("""reserved_keyword""", """SESSION_USER""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3177(p):
    """reserved_keyword : SOME"""
    p[0] = Expr("""reserved_keyword""", """SOME""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3178(p):
    """reserved_keyword : SYSDATE"""
    p[0] = Expr("""reserved_keyword""", """SYSDATE""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3179(p):
    """reserved_keyword : TABLE"""
    p[0] = Expr("""reserved_keyword""", """TABLE""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3180(p):
    """reserved_keyword : THEN"""
    p[0] = Expr("""reserved_keyword""", """THEN""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3181(p):
    """reserved_keyword : TO"""
    p[0] = Expr("""reserved_keyword""", """TO""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3182(p):
    """reserved_keyword : TRAILING"""
    p[0] = Expr("""reserved_keyword""", """TRAILING""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3183(p):
    """reserved_keyword : TRUE_P"""
    p[0] = Expr("""reserved_keyword""", """TRUE_P""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3184(p):
    """reserved_keyword : UNION"""
    p[0] = Expr("""reserved_keyword""", """UNION""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3185(p):
    """reserved_keyword : UNIQUE"""
    p[0] = Expr("""reserved_keyword""", """UNIQUE""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3186(p):
    """reserved_keyword : USER"""
    p[0] = Expr("""reserved_keyword""", """USER""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3187(p):
    """reserved_keyword : USING"""
    p[0] = Expr("""reserved_keyword""", """USING""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3188(p):
    """reserved_keyword : WHEN"""
    p[0] = Expr("""reserved_keyword""", """WHEN""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3189(p):
    """reserved_keyword : WHERE"""
    p[0] = Expr("""reserved_keyword""", """WHERE""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3190(p):
    """reserved_keyword : WINDOW"""
    p[0] = Expr("""reserved_keyword""", """WINDOW""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3191(p):
    """reserved_keyword : WITH"""
    p[0] = Expr("""reserved_keyword""", """WITH""", p[1:] if len(p or []) > 1 else [], p)


def p_reserved_keyword_3192(p):
    """reserved_keyword : WITHIN"""
    p[0] = Expr("""reserved_keyword""", """WITHIN""", p[1:] if len(p or []) > 1 else [], p)


def p_SpecialRuleRelation_3193(p):
    """SpecialRuleRelation : OLD"""
    p[0] = Expr("""SpecialRuleRelation""", """OLD""", p[1:] if len(p or []) > 1 else [], p)


def p_SpecialRuleRelation_3194(p):
    """SpecialRuleRelation : NEW"""
    p[0] = Expr("""SpecialRuleRelation""", """NEW""", p[1:] if len(p or []) > 1 else [], p)


def p_CopyFromStaging(p):
    """a_stmt : COPY FROM IDENT SCONST"""
    p[0] = Expr("""a_stmt""", """COPY FROM IDENT SCONST""", p[1:] if len(p or []) > 1 else [], p)


# -------------- RULES END ----------------


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
            yacc.parse(content)
            # print_expr(yacc.parse(content))
    else:
        run_interactive()


