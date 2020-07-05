%{ /* Copyright (c) 2007 EntIT Software LLC, a Micro Focus company */

#define YYDEBUG 1
/*-------------------------------------------------------------------------
 *
 * gram.y
 *      POSTGRES SQL YACC rules/actions
 *
 * Portions Copyright (c) 1996-2005, PostgreSQL Global Development Group
 * Portions Copyright (c) 1994, Regents of the University of California
 *
 *
 * IDENTIFICATION
 *      $PostgreSQL: pgsql/src/backend/parser/gram.y,v 2.481 2004/12/31 22:00:27 pgsql Exp $
 *
 * HISTORY
 *      AUTHOR            DATE            MAJOR EVENT
 *      Andrew Yu            Sept, 1994        POSTQUEL to SQL conversion
 *      Andrew Yu            Oct, 1994        lispy code conversion
 *
 * NOTES
 *      CAPITALS are used to represent terminal symbols.
 *      non-capitals are used to represent non-terminals.
 *      SQL92-specific syntax is separated from plain SQL/Postgres syntax
 *      to help isolate the non-extensible portions of the parser.
 *
 *      In general, nothing in this file should initiate database accesses
 *      nor depend on changeable state (such as SET variables).  If you do
 *      database accesses, your code will fail when we have aborted the
 *      current transaction and are just parsing commands to find the next
 *      ROLLBACK or COMMIT.  If you make use of SET variables, then you
 *      will do the wrong thing in multi-query strings like this:
 *            SET SQL_inheritance TO off; SELECT * FROM foo;
 *      because the entire string is parsed by gram.y before the SET gets
 *      executed.  Anything that depends on the database or changeable state
 *      should be handled inside parse_analyze() so that it happens at the
 *      right time not the wrong time.  The handling of SQL_inheritance is
 *      a good example.
 *
 * WARNINGS
 *      If you use a list, make sure the datum is a node so that the printing
 *      routines work.
 *
 *      Sometimes we assign constants to makeStrings. Make sure we don't free
 *      those.
 *
 *-------------------------------------------------------------------------
 */
#include "postgres.h"

#include <ctype.h>
#include <limits.h>

//#include "catalog/index.h"
#include "catalog/namespace.h"
#include "nodes/makefuncs.h"
#include "nodes/parsenodes.h"
#include "parser/gramparse.h"
#include "parser/parse_clause.h"
#include "parser/vertica.h"
#include "Transaction/LockModes.h"
#include "EE/Functions/Date.h"
#include "EE/Functions/Datetime.h"
#include "utils/uuid.h"     // UUID_LEN
#define INVALID_EPOCH 0x8000000000000000LL
#define VINT_NULL 0x8000000000000000LL

extern List *parsetree;            /* final parse result is delivered here */
extern int32 getComputedMaxAttrSize(void);
extern int32 getComputedMaxLongAttrSize(void);
extern int32 getDfltAttrSize(void);
extern int32 getDfltLongAttrSize(void);
extern unsigned int getUseLongStrings(void);

static bool QueryIsRule = FALSE;

/* Location tracking support --- simpler than bison's default */
#define YYLLOC_DEFAULT(Current, Rhs, N) \
    do { \
        if (N) \
            (Current) = (Rhs)[1]; \
        else \
            (Current) = (Rhs)[0]; \
    } while (0)

/*
 * The %name-prefix option below will make bison call base_yylex, but we
 * really want it to call filtered_base_yylex (see parser.c).
 */
#define base_yylex filtered_base_yylex

/*
 * Bison doesn't allocate anything that needs to live across parser calls,
 * so we can easily have it use palloc instead of malloc.  This prevents
 * memory leaks if we error out during parsing.  Note this only works with
 * bison >= 2.0.  However, in bison 1.875 the default is to use alloca()
 * if possible, so there's not really much problem anyhow, at least if
 * you're building with gcc.
 */
#define YYMALLOC palloc
#define YYFREE   pfree

extern List *parsetree;            /* final parse result is delivered here */
/*
 * If you need access to certain yacc-generated variables and find that
 * they're static by default, uncomment the next line.  (this is not a
 * problem, yet.)
 */
/*#define __YYSCLASS*/

static Node *makeColumnRef(const char *relname, List *indirection);
static Node *makeTypeCast(Node *arg, TypeName *typeInfo, bool soft);
static Node *makeTypeCastWithHints(Node *arg, TypeName *typeInfo,
                                   List *hintClause, bool soft);
static Node *makeStringConst(ctStr str, TypeName *typeInfo);
static Node *makeIntConst(int64 val);
static Node *makeFloatConst(const char *str);
static Node *makeAConst(Value *v);
static Node *makeRowNullTest(NullTestType test, RowExpr *row);
static MapElem *makeMapElem(int64 ind, Node *arg);
static A_Const *makeBoolAConst(bool state);
static FuncCall *makeOverlaps(List *largs, List *rargs);
static void check_qualified_name(List *names);
static List *check_func_name(List *names);
static List *extractArgTypes(List *parameters);
static void insertSelectOptions(SelectStmt *stmt,
                                List *sortClause, List *forUpdate,
                                Node *limitOffset, Node *limitCount,
                                List *limitPartition, List *limitSort,
                                WithClause *withClause);
//static void insertSamplingOptions(SelectStmt *stmt, Node *sampleStorageCount, Node *sampleStoragePercent, Node *sampleStorageBandCount);
static Node *makeSetOp(SetOperation op, bool all, List *setopHints, Node *larg, Node *rarg, int loc);
static Node *doNegate(Node *n);
static void doNegateFloat(Value *v);
static SortOpType getOrderbyKind(SortOpType ascDecs, SortNullsMask nullsFirstLastAuto);
void isFirstLastValueFunc(List *name);
static const char * convertPercentageToQuestionMark(const char *operName);
static PatternRegExprType getPatternRegExprType(const char *operName);
static bool isPatternOpLazy(const char *operName);
static bool isPatternOpPossessive(const char *operName);
extern int getFlexTableFieldWidth(void);
extern const char *getTheDatabaseName(void);
static void addFlexTableColumns(CreateStmt *stmt);
void confirmHiveFormatLimits(CopyStmt *stmt);
void confirmFlexNotUsingHive(CopyStmt *stmt);

%}

%code requires {
   typedef struct GroupByPair {
		List *vhints;
		List *grouping_clause;
	} GroupByPair;

   typedef struct PartnByPair {
       Node *partnExpr;
       Node *groupExpr;
       int64 activePartitionCount;
   } PartnByPair;
}

%expect 0
%name-prefix "base_yy"
%locations

%union
{
    int64               ival;
    char                chr;
    ctStr               str;
    const char            *keyword;
    bool                boolean;
    JoinType            jtype;
    DropBehavior        dbehavior;
    InheritPrivilegesBehavior ibehavior;
    OnCommitAction        oncommit;
    ProjSourceType        createType;
    ConstrStatus        constrStatus;
    ContainsOids        withoids;
    List                *list;
    Node                *node;
    Value                *value;
    ObjectType            objtype;

    TypeName            *typnam;
    FunctionParameter   *fun_param;
    DefElem                *defelt;
    MapElem                *mapelt;
    SortBy                *sortby;
    VAnalyticClause       *windef;
    VFrameBound           *frmbd;
    JoinExpr            *jexpr;
    IndexElem            *ielem;
    Alias                *alias;
    RangeVar            *range;
    WithClause        *with;
    A_Indices            *aind;
    ResTarget            *target;
    PrivTarget            *privtarget;
    GranteesWithOption    *granteeswithoption;

    InsertStmt            *istmt;
    VariableSetStmt        *vsetstmt;
    VNodeParams            *nodeparams;
    AlterProjectionAction        ap_action;

    FuncCall         *funccall;
    /*    KWarg            *kwarg; */
    DefElem          *paramarg;
    GroupByPair gbypair;
    PartnByPair partnpair;
}

%type <node>    stmt a_stmt schema_stmt
        AlterDatabaseSetStmt AlterDomainStmt AlterFaultGroupStmt AlterGroupStmt AlterHCatalogSchemaStmt AlterLibraryStmt AlterModelStmt AlterNotifierStmt AlterProfileStmt
        AlterSchemaStmt AlterViewPrivilegesStmt AlterSeqStmt AlterSessionStmt AlterTableStmt AlterTuningRuleStmt
        AlterUserDefaultRoleStmt AlterUserStmt AlterUserSetStmt AlterViewStmt
        AlterAuthStmt AlterAccessPolicyStmt AlterAddressStmt AlterLoadBalanceGroupStmt AlterRoutingRuleStmt
        AlterFunctionStmt AlterUDxFenceStmt AnalyzeStmt ClosePortalStmt ClusterStmt CommentStmt ConnectStmt
        ConstraintsSetStmt CopyStmt
        CopyAccessPolicyStmt
        CreateAsStmt CreateCastStmt
        CreateBranchStmt CreateDomainStmt CreateGroupStmt CreateOpClassStmt CreatePLangStmt
        CreateRoleStmt CreateModelStmt CreateSchemaStmt CreateSeqStmt CreateStmt CreateTableSpaceStmt
        CreateAssertStmt CreateNotifierStmt CreateTrigStmt CreateUserStmt CreateProfileStmt CreateTuningRuleStmt
        CreateFunctionStmt CreateProcStmt CreateLibraryStmt CreateLocationStmt CreateUDXStmt
        CreateAuthStmt CreateAccessPolicyStmt
        CreatedbStmt CreateSubnetStmt CreateInterfaceStmt CreateLoadBalanceGroupStmt CreateRoutingRuleStmt CreateFaultGroupStmt CurrentVariableShowStmt
        DeclareCursorStmt DefineStmt DeleteStmt
        DisconnectStmt DropGroupStmt DropOpClassStmt DropPLangStmt DropStmt
        DropAssertStmt DropTrigStmt DropRuleStmt DropCastStmt DropAccessPolicyStmt
        DropUserStmt DropdbStmt DropTableSpaceStmt ExplainStmt FetchStmt
        GrantStmt IndexStmt InsertStmt ListenStmt LoadStmt
        LockStmt NotifyStmt ExplainableStmt ExternalTableCopyStmt
        PlanStabilityAssociatePlanStmt
        PlanStabilitySupportedStmt PlanStabilitySavePlanStmt
        PlanStabilityRemovePlanStmt PlanStabilityGetPlanStmt
        PlanStabilityActivatePlanStmt
        PreparableStmt ProfileStmt ProfileableStmt
        ReindexStmt RemoveAggrStmt
        RemoveFuncStmt RemoveProcStmt RemoveOperStmt RemoveUDXStmt
        RenameStmt RevokeStmt RuleActionStmt RuleActionStmtOrEmpty RuleStmt
        SelectStmt VSelectStmt SelectIntoStmt VSelectIntoStmt ShowDatabaseStmt ShowNodeStmt
        TransactionStmt TruncateStmt
        UnlistenStmt UpdateStmt
        VariableResetStmt VariableSetStmt VariableShowStmt
        ViewStmt CheckPointStmt
        DeallocateStmt PrepareStmt ExecuteStmt ExportStmt
        CreateResourcePoolStmt AlterResourcePoolStmt
        opt_copy_from_clause
        rollup_clause cube_clause grouping_sets_clause

%type <node>    select_no_parens select_with_parens select_clause
                simple_select simple_select_into select_clauses

%type <node>    alter_column_default opclass_item opt_access_rank
%type <node>    alter_column_setusing alter_column_defaultusing
%type <ival>    add_drop

%type <node>    alter_table_cmd alter_rel_cmd alter_model_cmd
%type <list>    alter_table_cmds alter_rel_cmds alter_model_cmds

%type <list>    optNotifierParams notifierParams
%type <defelt>  notifierParam

%type <list>    opt_res_pool_params res_pool_params
%type <defelt>    res_pool_param

%type <dbehavior>    opt_drop_behavior opt_setschema_behavior
%type <constrStatus>  set_constr_status

%type <boolean>      opt_schema_owner_behavior
%type <ibehavior>    OptInheritPrivileges
%type <boolean>      OptDefaultInheritPrivileges

%type <list>    createdb_opt_list hcat_opt_list copy_opt_list transaction_mode_list
%type <defelt>  createdb_opt_item hcat_opt_item copy_opt_item transaction_mode_item copy_rej_clause
%type <node>    parquetOptElem orcOptElem

%type <ival>    opt_lock lock_type cast_context
%type <boolean>    opt_force opt_or_replace opt_nowait

%type <boolean> like_including_projections
%type <boolean> using_octets
%type <boolean> fenced_property

%type <list>    user_list SetParamList OptSetTuningParamList
%type <boolean> OptSystem

%type <list>    OptGroupList
%type <defelt>    OptGroupElem

%type <list>    OptUserList
%type <defelt>  OptUserElem

%type <boolean> optDisableEnableParam

%type <boolean> optConfirmDeliveryParam
%type <str>     optIdentifiedByParam
%type <str>     optActionName OptSize
%type <str>     optMaxPayloadParam optMaxMemorySizeParam optParameters

%type <ival>    optHOSTParam
%type <boolean> optEnableDisableParam
%type <boolean> nonoptEnableDisableParam
%type <str>     authHostIPAddress
%type <str>     authMethodName
%type <list>    optAuthParamList
%type <defelt>  optAuthParamElem

%type <list>    OptProfileList
%type <mapelt>  OptProfileElem
%type <ival>    PasswordParamIndex
%type <node>    PasswordParamExpr;

%type <str>        OptSchemaName
%type<keyword>  Opt_language
%type<keyword>  Opt_depends
%type <list>    OptSchemaEltList

%type <boolean> TriggerActionTime TriggerForSpec opt_trusted
%type <str>        opt_lancompiler opt_grant_grantadmin_option 

%type <str>        TriggerEvents
%type <value>    TriggerFuncArg

%type <str>        relation_name
                database_name access_method_clause access_method attr_name
                name function_name file_name qualified_schema_name
                udx_function_name

%type <list>    func_name handler_name qual_Op qual_all_Op subquery_Op
                opt_class opt_validator

%type <range>   index_name qualified_name OptConstrFromTable relname_w_indirection
                udx_func_name tokenizer_clause stemmer_clause opt_namespace

%type <str>     OptUsage OptNodes OptLabel
%type <boolean> OptShared

%type <str>        all_Op MathOp SpecialRuleRelation

%type <str>        iso_level
%type <node>    grantee
%type <granteeswithoption> revoke_privileges_or_roles
%type <list>    grantee_list
%type <str>     privilege_or_role
%type <list>    privileges_or_roles privilege_or_role_list auth_list
%type <privtarget> privilege_target opt_on_target_clause
%type <node>    function_with_argtypes proc_with_argtypes opt_columns_count
%type <list>    function_with_argtypes_list proc_with_argtypes_list
%type <chr>     TriggerOneEvent

%type <list>    stmtblock stmtmulti tokenizer_args stemmer_args
                OptTableElementList TableElementList OptInherit definition
                opt_distinct /*opt_definition*/ func_args proc_args
                func_args_list proc_args_list /*func_as*/
                createfunc_opt_list createproc_opt_list createtransform_opt_list
                oper_argtypes RuleActionList RuleActionMulti
                opt_column_list opt_copy_column_list
                opt_parse_option_list
                copyColumnList widthsList copyParseList columnList orc_opt_list
                opt_name_list opt_encode_clause opt_hint_list parquet_opt_list
                sort_clause opt_sort_clause sortby_list index_params
                name_list hint_list from_clause from_list opt_array_bounds
                qualified_name_list any_name any_name_list
                any_operator expr_list attrs
                target_list update_target_list insert_column_list
                insert_target_list def_list indirection opt_indirection
                TriggerFuncArgs select_limit opt_export_target_list
                opt_select_limit /*select_sample_storage*/ /*opt_select_sample_storage*/ opclass_item_list
                transaction_mode_list_or_empty opt_durable
                TableFuncElementList
                prep_type_clause prep_type_list
                execute_param_clause opt_export_column_list export_column_list
                qualified_schema_name_list
                dbname_list
                opt_determines_clause opt_proj_list
groupby_expr_list grouping_expr_list grouping_expr grouping_set_expr_list grouping_set_expr 

%type <range>   OptTempTableName

%type <defelt>    createfunc_opt_item createproc_opt_item createtransform_opt_item
%type <fun_param> func_arg proc_arg
%type <typnam>    func_return func_type proc_type aggr_argtype

%type <boolean> arg_class TriggerForType OptTemp OptLocalTempOnly
%type <oncommit> OnCommitOption
%type <withoids> OptWithOids
%type <node> AutoProjectionDef
%type <node> ProjectionClauses ProjectionClausesRequireKsafe ProjectionClausesNoKsafe

%type <list>    for_update_clause opt_for_update_clause update_list
%type <boolean>    opt_all

%type <node>    join_outer join_qual
%type <jtype>    join_type join_type_ext

%type <list>    datediff_list extract_list overlay_list position_list
%type <list>    substr_list trim_list
%type <ival>    leading_precision seconds_precision interval_qualifier
%type <boolean> opt_minus

%type <node>    overlay_placing substr_from substr_for

%type <boolean> opt_instead opt_analyze opt_local opt_annotated
%type <boolean> index_opt_text index_opt_unique opt_verbose opt_json
%type <boolean> opt_default opt_recheck
%type <defelt>    opt_binary copy_delimiter

%type <boolean> copy_from opt_hold copy_opt_commit opt_reorganize
%type <keyword> copy_storage_target

%type <ival>    fetch_count    opt_column event cursor_options
%type <objtype>    reindex_type drop_type comment_type udx_type

%type <node>    fetch_direction select_limit_value select_offset_value /*select_sample_storage_count select_sample_storage_percent select_sample_storage_band_count*/

%type <list>    OptSeqList
%type <defelt>    OptSeqElem

%type <istmt>    insert_rest

%type <vsetstmt> set_rest

%type <node>    TableElement ConstraintElem TableFuncElement
%type <node>    columnDef
%type <defelt>    def_elem
%type <node>    def_arg copyColumnElem copyParseElem where_clause
                a_expr b_expr c_expr func_expr AexprConst indirection_el d_expr ad_expr bd_expr
                columnref in_expr having_clause func_table array_expr interpolate_expr groupby_expr
%type <list>    row type_list array_expr_list
%type <node>    case_expr case_arg when_clause case_default
%type <list>    when_clause_list
%type <boolean> nullsequal
%type <node>    decode_search_result decode_default
%type <list>    decode_search_result_list
%type <ival>    sub_type
%type <value>    NumericOnly IntegerOnly RuntimePriorityValue OptionalStrengthValue
%type <alias>    alias_clause
%type <sortby>    sortby
%type <ielem>    index_elem
%type <node>    table_ref merge_table_src_ref merge_table_tgt_ref table_sample
%type <jexpr>    joined_table
%type <range>    relation_expr
%type <range>   relation_expr_opt_alias
%type <target>    target_el insert_target_el update_target_el insert_column_item

%type <typnam>  TypenameWithTypmod Typename SimpleTypename ConstTypename
                GenericType Numeric opt_float
                Character ConstCharacter
                CharacterWithLength CharacterWithoutLength
                ConstDatetime ConstInterval ConstIntervalYM
                Bit ConstBit BitWithLength BitWithoutLength
                Binary ConstBinary BinaryWithLength BinaryWithoutLength
                GenericTypeWithLength GenericTypeWithoutLength
                Uuid
%type <str>        sequencetype
%type <str>        binary
%type <str>        character
%type <str>        extract_arg
%type <ival>    opt_numeric opt_decimal OptCopy copy_storage_mode active_partition_count opt_count opt_atver
%type <str>     opt_like
%type <boolean> opt_varying opt_timezone

%type <ival>    Iconst
%type <str>        Sconst comment_text
%type <str>        UserId ProfileId opt_boolean ColId_or_Sconst AliasColId
%type <ival>     simple_boolean
%type <list>    var_list var_list_or_default var_list_or_default_all_except
%type <str>        ColId columnElem ColLabel type_name param_name proc_param_name
%type <str>     BareColLabel
%type <node>    var_value zone_value
%type <ival>    opt_minutes
%type <ival> 	force_outer_lvl

%type <keyword> unreserved_keyword bare_col_alias_excluded_keyword bare_col_rel_alias_excl_keyword
%type <keyword> func_name_keyword alias_excluded_keyword func_excluded_keyword
%type <keyword> type_excluded_keyword col_name_keyword reserved_keyword

%type <node>    TableConstraint TableLikeClause
%type <list>    ColQualList
%type <node>    ColConstraint ColConstraintElem ConstraintAttr
%type <ival>    key_actions key_delete key_match key_update key_action
%type <ival>    ConstraintAttributeSpec ConstraintDeferrabilitySpec
                ConstraintTimeSpec

%type <list>    constraints_set_list
%type <boolean> constraints_set_mode
%type <str>     OptTableSpace OptConsTableSpace OptTableSpaceOwner
%type <constrStatus> OptConsStatus

%type <node>    analytic_function non_analytic_function timeseries_clause

%type <node>    copy_opt_udls
%type <funccall> load_function copy_opt_source copy_filter copy_opt_parser
 /*
%type <list>    kwarg_list
%type <kwarg>   kwarg
 */
%type <list>    paramarg_list
%type <paramarg> paramarg
%type <gbypair> group_clause

%type <node>    pattern_clause event_definition pattern regexp regexpprime
%type <list>    pattern_in_clause pattern_list event_definition_list pattern_define_clause
%type <ival>    pattern_results_clause pattern_match_options_clause
%type <str>     pattern_quantifier

%type <list>    window_clause window_definition_list partition_clause opt_partition_clause within_clause
%type <windef>  window_definition opt_export_over_clause over_clause window_specification
%type <str>     opt_existing_window_name
%type <ival>    frame_exclusion

%type <frmbd>   opt_frame_clause frame_extent frame_bound1 frame_bound2

%type <list>    orderby_clause opt_orderby_clause orderby_list
%type <ival>    asc_desc_sort opt_nulls_order
%type <sortby>  orderby
%type <ival>    asc_desc
%type <str>     opt_copy_compr_type
%type <list>    opt_copy_node

%type <list>    copy_file copy_file_list copy_error_list
                copy_node_list copy_node_list_inner
                copyColumnFeatureList
                copy_filter_list copy_opt_filter_list opt_copy_file_format

%type <node>    copy_file_type export_segmentation copy_source
%type <defelt>  copyColumnFeature

%type <node>    timezone
%type <boolean> opt_to_or_equalsign
%type <range>   export_relation

%type <node>    common_table_expr
%type <with>    with_clause
%type <list>    cte_list
%type <list>    knob_list
%type <str>     PlanIdentifier
%type <list>    PlanIdentifierList
%type <str>     PlanDescription
%type <str>     OptimizerVersion
%type <str>     DirectedQueryCreationDate
%type <boolean> OptPlan
%type <value>   OptSchemaKeyword
%type <str>     opt_connect_addr_family
%type <boolean> opt_connect_tls_mode
%type <ival>     Interface_or_address
%type <ival>     Interface_or_address_drop
%type <boolean> opt_nocheck opt_enabled enable_disable
%type <ival>    load_balance_type
%type <str>     load_balance_policy
/*
 * If you make any token changes, update the keyword table in
 * parser/keywords.c and add new keywords to the appropriate one of
 * the reserved-or-not-so-reserved keyword lists, below.
 */

/* ordinary key words in alphabetical order */

%token <keyword> ABORT_P ABSOLUTE_P ACCESS ACCESSRANK ACCOUNT ACTION ACTIVATE ACTIVEPARTITIONCOUNT ADD ADDRESS ADMIN AFTER
    AGGREGATE ALL ALSO ALTER ANALYSE ANALYTIC ANALYZE AND ANNOTATED ANTI ANY ARRAY AS ASC
    ASSERTION ASSIGNMENT AT AUTHORIZATION AUTO AUTO_INC AVAILABLE
    AUTHENTICATION

    BACKWARD BALANCE BASENAME BATCH BEFORE BEGIN_P BEST BETWEEN BIGINT BINARY BIT
    BLOCK_DICT BLOCKDICT_COMP BOOLEAN_P BOTH BRANCH BROADCAST BY BYTEA BYTES BZIP BZIP_COMP
        BLOCK

    CACHE CALLED CASCADE CASE CAST CHAIN CHAR_P CHAR_LENGTH
    CHARACTER CHARACTER_LENGTH CHARACTERISTICS CHARACTERS
    CHECK CHECKPOINT CLASS CLEAR CLOSE
    CLUSTER COLLATE COLSIZES COLUMN COLUMNS_COUNT COMMENT COMMIT COMMITTED COMMONDELTA_COMP COMPLEX COMMUNAL
    CONNECT CONSTRAINT CONSTRAINTS CONTROL COPY
    CPUAFFINITYMODE CPUAFFINITYSET CREATE CREATEDB
    CREATEUSER CROSS CSV CUBE CURRENT_DATABASE CURRENT_DATE CURRENT_SCHEMA
    CURRENT_TIME CURRENT_TIMESTAMP CURRENT_USER CURRENT_P CURSOR CUSTOM CUSTOM_PARTITIONS CYCLE
    DATA_P DATABASE DATEDIFF DATETIME DAY_P DEACTIVATE DEALLOCATE DEC DECIMAL_P DECLARE
    DECODE DEFAULT DEFAULTS
    DEFERRABLE DEFERRED DEFINE DEFINER DELETE_P DELIMITER DELIMITERS DELTARANGE_COMP
    DELTARANGE_COMP_SP
    DELTAVAL DEPENDS DESC DISABLE DISABLED
    DISCONNECT DIRECT DIRECTCOLS DIRECTED DIRECTGROUPED DIRECTPROJ
    DISTINCT DISTVALINDEX DO DOMAIN_P DOUBLE_P DROP DURABLE

    EACH ELSE ENABLE ENABLED ENCODED ENCODING ENCRYPTED ENCLOSED END_P
    ENFORCELENGTH EPHEMERAL ERROR_P ESCAPE EVENT_P EVENTS_P EXCEPT EXCEPTION EXCEPTIONS
    EXCLUDE EXCLUDING EXCLUSIVE EXECUTE EXECUTIONPARALLELISM EXISTS EXPIRE EXPLAIN EXPORT EXTEND EXTERNAL EXTRACT

    FAILED_LOGIN_ATTEMPTS
    FALSE_P FAULT FENCED FETCH FILESYSTEM FILLER FILTER FIRST_P FIXEDWIDTH FLEX FLEXIBLE FLOAT_P FOLLOWING FOR FORCE FOREIGN FORMAT FORWARD

    FREEZE FROM FULL FUNCTION FUNCTIONS

    GCDDELTA GET GLOBAL GRACEPERIOD GRANT GROUP_P GROUPED GROUPING GZIP GZIP_COMP

    HANDLER HAVING HCATALOG HCATALOG_CONNECTION_TIMEOUT HCATALOG_DB HCATALOG_SCHEMA HCATALOG_SLOW_TRANSFER_LIMIT HCATALOG_SLOW_TRANSFER_TIME HCATALOG_USER HIGH HIVESERVER2_HOSTNAME HOLD HOSTNAME HOUR_P HOURS_P
    HOST

    IDENTIFIED IDENTITY_P IDLESESSIONTIMEOUT IF_P IGNORE ILIKE ILIKEB IMMEDIATE IMMUTABLE IMPLICIT_P
    IN_P INCLUDING INCREMENT
    INDEX INCLUDE INHERITS INITIALLY INNER_P INOUT INPUT_P
    INSENSITIVE INSERT INSTEAD INT_P INTEGER INTERFACE INTERPOLATE INTERSECT
    INTERVAL INTERVALYM INTO INVOKER IS ISNULL ISOLATION

    JOIN JSON

    KEY KSAFE

    LABEL LANCOMPILER LANGUAGE LARGE_P LAST_P LATEST LEADING LEFT LEVEL LIBRARY LIKE LIKEB
    LIMIT LISTEN LOAD LOCAL LOCALTIME LOCALTIMESTAMP LOCATION
    LOCK_P LONG LOW LZO

    MANAGED MASK MATCH MATCHED MATERIALIZE MAXCONCURRENCY MAXCONCURRENCYGRACE MAXCONNECTIONS
    MAXMEMORYSIZE MAXPAYLOAD MAXQUERYMEMORYSIZE MAXVALUE MEDIUM MEMORYCAP MEMORYSIZE
    MERGE MICROSECONDS_P MILLISECONDS_P MINUS MINUTE_P MINUTES_P MINVALUE MODE MODEL MONEY MONTH_P MOVE
    METHOD

    NAME_P NATIONAL NATIVE NATURAL NCHAR NETWORK NEW NEXT NO NOCREATEDB
    NOCREATEUSER NODE NODES NONE NOT NOTHING NOTIFIER NOTIFY NOTNULL NOWAIT  NULLAWARE NULLCOLS NULL_P
    NULLS NULLSEQUAL NUMBER_P NUMERIC

    OBJECT_P OCTETS OF OFF OFFSET OIDS OLD ON ONLY OPERATOR OPT OPTIMIZER
    OPTION OPTVER OR ORC ORDER OTHERS OUT_P OUTER_P OVER OVERLAPS OVERLAY OWNER

    PARAMETER PARAMETERS PARQUET PARSER PARTIAL PASSWORD PASSWORD_GRACE_TIME
    PASSWORD_LIFE_TIME PASSWORD_LOCK_TIME PASSWORD_REUSE_TIME
    PASSWORD_MAX_LENGTH PASSWORD_MIN_DIGITS PASSWORD_MIN_LENGTH PASSWORD_MIN_LETTERS
    PASSWORD_MIN_LOWERCASE_LETTERS PASSWORD_MIN_SYMBOLS PASSWORD_MIN_UPPERCASE_LETTERS PASSWORD_REUSE_MAX
    PATH PATTERN
    PERCENT PERMANENT PRECEDING PLACING PLANNEDCONCURRENCY
    POOL PORT POSITION PRECISION PREFER PREPASS PRESERVE PREPARE PREVIOUS_P PRIMARY
    PRIOR PRIORITY PRIVILEGES PROCEDURAL PROCEDURE PROFILE PROJECTIONS POLICY
    PSDATE QUERY QUEUETIMEOUT QUOTE
    RANDOM RANGE RAW READ REAL RECHECK RECORD_P RECURSIVE REFERENCES REINDEX REJECTED_P REJECTMAX RELATIVE_P RELEASE REMOVE RENAME REORGANIZE
    REPEATABLE REPLACE RESET RESOURCE RESTART RESTRICT RESULTS RETURN RETURNREJECTED REVOKE RIGHT RLE ROLE ROLES
    ROLLBACK_P ROLLUP ROUTE ROUTING ROW ROWS RULE RUNTIMECAP RUNTIMEPRIORITY RUNTIMETHRESHOLD

    /*SAMPLE*/ SAVE SAVEPOINT SCHEMA SCROLL SEARCH_PATH SECOND_P SECONDS_P SECURITY SECURITY_ALGORITHM SELECT SEMI SEMIALL SEQUENCE
    SEQUENCES SERIALIZABLE SESSION SESSION_USER SET SETOF SETS SHARE SHARED
    SHOW SIMILAR SIMPLE SINGLEINITIATOR SKIP SMALLDATETIME SMALLINT SOME SOURCE
    SSL_CONFIG
    STABLE STANDBY START STATEMENT
    STATISTICS STDIN STDOUT STEMMER STORAGE STREAM_P STRICT_P SUBSTRING SUBNET SYSDATE SYSID SYSTEM

    TABLE TABLES TABLESAMPLE TABLESPACE TEMP TEMPLATE TEMPORARY TEMPSPACECAP TERMINATOR_P TEXT THEN
    TIES TIME TIMESERIES TIMESTAMP TIMESTAMPADD TIMESTAMPDIFF
    TIMESTAMPTZ TIMETZ TIMEZONE TINYINT TLSMODE TO TOAST TOKENIZER TOLERANCE
    TRAILING TRANSACTION TRANSFORM TREAT
    TRICKLE TRIGGER TRIM TRUE_P TRUNCATE TRUSTED TUNING TYPE_P
    TLS

    UDPARAMETER UNBOUNDED UNCOMMITTED UNCOMPRESSED UNI UNION UNINDEXED UNIQUE UNKNOWN UNLIMITED UNLISTEN UNLOCK_P UNPACKER
    UPDATE USAGE USER USING UUID

    VACUUM VALIDATE VALIDATOR VALINDEX VALUE_P VALUES VARBINARY VARCHAR VARCHAR2 VARYING
    VERBOSE VERTICA VIEW VOLATILE

    WAIT WEBHDFS_ADDRESS WEBSERVICE_HOSTNAME WEBSERVICE_PORT WHEN WHERE WINDOW WITH WITHIN WITHOUT WORK WRITE

    YEAR_P

    ZONE ZSTD ZSTD_COMP ZSTD_FAST_COMP ZSTD_HIGH_COMP

/* The grammar thinks these are keywords, but they are not in the keywords.c
 * list and so can never be entered directly.  The filter in parser.c
 * creates these tokens when required.
 */
%token          UNIONJOIN

/* Special token types, not actually keywords - see the "lex" file */
%token <str>    IDENT FCONST SCONST BCONST XCONST Op Op_SS Op_Cmp HINT_BEGIN HINT_END
%token <ival>    ICONST PARAM
///vertica
%type <node>    VCreateProjectionStmt
                VNode VAlterNode VAlterNodeDetails AlterNodeList
                VColumnElem CreateNodeList CreateNodeDetails

%type <node>    VAlterProjection AlterProjSpec RecoverSpec RefreshSpec
                ToEpochSpec SplitSpec OrderTrimSpec MergeMoveSpec Vmergeout_range

%type <node>    VSegmentation
%type <node>    VSegmentedBy
%type <node>    VSegmentedByMAX

%type <node>    VHistoricalSelectStmt EpochOrTime EpochSpec EpochNumber
                EpochLatest TimeSpec export_select

%type <node>    VMergeStmt
%type <node>    merge_clause merge_update_clause merge_insert_clause merge_insert_target_list 
%type <list>    merge_clause_list

%type <list> vt_segmented_by
%type <list> vt_segmented_by_MAX

%type <nodeparams>    VNodeParams
%type <boolean>    WaitForJoin

%type <list>    vt_columnList opt_vt_columnGroupList
%type <list>    vt_columnGroupList VColumnGroupElem

%type <ival>    index_type encode_type ksafe_num ksafe_num_required opt_offset
%type <ap_action>  alter_projection_action
%type <str>     VHostName  CatalogPath NodeFaultGroup ExportAddress ControlAddress BroadcastAddress ControlNode
%type <ival>    NodeType PortSpecification
%type <list>    DataPath DataPathList

%token <ival> vmem ival1 Istart_epoch Iend_epoch
%token <str> vpath
%token <boolean> pg_vbool

%token <str>        enCodeType

%type <str>     hint_name
%type <str>     hive_arg_name
%type <node>    hint
%type <list>    hint_clause hint_rest hints

%type <partnpair> VPartition

/* CB: Why not intersperse these in the regular keyword list? */
%token <keyword> PROJECTION SEGMENTED UNSEGMENTED LESS THAN MERGEOUT
                MOVEOUT CATALOGPATH DATAPATH EPOCH_P RECOVER SPLIT REFRESH
                CORRELATION DETERMINES STRENGTH PINNED PARTITION PARTITIONING

///-vertica  gdb: set base_yydebug=1  to activate debugging

%debug

/* precedence: lowest to highest */
%nonassoc       SET                             /* see relation_expr_opt_alias */
%left        UNION EXCEPT MINUS
%left        INTERSECT
%left        OR
%left        AND
%right        NOT
%right        '='
%left        Op_Cmp
%nonassoc    '<' '>'
%nonassoc    LIKE ILIKE LIKEB ILIKEB SIMILAR
%nonassoc    ESCAPE
%nonassoc    OVERLAPS
%nonassoc    BETWEEN
%nonassoc    IN_P

/*
 * To support target_el without AS, we must give IDENT an explicit priority
 * between POSTFIXOP and Op.  We can safely assign the same priority to
 * various unreserved keywords as needed to resolve ambiguities (this can't
 * have any bad effects since obviously the keywords will still behave the
 * same as if they weren't keywords).  We need to do this for PARTITION,
 * RANGE, ROWS to support opt_existing_window_name; and for RANGE, ROWS
 * so that they can follow a_expr without creating
 * postfix-operator problems.
 */
%nonassoc    IDENT PARTITION RANGE ROWS ROLLUP CUBE
%left        Op OPERATOR        /* multi-character ops and user-defined operators */
%nonassoc    NOTNULL
%nonassoc    ISNULL
%nonassoc    IS NULL_P TRUE_P FALSE_P UNKNOWN /* sets precedence for IS NULL, etc */
%left        '|'
%left        '+' '-'
%left        '*' '/' Op_SS '%'
%left        '^'
/* Unary Operators */
%left        AT ZONE TIMEZONE LOCAL /* sets precedence for AT TIME ZONE */
%right        UMINUS
%left        '!'                /* postfix only */
%left        '[' ']'
%left        '(' ')'
%left        TYPECAST SOFTTYPECAST
%left        '.'
/*
 * These might seem to be low-precedence, but actually they are not part
 * of the arithmetic hierarchy at all in their use as JOIN operators.
 * We make them high-precedence to support their use as function names.
 * They wouldn't be given a precedence at all, were it not that we need
 * left-associativity among the JOIN rules themselves.
 */
%left        JOIN UNIONJOIN CROSS LEFT FULL RIGHT INNER_P NATURAL COMPLEX SEMI UNI SEMIALL ANTI NULLAWARE 
%%

/*
 *    Handle comment-only lines, and ;; SELECT * FROM pg_class ;;;
 *    psql already handles such cases, but other interfaces don't.
 *    bjm 1999/10/05
 */

stmtblock:    stmtmulti                                { parsetree = $1; }
        ;

/* the thrashing around here is to discard "empty" statements... */
stmtmulti:    stmtmulti ';' stmt
                { if ($3 != NULL)
                    $$ = lappend($1, $3);
                  else
                    $$ = $1;
                }
            | stmt
                    { if ($1 != NULL)
                        $$ = list_make1($1);
                      else
                        $$ = NIL;
                    }
        ;

stmt:   a_stmt
            {
                /*set the offset (in bytes) of this statement in the stmtmulti*/
                StmtTag* n = (StmtTag*)$1;
                n->offset = yyloc;
                $$=$1;
            }
        | /*EMPTY*/
            { $$ = NULL; }
       ;

a_stmt :
            AlterAccessPolicyStmt
            | AlterAddressStmt
            | AlterDatabaseSetStmt
            | VAlterProjection
            | AlterDomainStmt
            | AlterFaultGroupStmt
            | AlterGroupStmt
            | AlterHCatalogSchemaStmt
            | AlterLibraryStmt
            | AlterLoadBalanceGroupStmt
            | AlterRoutingRuleStmt
            | AlterModelStmt
            | AlterNotifierStmt
            | AlterProfileStmt
            | AlterResourcePoolStmt
            | AlterSchemaStmt
            | AlterViewPrivilegesStmt
            | AlterSeqStmt
            | AlterSessionStmt
            | AlterTableStmt
            | AlterTuningRuleStmt
            | AlterUserDefaultRoleStmt
            | AlterUserSetStmt
            | AlterUserStmt
            | AlterFunctionStmt
            | AlterAuthStmt
            | AlterUDxFenceStmt
            | AlterViewStmt
            | AnalyzeStmt
            | CheckPointStmt
            | ClosePortalStmt
            | ClusterStmt
            | CommentStmt
            | ConnectStmt
            | ConstraintsSetStmt
            | CopyStmt
            | CopyAccessPolicyStmt
            | VCreateProjectionStmt
            | VNode
            | VAlterNode
            | CreateAccessPolicyStmt
            | CreateAsStmt
            | CreateAssertStmt
            | CreateBranchStmt
            | CreateCastStmt
            | CreateDomainStmt
            | CreateFaultGroupStmt
            | CreateFunctionStmt
            | CreateGroupStmt
            | CreateInterfaceStmt
			| CreateLoadBalanceGroupStmt
			| CreateRoutingRuleStmt
            | CreateLibraryStmt
            | CreateLocationStmt
            | CreateModelStmt
            | CreateNotifierStmt
            | CreateOpClassStmt
            | CreateProcStmt
            | CreateProfileStmt
            | CreatePLangStmt
            | CreateResourcePoolStmt
            | CreateRoleStmt
            | CreateSchemaStmt
            | CreateSeqStmt
            | CreateStmt
            | CreateSubnetStmt
            | CreateTableSpaceStmt
            | CreateTrigStmt
            | CreateTuningRuleStmt
            | CreateAuthStmt
            | CreateUDXStmt
            | CreateUserStmt
            | CreatedbStmt
            | CurrentVariableShowStmt
            | DeallocateStmt
            | DeclareCursorStmt
            | DefineStmt
            | DeleteStmt
            | DisconnectStmt
            | DropAssertStmt
            | DropCastStmt
            | DropGroupStmt
            | DropOpClassStmt
            | DropPLangStmt
            | DropRuleStmt
            | DropStmt
            | DropTableSpaceStmt
            | DropTrigStmt
            | DropUserStmt
            | DropdbStmt
            | DropAccessPolicyStmt
            | ExecuteStmt
            | ExplainStmt
            | FetchStmt
            | GrantStmt
            | IndexStmt
            | InsertStmt
            | ListenStmt
            | LoadStmt
            | LockStmt
            | NotifyStmt
            | PlanStabilityActivatePlanStmt
            | PlanStabilityAssociatePlanStmt
            | PlanStabilityGetPlanStmt
            | PlanStabilityRemovePlanStmt
            | PlanStabilitySavePlanStmt
            | PrepareStmt
            | ProfileStmt
            | ReindexStmt
            | RemoveAggrStmt
            | RemoveFuncStmt
            | RemoveProcStmt
            | RemoveOperStmt
            | RemoveUDXStmt
            | RenameStmt
            | RevokeStmt
            | RuleStmt
            | ShowDatabaseStmt
            | ShowNodeStmt
            | TransactionStmt
            | TruncateStmt
            | UnlistenStmt
            | UpdateStmt
            | VariableResetStmt
            | VariableSetStmt
            | VariableShowStmt
            | VSelectIntoStmt
            | VSelectStmt
            | ViewStmt
            | ExportStmt
            | VMergeStmt
        ;

///vertica

VAlterProjection:
        ALTER PROJECTION qualified_name AlterProjSpec
        {
            VAlterProjection *n = makeNode(VAlterProjection);
            n->relation = $3;
            n->alterParseSpec = $4;
            $$ = (Node *)n;
        }
        ;

AlterProjSpec:
        MergeMoveSpec {$$ = $1;}
        | RecoverSpec {$$ = $1;}
        | SplitSpec {$$ = $1;}
        | RefreshSpec {$$ = $1;}
        | OrderTrimSpec {$$ = $1;}
        ;

RecoverSpec:
        RECOVER qualified_name FROM Iconst ToEpochSpec
         {
            VAlterParseSpec* spec = makeNode(VAlterParseSpec);
            spec->action = PROJ_RECOVER;
            spec->segName = $2;
            spec->startEpoch = $4;
            spec->endEpoch = INVALID_EPOCH;
            if ($5 != NULL)
            {
                VEpochNumSpec* epochSpec = (VEpochNumSpec*)$5;
                spec->endEpoch = epochSpec->epoch;
            }
            $$ = (Node*)spec;
        }
        ;

RefreshSpec:
        REFRESH
        {
            VAlterParseSpec* spec = makeNode(VAlterParseSpec);
            spec->action = PROJ_REFRESH;
            spec->startEpoch = INVALID_EPOCH;
            spec->endEpoch = INVALID_EPOCH;
            $$ = (Node*)spec;
        }
        ;

ToEpochSpec:
        TO Iconst
        {
            VEpochNumSpec* spec = makeNode(VEpochNumSpec);
            spec->epoch = $2;
            $$ = (Node*)spec;
        }
        | /*EMPTY*/
        {
            $$ = NULL;
        }
        ;

SplitSpec:
        SPLIT qualified_name FROM Iconst
        {
            VAlterParseSpec* spec = makeNode(VAlterParseSpec);
            spec->action = PROJ_SPLIT;
            spec->segName = $2;
            spec->startEpoch = $4;
            spec->endEpoch = $4;
            $$ = (Node*)spec;
        }
        ;

MergeMoveSpec:
        alter_projection_action Vmergeout_range
         {
            Vmergeout_range* range;
             VAlterParseSpec* spec = makeNode(VAlterParseSpec);
            spec->action = $1;
            range = (Vmergeout_range*)$2;
            spec->startEpoch = range->start_epoch;
            spec->endEpoch = range->end_epoch;
            $$ = (Node*)spec;
        }
        ;

alter_projection_action:
        MERGEOUT { $$ = PROJ_MERGEOUT; }
        | MOVEOUT { $$ = PROJ_MOVEOUT; }
        ;

Vmergeout_range:
        FROM Iconst TO Iconst
            {
                Vmergeout_range *n = makeNode(Vmergeout_range);
                n->start_epoch = $2;
                n->end_epoch = $4;
                $$ = (Node *)n;
            }
        | UNCOMMITTED
            {
                Vmergeout_range *n = makeNode(Vmergeout_range);
                n->start_epoch = 0;
                n->end_epoch = 0;
                $$ = (Node *)n;
            }
        | /*EMPTY*/
            {
                Vmergeout_range *n = makeNode(Vmergeout_range);
                n->start_epoch = INVALID_EPOCH;
                n->end_epoch = INVALID_EPOCH;
                $$ = (Node *)n;
            }
        ;

OrderTrimSpec:
        SET sort_clause
        {
            VAlterParseSpec* spec = makeNode(VAlterParseSpec);
            spec->action = PROJ_TRIM_ORDER;
            spec->sortClause = $2;
            $$ = (Node*)spec;
        };

VCreateProjectionStmt: CREATE PROJECTION IF_P NOT EXISTS qualified_name hint_clause opt_vt_columnGroupList AS SelectStmt ProjectionClauses
        {
            VCreateProjectionStmt *n = (VCreateProjectionStmt*)$11;
            n->exists_ok = TRUE;
            n->createType = PROJ_MANUAL;
            n->relation = $6;
            n->hintClause = $7;
            n->targetList = $8;
            if (n->targetList && n->encodeClause)
            {
                ereport(ERROR,
                        (errcode(ERRCODE_SYNTAX_ERROR),
                         errmsg("ENCODED BY is not supported in CREATE PROJECTION statement with column definition list"),
                         errhint("Column encoding can be defined in projection column definition list")));
            }
            n->query = (Query *)$10;
            $$ = (Node *)n;
        }
      | CREATE PROJECTION qualified_name hint_clause opt_vt_columnGroupList AS SelectStmt ProjectionClauses
        {
            VCreateProjectionStmt *n = (VCreateProjectionStmt*)$8;
            n->exists_ok = FALSE;
            n->createType = PROJ_MANUAL;
            n->relation = $3;
            n->hintClause = $4;
            n->targetList = $5;
            if (n->targetList && n->encodeClause)
            {
                ereport(ERROR,
                        (errcode(ERRCODE_SYNTAX_ERROR),
                         errmsg("ENCODED BY is not supported in CREATE PROJECTION statement with column definition list"),
                         errhint("Column encoding can be defined in projection column definition list")));
            }
            n->query = (Query *)$7;
            $$ = (Node *)n;
        }
        ;

opt_vt_columnGroupList:
            '(' vt_columnGroupList ')'                          { $$ = $2; }
            | /* EMPTY */                                       { $$ = NULL; }
;

vt_columnGroupList:
            VColumnGroupElem
            {
                // if a group, mark as such
                if (list_length($1) > 1) {
                    ListCell *ll;
                    foreach (ll, $1)
                    {
                        VColumnElem *ve = (VColumnElem *)lfirst(ll);
                        ve->group = 0;
                    }
                }
                $$ = $1;
            }
            | vt_columnGroupList ',' VColumnGroupElem
            {
                // append & mark all elems in list
                int groupNo = list_length($1);
                bool shouldMark = list_length($3) > 1;
                ListCell *ll;
                foreach (ll, $3)
                {
                    VColumnElem *ve = (VColumnElem *)lfirst(ll);
                    if (shouldMark) ve->group = groupNo;
                    $$ = lappend($1, ve);
                }
            }
        ;

VColumnGroupElem:
            VColumnElem                                { $$ = list_make1($1); }
            | GROUPED '(' VColumnElem ',' vt_columnList ')'
            {
                $$ = list_concat(list_make1($3), $5);
            }
        ;

vt_columnList:
            VColumnElem                                    { $$ = list_make1($1); }
            | vt_columnList ',' VColumnElem                { $$ = lappend($1, $3); }
        ;

VColumnElem:
            ColId encode_type index_type opt_access_rank
                {
                    VColumnElem *n = makeNode(VColumnElem);
                    n->colId=$1.str; // ignore leng
                    n->encodeType=$2;
                    n->accTypes=$3;
                    n->accessRank=$4;
                    n->group = -1;
                    $$ = (Node *)n;
                }
        ;

encode_type:
            ENCODING NONE
                {
                    $$=COL_ENC_NONE;
                }
            | ENCODING RLE
                {
                    $$=COL_ENC_RLE;
                }
            | ENCODING BLOCK_DICT
                {
                    $$=COL_ENC_BDICT;
                }
            | ENCODING BLOCKDICT_COMP
                {
                    $$=COL_ENC_BDICT_COMP;
                }
            | ENCODING DELTAVAL
                {
                    $$=COL_ENC_DELVAL;
                }
            | ENCODING GCDDELTA
                {
                    $$=COL_ENC_GCDDELTA;
                }
            | ENCODING DELTARANGE_COMP
                {
                    $$=COL_ENC_DRANGE_COMP;
                }
            | ENCODING DELTARANGE_COMP_SP
                {
                    $$=COL_ENC_DRANGE_COMP_SP;
                }
            | ENCODING COMMONDELTA_COMP
                {
                    $$=COL_ENC_CDELTA_COMP;
                }
            | ENCODING BZIP_COMP
                {
                        $$=COL_ENC_BZIP_COMP;
                }
            | ENCODING GZIP_COMP
                {
                    $$=COL_ENC_GZIP_COMP;
                }
            | ENCODING ZSTD_COMP
                {
                    $$=COL_ENC_ZSTD_COMP;
                }
            | ENCODING ZSTD_FAST_COMP
                {
                    $$=COL_ENC_ZSTD_FAST_COMP;
                }
            | ENCODING ZSTD_HIGH_COMP
                {
                    $$=COL_ENC_ZSTD_HIGH_COMP;
                }
            | ENCODING AUTO
                {
                    $$=COL_ENC_AUTO;
                }
            | /*EMPTY*/     { $$=COL_ENC_NOOP;}
        ;

opt_access_rank:
            ACCESSRANK IntegerOnly            {$$=(Node*)$2;}
            | /*EMPTY*/                        {$$=NIL;}
		;

index_type:
            VALINDEX
                {
                    $$=COL_ACC_IDX;
                }
// Unsupported in Beta
//            | DISTVALINDEX
//                {
//                    $$=COL_ACC_DISTIDX;
//                }
            | /*EMPTY*/                                         { $$=0 ;}
        ;

VSegmentation:
            SEGMENTED BY b_expr vt_segmented_by_MAX
                {
                    VSegmentation *n=makeNode(VSegmentation);
                    n->segExpr=$3;
                    n->nodeList=NIL;
                    n->segRanges=$4;
                    n->allFlag=false;
                    n->pinned=false;
                    $$ = (Node *)n;
                }
            | UNSEGMENTED NODE qualified_name
                {
                    VSegmentation *n=makeNode(VSegmentation);

                    n->segExpr=NIL;
                    n->nodeList=list_make1($3);
                    n->segRanges=NIL;
                    n->allFlag=false;
                    n->pinned=false;
                    $$ = (Node *)n;
                }
            | UNSEGMENTED ALL NODES
                {
                    VSegmentation *n=makeNode(VSegmentation);
                    n->segExpr=NIL;
                    n->nodeList=NIL;
                    n->segRanges=NIL;
                    n->allFlag=true;
                    n->pinned=false;
                    $$ = (Node *)n;
                }
            | SEGMENTED BY b_expr NODES qualified_name_list opt_offset
                {
                    VSegmentation *n=makeNode(VSegmentation);
                    n->segExpr=$3;
                    n->nodeList=$5;
                    n->offset=$6;
                    n->segRanges=NIL;
                    n->allFlag=false;
                    n->pinned=false;
                    $$ = (Node *)n;
                }
            | SEGMENTED BY b_expr ALL NODES opt_offset
                {
                    VSegmentation *n=makeNode(VSegmentation);
                    n->segExpr=$3;
                    n->offset=$6;
                    n->nodeList=NIL;
                    n->segRanges=NIL;
                    n->allFlag=true;
                    n->pinned=false;
                    $$ = (Node *)n;
                }
            | PINNED
                {
                    VSegmentation *n=makeNode(VSegmentation);
                    n->segExpr=NIL;
                    n->offset=0;
                    n->nodeList=NIL;
                    n->segRanges=NIL;
                    n->allFlag=false;
                    n->pinned=true;
                    $$ = (Node *)n;
                }
            | /*EMPTY*/                                         { $$=NULL ;}

        ;

opt_offset:
        OFFSET Iconst       { $$=$2; }
        | /*EMPTY*/        { $$=OFFSET_NONE; }
        ;

vt_segmented_by_MAX:
            VSegmentedByMAX                           { $$ = list_make1($1); }
            | vt_segmented_by VSegmentedByMAX         { $$ = lappend($1, $2); }
        ;

vt_segmented_by:
            VSegmentedBy                              { $$ = list_make1($1); }
            | vt_segmented_by VSegmentedBy            { $$ = lappend($1, $2); }
        ;

VSegmentedBy:
            NODE qualified_name VALUES LESS THAN a_expr
                {
                    VSegmentedBy *n=makeNode(VSegmentedBy);
                    n->name=$2;
                    n->expr=$6;
                    $$ = (Node *)n;
                }
         ;

VSegmentedByMAX:
            NODE qualified_name VALUES LESS THAN MAXVALUE
                {
                    VSegmentedBy *n=makeNode(VSegmentedBy);
                    n->name=$2;
                    n->expr=NULL;
                    $$ = (Node *)n;
                }
        ;

VNode:
            CREATE NODE CreateNodeList
                {
                    $$ = $3;
                }
        ;

CreateNodeDetails:
            name opt_is VNodeParams
                {
                    VNode *node= makeNode(VNode);
                    node->name=$1.str;
                    node->param=$3;
                    $$ = (Node *)node;
                }
        ;

CreateNodeList:
            CreateNodeDetails
                {
                    $$ = $1;
                }
            | CreateNodeDetails AND CreateNodeList
                {
                    ((VNode *)$1)->next = (VNode *)$3;
                    $$ = $1;
                }
        ;


/*****************************************************************************
 *
 *        ALTER NODE
 *
 *****************************************************************************/

VAlterNode:
            ALTER NODE AlterNodeList
                {
                    $$ = $3;
                }
        ;

VAlterNodeDetails: name opt_is VNodeParams
                {
                    VAlterNode *node = makeNode(VAlterNode);
                    node->name=$1.str;
                    node->param=$3;
                    node->next=NULL;
                    $$ = (Node *)node;
                }
            | name REPLACE
                {
                    VAlterNode *node = makeNode(VAlterNode);
                    node->name=$1.str;
                    VNodeParams *params = makeNode(VNodeParams);
                    node->param = params;
                    params->replaceOp = 1; // replace
                    params->replaceWith = NULL; // pick auto
                    node->next=NULL;
                    $$ = (Node *)node;
                }
            | name REPLACE WITH name
                {
                    VAlterNode *node = makeNode(VAlterNode);
                    node->name=$1.str;
                    VNodeParams *params = makeNode(VNodeParams);
                    node->param = params;
                    params->replaceOp = 1; // replace
                    params->replaceWith = $4.str;
                    node->next=NULL;
                    $$ = (Node *)node;
                }
            | name RESET
                {
                    VAlterNode *node = makeNode(VAlterNode);
                    node->name=$1.str;
                    VNodeParams *params = makeNode(VNodeParams);
                    node->param = params;
                    params->replaceOp = 2; // reset
                    params->replaceWith = NULL; // pick auto
                    node->next=NULL;
                    $$ = (Node *)node;
                }
           | name SET PARAMETER paramarg_list
                {
                    VAlterNode *node = makeNode(VAlterNode);
                    node->name = $1.str;
                    VNodeParams *params = makeNode(VNodeParams);
                    node->param = params;
                    params->setParams = true;
                    params->params = $4;
                    node->next=NULL;
                    $$ = (Node *)node;
                }
           | name SET paramarg_list
                {
                    VAlterNode *node = makeNode(VAlterNode);
                    node->name = $1.str;
                    VNodeParams *params = makeNode(VNodeParams);
                    node->param = params;
                    params->setParams = true;
                    params->params = $3;
                    node->next=NULL;
                    $$ = (Node *)node;
                }
           | name CLEAR PARAMETER knob_list
                {
                    VAlterNode *node = makeNode(VAlterNode);
                    node->name = $1.str;
                    VNodeParams *params = makeNode(VNodeParams);
                    node->param = params;
                    params->setParams = false;
                    params->params = $4;
                    node->next=NULL;
                    $$ = (Node *)node;
                }
           | name CLEAR knob_list
                {
                    VAlterNode *node = makeNode(VAlterNode);
                    node->name = $1.str;
                    VNodeParams *params = makeNode(VNodeParams);
                    node->param = params;
                    params->setParams = false;
                    params->params = $3;
                    node->next=NULL;
                    $$ = (Node *)node;
                }
            ;

AlterNodeList:
            VAlterNodeDetails
                {
                    $$ = $1;
                }
            | AlterNodeList AND VAlterNodeDetails
                {
                    ((VAlterNode *)$3)->next = (VAlterNode *)$1;
                    $$ = $3;
                }
            ;

/*****************************************************************************
 *
 *        SHOW NODE
 *
 *****************************************************************************/
ShowNodeStmt: SHOW NODE name knob_list
                {
                    ShowNodeStmt *n = makeNode(ShowNodeStmt);
                    n->node = $3.str;
                    n->params = $4;
                    n->all = false;
                    $$ = (Node *)n;
                }
           | SHOW NODE name PARAMETER knob_list
                {
                    ShowNodeStmt *n = makeNode(ShowNodeStmt);
                    n->node = $3.str;
                    n->params = $5;
                    n->all = false;
                    $$ = (Node *)n;
                }
           | SHOW NODE name ALL
                {
                    ShowNodeStmt *n = makeNode(ShowNodeStmt);
                    n->node = $3.str;
                    n->all = true;
                    $$ = (Node *)n;
                }
           | SHOW NODE name PARAMETER ALL
                {
                    ShowNodeStmt *n = makeNode(ShowNodeStmt);
                    n->node = $3.str;
                    n->all = true;
                    $$ = (Node *)n;
                }
        ;

opt_is:    IS                                    {}
            | /*EMPTY*/                                {}
        ;
VNodeParams:
        VHostName DataPath CatalogPath NodeType NodeFaultGroup ExportAddress PortSpecification WaitForJoin
        {
            VNodeParams *n = makeNode(VNodeParams);
            n->address = $1.str;
            n->dataPathList = $2;
            n->catalogPath = $3.str;
            n->nodeType = $4;
            n->faultGroupName = $5.str;
            n->ei_address = $6.str;
            n->clientPort = $7;
            n->waitForJoin = $8;
            n->controlAddress = NULL;
            n->controlBroadcast = NULL;
            n->controlPort = 0;
            n->controlNodeName = NULL;
            n->replaceOp = 0;
            $$ = (VNodeParams *) n;
        }
        | VHostName DataPath CatalogPath NodeType NodeFaultGroup ExportAddress PortSpecification CONTROL ControlAddress BroadcastAddress PortSpecification ControlNode WaitForJoin
        {
            VNodeParams *n = makeNode(VNodeParams);
            n->address = $1.str;
            n->dataPathList = $2;
            n->catalogPath = $3.str;
            n->nodeType = $4;
            n->faultGroupName = $5.str;
            n->ei_address = $6.str;
            n->clientPort = $7;
            n->controlAddress = $9.str;
            n->controlBroadcast = $10.str;
            n->controlPort = $11;
            n->controlNodeName = $12.str;
            n->waitForJoin = $13;
            n->replaceOp = 0;
            $$ = (VNodeParams *) n;
        }
        ;



VHostName:
        HOSTNAME Sconst { $$ = $2; }
        | /*empty*/ { $$ = ctNULL; }
        ;


DataPath:
        DATAPATH DataPathList { $$ = $2; }
        | /*empty*/ { $$ = NULL; }
        ;

DataPathList:
        Sconst
        {
            $$ = list_make1((Node *)makeStr($1));
        }
        | DataPathList ',' Sconst
        {
            $$ = lappend($1, (Node *)makeStr($3));
        }
        ;
WaitForJoin:
        WAIT FOR JOIN { $$ = true; }
        | /*empty*/ { $$ = false; }
		;

CatalogPath:
        CATALOGPATH Sconst {$$ = $2;}
        | /*empty*/ { $$ = ctNULL; }
        ;

NodeType:
        PERMANENT           {$$ = 0; /* must match CAT::Node::NodeType */}
        | EPHEMERAL         {$$ = 1; /* must match CAT::Node::NodeType */}
        | EXECUTE           {$$ = 2; /* must match CAT::Node::NodeType */}
        | STANDBY           {$$ = 3; /* must match CAT::Node::NodeType */}
        | /*empty*/         {$$ = -1;}
        ;

NodeFaultGroup:
        FAULT GROUP_P name  {$$ = $3;}
        | /*empty*/         {$$ = ctNULL;}
        ;

ExportAddress:
        EXPORT ON name {$$ = $3; }
        | EXPORT ON DEFAULT {$$ = ctString(""); }
        | /* empty*/ {$$ = ctNULL; }
        ;

PortSpecification:
        PORT Iconst    { $$ = $2; }
        | /*EMPTY*/ { $$=0; }
        ;

ControlAddress:
        HOSTNAME Sconst { $$ = $2; }
        | HOSTNAME DEFAULT { $$ = ctString(""); }
        | /* empty */ { $$ = ctNULL; }
        ;

BroadcastAddress:
        BROADCAST Sconst { $$ = $2; }
        | /* empty */ { $$ = ctNULL; }
        ;

ControlNode:
        NODE name { $$ = $2; }
        | /* empty */ { $$ = ctNULL; }
        ;

ksafe_num:
        KSAFE Iconst       { $$=$2; }
        | KSAFE            { $$=KSAFE_SYSTEM; }
        | /*EMPTY*/        { $$=KSAFE_NONE; }
        ;

ksafe_num_required:
        KSAFE Iconst       { $$=$2; }
        | KSAFE            { $$=KSAFE_SYSTEM; }
        ;

VSelectStmt:
        SelectStmt  {$$=$1;}
        | VHistoricalSelectStmt  {$$=$1;}
        ;

VHistoricalSelectStmt:
        EpochOrTime SelectStmt
        {
            VHistoricalSelectStmt* n = makeNode(VHistoricalSelectStmt);
            n->epochSpec = $1;
            n->selectStmt = $2;
            $$ = (Node*)n;
        }
        ;

EpochOrTime:
        EpochSpec {$$ = $1;}
        | TimeSpec {$$ = $1;}
        ;

TimeSpec:
        AT TIME Sconst
          {
            VEpochSpec* epochSpec = makeNode(VEpochSpec);
            A_Const* n1 = makeNode(A_Const);
            n1->val.type = T_String;
            n1->val.val.str = $3;
            n1->typeInfo = SystemTypeName("varchar");
            epochSpec->specType = EPOCH_SPEC_TIME;
            epochSpec->epoch = (Node*)n1;
            $$ = (Node*)epochSpec;
        }
        ;

EpochSpec:
        EpochNumber {$$ = $1;}
        | EpochLatest {$$ = $1;}
        ;

EpochNumber:
        AT EPOCH_P Iconst
         {
            VEpochSpec* epochSpec = makeNode(VEpochSpec);
            A_Const* n1 = makeNode(A_Const);
            n1->val.type = T_Integer;
            n1->val.val.ival = $3;
            epochSpec->specType = EPOCH_SPEC_EPOCH;
            epochSpec->epoch = (Node*)n1;
            $$ = (Node*)epochSpec;
        }
        ;

EpochLatest:
        AT EPOCH_P LATEST
         {
            VEpochSpec* epochSpec = makeNode(VEpochSpec);
            A_Const* n1 = makeNode(A_Const);
            n1->val.type = T_Integer;
            n1->val.val.ival = INVALID_EPOCH;
            epochSpec->specType = EPOCH_SPEC_LATEST;
            epochSpec->epoch = (Node*)n1;
            $$ = (Node*)epochSpec;
        }
        ;

/*****************************************************************************
 *
 *        CREATE LOAD BALANCE GROUP
 *
 *****************************************************************************/

CreateLoadBalanceGroupStmt:
            CREATE LOAD BALANCE GROUP_P name opt_with ADDRESS name_list load_balance_policy
                {
                    CreateLoadBalanceGroupStmt *n = makeNode(CreateLoadBalanceGroupStmt);
                    n->name = $5.str;
                    n->group_type = OBJECT_INTERFACE;
                    n->entries = $8;
                    n->filter = "";
					n->policy = $9.str;
                    $$ = (Node *)n;
                }
          | CREATE LOAD BALANCE GROUP_P name opt_with load_balance_type name_list FILTER Sconst load_balance_policy
                {
                    CreateLoadBalanceGroupStmt *n = makeNode(CreateLoadBalanceGroupStmt);
                    n->name = $5.str;
                    n->group_type = $7;
                    n->entries = $8;
                    n->filter = $10.str;
					n->policy = $11.str;
                    $$ = (Node *)n;
                }
                ;

AlterLoadBalanceGroupStmt:
             ALTER LOAD BALANCE GROUP_P name ADD ADDRESS name_list
             {
                 AlterLoadBalanceGroupStmt *n = makeNode(AlterLoadBalanceGroupStmt);
                 n->name = $5.str;
                 n->statement_type = ALTER_LBG_ADD_NETWORK_ADDRESS;
                 n->addEntries = $8;
                 $$ = (Node *) n;
             }
        |    ALTER LOAD BALANCE GROUP_P name DROP ADDRESS name_list
             {
                 AlterLoadBalanceGroupStmt *n = makeNode(AlterLoadBalanceGroupStmt);
                 n->name = $5.str;
                 n->statement_type = ALTER_LBG_DROP_NETWORK_ADDRESS;
                 n->dropEntries = $8;
                 $$ = (Node *) n;
             }
        |    ALTER LOAD BALANCE GROUP_P name DROP ADDRESS name_list ADD ADDRESS name_list
             {
                 AlterLoadBalanceGroupStmt *n = makeNode(AlterLoadBalanceGroupStmt);
                 n->name = $5.str;
                 n->statement_type = ALTER_LBG_BOTH_DROP_ADD_NETWORK_ADDRESS;
                 n->dropEntries = $8;
                 n->addEntries = $11;
                 $$ = (Node *) n;
             }
        |    ALTER LOAD BALANCE GROUP_P name ADD FAULT GROUP_P name_list
             {
                 AlterLoadBalanceGroupStmt *n = makeNode(AlterLoadBalanceGroupStmt);
                 n->name = $5.str;
                 n->statement_type = ALTER_LBG_ADD_FAULT_GROUP;
                 n->addEntries = $9;
                 $$ = (Node *) n;
             }
        |    ALTER LOAD BALANCE GROUP_P name ADD FAULT GROUP_P name_list SET FILTER TO Sconst
             {
                 AlterLoadBalanceGroupStmt *n = makeNode(AlterLoadBalanceGroupStmt);
                 n->name = $5.str;
                 n->statement_type = ALTER_LBG_ADD_FAULT_GROUP_W_FILTER;
                 n->addEntries = $9;
                 n->newFilter = $13.str;
                 $$ = (Node *) n;
             }
        |    ALTER LOAD BALANCE GROUP_P name DROP FAULT GROUP_P name_list
             {
                 AlterLoadBalanceGroupStmt *n = makeNode(AlterLoadBalanceGroupStmt);
                 n->name = $5.str;
                 n->statement_type = ALTER_LBG_DROP_FAULT_GROUP;
                 n->dropEntries = $9;
                 $$ = (Node *) n;
             }
        |    ALTER LOAD BALANCE GROUP_P name DROP FAULT GROUP_P name_list ADD FAULT GROUP_P name_list
             {
                 AlterLoadBalanceGroupStmt *n = makeNode(AlterLoadBalanceGroupStmt);
                 n->name = $5.str;
                 n->statement_type = ALTER_LBG_BOTH_DROP_ADD_FAULT_GROUP;
                 n->dropEntries = $9;
                 n->addEntries = $13;
                 $$ = (Node *) n;
             }
        |    ALTER LOAD BALANCE GROUP_P name RENAME TO name
             {
                 AlterLoadBalanceGroupStmt *n = makeNode(AlterLoadBalanceGroupStmt);
                 n->name = $5.str;
                 n->newName = $8.str;
                 n->statement_type = ALTER_LBG_RENAME;
                 $$ = (Node *) n;
             }
         |   ALTER LOAD BALANCE GROUP_P name SET POLICY TO Sconst
             {
                 AlterLoadBalanceGroupStmt *n = makeNode(AlterLoadBalanceGroupStmt);
                 n->name = $5.str;
                 n->newPolicy = $9.str;
                 n->statement_type = ALTER_LBG_POLICY;
                 $$ = (Node *) n;
             }
         |   ALTER LOAD BALANCE GROUP_P name SET FILTER TO Sconst
             {
                 AlterLoadBalanceGroupStmt *n = makeNode(AlterLoadBalanceGroupStmt);
                 n->name = $5.str;
                 n->newFilter = $9.str;
                 n->statement_type = ALTER_LBG_FILTER;
                 $$ = (Node *) n;
             }
             ;

load_balance_type:
            FAULT GROUP_P                     {  $$ = OBJECT_FAULTGROUP; }
            ;

load_balance_policy:
          POLICY Sconst                        {  $$ = $2; }
        | /* EMPTY */                          {  $$ = ctString("ROUNDROBIN"); }
        ;



/*****************************************************************************
 *
 *        CREATE ROUTING RULE
 *
 *****************************************************************************/

CreateRoutingRuleStmt:
            CREATE ROUTING RULE name ROUTE Sconst TO name
                {
                    CreateRoutingRuleStmt *n = makeNode(CreateRoutingRuleStmt);
                    n->name = $4.str;
                    n->source = $6.str;
                    n->dest = $8.str;

                    $$ = (Node *)n;
                }
        ;

AlterRoutingRuleStmt:
            ALTER ROUTING RULE name RENAME TO name
            {
                AlterRoutingRuleStmt *n = makeNode(AlterRoutingRuleStmt);
                n->name = $4.str;
                n->newName = $7.str;
                n->statement_type = ALTER_RR_RENAME;

                $$ = (Node *)n;
            }
         |  ALTER ROUTING RULE name SET ROUTE TO Sconst
            {
                AlterRoutingRuleStmt *n = makeNode(AlterRoutingRuleStmt);
                n->name = $4.str;
                n->newSource = $8.str;
                n->statement_type = ALTER_RR_SOURCE;

                $$ = (Node *)n;
            }
         |  ALTER ROUTING RULE name SET GROUP_P TO name
            {
                AlterRoutingRuleStmt *n = makeNode(AlterRoutingRuleStmt);
                n->name = $4.str;
                n->newDest = $8.str;
                n->statement_type = ALTER_RR_DEST;

                $$ = (Node *)n;
            }
         ;


/*****************************************************************************
 *
 *        CREATE INTERFACE/ADDRESS
 *
 *****************************************************************************/

CreateInterfaceStmt:
            CREATE NETWORK Interface_or_address name ON name opt_with Sconst PortSpecification opt_enabled opt_nocheck
                {
                    CreateInterfaceStmt *n = makeNode(CreateInterfaceStmt);
                    n->name = $4.str;
                    n->node = $6.str;
                    n->addr = $8.str;
					n->port = $9;
					n->enabled =$10;
                    n->force = $11;
                    n->statement_type = $3;
                    $$ = (Node *)n;
                }
        ;

AlterAddressStmt:
          ALTER NETWORK ADDRESS name RENAME TO name
          {
              AlterAddressStmt *n = makeNode(AlterAddressStmt);
              n->name = $4.str;
              n->newName = $7.str;
              n->statement_type = ALTER_ADDR_RENAME;
              $$ = (Node *) n;
          }
      |   ALTER NETWORK ADDRESS name SET TO Sconst PortSpecification
          {
              AlterAddressStmt *n = makeNode(AlterAddressStmt);
              n->name = $4.str;
              n->newAddr = $7.str;
              n->newPort = $8;
              n->statement_type = ALTER_ADDR_RESET;
              $$ = (Node *) n;
          }
      |   ALTER NETWORK ADDRESS name enable_disable
          {
              AlterAddressStmt *n = makeNode(AlterAddressStmt);
              n->name = $4.str;
              n->newEnabled = $5;
              n->statement_type = ALTER_ADDR_TOGGLE;
              $$ = (Node *) n;
          }
          ;

/* Be tolerant of spelling ENABLE=ENABLED */
enable_disable:
        ENABLE                         {$$ = TRUE;}
      | ENABLED                        {$$ = TRUE;}
      | DISABLE                        {$$ = FALSE;}
      | DISABLED                       {$$ = FALSE;}
      ;

opt_nocheck:  
          FORCE                                    {  $$ = TRUE; }
        | CHECK                                    {  $$ = FALSE; }
        | /* EMPTY*/  {  $$ = FALSE; }
        ;

opt_enabled:  
          ENABLED                                     {  $$ = TRUE; }
        | DISABLED                                    {  $$ = FALSE; }
        | /* EMPTY */                            {  $$ = TRUE; }
        ;

Interface_or_address: 
          INTERFACE                              { $$ = STMT_INTERFACE_TYPE; }
        | ADDRESS                                { $$ = STMT_ADDRESS_TYPE; }
        ;

/*****************************************************************************
 *
 *        CREATE AND ALTER FAULT GROUP
 *
 *****************************************************************************/

CreateFaultGroupStmt:
            CREATE FAULT GROUP_P name
                {
                    CreateFaultGroupStmt *n = makeNode(CreateFaultGroupStmt);
                    n->name = $4.str;
                    $$ = (Node *)n;
                }
        ;

AlterFaultGroupStmt:
            ALTER FAULT GROUP_P name ADD NODE name
                {
                    AlterFaultGroupStmt *n = makeNode(AlterFaultGroupStmt);
                    n->faultGroupName = $4.str;
                    n->subtype = AFG_AddNode;
                    n->objectName = $7.str;
                    $$ = (Node *)n;
                }
        |   ALTER FAULT GROUP_P name DROP NODE name
                {
                    AlterFaultGroupStmt *n = makeNode(AlterFaultGroupStmt);
                    n->faultGroupName = $4.str;
                    n->subtype = AFG_DropNode;
                    n->objectName = $7.str;
                    $$ = (Node *)n;
                }
        |   ALTER FAULT GROUP_P name ADD FAULT GROUP_P name
                {
                    AlterFaultGroupStmt *n = makeNode(AlterFaultGroupStmt);
                    n->faultGroupName = $4.str;
                    n->subtype = AFG_AddFaultGroup;
                    n->objectName = $8.str;
                    $$ = (Node *)n;
                }
        |   ALTER FAULT GROUP_P name DROP FAULT GROUP_P name
                {
                    AlterFaultGroupStmt *n = makeNode(AlterFaultGroupStmt);
                    n->faultGroupName = $4.str;
                    n->subtype = AFG_DropFaultGroup;
                    n->objectName = $8.str;
                    $$ = (Node *)n;
                }
        |   ALTER FAULT GROUP_P name RENAME TO name
                {
                    AlterFaultGroupStmt *n = makeNode(AlterFaultGroupStmt);
                    n->faultGroupName = $4.str;
                    n->subtype = AFG_RenameTo;
                    n->objectName = $7.str;
                    $$ = (Node *)n;
                }
        ;

/////////////////////// Branch
CreateBranchStmt:
            CREATE DATA_P IMMUTABLE BRANCH auth_list opt_count opt_like opt_atver
                {
                    CreateBranchStmt *n = makeNode(CreateBranchStmt);
                    n->brType = DATA_IMMUTABLE;
                    n->names = $5;
                    n->count = $6;
                    n->likeExisting = $7.str;
                    n->version = $8;
                    $$ = (Node *)n;
                }
        ;

opt_count: '*' Iconst
                {
                    $$ = $2;
                }
        |
                {
                    $$ = 1;
                }
        ;

opt_like: LIKE name
                {
                    $$ = $2;
                }
        |
                {
                    $$ = ctString("");
                }
        ;

opt_atver: AT Iconst
                {
                    $$ = $2;
                }
        |
                {
                    $$ = 0;
                }
        ;

///-vertica

// CREATE TUNING RULE r1 ( TINY_ROS, R_DBD, max_epoch_count = 5, tiny_ros_count = 6) AS select * from t
// ALTER TUNING RULE r1 SET max_epoch_count = 5, tiny_ros_count = 6;
// ALTER TUNING RULE r1 DISABLE;
// ALTER TUNING RULE r1 ENABLE;

CreateTuningRuleStmt:
        CREATE OptSystem TUNING RULE ColId '(' ColId ',' ColId OptSetTuningParamList ')' AS SelectStmt
        {
            CreateTuningRuleStmt *n = makeNode(CreateTuningRuleStmt);
            n->name = $5.str;
            n->otype = $7.str;
            n->ttype = $9.str;
            n->params = $10;
            n->query = (Query *) $13;
            n->issys = $2;
            $$ = (Node *)n;
        }
        ;

OptSystem:
        SYSTEM                { $$=TRUE; }
        | /* EMPTY */         { $$=FALSE; }
        ;

OptSetTuningParamList:
        ',' SetParamList       { $$ = $2; }
        | /*EMPTY*/             { $$ = NIL; }
        ;

SetParamList:
        ColId '=' IntegerOnly
        {
            $$ = list_make1(makeDefElem($1.str, (Node *)$3));
        }
        | SetParamList ',' ColId '=' IntegerOnly
        {
            $$ = lappend($1, makeDefElem($3.str, (Node *)$5));
        }
        ;

AlterTuningRuleStmt:
        ALTER TUNING RULE ColId SET SetParamList
        {
            AlterTuningRuleStmt *n = makeNode(AlterTuningRuleStmt);
            n->name = $4.str;
            n->params = $6;
            n->enabled = true;
            $$ = (Node *)n;
        }
        |
        ALTER TUNING RULE ColId DISABLE
        {
            AlterTuningRuleStmt *n = makeNode(AlterTuningRuleStmt);
            n->name = $4.str;
            n->params = NIL;
            n->enabled = false;
            $$ = (Node *)n;
        }
        |
        ALTER TUNING RULE ColId ENABLE
        {
            AlterTuningRuleStmt *n = makeNode(AlterTuningRuleStmt);
            n->name = $4.str;
            n->params = NIL;
            n->enabled = true;
            $$ = (Node *)n;
        }
        ;


/*****************************************************************************
 *
 * Create a new Postgres DBMS user
 *
 *
 *****************************************************************************/

CreateUserStmt:
            CREATE USER UserId opt_with OptUserList
                {
                    CreateUserStmt *n = makeNode(CreateUserStmt);
                    n->user = $3.str;
                    n->options = $5;
                    $$ = (Node *)n;
                }
        ;


opt_with:    WITH                                    {}
            | /*EMPTY*/                                {}
        ;

/*****************************************************************************
 *
 * Alter a postgresql DBMS user
 *
 *
 *****************************************************************************/

AlterUserStmt:
            ALTER USER UserId opt_with OptUserList
                 {
                    AlterUserStmt *n = makeNode(AlterUserStmt);
                    n->user = $3.str;
                    n->options = $5;
                    $$ = (Node *)n;
                 }
        ;


AlterUserSetStmt:
            ALTER USER UserId SET set_rest
                {
                    AlterUserSetStmt *n = makeNode(AlterUserSetStmt);
                    n->user = $3.str;
                    n->variable = $5->name;
                    n->value = $5->args;
                    $$ = (Node *)n;
                }
            | ALTER USER UserId VariableResetStmt
                {
                    AlterUserSetStmt *n = makeNode(AlterUserSetStmt);
                    n->user = $3.str;
                    n->variable = ((VariableResetStmt *)$4)->name;
                    n->value = NIL;
                    $$ = (Node *)n;
                }
            ;

AlterUserDefaultRoleStmt:
            ALTER USER UserId DEFAULT ROLE var_list_or_default_all_except
                {
                    AlterUserDefaultRoleStmt *n = makeNode(AlterUserDefaultRoleStmt);
                    n->user = $3.str;
                    n->values = $6;
                    $$ = (Node *)n;
                }
            ;

/*****************************************************************************
 *
 * Drop a postgresql DBMS user
 *
 * XXX Ideally this would have CASCADE/RESTRICT options, but since a user
 * might own objects in multiple databases, there is presently no way to
 * implement either cascading or restricting.  Caveat DBA.
 *****************************************************************************/

DropUserStmt:
            DROP USER IF_P EXISTS user_list opt_drop_behavior
                {
                    DropUserStmt *n = makeNode(DropUserStmt);
                    n->missing_ok = TRUE;
                    n->users = $5;
                    n->behavior = $6;
                    $$ = (Node *)n;
                }
            | DROP USER user_list opt_drop_behavior
                {
                    DropUserStmt *n = makeNode(DropUserStmt);
                    n->missing_ok = FALSE;
                    n->users = $3;
                    n->behavior = $4;
                    $$ = (Node *)n;
                }
            ;

/*
 * Options for CREATE USER and ALTER USER
 */
OptUserList:
            OptUserList OptUserElem                    { $$ = lappend($1, $2); }
            | OptUserList IDENTIFIED BY Sconst REPLACE Sconst
              {
                  $$ = lappend($1, makeDefElem("password", (Node *)makeStr($4)));
                  $$ = lappend($$, makeDefElem("replace", (Node *)makeStr($6)));
              }
            | OptUserList MAXCONNECTIONS Iconst ON NODE
              {
                  $$ = lappend($1, makeDefElem("maxconnections", (Node *)makeInteger($3)));
                  $$ = lappend($$, makeDefElem("connectionlimitmode", (Node *)makeString($5)));
              }
            | OptUserList MAXCONNECTIONS Iconst ON DATABASE
              {   
                  $$ = lappend($1, makeDefElem("maxconnections", (Node *)makeInteger($3)));
                  $$ = lappend($$, makeDefElem("connectionlimitmode", (Node *)makeString($5)));
              }
            | OptUserList MAXCONNECTIONS Iconst
              {
                  $$ = lappend($1, makeDefElem("maxconnections", (Node *)makeInteger($3)));
                  $$ = lappend($$, makeDefElem("connectionlimitmode", (Node *)makeString("database")));
              }
            | OptUserList MAXCONNECTIONS NONE
              {
                  $$ = lappend($1, makeDefElem("maxconnections", (Node *)makeInteger(-1)));
                  $$ = lappend($$, makeDefElem("connectionlimitmode", (Node *)makeString("")));
              }
            |  /* EMPTY */                            { $$ = NIL; }
        ;

OptUserElem:
            PASSWORD Sconst
                {
                    $$ = makeDefElem("password", (Node *)makeStr($2));
                }
            | ENCRYPTED PASSWORD Sconst
                {
                    $$ = makeDefElem("password", (Node *)makeStr($3));
                }
            | IDENTIFIED BY Sconst
                {
                    $$ = makeDefElem("password", (Node *)makeStr($3));
                }
            | SYSID Iconst
                {
                    $$ = makeDefElem("sysid", (Node *)makeInteger($2));
                }
            | CREATEDB
                {
                    $$ = makeDefElem("createdb", (Node *)makeInteger(TRUE));
                }
            | NOCREATEDB
                {
                    $$ = makeDefElem("createdb", (Node *)makeInteger(FALSE));
                }
            | CREATEUSER
                {
                    $$ = makeDefElem("createuser", (Node *)makeInteger(TRUE));
                }
            | NOCREATEUSER
                {
                    $$ = makeDefElem("createuser", (Node *)makeInteger(FALSE));
                }
            | IN_P GROUP_P user_list
                {
                    $$ = makeDefElem("groupElts", (Node *)$3);
                }
            | PASSWORD EXPIRE
                {
                    $$ = makeDefElem("expire", NULL);
                }
            | ACCOUNT LOCK_P
                {
                    $$ = makeDefElem("lock", (Node *)makeInteger(TRUE));
                }
            | ACCOUNT UNLOCK_P
                {
                    $$ = makeDefElem("lock", (Node *)makeInteger(FALSE));
                }
            | PROFILE ProfileId
                {
                    $$ = makeDefElem("profile", (Node *)makeStr($2));
                }
            | RESOURCE POOL name
                {
                    $$ = makeDefElem("resource_pool",(Node *)makeStr($3));
                }
            | MEMORYCAP Sconst
                {
                    $$ = makeDefElem("memorycap",(Node *)makeStr($2));
                }
            | MEMORYCAP NONE
                {
                    $$ = makeDefElem("memorycap",(Node *)makeStr(ctString("")));
                }
            | TEMPSPACECAP Sconst
                {
                    $$ = makeDefElem("tempspacecap",(Node *)makeStr($2));
                }
            | TEMPSPACECAP NONE
                {
                    $$ = makeDefElem("tempspacecap",(Node *)makeStr(ctString("")));
                }
            | RUNTIMECAP Sconst
                {
                    $$ = makeDefElem("runtimecap",(Node *)makeStr($2));
                }
            | RUNTIMECAP NONE
                {
                    $$ = makeDefElem("runtimecap",(Node *)makeStr(ctString("")));
                }
            | IDLESESSIONTIMEOUT Sconst
                {
                    $$ = makeDefElem("idlesessiontimeout", (Node *)makeStr($2));    
                }
            | IDLESESSIONTIMEOUT NONE
                {
                    $$ = makeDefElem("idlesessiontimeout", (Node *)makeStr(ctString("")));
                }
            | GRACEPERIOD Sconst
                {
                    $$ = makeDefElem("graceperiod", (Node *)makeStr($2));
                }
            | GRACEPERIOD NONE
                {
                    $$ = makeDefElem("graceperiod", (Node *)makeStr(ctString("")));
                }
            | SEARCH_PATH var_list_or_default
                {
                    $$ = makeDefElem("search_path", (Node *)$2);
                }
            | SECURITY_ALGORITHM Sconst
                {
                    $$ = makeDefElem("security_algorithm",(Node *)makeStr($2));
                }
        ;

user_list:    user_list ',' UserId        { $$ = lappend($1, makeStr($3)); }
            | UserId                    { $$ = list_make1(makeStr($1)); }
        ;

/* CREATE ACCESS POLICY ON name FOR ROWS WHERE expression [ENABLE]*/
/* CREATE ACCESS POLICY ON name FOR COLUMN name expression [ENABLE];*/
CreateAccessPolicyStmt:
        CREATE ACCESS POLICY ON qualified_name FOR ROWS WHERE a_expr optDisableEnableParam
            {
                CreateAccessPolicyStmt *n = makeNode(CreateAccessPolicyStmt);
                n->relation = $5;
                n->policy_type = AP_ROWS;
                n->expression = $9;
                n->is_enabled = $10;
                $$ = (Node *)n;
            }
        | CREATE ACCESS POLICY ON qualified_name FOR COLUMN columnElem a_expr optDisableEnableParam
            {
                CreateAccessPolicyStmt *n = makeNode(CreateAccessPolicyStmt);
                n->relation = $5;
                n->policy_type = AP_COLUMNS;
                n->column = $8.str;
                n->expression = $9;
                n->is_enabled = $10;
                $$ = (Node *)n;
            }
        ;
/* ALTER ACCESS POLICY ON name FOR ROWS WHERE expression [ENABLE]*/
/* ALTER ACCESS POLICY ON name FOR COLUMN name expression [ENABLE];*/
AlterAccessPolicyStmt:
        ALTER ACCESS POLICY ON qualified_name FOR ROWS WHERE a_expr optDisableEnableParam
            {
                AlterAccessPolicyStmt *n = makeNode(AlterAccessPolicyStmt);
                n->relation = $5;
                n->policy_type = AP_ROWS;
                n->expression = $9;
                n->is_enabled = $10;
                $$ = (Node *)n;
            }
        | ALTER ACCESS POLICY ON qualified_name FOR ROWS optDisableEnableParam
            {
                AlterAccessPolicyStmt *n = makeNode(AlterAccessPolicyStmt);
                n->relation = $5;
                n->policy_type = AP_ROWS;
                n->is_enabled = $8;
                $$ = (Node *)n;
            }
        | ALTER ACCESS POLICY ON qualified_name FOR COLUMN columnElem a_expr optDisableEnableParam
            {
                AlterAccessPolicyStmt *n = makeNode(AlterAccessPolicyStmt);
                n->relation = $5;
                n->policy_type = AP_COLUMNS;
                n->column = $8.str;
                n->expression = $9;
                n->is_enabled = $10;
                $$ = (Node *)n;
            }
        | ALTER ACCESS POLICY ON qualified_name FOR COLUMN columnElem optDisableEnableParam
            {
                AlterAccessPolicyStmt *n = makeNode(AlterAccessPolicyStmt);
                n->relation = $5;
                n->policy_type = AP_COLUMNS;
                n->column = $8.str;
                n->expression = NULL;
                n->is_enabled = $9;
                $$ = (Node *)n;
            }
        ;
/* COPY ACCESS POLICY ON name FOR COLUMN columnElem TO name */
CopyAccessPolicyStmt:
        ALTER ACCESS POLICY ON qualified_name FOR ROWS COPY TO TABLE qualified_name
            {
                CopyAccessPolicyStmt *n = makeNode(CopyAccessPolicyStmt);
                n->relation = $5;
                n->policy_type = AP_ROWS;
                n->other_relation = $11;
                $$ = (Node *)n;
            }
        | ALTER ACCESS POLICY ON qualified_name FOR COLUMN columnElem COPY TO TABLE qualified_name
            {
                CopyAccessPolicyStmt *n = makeNode(CopyAccessPolicyStmt);
                n->relation = $5;
                n->policy_type = AP_COLUMNS;
                n->column = $8.str;
                n->other_relation = $12;
                $$ = (Node *)n;
            }
        ;
/* DROP ACCESS POLICY FROM name */
DropAccessPolicyStmt:
        DROP ACCESS POLICY ON qualified_name FOR ROWS
            {
                DropAccessPolicyStmt *n = makeNode(DropAccessPolicyStmt);
                n->relation = $5;
                n->policy_type = AP_ROWS;
                $$ = (Node *)n;
            }
        | DROP ACCESS POLICY ON qualified_name FOR COLUMN columnElem
            {
                DropAccessPolicyStmt *n = makeNode(DropAccessPolicyStmt);
                n->relation = $5;
                n->policy_type = AP_COLUMNS;
                n->column = $8.str;
                $$ = (Node *)n;
            }
        ;
optDisableEnableParam:
            ENABLE             { $$ = true; }
            | DISABLE          { $$ = false; }
        ;

/*****************************************************************************
 *
 * Create and Alter Notifier
 *
 *
 *****************************************************************************/
/* CREATE NOTIFIER name ACTION 'URI' [ENABLE|DISABLE] [MAXPAYLOAD size] MAXMEMORYSIZE size [IDENTIFIED BY 'uuid'] [[NO] CHECK COMMITTED] [PARAMETERS 'adapter configs'] */
CreateNotifierStmt:
    CREATE NOTIFIER IF_P NOT EXISTS name optActionName optEnableDisableParam optMaxPayloadParam optMaxMemorySizeParam optIdentifiedByParam optConfirmDeliveryParam optParameters
    {
        CreateNotifierStmt *n = makeNode(CreateNotifierStmt);
        n->exists_ok          = TRUE;
        n->name               = $6.str;
        n->action             = $7.str;
        n->is_enabled         = $8;
        n->max_payload        = $9.str;
        n->max_memory_size    = $10.str;
        n->uuid               = $11.str;
        n->check_committed    = $12;
        n->adapter_params     = $13.str;
        $$ = (Node *)n;
    }
    | CREATE NOTIFIER name optActionName optEnableDisableParam optMaxPayloadParam optMaxMemorySizeParam optIdentifiedByParam optConfirmDeliveryParam optParameters
    {
        CreateNotifierStmt *n = makeNode(CreateNotifierStmt);
        n->exists_ok          = FALSE;
        n->name               = $3.str;
        n->action             = $4.str;
        n->is_enabled         = $5;
        n->max_payload        = $6.str;
        n->max_memory_size    = $7.str;
        n->uuid               = $8.str;
        n->check_committed    = $9;
        n->adapter_params     = $10.str;
        $$ = (Node *)n;
    }
    ;

AlterNotifierStmt:
/* ALTER NOTIFIER name ACTION 'URI' [MAXPAYLOAD size] [IDENTIFIED BY 'uuid'] [ENABLE|DISABLE] [[NO] CHECK COMMITTED] [PARAMETERS 'adapter configs'] */
/* ALTER NOTIFIER name [MAXPAYLOAD size] [MAXMEMORYSIZE size] [IDENTIFIED BY 'uuid'] [ENABLE|DISABLE] [[NO] CHECK COMMITTED] [PARAMETERS 'adapter configs'] */
   ALTER NOTIFIER name optActionName optNotifierParams
   {
       AlterNotifierStmt *n = makeNode(AlterNotifierStmt);
       n->name              = $3.str;
       n->action            = $4.str;
       n->params            = $5;
       $$ = (Node *)n;
   }
   |
   ALTER NOTIFIER name optNotifierParams
   {
       AlterNotifierStmt *n = makeNode(AlterNotifierStmt);
       n->name              = $3.str;
       n->params            = $4;
       $$ = (Node *)n;
   }
   ;

optNotifierParams:
    notifierParams { $$ = $1; }
    | /* EMPTY */  { $$ = NIL; }
    ;

notifierParams:
    notifierParams notifierParam { $$ = lappend($1, $2); }
    | notifierParam              { $$ = list_make1($1); }
    ;

notifierParam:
    ENABLE
    {
        $$ = makeDefElem("is_enabled",(Node *)makeInteger(TRUE));
    }
    | DISABLE
    {
        $$ = makeDefElem("is_enabled",(Node *)makeInteger(FALSE));
    }
    | MAXPAYLOAD NONE
    {
        $$ = makeDefElem("max_payload",(Node *)makeStr(ctString("")));
    }
    | MAXPAYLOAD Sconst
    {
        $$ = makeDefElem("max_payload",(Node *)makeStr($2));
    }
    | MAXMEMORYSIZE Sconst
    {
        $$ = makeDefElem("max_memory_size",(Node *)makeStr($2));
    }
    | IDENTIFIED BY NONE
    {
        $$ = makeDefElem("uuid",(Node *)makeStr(ctString("")));
    }
    | IDENTIFIED BY Sconst
    {
        $$ = makeDefElem("uuid",(Node *)makeStr($3));
    }
    | CHECK COMMITTED
    {
        $$ = makeDefElem("check_committed",(Node *)makeInteger(TRUE));
    }
    | NO CHECK COMMITTED
    {
        $$ = makeDefElem("check_committed",(Node *)makeInteger(FALSE));
    }
    | PARAMETERS NONE
    {
        $$ = makeDefElem("adapter_params",(Node *)makeStr(ctString("")));
    }
    | PARAMETERS Sconst
    {
        $$ = makeDefElem("adapter_params",(Node *)makeStr($2));
    }
    ;

optActionName:
    ACTION Sconst       { $$ = $2; };

optIdentifiedByParam:
    IDENTIFIED BY NONE      { $$ = ctString(""); }
    | IDENTIFIED BY Sconst  { $$ = $3; }
    | /* EMPTY */           { $$ = ctNULL; }
    ;

optMaxPayloadParam:
    MAXPAYLOAD NONE      { $$ = ctString(""); }
    | MAXPAYLOAD Sconst  { $$ = $2; }
    | /* EMPTY */        { $$ = ctNULL; }
    ;

optMaxMemorySizeParam:
    MAXMEMORYSIZE Sconst  { $$ = $2; };


optConfirmDeliveryParam:
    NO CHECK COMMITTED  { $$ = false; }
    | CHECK COMMITTED   { $$ = true; }
    | /* EMPTY */       { $$ = false; }
    ;

optParameters:
    PARAMETERS NONE      { $$ = ctString(""); }
    | PARAMETERS Sconst  { $$ = $2; }
    | /* EMPTY */        { $$ = ctNULL; }
    ;


/*****************************************************************************
 *
 * Create and Alter Authentication
 *
 *
 *****************************************************************************/
/* CREATE AUTHENTICATION name METHOD 'method_name' LOCAL [ENABLE|DISABLE]*/
/* CREATE AUTHENTICATION name METHOD 'method_name' HOST [[NO] TLS] ip_address [ENABLE|DISABLE] */
CreateAuthStmt:
        CREATE AUTHENTICATION name METHOD authMethodName LOCAL optEnableDisableParam
            {
                CreateAuthStmt *n = makeNode(CreateAuthStmt);
                n->auth_name = $3.str;
                n->auth_method = $5.str;
                n->host_type = AH_LOCAL;
                n->ip_address = NULL;
                n->is_enabled = $7;
                $$ = (Node *)n;
            }
        | CREATE AUTHENTICATION name METHOD authMethodName HOST optHOSTParam authHostIPAddress optEnableDisableParam
            {
                CreateAuthStmt *n = makeNode(CreateAuthStmt);
                n->auth_name = $3.str;
                n->auth_method = $5.str;
                n->host_type = $7;
                n->ip_address = $8.str;
                n->is_enabled = $9;
                $$ = (Node *)n;
            }
        ;

/* ALTER AUTHENTICATION name METHOD 'method_name' LOCAL ENABLE|DISABLE */
/* ALTER AUTHENTICATION name METHOD 'method_name' HOST [[NO] TLS] 'ip_address' ENABLE|DISABLE */
/* ALTER AUTHENTICATION name METHOD 'method_name' */
/* ALTER AUTHENTICATION name ENABLE|DISABLE */
/* ALTER AUTHENTICATION name LOCAL */
/* ALTER AUTHENTICATION name HOST [[NO] TLS] 'ip_address' */
/* ALTER AUTHENTICATION name SET <PARAMS> */
AlterAuthStmt:
        ALTER AUTHENTICATION name METHOD authMethodName LOCAL nonoptEnableDisableParam
            {
                AlterAuthStmt *n = makeNode(AlterAuthStmt);
                n->auth_name = $3.str;
                n->auth_method = $5.str;
                n->host_type = AH_LOCAL;
                n->ip_address = NULL;
                n->is_enabled = $7;
                n->update_flag = AAF_ALMOST_ALL;
                $$ = (Node *)n;
            }
        | ALTER AUTHENTICATION name METHOD authMethodName HOST optHOSTParam authHostIPAddress nonoptEnableDisableParam
            {
                AlterAuthStmt *n = makeNode(AlterAuthStmt);
                n->auth_name = $3.str;
                n->auth_method = $5.str;
                n->host_type = $7;
                n->ip_address = $8.str;
                n->is_enabled = $9;
                n->update_flag = AAF_ALMOST_ALL;
                $$ = (Node *)n;
            }
        | ALTER AUTHENTICATION name METHOD authMethodName
            {
                AlterAuthStmt *n = makeNode(AlterAuthStmt);
                n->auth_name = $3.str;
                n->auth_method = $5.str;
                n->update_flag = AAF_METHOD;

                //fillers
                n->host_type = AH_NONE;
                n->ip_address = NULL;
                n->is_enabled = false;

                $$ = (Node *)n;
            }
        | ALTER AUTHENTICATION name nonoptEnableDisableParam
            {
                AlterAuthStmt *n = makeNode(AlterAuthStmt);
                n->auth_name = $3.str;
                n->is_enabled = $4;
                n->update_flag = AAF_ENABLED;

                //fillers
                n->auth_method = NULL;
                n->host_type = AH_NONE;
                n->ip_address = NULL;

                $$ = (Node *)n;
            }
        | ALTER AUTHENTICATION name LOCAL
            {
                AlterAuthStmt *n = makeNode(AlterAuthStmt);
                n->auth_name = $3.str;
                n->host_type = AH_LOCAL;
                n->ip_address = NULL;
                n->update_flag = AAF_HOST;

                //fillers
                n->auth_method = NULL;
                n->is_enabled = false;

                $$ = (Node *)n;
            }
        | ALTER AUTHENTICATION name HOST optHOSTParam authHostIPAddress
           {
                AlterAuthStmt *n = makeNode(AlterAuthStmt);
                n->auth_name = $3.str;
                n->host_type = $5;
                n->ip_address = $6.str;
                n->update_flag = AAF_HOST;

                //fillers
                n->auth_method = NULL;
                n->is_enabled = false;

                $$ = (Node *)n;
            }
        | ALTER AUTHENTICATION name SET optAuthParamList
            {
                AlterAuthStmt *n = makeNode(AlterAuthStmt);
                n->auth_name = $3.str;
                n->parameters = $5;
                $$ = (Node *)n;
            }
        | ALTER AUTHENTICATION name PRIORITY Iconst
            {
                AlterAuthStmt *n = makeNode(AlterAuthStmt);
                n->auth_name = $3.str;
                n->update_flag = AAF_PRIORITY;
                n->prior = $5;
                $$ = (Node *)n;
            }
        ;

/*
 * Options for CREATE/ALTER AUTHENTICATION
 */
optHOSTParam:
            TLS                 { $$ = AH_HOSTTLS; }
            | NO TLS            { $$ = AH_HOSTNOTLS; }
            | /* EMPTY */       { $$ = AH_HOST; }
        ;
optEnableDisableParam:
            ENABLE             { $$ = true; }
            | DISABLE          { $$ = false; }
            | /* EMPTY */      { $$ = true; /* default */ }
        ;
nonoptEnableDisableParam:
            ENABLE             { $$ = true; }
            | DISABLE          { $$ = false; }
        ;
authMethodName:    Sconst       { $$ = $1; };
authHostIPAddress: Sconst       { $$ = $1; };

optAuthParamList:
            optAuthParamElem                        { $$ = list_make1($1); }
            | optAuthParamList ',' optAuthParamElem { $$ = lappend($1,$3); }
        ;

optAuthParamElem:
            name '=' Sconst                { $$ = makeDefElem( $1.str, (Node *)makeStr($3)); }
        ;

/*****************************************************************************
 *
 * Create a new Profile
 *
 *
 *****************************************************************************/

CreateProfileStmt:
        CREATE PROFILE ProfileId LIMIT OptProfileList
        {
            CreateProfileStmt *n = makeNode(CreateProfileStmt);
            n->profile = $3.str;
            n->options = $5;
            $$ = (Node *)n;
        }
        ;

AlterProfileStmt:
        ALTER PROFILE ProfileId LIMIT OptProfileList
        {
            AlterProfileStmt *n = makeNode(AlterProfileStmt);
            n->profile = $3.str;
            n->options = $5;
            $$ = (Node *)n;
        }
        ;

/*
 * Options for CREATE/ALTER PROFILE
 */
OptProfileList:
        OptProfileList OptProfileElem            { $$ = lappend($1, $2); }
        | /* EMPTY */                            { $$ = NIL; }
        ;

OptProfileElem:
        PasswordParamIndex PasswordParamExpr      { $$ = makeMapElem($1, $2); }
        ;

PasswordParamIndex:
        PASSWORD_LIFE_TIME                 { $$ = T_PASSWORD_LIFE_TIME; }
        | PASSWORD_REUSE_MAX               { $$ = T_PASSWORD_REUSE_MAX; }
        | PASSWORD_REUSE_TIME              { $$ = T_PASSWORD_REUSE_TIME; }
        | PASSWORD_GRACE_TIME              { $$ = T_PASSWORD_GRACE_TIME; }
        | PASSWORD_LOCK_TIME               { $$ = T_PASSWORD_LOCK_TIME; }
        | FAILED_LOGIN_ATTEMPTS            { $$ = T_FAILED_LOGIN_ATTEMPTS; }
        | PASSWORD_MAX_LENGTH              { $$ = T_PASSWORD_MAX_LENGTH; }
        | PASSWORD_MIN_LENGTH              { $$ = T_PASSWORD_MIN_LENGTH; }
        | PASSWORD_MIN_LETTERS             { $$ = T_PASSWORD_MIN_LETTERS; }
        | PASSWORD_MIN_UPPERCASE_LETTERS   { $$ = T_PASSWORD_MIN_UPPERCASE_LETTERS; }
        | PASSWORD_MIN_LOWERCASE_LETTERS   { $$ = T_PASSWORD_MIN_LOWERCASE_LETTERS; }
        | PASSWORD_MIN_DIGITS              { $$ = T_PASSWORD_MIN_DIGITS; }
        | PASSWORD_MIN_SYMBOLS             { $$ = T_PASSWORD_MIN_SYMBOLS; }
        ;

PasswordParamExpr:
        Iconst                                { $$ = (Node *)makeInteger($1); }
        | DEFAULT                             { $$ = (Node *)makeInteger(PASSWORD_PARAM_DEFAULT); }
        | UNLIMITED                           { $$ = (Node *)makeInteger(PASSWORD_PARAM_UNLIMITED); }
        ;


/*****************************************************************************
 *
 * Create a new Role
 *
 *
 *****************************************************************************/

CreateRoleStmt:
            CREATE ROLE UserId
            {
                CreateRoleStmt *n = makeNode(CreateRoleStmt);
                n->name = $3.str;
                $$ = (Node *) n;
            }
            ;


/*****************************************************************************
 *
 *
 * Create a new  Model
 *
 *
 *****************************************************************************/
CreateModelStmt:
           CREATE MODEL qualified_name
           {
               CreateModelStmt *m = makeNode(CreateModelStmt);
               m->var = $3;
               $$ = (Node *) m;
           }
           ;

AlterModelStmt:
           ALTER MODEL relation_expr alter_model_cmds
           {
                    AlterModelStmt *n = makeNode(AlterModelStmt);
                    n->relation = $3;
                    n->cmds = $4;
                    $$ = (Node *)n;
           }
           ;

alter_model_cmds:
            alter_model_cmd                             { $$ = list_make1($1); }
            | alter_model_cmds ',' alter_model_cmd      { $$ = lappend($1, $3); }
        ;

alter_model_cmd:
          OWNER TO UserId
            {
                    AlterModelCmd *n = makeNode(AlterModelCmd);
                    n->subtype = AM_ChangeOwner;
                    n->name = $3.str;
                    $$ = (Node *) n;
            }
          | SET SCHEMA qualified_schema_name
            {
                    AlterModelCmd *n = makeNode(AlterModelCmd);
                    n->subtype = AM_SetSchema;
                    n->name = $3.str;
                    $$ = (Node *)n;
            }
        ;

           
/*****************************************************************************
 *
 * Create a postgresql group
 *
 *
 *****************************************************************************/

CreateGroupStmt:
            CREATE GROUP_P UserId opt_with OptGroupList
                {
                    CreateGroupStmt *n = makeNode(CreateGroupStmt);
                    n->name = $3.str;
                    n->options = $5;
                    $$ = (Node *)n;
                }
        ;

/*
 * Options for CREATE GROUP
 */
OptGroupList:
            OptGroupList OptGroupElem                { $$ = lappend($1, $2); }
            | /* EMPTY */                            { $$ = NIL; }
        ;

OptGroupElem:
            USER user_list
                {
                    $$ = makeDefElem("userElts", (Node *)$2);
                }
            | SYSID Iconst
                {
                    $$ = makeDefElem("sysid", (Node *)makeInteger($2));
                }
        ;


/*****************************************************************************
 *
 * Alter a postgresql group
 *
 *
 *****************************************************************************/

AlterGroupStmt:
            ALTER GROUP_P UserId add_drop USER user_list
                {
                    AlterGroupStmt *n = makeNode(AlterGroupStmt);
                    n->name = $3.str;
                    n->action = $4;
                    n->listUsers = $6;
                    $$ = (Node *)n;
                }
        ;

add_drop:    ADD                                        { $$ = +1; }
            | DROP                                    { $$ = -1; }
        ;


/*****************************************************************************
 *
 * Drop a postgresql group
 *
 * XXX see above notes about cascading DROP USER; groups have same problem.
 *****************************************************************************/

DropGroupStmt:
            DROP GROUP_P UserId
                {
                    DropGroupStmt *n = makeNode(DropGroupStmt);
                    n->name = $3.str;
                    $$ = (Node *)n;
                }
        ;

/*****************************************************************************
 *
 * Create a resource pool
 *
 *****************************************************************************/

CreateResourcePoolStmt:
            CREATE RESOURCE POOL name opt_res_pool_params
            {
                ResourcePoolStmt *n = makeNode(ResourcePoolStmt);
                n->name = $4.str;
                n->action = CREATE_RESOURCE_POOL;
                n->params = $5;
                $$ = (Node *)n;
            }
         ;

opt_res_pool_params:
            res_pool_params
            { $$ = $1; }
            | /* nothing */
            {
                $$ = NIL;
            }
         ;

res_pool_params:
            res_pool_params res_pool_param
            { $$ = lappend($1, $2); }
            | res_pool_param
            { $$ = list_make1($1); }
         ;

res_pool_param:
            MEMORYSIZE Sconst
            {
                $$ = makeDefElem("memorySize",(Node *)makeStr($2));
            }
            | MEMORYSIZE DEFAULT
            {
                $$ = makeDefElem("memorySize",NULL);
            }
            | MAXMEMORYSIZE Sconst
            {
                $$ = makeDefElem("maxMemorySize",(Node *)makeStr($2));
            }
            | MAXMEMORYSIZE NONE
            {
                $$ = makeDefElem("maxMemorySize",(Node *)makeStr(ctString("")));
            }
            | MAXMEMORYSIZE DEFAULT
            {
                $$ = makeDefElem("maxMemorySize",NULL);
            }
            | MAXQUERYMEMORYSIZE Sconst
            {
                $$ = makeDefElem("maxQueryMemorySize",(Node *)makeStr($2));
            }
            | MAXQUERYMEMORYSIZE NONE
            {
                $$ = makeDefElem("maxQueryMemorySize",(Node *)makeStr(ctString("")));
            }
            | MAXQUERYMEMORYSIZE DEFAULT
            {
                $$ = makeDefElem("maxQueryMemorySize",NULL);
            }
            | EXECUTIONPARALLELISM Iconst
            {
                $$ = makeDefElem("executionParallelism",(Node *)makeInteger($2));
            }
            | EXECUTIONPARALLELISM AUTO
            {
                $$ = makeDefElem("executionParallelism",NULL);
            }
            | EXECUTIONPARALLELISM DEFAULT
            {
                $$ = makeDefElem("executionParallelism",NULL);
            }
            | QUEUETIMEOUT Sconst
            {
                $$ = makeDefElem("queueTimeout",(Node *)makeStr($2));
            }
			| QUEUETIMEOUT Iconst
			{
				$$ = makeDefElem("queueTimeout", (Node *)makeInteger($2));
			}
            | QUEUETIMEOUT NONE
            {
                $$ = makeDefElem("queueTimeout",(Node *)makeStr(ctString("")));
            }
            | QUEUETIMEOUT DEFAULT
            {
                $$ = makeDefElem("queueTimeout",NULL);
            }
            | PRIORITY IntegerOnly
            {
                $$ = makeDefElem("priority",(Node *)$2);
            }
            | PRIORITY DEFAULT
            {
                $$ = makeDefElem("priority",NULL);
            }
            | PRIORITY HOLD
            {
                $$ = makeDefElem("priority",(Node *)makeInteger(-999));
            }
            | PLANNEDCONCURRENCY Iconst
            {
                $$ = makeDefElem("plannedConcurrency",(Node *)makeInteger($2));
            }
            | PLANNEDCONCURRENCY AUTO
            {
                $$ = makeDefElem("plannedConcurrency",(Node *)makeInteger(-1));
            }
            | PLANNEDCONCURRENCY DEFAULT
            {
                $$ = makeDefElem("plannedConcurrency",(Node *)makeInteger(-1));
            }
            | RUNTIMEPRIORITY RuntimePriorityValue
            {
                $$ = makeDefElem("runtimePriority",(Node *)$2);
            }
            | RUNTIMEPRIORITY DEFAULT
            {
                $$ = makeDefElem("runtimePriority",NULL);
            }
            | RUNTIMETHRESHOLD Iconst
            {
                $$ = makeDefElem("runtimePriorityThreshold",(Node *)makeInteger($2));
            }
            | RUNTIMETHRESHOLD DEFAULT
            {
                $$ = makeDefElem("runtimePriorityThreshold",NULL);
            }
            | SINGLEINITIATOR simple_boolean
            {
                $$ = makeDefElem("singleInitiator",(Node *)makeInteger($2));
            }
            | SINGLEINITIATOR AUTO
            {
                $$ = makeDefElem("singleInitiator",(Node *)makeInteger(-1));
            }
            | SINGLEINITIATOR DEFAULT
            {
                $$ = makeDefElem("singleInitiator",NULL);
            }
            | MAXCONCURRENCY Iconst
            {
                $$ = makeDefElem("maxConcurrency",(Node *)makeInteger($2));
            }
            | MAXCONCURRENCY NONE
            {
                $$ = makeDefElem("maxConcurrency",(Node *)makeInteger(-1));
            }
            | MAXCONCURRENCY DEFAULT
            {
                $$ = makeDefElem("maxConcurrency",NULL);
            }
            | MAXCONCURRENCYGRACE Iconst
            {
                $$ = makeDefElem("maxConcurrencyGrace",(Node *)makeInteger($2));
            }
            | RUNTIMECAP Sconst
            {
                $$ = makeDefElem("runTimeCap",(Node *)makeStr($2));
            }
            | RUNTIMECAP NONE
            {
                $$ = makeDefElem("runTimeCap",(Node *)makeStr(ctString("")));
            }
            | RUNTIMECAP DEFAULT
            {
                $$ = makeDefElem("runTimeCap",NULL);
            }
            | CPUAFFINITYSET Sconst
            {
                $$ = makeDefElem("cpuAffinitySet",(Node *)makeStr($2));
            }
            | CPUAFFINITYSET Iconst
            {
                $$ = makeDefElem("cpuAffinitySet",(Node *)makeInteger($2));
            }
            | CPUAFFINITYSET NONE
            {
                $$ = makeDefElem("cpuAffinitySet",NULL);
            }
            | CPUAFFINITYSET DEFAULT
            {
                $$ = makeDefElem("cpuAffinitySet",NULL);
            }
            | CPUAFFINITYMODE ANY
            {
                $$ = makeDefElem("cpuAffinityMode",(Node *)makeInteger(0));
            }
            | CPUAFFINITYMODE SHARED
            {
                $$ = makeDefElem("cpuAffinityMode",(Node *)makeInteger(1));
            }
            | CPUAFFINITYMODE EXCLUSIVE
            {
                $$ = makeDefElem("cpuAffinityMode",(Node *)makeInteger(3));
            }
            | CPUAFFINITYMODE DEFAULT
            {
                $$ = makeDefElem("cpuAffinityMode",NULL);
            }
            | CASCADE TO name
            {
                $$ = makeDefElem("cascadeTo",(Node *)makeStr($3));
            }
            | CASCADE TO DEFAULT
            {
                $$ = makeDefElem("cascadeTo",NULL);
            }
         ;

/*****************************************************************************
 *
 * Alter a resource pool
 *
 *****************************************************************************/

AlterResourcePoolStmt:
            ALTER RESOURCE POOL name res_pool_params
            {
                ResourcePoolStmt *n = makeNode(ResourcePoolStmt);
                n->name = $4.str;
                n->action = ALTER_RESOURCE_POOL;
                n->params = $5;
                $$ = (Node *)n;
            }
         ;

/*****************************************************************************
 *
 * Manipulate a schema
 *
 *****************************************************************************/

CreateSchemaStmt:
CREATE SCHEMA OptSchemaName AUTHORIZATION UserId OptDefaultInheritPrivileges OptSchemaEltList
                {
                    CreateSchemaStmt *n = makeNode(CreateSchemaStmt);
                    /* One can omit the schema name or the authorization id. */
                    if ($3.str != NULL)
                        n->schemaname = $3.str;
                    else
                        n->schemaname = $5.str;
                    n->schematype = CREATE_SCHEMA_TYPE_NORMAL;
                    n->authid = $5.str;
                    n->schemaElts = $7;
                    n->exists_ok = FALSE;
                    n->defaultInheritPrivileges = $6;
                    $$ = (Node *)n;
                }
| CREATE SCHEMA qualified_schema_name OptDefaultInheritPrivileges OptSchemaEltList
               {
                    CreateSchemaStmt *n = makeNode(CreateSchemaStmt);
                    /* ...but not both */
                    n->schemaname = $3.str;
                    n->schematype = CREATE_SCHEMA_TYPE_NORMAL;
                    n->authid = NULL;
                    n->schemaElts = $5;
                    n->defaultInheritPrivileges = $4;
                    $$ = (Node *)n;
                }
| CREATE SCHEMA IF_P NOT EXISTS OptSchemaName AUTHORIZATION UserId OptDefaultInheritPrivileges OptSchemaEltList
                {
                    CreateSchemaStmt *n = makeNode(CreateSchemaStmt);
                    /* One can omit the schema name or the authorization id. */
                    if ($6.str != NULL)
                        n->schemaname = $6.str;
                    else
                        n->schemaname = $8.str;
                    n->schematype = CREATE_SCHEMA_TYPE_NORMAL;
                    n->authid = $8.str;
                    n->schemaElts = $10;
                    n->exists_ok = TRUE;
                    n->defaultInheritPrivileges = $9;
                    $$ = (Node *)n;
                }
            // | CREATE SCHEMA IF_P NOT EXISTS ColId OptSchemaEltList
            //     {
            //         CreateSchemaStmt *n = makeNode(CreateSchemaStmt);
            //         /* ...but not both */
            //         n->schemaname = $6.str;
            //         n->schematype = CREATE_SCHEMA_TYPE_NORMAL;
            //         n->authid = NULL;
            //         n->schemaElts = $7;
            //         n->exists_ok = TRUE;
            //         $$ = (Node *)n;
            //     }
| CREATE SCHEMA IF_P NOT EXISTS qualified_schema_name OptDefaultInheritPrivileges OptSchemaEltList
                {
                    CreateSchemaStmt *n = makeNode(CreateSchemaStmt);
                    /* ...but not both */
                    n->schemaname = $6.str;
                    n->schematype = CREATE_SCHEMA_TYPE_NORMAL;
                    n->authid = NULL;
                    n->schemaElts = $8;
                    n->exists_ok = TRUE;
                    n->defaultInheritPrivileges = $7;
                    $$ = (Node *)n;
                }
| CREATE HCATALOG SCHEMA qualified_schema_name AUTHORIZATION UserId opt_with hcat_opt_list OptDefaultInheritPrivileges
                {
                    CreateSchemaStmt *n = makeNode(CreateSchemaStmt);
                    n->schemaname = $4.str;
                    n->schematype = CREATE_SCHEMA_TYPE_HCAT;
                    n->authid = $6.str;
                    n->schemaElts = NULL;
                    n->exists_ok = FALSE;
                    n->options = $8;
                    n->defaultInheritPrivileges = $9;
                    $$ = (Node *)n;
                }
| CREATE HCATALOG SCHEMA qualified_schema_name opt_with hcat_opt_list OptDefaultInheritPrivileges
                {
                    CreateSchemaStmt *n = makeNode(CreateSchemaStmt);
                    n->schemaname = $4.str;
                    n->schematype = CREATE_SCHEMA_TYPE_HCAT;
                    n->authid = NULL;
                    n->schemaElts = NULL;
                    n->exists_ok = FALSE;
                    n->options = $6;
                    n->defaultInheritPrivileges = $7;
                    $$ = (Node *)n;
                }
| CREATE HCATALOG SCHEMA IF_P NOT EXISTS qualified_schema_name AUTHORIZATION UserId opt_with hcat_opt_list OptDefaultInheritPrivileges
                {
                    CreateSchemaStmt *n = makeNode(CreateSchemaStmt);
                    n->schemaname = $7.str;
                    n->schematype = CREATE_SCHEMA_TYPE_HCAT;
                    n->authid = $9.str;
                    n->schemaElts = NULL;
                    n->exists_ok = TRUE;
                    n->options = $11;
                    n->defaultInheritPrivileges = $12;
                    $$ = (Node *)n;
                }
| CREATE HCATALOG SCHEMA IF_P NOT EXISTS qualified_schema_name opt_with hcat_opt_list OptDefaultInheritPrivileges
                {
                    CreateSchemaStmt *n = makeNode(CreateSchemaStmt);
                    n->schemaname = $7.str;
                    n->schematype = CREATE_SCHEMA_TYPE_HCAT;
                    n->authid = NULL;
                    n->schemaElts = NULL;
                    n->exists_ok = TRUE;
                    n->options = $9;
                    n->defaultInheritPrivileges = $10;
                    $$ = (Node *)n;
                }
        ;

OptDefaultInheritPrivileges:
            DEFAULT INCLUDE SCHEMA PRIVILEGES { $$ = true; }
            |DEFAULT INCLUDE PRIVILEGES { $$ = true; }
            |DEFAULT EXCLUDE SCHEMA PRIVILEGES { $$ = false; }
            |DEFAULT EXCLUDE PRIVILEGES { $$ = false; }
            | /*EMPTY*/ { $$ = false; }                   
        ;

hcat_opt_list:
            hcat_opt_list hcat_opt_item        { $$ = lappend($1, $2); }
            | /* EMPTY */                      { $$ = NIL; }
        ;

hcat_opt_item:
            HOSTNAME opt_equal Sconst
                {
                    $$ = makeDefElem("hostname", (Node *)makeStr($3));
                }
            | PORT opt_equal Iconst
                {
                    $$ = makeDefElem("port", (Node *)makeInteger($3));
                }
            | HIVESERVER2_HOSTNAME opt_equal Sconst
                {
                    $$ = makeDefElem("hiveserver2_hostname", (Node *)makeStr($3));
                }
            | WEBSERVICE_PORT opt_equal Iconst
                {
                    $$ = makeDefElem("webservice_port", (Node *)makeInteger($3));
                }
            | WEBHDFS_ADDRESS opt_equal Sconst
                {
                    $$ = makeDefElem("webhdfs_address", (Node *)makeStr($3));
                }
            | HCATALOG_SCHEMA opt_equal Sconst
                {
                    $$ = makeDefElem("hcat_schema", (Node *)makeStr($3));
                }
            | HCATALOG_DB opt_equal Sconst // Same as above.
                {
                    $$ = makeDefElem("hcat_schema", (Node *)makeStr($3));
                }
            | HCATALOG_USER opt_equal Sconst
                {
                    $$ = makeDefElem("hcat_user", (Node *)makeStr($3));
                }
            | WEBSERVICE_HOSTNAME opt_equal Sconst
                {
                    $$ = makeDefElem("webservice_hostname", (Node *)makeStr($3));
                }
            | SSL_CONFIG opt_equal Sconst
                {
                    $$ = makeDefElem("ssl_config", (Node *)makeStr($3));
                }
            | CUSTOM_PARTITIONS opt_equal Iconst
                {
                    $$ = makeDefElem("custom_partitions", (Node *)makeInteger($3));
                }
            | CUSTOM_PARTITIONS opt_equal Sconst
                {
                    $$ = makeDefElem("custom_partitions", (Node *)makeStr($3));
                }
            | CUSTOM_PARTITIONS opt_equal simple_boolean
                {
                    $$ = makeDefElem("custom_partitions", (Node *)makeInteger($3));
                }
            | HCATALOG_CONNECTION_TIMEOUT opt_equal Iconst
                {
                    $$ = makeDefElem("hcat_connection_timeout", (Node *)makeInteger($3));
                }
            | HCATALOG_SLOW_TRANSFER_LIMIT opt_equal Iconst
                {
                    $$ = makeDefElem("hcat_slow_transfer_limit", (Node *)makeInteger($3));
                }
            | HCATALOG_SLOW_TRANSFER_TIME opt_equal Iconst
                {
                    $$ = makeDefElem("hcat_slow_transfer_time", (Node *)makeInteger($3));
                }

        ;

OptSchemaName:
            qualified_schema_name                    { $$ = $1; }
            | /* EMPTY */                            { $$ = ctNULL; }
        ;

OptSchemaEltList:
            OptSchemaEltList schema_stmt            { $$ = lappend($1, $2); }
            | /* EMPTY */                            { $$ = NIL; }
        ;

/*
 *    schema_stmt are the ones that can show up inside a CREATE SCHEMA
 *    statement (in addition to by themselves).
 */
schema_stmt:
            CreateStmt
            | IndexStmt
            | CreateSeqStmt
            | CreateTrigStmt
            | GrantStmt
            | ViewStmt
            | VCreateProjectionStmt
        ;


/*****************************************************************************
 *
 *        ALTER HCATALOG SCHEMA
 *
 *****************************************************************************/
AlterHCatalogSchemaStmt:
          ALTER HCATALOG SCHEMA qualified_schema_name SET PARAMETER hcat_opt_list
               {
                   AlterHCatalogSchemaStmt *n = makeNode(AlterHCatalogSchemaStmt);
                   n->schemaname = $4.str;
                   n->params = $7;
                   $$ = (Node *)n;
               }
          | ALTER HCATALOG SCHEMA qualified_schema_name SET hcat_opt_list
               {
                   AlterHCatalogSchemaStmt *n = makeNode(AlterHCatalogSchemaStmt);
                   n->schemaname = $4.str;
                   n->params = $6;
                   $$ = (Node *)n;
               }
          ;   

/*****************************************************************************
 *
 *        ALTER SESSION
 *
 *****************************************************************************/
AlterSessionStmt:
           ALTER SESSION SET PARAMETER paramarg_list
                {
                    AlterSessionStmt *n = makeNode(AlterSessionStmt);
                    n->setParams = true;
                    n->udParams = false;
                    n->params = $5;
                    n->nsp = NULL;
                    $$ = (Node *)n;
                }
           | ALTER SESSION SET paramarg_list
                {
                    AlterSessionStmt *n = makeNode(AlterSessionStmt);
                    n->setParams = true;
                    n->udParams = false;
                    n->params = $4;
                    n->nsp = NULL;
                    $$ = (Node *)n;
                }
           | ALTER SESSION CLEAR PARAMETER knob_list
                {
                    AlterSessionStmt *n = makeNode(AlterSessionStmt);
                    n->setParams = false;
                    n->udParams = false;
                    n->params = $5;
                    n->nsp = NULL;
                    $$ = (Node *)n;
                }
           | ALTER SESSION CLEAR knob_list
                {
                    AlterSessionStmt *n = makeNode(AlterSessionStmt);
                    n->setParams = false;
                    n->udParams = false;
                    n->params = $4;
                    n->nsp = NULL;
                    $$ = (Node *)n;
                }
           | ALTER SESSION SET UDPARAMETER opt_namespace paramarg_list
                {
                    AlterSessionStmt *n = makeNode(AlterSessionStmt);
                    n->setParams = true;
                    n->udParams = true;
                    n->nsp = $5;
                    n->params = $6;
                    $$ = (Node *)n;
                }
           | ALTER SESSION CLEAR UDPARAMETER opt_namespace knob_list
                {
                    AlterSessionStmt *n = makeNode(AlterSessionStmt);
                    n->setParams = false;
                    n->udParams = true;
                    n->nsp = $5;                  
                    n->params = $6;
                    $$ = (Node *)n;
                }
          | ALTER SESSION CLEAR UDPARAMETER ALL opt_namespace
                {
                    AlterSessionStmt *n = makeNode(AlterSessionStmt);
                    n->setParams = false;
                    n->udParams = true;
                    n->nsp = $6;                  
                    n->params = NULL;
                    $$ = (Node *)n;
                }


        ;

opt_namespace:
            FOR qualified_name            
                { 
                    $$=  $2;
                }
            | /*EMPTY*/                   
                { 
                    $$ = NULL; 
                }
        ;


/*****************************************************************************
 *
 * Set PG internal variable
 *      SET name TO 'var_value'
 * Include SQL92 syntax (thomas 1997-10-22):
 *      SET TIME ZONE 'var_value'
 *
 *****************************************************************************/

VariableSetStmt:
            SET set_rest
                {
                    VariableSetStmt *n = $2;
                    n->is_local = false;
                    $$ = (Node *) n;
                }
            | SET LOCAL set_rest
                {
                    VariableSetStmt *n = $3;
                    n->is_local = true;
                    $$ = (Node *) n;
                }
            | SET SESSION set_rest
                {
                    VariableSetStmt *n = $3;
                    n->is_local = false;
                    $$ = (Node *) n;
                }
        ;

set_rest:   function_name TO var_list_or_default_all_except
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = $1.str;
                    n->args = $3;
                    $$ = n;
                }
            | function_name '=' var_list_or_default_all_except
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = $1.str;
                    n->args = $3;
                    $$ = n;
                }
            | timezone opt_to_or_equalsign zone_value
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "timezone";
                    if ($3 != NULL)
                        n->args = list_make1($3);
                    $$ = n;
                }
            | SESSION CHARACTERISTICS AS TRANSACTION transaction_mode_list
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "SESSION CHARACTERISTICS";
                    n->args = $5;
                    $$ = n;
                }
            | SESSION AUTHORIZATION ColId_or_Sconst
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "session_authorization";
                    n->args = list_make1(makeStringConst($3, NULL));
                    $$ = n;
                }
            | SESSION AUTHORIZATION DEFAULT
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "session_authorization";
                    n->args = NIL;
                    $$ = n;
                }
            | SESSION RESOURCE POOL name
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "resource_pool";
                    n->args = list_make1(makeStringConst($4, NULL));
                    $$ = n;
                }
            | SESSION MEMORYCAP Sconst
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "memorycap";
                    n->args = list_make1(makeStringConst($3,NULL));
                    $$ = n;
                }
            | SESSION MEMORYCAP NONE
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "memorycap";
                    n->args = list_make1(makeStringConst(ctString(""),NULL));
                    $$ = n;
                }
            | SESSION TEMPSPACECAP Sconst
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "tempspacecap";
                    n->args = list_make1(makeStringConst($3,NULL));
                    $$ = n;
                }
            | SESSION TEMPSPACECAP NONE
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "tempspacecap";
                    n->args = list_make1(makeStringConst(ctString(""),NULL));
                    $$ = n;
                }
            | SESSION RUNTIMECAP Sconst
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "runtimecap";
                    n->args = list_make1(makeStringConst($3,NULL));
                    $$ = n;
                }
            | SESSION RUNTIMECAP NONE
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "runtimecap";
                    n->args = list_make1(makeStringConst(ctString(""),NULL));
                    $$ = n;
                }
            | SESSION IDLESESSIONTIMEOUT Sconst
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "idlesessiontimeout";
                    n->args = list_make1(makeStringConst($3, NULL));
                    $$ = n;
                }
            | SESSION IDLESESSIONTIMEOUT NONE
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "idlesessiontimeout";
                    n->args = list_make1(makeStringConst(ctString(""), NULL));
                    $$ = n;
                }
            | SESSION GRACEPERIOD Sconst
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "graceperiod";
                    n->args = list_make1(makeStringConst($3, NULL));
                    $$ = n;
                }
            | SESSION GRACEPERIOD NONE
                {
                    VariableSetStmt *n = makeNode(VariableSetStmt);
                    n->name = "graceperiod";
                    n->args = list_make1(makeStringConst(ctString(""), NULL));
                    $$ = n;
                }
            | ROLE var_list_or_default_all_except
               {
                   VariableSetStmt *n = makeNode(VariableSetStmt);
                   n->name = "role";
                   n->args = $2;
                   $$ = n;
               }
/*            | SECURITY_ALGORITHM Sconst
                {
                    $$ = makeDefElem("security_algorithm",(Node *)makeStr($2));
                }
*/        ;

timezone:   TIME ZONE                            { $$ = NULL; }
            | TIMEZONE                           { $$ = NULL; }
        ;

opt_to_or_equalsign:
            TO                                   { $$ = TRUE; }
            | '='                                { $$ = TRUE; }
            | /*EMPTY*/                          { $$ = FALSE; }
        ;

var_list_or_default_all_except:
            var_list_or_default                     { $$ = $1; }
            | ALL                                   { $$ = list_make1(makeStringConst(ctString($1),NULL)); }
            | ALL EXCEPT var_list                   { $$ = list_concat(list_make1(makeStringConst(ctString($2),NULL)), $3); }
        ;

var_list_or_default:
            var_list                                { $$ = $1; }
            | DEFAULT                               { $$ = NIL; }
        ;

var_list:    var_value                                { $$ = list_make1($1); }
            | var_list ',' var_value                { $$ = lappend($1, $3); }
        ;

var_value:    opt_boolean
                { $$ = makeStringConst($1, NULL); }
            | ColId_or_Sconst
                { $$ = makeStringConst($1, NULL); }
            | NumericOnly
                { $$ = makeAConst($1); }
        ;

iso_level:    READ UNCOMMITTED          { $$ = ctString("read uncommitted"); }
            | READ COMMITTED            { $$ = ctString("read committed"); }
            | REPEATABLE READ           { $$ = ctString("repeatable read"); }
            | SERIALIZABLE              { $$ = ctString("serializable"); }
        ;

opt_boolean: /* Only values that can't be ColId, see above */ 
            TRUE_P                      { $$ = ctString("true"); }
            | FALSE_P                   { $$ = ctString("false"); }
            | ON                        { $$ = ctString("on"); }
        ;

simple_boolean:
            TRUE_P                      { $$ = 1; }
            | FALSE_P                   { $$ = 0; }
        ;

/* Timezone values can be:
 * - a string such as 'pst8pdt'
 * - an identifier such as "pst8pdt"
 * - something like America/New_York
 * - a signed floating point number, in hours
 * - something like -515 or -5:15
 * - a time interval per SQL99
 * ColId gives reduce/reduce errors against ConstInterval and LOCAL,
 * so use IDENT and reject anything which is a reserved word.
 */
zone_value:
            Sconst
                {
                    $$ = makeStringConst($1, NULL);
                }
            | IDENT
                {
                    $$ = makeStringConst($1, NULL);
                }
            | IDENT '/' IDENT
                {
                    int32 sz = $1.leng + 1 + $3.leng;
                    char *s = (char *) palloc(sz + 1);
                    ctStr str = {s, sz};
                    strcpy(s, $1.str);
                    strcat(s, "/");
                    strcat(s, $3.str);
                    $$ = makeStringConst(str, NULL);
                }
            | ConstInterval opt_minus Sconst interval_qualifier
                {
                    A_Const *n = (A_Const *) makeStringConst($3, $1);
                    if (INTERVAL_RANGE($4) == 0) // unspecified
                        $4 = INTERVAL_TYPMOD(0,
                                             INTERVAL_MASK(HOUR) |
                                             INTERVAL_MASK(MINUTE));
                    if ($2)
                        $4 |= INTERVAL_TYPMOD(0, INTERVAL_MASK(NEG_INTERVAL));
                    n->typeInfo->typmod = $4;
                    $$ = (Node *)n;
                }
            | opt_minus FCONST
                {
                    Value *f = makeFloat($2);
                    if ($1)
                        doNegateFloat(f);
                    $$ = makeAConst(f);
                }
            | opt_minus Iconst opt_minutes
                {
                    if ($3)
                        $2 = 100 * $2 + $3;
                    $$ = makeIntConst($1 ? -$2 : $2);
                }
            | DEFAULT                                { $$ = NULL; }
            | LOCAL                                  { $$ = NULL; }
        ;

ColId_or_Sconst:
            ColId                                    { $$ = $1; }
            | SCONST                                { $$ = $1; }
        ;

opt_minutes:
            ':' Iconst                               { $$ = $2; }
            | /*EMPTY*/                              { $$ = 0; }
        ;

CurrentVariableShowStmt:
            SHOW CURRENT_P ALL
                {
                    CurrentVariableShowStmt *n = makeNode(CurrentVariableShowStmt);
                    n->all = true;
                    $$ = (Node *) n;
                }
            | SHOW CURRENT_P PARAMETER ALL
                {
                    CurrentVariableShowStmt *n = makeNode(CurrentVariableShowStmt);
                    n->all = true;
                    $$ = (Node *) n;
                }
            | SHOW CURRENT_P knob_list
                {
                    CurrentVariableShowStmt *n = makeNode(CurrentVariableShowStmt);
                    n->all = false;
                    n->params = $3;
                    $$ = (Node *) n;
                }
            | SHOW CURRENT_P PARAMETER knob_list
                {
                    CurrentVariableShowStmt *n = makeNode(CurrentVariableShowStmt);
                    n->all =false;
                    n->params = $4;
                    $$ = (Node *) n;
                }
        ;

VariableShowStmt:
            SHOW ColId
                {
                    VariableShowStmt *n = makeNode(VariableShowStmt);
                    n->configParams = false;
                    n->all = false;
                    n->udParams=false;
                    n->name = $2.str;
                    $$ = (Node *) n;
                }
            | SHOW TIME ZONE            // or TIMEZONE
                {
                    VariableShowStmt *n = makeNode(VariableShowStmt);
                    n->configParams = false;
                    n->all = false;
                    n->udParams=false;
                    n->name = "timezone";
                    $$ = (Node *) n;
                }
            | SHOW TRANSACTION ISOLATION LEVEL
                {
                    VariableShowStmt *n = makeNode(VariableShowStmt);
                    n->configParams = false;
                    n->all = false;
                    n->udParams=false;
                    n->name = "transaction_isolation";
                    $$ = (Node *) n;
                }
            | SHOW SESSION AUTHORIZATION
                {
                    VariableShowStmt *n = makeNode(VariableShowStmt);
                    n->configParams = false;
                    n->all = false;
                    n->udParams=false;
                    n->name = "session_authorization";
                    $$ = (Node *) n;
                }
            | SHOW RESOURCE POOL
                {
                    VariableShowStmt *n = makeNode(VariableShowStmt);
                    n->configParams = false;
                    n->all = false;
                    n->udParams=false;
                    n->name = "resource_pool";
                    $$ = (Node *) n;
                }
            | SHOW ENABLED ROLES
                {
                    VariableShowStmt *n = makeNode(VariableShowStmt);
                    n->configParams = false;
                    n->all = false;
                    n->udParams=false;
                    n->name = "enabled_roles";
                    $$ = (Node *) n;
                }
            | SHOW AVAILABLE ROLES
                {
                    VariableShowStmt *n = makeNode(VariableShowStmt);
                    n->configParams = false;
                    n->all = false;
                    n->udParams=false;
                    n->name = "available_roles";
                    $$ = (Node *) n;
                }
            | SHOW ALL
                {
                    VariableShowStmt *n = makeNode(VariableShowStmt);
                    n->configParams = false;
                    n->all = true;
                    n->udParams=false;
                    $$ = (Node *) n;
                }
            | SHOW SESSION ALL
                {
                    VariableShowStmt *n = makeNode(VariableShowStmt);
                    n->configParams = true;
                    n->all = true;
                    n->udParams=false;
                    $$ = (Node *) n;
                }
            | SHOW SESSION PARAMETER ALL
                {
                    VariableShowStmt *n = makeNode(VariableShowStmt);
                    n->configParams = true;
                    n->all = true;
                    n->udParams=false;
                    $$ = (Node *) n;
                }
            | SHOW SESSION knob_list
                {
                    VariableShowStmt *n = makeNode(VariableShowStmt);
                    n->configParams = true;
                    n->all = false;
                    n->udParams=false;
                    n->params = $3;
                    $$ = (Node *) n;
                }
            | SHOW SESSION PARAMETER knob_list
                {
                    VariableShowStmt *n = makeNode(VariableShowStmt);
                    n->configParams = true;
                    n->all = false;
                    n->udParams=false;
                    n->params = $4;
                    $$ = (Node *) n;
                }
            | SHOW SESSION UDPARAMETER ALL
                {
                    VariableShowStmt *n = makeNode(VariableShowStmt);
                    n->configParams = false;
                    n->all = true;
                    n->udParams=true;
                    $$ = (Node *) n;
                }
        ;

VariableResetStmt:
            RESET ColId
                {
                    VariableResetStmt *n = makeNode(VariableResetStmt);
                    n->name = $2.str;
                    $$ = (Node *) n;
                }
            | RESET TIME ZONE           // or TIMEZONE
                {
                    VariableResetStmt *n = makeNode(VariableResetStmt);
                    n->name = "timezone";
                    $$ = (Node *) n;
                }
            | RESET TRANSACTION ISOLATION LEVEL
                {
                    VariableResetStmt *n = makeNode(VariableResetStmt);
                    n->name = "transaction_isolation";
                    $$ = (Node *) n;
                }
            | RESET SESSION AUTHORIZATION
                {
                    VariableResetStmt *n = makeNode(VariableResetStmt);
                    n->name = "session_authorization";
                    $$ = (Node *) n;
                }
            | RESET ALL
                {
                    VariableResetStmt *n = makeNode(VariableResetStmt);
                    n->name = "all";
                    $$ = (Node *) n;
                }
        ;


ConstraintsSetStmt:
            SET CONSTRAINTS constraints_set_list constraints_set_mode
                {
                    ConstraintsSetStmt *n = makeNode(ConstraintsSetStmt);
                    n->constraints = $3;
                    n->deferred    = $4;
                    $$ = (Node *) n;
                }
        ;

constraints_set_list:
            ALL                                        { $$ = NIL; }
            | name_list                                { $$ = $1; }
        ;

constraints_set_mode:
            DEFERRED                                { $$ = TRUE; }
            | IMMEDIATE                                { $$ = FALSE; }
        ;


/*
 * Checkpoint statement
 */
CheckPointStmt:
            CHECKPOINT
                {
                    CheckPointStmt *n = makeNode(CheckPointStmt);
                    $$ = (Node *)n;
                }
        ;

AlterViewStmt:
            ALTER VIEW qualified_name OWNER TO UserId
            {
                AlterViewStmt *n = makeNode(AlterViewStmt);
                n->subtype = AT_AlterOwner;
                n->viewname = $3;
                n->name = $6.str;
                $$ = (Node *)n;
            }
            | ALTER VIEW qualified_name SET SCHEMA qualified_schema_name
            {
                AlterViewStmt *n = makeNode(AlterViewStmt);
                n->subtype = AT_AlterSchema;
                n->viewname = $3;
                n->name = $6.str;
                $$ = (Node *)n;
            }
        ;
        
/*********************************
 *
 *    ALTER SCHEMA (except rename)
 *
 *********************************/
AlterSchemaStmt:
            ALTER SCHEMA qualified_schema_name DEFAULT INCLUDE OptSchemaKeyword PRIVILEGES
                {
                    AlterSchemaStmt *n = makeNode(AlterSchemaStmt);
                    n->alterSchemaType = ALTER_SCHEMA_INHERITED_PRIVILEGE;
                    n->schemaname = $3.str;
                    n->defaultInheritPrivileges = true;
                    $$ = (Node *)n;
                }
            | ALTER SCHEMA qualified_schema_name DEFAULT EXCLUDE OptSchemaKeyword PRIVILEGES
                {
                    AlterSchemaStmt *n = makeNode(AlterSchemaStmt);
                    n->alterSchemaType = ALTER_SCHEMA_INHERITED_PRIVILEGE;
                    n->schemaname = $3.str;
                    n->defaultInheritPrivileges = false;
                    $$ = (Node *)n;
                }
            | ALTER SCHEMA qualified_schema_name OWNER TO UserId opt_schema_owner_behavior
                {
                    AlterSchemaStmt *n = makeNode(AlterSchemaStmt);
                    n->alterSchemaType = ALTER_SCHEMA_OWNER;
                    n->schemaname = $3.str;
                    n->newOwner = $6.str;
                    n->cascade = $7;
                    $$ = (Node *)n;
                }
        ;
        
opt_schema_owner_behavior:
        CASCADE                  { $$=TRUE; }
        | /* EMPTY */            { $$=FALSE; }
        ;

/*****************************************************************************
 *
 *    ALTER VIEW operations to change inherited privileges
 *
 *****************************************************************************/                
AlterViewPrivilegesStmt:
            ALTER VIEW qualified_name INCLUDE OptSchemaKeyword PRIVILEGES
                {
                    AlterViewPrivilegesStmt *n = makeNode(AlterViewPrivilegesStmt);
                    n->view = $3;
                    n->inheritPrivileges = true;
                    n->subtype = AV_InheritPrivileges;
                    $$ = (Node *)n;
                }
            | ALTER VIEW qualified_name EXCLUDE OptSchemaKeyword PRIVILEGES
                {
                    AlterViewPrivilegesStmt *n = makeNode(AlterViewPrivilegesStmt);
                    n->view = $3;
                    n->inheritPrivileges = false;
                    n->subtype = AV_InheritPrivileges;
                    $$ = (Node *)n;
                }
            | ALTER VIEW qualified_name MATERIALIZE OptSchemaKeyword PRIVILEGES
                {
                    AlterViewPrivilegesStmt *n = makeNode(AlterViewPrivilegesStmt);
                    n->view = $3;
                    n->inheritPrivileges = false;
                    n->subtype = AV_MaterializePrivileges;
                    $$ = (Node *)n;
                }
		;

/*****************************************************************************
 *
 *    ALTER [ TABLE | INDEX ] variations
 *
 *****************************************************************************/

AlterTableStmt:
            ALTER TABLE relation_expr alter_table_cmds
                {
                    AlterTableStmt *n = makeNode(AlterTableStmt);
                    n->relation = $3;
                    n->cmds = $4;
                    n->relkind = OBJECT_TABLE;
                    $$ = (Node *)n;
                }
        |    ALTER INDEX relation_expr alter_rel_cmds
                {
                    AlterTableStmt *n = makeNode(AlterTableStmt);
                    n->relation = $3;
                    n->cmds = $4;
                    n->relkind = OBJECT_INDEX;
                    $$ = (Node *)n;
                }
        ;

alter_table_cmds:
            alter_table_cmd                            { $$ = list_make1($1); }
            | alter_table_cmds ',' alter_table_cmd    { $$ = lappend($1, $3); }
        ;

/* Subcommands that are for ALTER TABLE only */
alter_table_cmd:
            /* ALTER TABLE <relation> ADD [COLUMN] <coldef> */
            ADD opt_column columnDef encode_type opt_proj_list opt_drop_behavior
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_AddColumn;
                    n->def = $3;
                    n->encodeType = $4;
                    n->projList = $5;
                    n->includeAllProjs = FALSE;
                    n->behavior = $6;
                    n->column_exists_ok = FALSE;
                    $$ = (Node *)n;
                }
            | ADD opt_column IF_P NOT EXISTS columnDef encode_type opt_proj_list opt_drop_behavior
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_AddColumn;
                    n->def = $6;
                    n->encodeType = $7;
                    n->projList = $8;
                    n->includeAllProjs = FALSE;
                    n->behavior = $9;
                    n->column_exists_ok = TRUE;
                    $$ = (Node *)n;
                }
            | ADD opt_column columnDef encode_type ALL PROJECTIONS opt_drop_behavior
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_AddColumn;
                    n->def = $3;
                    n->encodeType = $4;
                    n->includeAllProjs = TRUE;
                    n->behavior = $7;
                    n->column_exists_ok = FALSE;
                    $$ = (Node *)n;
                }
            | ADD opt_column IF_P NOT EXISTS columnDef encode_type ALL PROJECTIONS opt_drop_behavior
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_AddColumn;
                    n->def = $6;
                    n->encodeType = $7;
                    n->includeAllProjs = TRUE;
                    n->behavior = $10;
                    n->column_exists_ok = TRUE;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <relation> ALTER [COLUMN] <colname> {SET DEFAULT <expr>|DROP DEFAULT} */
            | ALTER opt_column columnElem alter_column_default
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_ColumnDefault;
                    n->name = $3.str;
                    n->def = $4;
                    $$ = (Node *)n;
                }
            | ALTER opt_column columnElem alter_column_setusing
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_ColumnSetUsing;
                    n->name = $3.str;
                    n->def = $4;
                    $$ = (Node *)n;
                }
            | ALTER opt_column columnElem alter_column_defaultusing
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_ColumnDefaultUsing;
                    n->name = $3.str;
                    n->def = $4;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <relation> ALTER [COLUMN] <colname> DROP NOT NULL */
            | ALTER opt_column columnElem DROP NOT NULL_P
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_DropNotNull;
                    n->name = $3.str;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <relation> ALTER [COLUMN] <colname> SET NOT NULL */
            | ALTER opt_column columnElem SET NOT NULL_P
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_SetNotNull;
                    n->name = $3.str;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <relation> ALTER [COLUMN] <colname> SET STATISTICS <IntegerOnly> */
            | ALTER opt_column columnElem SET STATISTICS IntegerOnly
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_SetStatistics;
                    n->name = $3.str;
                    n->def = (Node *) $6;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <relation> ALTER [COLUMN] <colname> SET STORAGE <storagemode> */
            | ALTER opt_column columnElem SET STORAGE ColId
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_SetStorage;
                    n->name = $3.str;
                    n->def = (Node *) makeStr($6);
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <relation> DROP [COLUMN] <colname> [RESTRICT|CASCADE] */
            | DROP opt_column columnElem opt_drop_behavior
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_DropColumn;
                    n->name = $3.str;
                    n->behavior = $4;
                    n->column_missing_ok = FALSE;
                    $$ = (Node *)n;
                }
            | DROP opt_column IF_P EXISTS columnElem opt_drop_behavior
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_DropColumn;
                    n->name = $5.str;
                    n->behavior = $6;
                    n->column_missing_ok = TRUE;
                    $$ = (Node *)n;
                }
            /*
             * ALTER TABLE <relation> ALTER [COLUMN] <colname> TYPE <typename>
             *        [ USING <expression> ]
             */
            | ALTER opt_column columnElem SET DATA_P TYPE_P TypenameWithTypmod
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_AlterColumnType;
                    n->name = $3.str;
                    n->def = (Node *) $7;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <relation> ADD CONSTRAINT ... */
            | ADD TableConstraint
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_AddConstraint;
                    n->def = $2;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <relation> SET OPTION ... */
            | SET STORAGE copy_storage_mode
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = $3;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <relation> SET ACTIVEPARTITIONCOUNT ... */
            | SET ACTIVEPARTITIONCOUNT active_partition_count
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_AlterActivePartitionCount;
                    n->activePartitionCount = $3;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <relation> DROP CONSTRAINT IF EXISTS <name> [RESTRICT|CASCADE] */
            | DROP CONSTRAINT IF_P EXISTS name opt_drop_behavior
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_DropConstraint;
                    n->name = $5.str;
                    n->behavior = $6;
                    n->missing_ok = TRUE;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <relation> DROP CONSTRAINT <name> [RESTRICT|CASCADE] */
            | DROP CONSTRAINT name opt_drop_behavior
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_DropConstraint;
                    n->name = $3.str;
                    n->behavior = $4;
                    n->missing_ok = FALSE;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <relation> ALTER CONSTRAINT <name> [ENABLED|DISABLED] */
            | ALTER CONSTRAINT name set_constr_status
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_AlterConstraintStatus;
                    n->name = $3.str;
                    n->def = (Node *)makeNode(Constraint);
                    ((Constraint *)n->def)->name = $3.str;
                    ((Constraint *)n->def)->status = $4;
                    n->missing_ok = FALSE;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <relation> SET WITHOUT OIDS  */
            | SET WITHOUT OIDS
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_DropOids;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <name> CREATE TOAST TABLE -- ONLY */
            | CREATE TOAST TABLE
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_ToastTable;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <name> CLUSTER ON <indexname> */
            | CLUSTER ON name
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_ClusterOn;
                    n->name = $3.str;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <name> SET WITHOUT CLUSTER */
            | SET WITHOUT CLUSTER
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_DropCluster;
                    n->name = NULL;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <name> SET SCHEMA <schemaname> [CASCADE|RESTRICT] */
            | SET SCHEMA qualified_schema_name opt_setschema_behavior
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_SetSchema;
                    n->name = $3.str;
                    n->behavior = $4;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <name> PARTITION BY <b_expr> GROUP BY <b_expr> SET ACTIVEPARTITIONCOUNT <active_partition_count> [REORGANIZE] */
            | PARTITION BY b_expr GROUP_P BY b_expr SET ACTIVEPARTITIONCOUNT active_partition_count opt_reorganize
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_PartitionBy;
                    n->name = NULL;
                    n->partitionExpr = $3;
                    n->partnGroupExpr = $6;
                    n->activePartitionCount = $9;
                    n->reorganize = $10;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <name> PARTITION BY <b_expr> GROUP BY <b_expr> [REORGANIZE] */
            | PARTITION BY b_expr GROUP_P BY b_expr opt_reorganize
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_PartitionBy;
                    n->name = NULL;
                    n->partitionExpr = $3;
                    n->partnGroupExpr = $6;
                    n->activePartitionCount = VINT_NULL;
                    n->reorganize = $7;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <name> PARTITION BY <b_expr> SET ACTIVEPARTITIONCOUNT <active_partition_count> [REORGANIZE] */
            | PARTITION BY b_expr SET ACTIVEPARTITIONCOUNT active_partition_count opt_reorganize
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_PartitionBy;
                    n->name = NULL;
                    n->partitionExpr = $3;
                    n->partnGroupExpr = NULL;
                    n->activePartitionCount = $6;
                    n->reorganize = $7;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <name> PARTITION BY <b_expr> [REORGANIZE] */
            | PARTITION BY b_expr opt_reorganize
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_PartitionBy;
                    n->name = NULL;
                    n->partitionExpr = $3;
                    n->partnGroupExpr = NULL;
                    n->activePartitionCount = VINT_NULL;
                    n->reorganize = $4;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <name> REORGANIZE */
            | REORGANIZE
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_PartitionBy;
                    n->name = NULL;
                    n->partitionExpr = NULL;
                    n->partnGroupExpr = NULL;
                    n->activePartitionCount = VINT_NULL;
                    n->reorganize = TRUE;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <name> REMOVE PARTITIONING */
            | REMOVE PARTITIONING
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_PartitionBy;
                    n->name = NULL;
                    n->partitionExpr = NULL;
                    n->partnGroupExpr = NULL;
                    n->activePartitionCount = VINT_NULL;
                    n->reorganize = FALSE;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <name> INCLUDE SCHEMA PRIVILEGES */
            | INCLUDE OptSchemaKeyword PRIVILEGES
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_InheritPrivileges;
                    n->inheritPrivileges = true;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <name> EXCLUDE SCHEMA PRIVILEGES */
            | EXCLUDE OptSchemaKeyword PRIVILEGES
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_InheritPrivileges;
                    n->inheritPrivileges = false;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <name> MATERIALIZE [SCHEMA] PRIVILEGES */
            | MATERIALIZE OptSchemaKeyword PRIVILEGES
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_MaterializePrivileges;
                    $$ = (Node *)n;
                }
            /* ALTER TABLE <name> OUTER ONLY [<level>] */
            | FORCE OUTER_P force_outer_lvl
            	{
            		AlterTableCmd *n = makeNode(AlterTableCmd);
            		n->subtype = AT_ForceOuterToggle;
            		n->name = NULL;
            		n->forceOuter = $3;
            		$$ = (Node *)n;
            	}
            | alter_rel_cmd
                {
                    $$ = $1;
                }
        ;
        
opt_proj_list:
            PROJECTIONS '(' qualified_name_list ')'  { $$ = $3; }
            | /* EMPTY */ { $$ = NIL; }
        ;

alter_rel_cmds:
            alter_rel_cmd                            { $$ = list_make1($1); }
            | alter_rel_cmds ',' alter_rel_cmd        { $$ = lappend($1, $3); }
        ;

/* Subcommands that are for ALTER TABLE or ALTER INDEX */
alter_rel_cmd:
            /* ALTER [TABLE|INDEX] <name> OWNER TO UserId */
            OWNER TO UserId
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_ChangeOwner;
                    n->name = $3.str;
                    $$ = (Node *)n;
                }
            /* ALTER [TABLE|INDEX] <name> SET TABLESPACE <tablespacename> */
            | SET TABLESPACE name
                {
                    AlterTableCmd *n = makeNode(AlterTableCmd);
                    n->subtype = AT_SetTableSpace;
                    n->name = $3.str;
                    $$ = (Node *)n;
                }
        ;

alter_column_default:
            SET DEFAULT a_expr
                {
                    /* Treat SET DEFAULT NULL the same as DROP DEFAULT */
                    if (exprIsNullConstant($3))
                        $$ = NULL;
                    else
                        $$ = $3;
                }
            | DROP DEFAULT                { $$ = NULL; }
        ;

alter_column_setusing:
        SET USING b_expr
        {
            $$ = $3;
        }
        | DROP SET USING
        {
            $$ = NULL;
        }
;

alter_column_defaultusing:
        SET DEFAULT USING b_expr
        {
            $$ = $4;
        }
        | DROP DEFAULT USING
        {
            $$ = NULL;
        }
;

opt_drop_behavior:
            CASCADE                        { $$ = DROP_CASCADE; }
            | RESTRICT                    { $$ = DROP_RESTRICT; }
            | /* EMPTY */                { $$ = DROP_RESTRICT; /* default */ }
        ;

set_constr_status:
            ENABLED                          { $$ = CONSTR_STAT_ENABLED; }
            |    DISABLED                    { $$ = CONSTR_STAT_DISABLED; }
        ;
        
force_outer_lvl:
			ICONST						{ $$=$1; }
			| /* EMPTY */				{ $$=FORCE_OUTER_NONE; }
		;
		
opt_setschema_behavior:
            RESTRICT                     { $$ = DROP_RESTRICT; }
            | CASCADE                    { $$ = DROP_CASCADE; }
            | /* EMPTY */                { $$ = DROP_CASCADE; /* default */ }
        ;

opt_reorganize:
            REORGANIZE                  { $$=TRUE; }
            | /* EMPTY */               { $$=FALSE; }
        ;

active_partition_count:
        Iconst                                { $$ = $1; }
        | DEFAULT                             { $$ = VINT_NULL; }
        ;

/*****************************************************************************
 *
 *        QUERY :
 *                close <portalname>
 *
 *****************************************************************************/

ClosePortalStmt:
            CLOSE name
                {
                    ClosePortalStmt *n = makeNode(ClosePortalStmt);
                    n->portalname = $2.str;
                    $$ = (Node *)n;
                }
        ;


/*****************************************************************************
 *
 *        QUERY :
 *                COPY <relname> ['(' columnList ')'] FROM/TO [WITH options]
 *
 *                BINARY, OIDS, and DELIMITERS kept in old locations
 *                for backward compatibility.  2002-06-18
 *
 *****************************************************************************/

CopyStmt:   COPY opt_binary qualified_name opt_copy_column_list opt_columns_count
            opt_parse_option_list opt_copy_from_clause opt_copy_file_format
            copy_delimiter opt_with copy_opt_udls copy_opt_list copy_opt_commit
                {
                    CopyStmt *n = makeNode(CopyStmt);
                    n->relation = $3;
                    n->attlist  = $4;
                    n->columns_count = $5;
                    n->parseOptions = $6;

                    CopyStmt *tmpSourceData = (CopyStmt*)$7;
                    if (tmpSourceData) {
                        n->is_from = tmpSourceData->is_from;
                        n->sources = tmpSourceData->sources;
                    } else {
                        n->is_from = TRUE;
                        n->sources = NULL;
                    }

                    n->options = NIL;
                    if (lsecond($8) != NIL)
                        n->options = list_concat(n->options, lsecond($8));
                    /* Concatenate user-supplied flags */
                    if ($2)
                        n->options = lappend(n->options, $2);
                    if ($9)
                        n->options = lappend(n->options, $9);
                    n->userdefined_copy = (CopyUDL*)$11;
                    if ($12)
                        n->options = list_concat(n->options, $12);
                    n->commit = $13;

                    if (n->userdefined_copy->parser) {
                        n->format = "user defined";
                    } else {
                        n->format   = strVal(linitial($8));
                    }
                    confirmHiveFormatLimits(n);

                    // TODO Future: Support source-less COPY statements with
                    // special UDParsers that don't require an independent source
                    if (n->sources == NULL && n->userdefined_copy->source == NULL) {
                        ereport(ERROR, (errmsg("COPY requires a data source; either a FROM clause or a WITH SOURCE for a user-defined source"),
                            errcode(ERRCODE_SYNTAX_ERROR)));
                    }

                    $$ = (Node *)n;
                }
        ;

ExternalTableCopyStmt:   COPY opt_copy_column_list opt_columns_count
                         opt_parse_option_list opt_copy_from_clause opt_copy_file_format
                         copy_delimiter opt_with copy_opt_udls copy_opt_list copy_opt_commit
                         {
                             CopyStmt *n = makeNode(CopyStmt);
                             n->stmt.offset = yyloc;  // External tables: remember where the COPY was
                             n->attlist  = $2;
                             n->columns_count = $3;
                             n->parseOptions = $4;

                             CopyStmt *tmpSourceData = (CopyStmt*)$5;
                             if (tmpSourceData) {
                                 n->is_from = tmpSourceData->is_from;
                                 n->sources = tmpSourceData->sources;
                             } else {
                                 n->is_from = TRUE;
                                 n->sources = NULL;
                             }

                             n->options = NIL;
                             if (lsecond($6) != NIL)
                                 n->options = list_concat(n->options, lsecond($6));
                             /* Concatenate user-supplied flags */
                             if ($7)
                                 n->options = lappend(n->options, $7);
                             n->userdefined_copy = (CopyUDL*)$9;
                             if ($10)
                                 n->options = list_concat(n->options, $10);
                             n->commit = $11;

                             if (n->userdefined_copy->parser) {
                                 n->format = "user defined";
                             } else {
                                 n->format   = strVal(linitial($6));
                             }
                             confirmHiveFormatLimits(n);
 
                             // TODO Future: Support source-less COPY statements with
                             // special UDParsers that don't require an independent source
                             if (n->sources == NULL && n->userdefined_copy->source == NULL) {
                                 ereport(ERROR, (errmsg("COPY requires a data source; either a FROM clause or a WITH SOURCE for a user-defined source"),
                                                 errcode(ERRCODE_SYNTAX_ERROR)));
                             }

                             $$ = (Node *)n;
                         }
        ;


opt_copy_from_clause:
            copy_from copy_source {
                // Create a temporary CopyStmt
                CopyStmt *n = makeNode(CopyStmt);
                n->is_from = $1;
                n->sources = (VCopySource*) $2;
                $$ = (Node*)n;
            }
            | /* EMPTY */ { $$ = NULL; }
			;

copy_opt_udls:
            copy_opt_source copy_opt_filter_list copy_opt_parser {
                CopyUDL *u = makeNode(CopyUDL);
                u->source = (Node*)$1;
                u->filter = (List*)$2;
                u->parser = (Node*)$3;
                $$ = (Node *)u;
            };

copy_opt_source:
            SOURCE load_function {
                $$ = $2;
            }
            | /* EMPTY */           { $$ = NULL; }
            ;

copy_opt_filter_list:
            copy_filter_list      { $$ = $1; }
            | /* EMPTY */           { $$ = NULL; }
            ;

copy_filter_list:
            copy_filter                       { $$ = list_make1($1); }
            | copy_filter_list copy_filter  { $$ = lappend($1, $2); }
            ;

copy_filter:
            FILTER load_function {
                $$ = $2;
            }
            | UNPACKER load_function {
                $$ = $2;
            }
            ;

copy_opt_parser:
            PARSER load_function {
                $$ = $2;
            }
            | /* EMPTY */           { $$ = NULL; }
            ;

copy_from:
            FROM                                    { $$ = TRUE; }
            | TO                                    { $$ = FALSE; }
        ;
/*
 * copy_file_name NULL indicates stdio is used. Whether stdin or stdout is
 * used depends on the direction. (It really doesn't make sense to copy from
 * stdout. We silently correct the "typo".         - AY 9/94
 */


copy_source:
            copy_file_list
             {
                VCopySource* s = makeNode(VCopySource);
                s->sources = $1;
                s->loadType = BULKLOAD_FILE;
                $$ = (Node*) s;
             }
           | LOCAL copy_file_list
             {
                VCopySource* s = makeNode(VCopySource);
                s->sources = $2;
                s->loadType = BULKLOAD_LOCAL;
                $$ = (Node*) s;
             }
           | LOCAL STDIN opt_copy_compr_type
             {
                VCopySource* s = makeNode(VCopySource);
                s->loadType = BULKLOAD_LOCAL;
                VCopySource* sin = makeNode(VCopySource);
                sin->filename = NULL;
                sin->compression = $3.str;
                sin->nodes = NIL;
                sin->loadType = BULKLOAD_STDIN;
                s->sources = list_make1((Node*)sin);
                $$ = (Node*) s;
             }
           | STDIN opt_copy_compr_type
             {
                VCopySource* s = makeNode(VCopySource);
                s->filename = NULL;
                s->compression = $2.str;
                s->nodes = NIL;
                s->loadType = BULKLOAD_STDIN;
                $$ = (Node*) s;
             }
           | EXPORT Sconst
             {
                 VCopySource* s = makeNode(VCopySource);
                 s->filename = $2.str;
                 s->loadType = BULKLOAD_EXPORT;
                 $$ = (Node*) s;
             }
           | VERTICA export_relation opt_export_column_list
             {
                 VCopySource* s = makeNode(VCopySource);
                 s->relation = $2;
                 s->columns  = $3;
                 s->loadType = BULKLOAD_IMPORT;
                 $$ = (Node*) s;
             }
        ;

copy_file_list:
            copy_file_type                         { $$ = list_make1($1); }
            | copy_file_list ',' copy_file_type    { $$ = lappend($1, $3);}
        ;

copy_file_type:
            copy_file opt_copy_compr_type
            {
                    VCopySource* s = makeNode(VCopySource);
                    s->filename = strVal(linitial($1));

                    List *target = (List *)lsecond($1);
                    if (target == NULL) {
                        /* default to initiator */
                        s->nodes = NIL;
                        s->autoAssignNode = false;
                    } else if (target == NODE__ON_ANY) {
                        s->nodes = NIL;
                        s->autoAssignNode = true;
                    } else {
                        s->nodes = target;
                        s->autoAssignNode = false;
                    }

                    s->compression = $2.str;
                    s->loadType = BULKLOAD_FILE;
                    $$ = (Node*) s;
            }
        ;
opt_copy_file_format:
              NATIVE                                  { $$ = list_make2((Node*)makeStr(ctString("native")), NIL);}
            | NATIVE VARCHAR                          { $$ = list_make2((Node*)makeStr(ctString("native varchar")), NIL);}
            | FIXEDWIDTH COLSIZES '(' widthsList ')'
              {
                  $$ = list_make2((Node*)makeStr(ctString("fixed width")),
                          (Node*)list_make1(makeDefElem("columnwidths", (Node*)$4)));}
            | PARQUET                                 { $$ = list_make2((Node*)makeStr(ctString("parquet")), NIL);}
            | PARQUET '(' parquet_opt_list ')' 
              { 
                  $$ = list_make2((Node*)makeStr(ctString("parquet")), (Node*)list_make1(makeDefElem("hive_args", (Node*)$3)));
              }
            | ORC                                     { $$ = list_make2((Node*)makeStr(ctString("orc")), NIL);}
            | ORC '(' orc_opt_list ')' 
              { 
                  $$ = list_make2((Node*)makeStr(ctString("orc")), (Node*)list_make1(makeDefElem("hive_args", (Node*)$3)));
              }        
            |                                         { $$ = list_make2((Node*)makeStr(ctString("delimited")), NIL);}
        ;

parquet_opt_list:
            parquetOptElem                              { $$ = list_make1($1); }
            | parquet_opt_list ',' parquetOptElem       { $$ = lappend($1, $3); }
      ;

parquetOptElem:
             hive_arg_name '=' Sconst
                { 
                    $$ = (Node *)(list_make2(makeStr($1), makeStr($3))); 
                }
       ;

orc_opt_list:
            orcOptElem                              { $$ = list_make1($1); }
            | orc_opt_list ',' orcOptElem           { $$ = lappend($1, $3); }
      ;

orcOptElem:
             hive_arg_name '=' Sconst
                { 
                    $$ = (Node *)(list_make2(makeStr($1), makeStr($3))); 
                }
       ;

opt_copy_compr_type:
            GZIP                                    {$$=ctString("GZIP");}
            | BZIP                                  {$$=ctString("BZIP");}
            | ZSTD                                  {$$=ctString("ZSTD");}
            | LZO                                   {$$=ctString("LZO");}
            | UNCOMPRESSED                          {$$=ctString("UNCOMPRESSED");}
            |                                       {$$=ctString("UNCOMPRESSED");}
        ;
        
OptCopy:
            copy_storage_mode
                {
                    $$ = $1;
                }
            | /*EMPTY*/
                {
                    $$ = AT_AddOptionEmpty;
                }
		;

copy_storage_mode:
            DIRECT
                {
                    $$ = AT_AddOptionDirect;
                }
            | TRICKLE
                {
                    $$ = AT_AddOptionTrickle;
                }
            | AUTO
                {
                    $$ = AT_AddOptionAuto;
                }
            | DEFAULT
                {
                    $$ = AT_AddOptionAuto;
                }
            ;
            
copy_storage_target:
            DIRECT
                {
                    $$ = $1;
                }
            | DIRECTCOLS
                {
                    $$ = $1;
                }
            | DIRECTGROUPED
                {
                    $$ = $1;
                }
            | DIRECTPROJ
                {
                    $$ = $1;
                }
            | TRICKLE
                {
                    $$ = $1;
                }
            | AUTO
                {
                    $$ = $1;
                }
            ;

copy_opt_list:
            copy_opt_list copy_opt_item             { $$ = lappend($1, $2); }
            | /* EMPTY */                           { $$ = NIL; }
;

copy_rej_clause:
            copy_error_list
                {
                    $$ = makeDefElem("rejected_data", (Node *)($1));
                }
            | TABLE qualified_name
                {
                    $$ = makeDefElem("rejected_table", (Node *)($2));
                }
        ;
/* If you add a copy item consider whether or not it should be a UDL option (see parseUDLOptions) */
copy_opt_item:
            ABORT_P ON ERROR_P
                {
                    $$ = makeDefElem("abort_on_error", (Node *)makeInteger(TRUE));
                }
            | BINARY
                {
                    ereport(ERROR, (errmsg("COPY FROM does not support the BINARY option"),
                            errcode(ERRCODE_FEATURE_NOT_SUPPORTED)));
                    $$ = makeDefElem("binary", (Node *)makeInteger(TRUE));
                }
            | CSV
                {
                    ereport(ERROR, (errmsg("COPY FROM does not support the CSV option"),
                            errcode(ERRCODE_FEATURE_NOT_SUPPORTED)));
                    $$ = makeDefElem("csv", (Node *)makeInteger(TRUE));
                }
            | DELIMITER opt_as Sconst
                {
                    $$ = makeDefElem("delimiter", (Node *)makeStr($3));
                }
            | ENCLOSED opt_by Sconst
                {
                    $$ = makeDefElem("enclosed_by", (Node *)makeStr($3));
                }
            | ENFORCELENGTH
                {
                    $$ = makeDefElem("enforcelength", (Node *)makeInteger(TRUE));
                }
            | ERROR_P TOLERANCE
                {
                    $$ = makeDefElem("error_tolerance", (Node*)makeInteger(TRUE));
                }
            | ESCAPE opt_as Sconst
                {
                    $$ = makeDefElem("escape", (Node *)makeStr($3));
                }
            | NO ESCAPE
                {
                    $$ = makeDefElem("no_escape", (Node *)makeInteger(TRUE));
                }
            | EXCEPTIONS opt_as copy_error_list
                {
                    $$ = makeDefElem("exceptions", (Node *)($3));
                }
            | FORCE NOT NULL_P columnList
                {
                    ereport(ERROR, (errmsg("COPY force not null is available only in CSV mode, but CSV mode is not supported"),
                        errcode(ERRCODE_FEATURE_NOT_SUPPORTED)));
                    $$ = makeDefElem("force_notnull", (Node *)$4);
                }
            | FORCE QUOTE columnList
                {
                    ereport(ERROR, (errmsg("COPY force quote is available only in CSV mode, but CSV mode is not supported"),
                        errcode(ERRCODE_FEATURE_NOT_SUPPORTED)));
                    $$ = makeDefElem("force_quote", (Node *)$3);
                }
            | MANAGED
                {
                    $$ = makeDefElem("managed", (Node *)makeInteger(TRUE));
                }
            | NULL_P opt_as Sconst
                {
                    $$ = makeDefElem("null", (Node *)makeStr($3));
                }
            | OIDS
                {
                    ereport(ERROR, (errmsg("COPY FROM does not support the OIDS option"),
                        errcode(ERRCODE_FEATURE_NOT_SUPPORTED)));
                    $$ = makeDefElem("oids", (Node *)makeInteger(TRUE));
                }
            | QUOTE opt_as Sconst
                {
                    ereport(ERROR, (errmsg("COPY quote is available only in CSV mode, but CSV mode is not supported"),
                        errcode(ERRCODE_FEATURE_NOT_SUPPORTED)));
                    $$ = makeDefElem("quote", (Node *)makeStr($3));
                }
            | RECORD_P TERMINATOR_P opt_as Sconst
                {
                    $$ = makeDefElem("record_terminator", (Node *)makeStr($4));
                }
            | REJECTED_P DATA_P opt_as copy_rej_clause
                {
                    $$ = $4;
                }
            | REJECTMAX IntegerOnly
                {
                    $$ = makeDefElem("rejectmax", (Node*)$2);
                }
            | RETURNREJECTED
                {
                    $$ = makeDefElem("rejectrows", (Node*)makeInteger(TRUE));
                }
            | SKIP IntegerOnly
                {
                    $$ = makeDefElem("skip", (Node*)$2);
                }
            | SKIP BYTES IntegerOnly
                {
                    $$ = makeDefElem("skip_bytes", (Node*)$3);
                }
            | STORAGE copy_storage_target
                {
                    $$ = makeDefElem("storage", (Node *)makeStr(ctString(pstrdup($2))));
                }
            | STREAM_P NAME_P opt_as Sconst
                {
                    $$ = makeDefElem("stream_name", (Node *)makeStr($4));
                }
            | TRAILING NULLCOLS
                {
                    $$ = makeDefElem("trailing_nullcols", (Node*)makeInteger(TRUE));
                }
            | TRIM Sconst
                {
                    $$ = makeDefElem("trim", (Node *)makeStr($2));
                }
            | copy_storage_target
                {
                    $$ = makeDefElem("storage", (Node *)makeStr(ctString(pstrdup($1))));
                }
        ;

copy_opt_commit:
            COMMIT                    {$$=TRUE;}
            | NO COMMIT               {$$=FALSE;}
            | /* EMPTY */             {$$=TRUE;}
        ;

/* The following exist for backward compatibility */

opt_binary:
            BINARY
                {
                    ereport(ERROR, (errmsg("COPY FROM does not support the BINARY option"),
                            errcode(ERRCODE_FEATURE_NOT_SUPPORTED)));
                    $$ = makeDefElem("binary", (Node *)makeInteger(TRUE));
                }
            | /*EMPTY*/                                { $$ = NULL; }
        ;

copy_delimiter:
            /* USING DELIMITERS kept for backward compatibility. 2002-06-15 */
            opt_using DELIMITERS Sconst
                {
                    $$ = makeDefElem("delimiter", (Node *)makeStr($3));
                }
            | /*EMPTY*/                                { $$ = NULL; }
        ;

opt_using:
            USING                                    {}
            | /*EMPTY*/                                {}
        ;


copy_error_list:
            copy_file                                {$$=list_make1($1);}
            | copy_error_list ',' copy_file          {$$=lappend($1, $3);}
        ;

copy_file:
            file_name opt_copy_node
            {
                $$ = list_make2((Node*)makeStr($1),$2);
            }
        ;

opt_copy_node:
            ON copy_node_list
            {
                $$ = $2;
            }
            | ON ANY NODE
            {
                $$ = NODE__ON_ANY; /* presumably this will never be a valid address */
            }
            | /*EMPTY*/ 
            {
                $$ = NULL;
            }
        ;

copy_node_list:
            name
            {
                $$ = list_make1((Node *)makeStr($1));
            }
            | '(' copy_node_list_inner ')'
            {
                $$ = $2;
            }
        ;
copy_node_list_inner:
            name
            {
                $$ = list_make1((Node *)makeStr($1));
            }
            | copy_node_list_inner ',' name
            {
                $$ = lappend($1, (Node *)makeStr($3));
            }
        ;

opt_parse_option_list:
            COLUMN OPTION '(' copyParseList ')'    { $$=$4;}
            | /*EMPTY*/                               { $$ = NIL;}
        ;

copyParseList:
            copyParseElem                                { $$ = list_make1($1); }
            | copyParseList ',' copyParseElem            { $$ = lappend($1, $3); }
        ;

copyParseElem: ColId copyColumnFeatureList  /*Match column with options*/
                {
                    VCopyCol *n = makeNode(VCopyCol);
                    n->attname    = $1.str;
                    n->colRef     = NIL;
                    n->attributes = $2;
                    n->valueExpr  = NIL;
                    n->typeOfCol  = NIL;
                    $$ = (Node *)n;
                }
        ;

widthsList:
            Iconst                        { $$ = list_make1(makeInteger($1));  }
            | widthsList ',' Iconst        { $$ = lappend($1, makeInteger($3)); }
        ;

opt_copy_column_list:
            '(' copyColumnList ')'                        { $$ = $2; }
            | /*EMPTY*/                                { $$ = NIL; }
        ;

copyColumnList:
            copyColumnElem                                { $$ = list_make1($1); }
            | copyColumnList ',' copyColumnElem                { $$ = lappend($1, $3); }
        ;

copyColumnElem: columnref                          /*Match a column name*/
                {
                    VCopyCol *n = makeNode(VCopyCol);
                    n->attname    = NIL;
                    n->colRef     = $1;
                    n->valueExpr  = NIL;
                    n->attributes = NIL;
                    n->kwargs     = NIL;
                    n->typeOfCol  = NIL;
                    $$ = (Node *)n;
                }
                | columnref copyColumnFeatureList  /*Match column with options*/
                {
                    VCopyCol *n = makeNode(VCopyCol);
                    n->attname    = NIL;
                    n->colRef     = $1;
                    n->attributes = $2;
                    n->valueExpr  = NIL;
                    n->kwargs     = NIL;
                    n->typeOfCol  = NIL;
                    $$ = (Node *)n;
                }
                | columnref AS a_expr             /*Match column with expression*/
                {
                    VCopyCol *n = makeNode(VCopyCol);
                    n->attname    = NIL;
                    n->colRef     = $1;
                    n->valueExpr  = $3;
                    n->attributes = NIL;
                    n->kwargs     = NIL;
                    n->typeOfCol  = NIL;
                    $$ = (Node *)n;
                }
                | columnref FILLER TypenameWithTypmod       /*Filler column no options*/
                {
                    VCopyCol *n = makeNode(VCopyCol);
                    n->attname    = NIL;
                    n->colRef     = $1;
                    n->attributes = NIL;
                    n->valueExpr  = NIL;
                    n->kwargs     = NIL;
                    n->typeOfCol  = $3;
                    $$ = (Node *)n;
                }
                | columnref FILLER TypenameWithTypmod copyColumnFeatureList  /*FILLER column with options*/
                {
                    VCopyCol *n = makeNode(VCopyCol);
                    n->attname    = NIL;
                    n->colRef     = $1;
                    n->attributes = $4;
                    n->valueExpr  = NIL;
                    n->kwargs     = NIL;
                    n->typeOfCol  = $3;
                    $$ = (Node *)n;
                }
                | columnref '(' paramarg_list ')' {
                    VCopyCol *n = makeNode(VCopyCol);
                    n->attname    = NIL;
                    n->colRef     = $1;
                    n->attributes = NIL;
                    n->valueExpr  = NIL;
                    n->kwargs     = $3;
                    n->typeOfCol  = NIL;
                    $$ = (Node *)n;
                }
        ;

copyColumnFeatureList: copyColumnFeature                     { $$ = list_make1($1); }
            | copyColumnFeatureList copyColumnFeature         { $$ = lappend($1, $2); }
        ;

copyColumnFeature: FORMAT Sconst
                    {
                        $$ = makeDefElem("format", (Node *)makeStr($2));
                    }
                | DELIMITER opt_as Sconst
                    {
                        $$ = makeDefElem("delimiter", (Node *)makeStr($3));
                    }
                | NULL_P opt_as Sconst
                    {
                        $$ = makeDefElem("null", (Node *)makeStr($3));
                    }
                | ENCLOSED opt_by Sconst
                    {
                        $$ = makeDefElem("enclosed_by", (Node *)makeStr($3));
                    }
                | ENFORCELENGTH
                    {
                        $$ = makeDefElem("enforcelength", (Node *)makeInteger(TRUE));
                    }
                | ESCAPE opt_as Sconst
                    {
                        $$ = makeDefElem("escape", (Node *)makeStr($3));
                    }
                | NO ESCAPE
                    {
                        $$ = makeDefElem("no_escape", (Node *)makeInteger(TRUE));
                    }
                | TRIM Sconst
                    {
                        $$ = makeDefElem("trim", (Node *)makeStr($2));
                    }
        ;

opt_columns_count: COLUMNS_COUNT IntegerOnly
                {
                    $$ = (Node *)$2;
                }
                | /*EMPTY*/                        {$$=NIL;}
        ;

/*****************************************************************************
 *
 *        QUERY :
 *                CREATE TABLE relname
 *
 *****************************************************************************/

CreateStmt:    CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')'
            OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges
                {
                    CreateStmt *n = makeNode(CreateStmt);
                    n->exists_ok = TRUE;
                    $7->temptype = $2;
                    n->relation = $7;
                    n->tableElts = $9;
                    n->inhRelations = $11;
                    n->constraints = NIL;
                    n->hasoids = $12;
                    n->oncommit = $13;
                    n->tablespacename = $14.str;
                    n->copyMode = $15;
                     n->projStmt = $16;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->partitionExpr = $17.partnExpr;
                    n->partnGroupExpr = $17.groupExpr;
                    n->activePartitionCount = $17.activePartitionCount;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = $18;
                    $$ = (Node *)n;
                }
        |     CREATE OptTemp TABLE qualified_name '(' OptTableElementList ')'
            OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges
                {
                    CreateStmt *n = makeNode(CreateStmt);
                    n->exists_ok = FALSE;
                    $4->temptype = $2;
                    n->relation = $4;
                    n->tableElts = $6;
                    n->inhRelations = $8;
                    n->constraints = NIL;
                    n->hasoids = $9;
                    n->oncommit = $10;
                    n->tablespacename = $11.str;
                    n->copyMode = $12;
                    n->projStmt = $13;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->partitionExpr = $14.partnExpr;
                    n->partnGroupExpr = $14.groupExpr;
                    n->activePartitionCount = $14.activePartitionCount;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = $15;
                    $$ = (Node *)n;
                }
        |     CREATE FLEX OptTemp TABLE qualified_name '(' OptTableElementList ')'
            OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges
                {
                    CreateStmt *n = makeNode(CreateStmt);
                    n->exists_ok = FALSE;
                    $5->temptype = $3;
                    n->relation = $5;
                    n->tableElts = $7;
                    n->inhRelations = $9;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = $11;
                    n->tablespacename = $12.str;
                    n->copyMode = $13;
                    n->projStmt = $14;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->partitionExpr = $15.partnExpr;
                    n->partnGroupExpr = $15.groupExpr;
                    n->activePartitionCount = $15.activePartitionCount;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->inheritPrivileges = $16;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    $$ = (Node *)n;
                }
        |     CREATE FLEXIBLE OptTemp TABLE qualified_name '(' OptTableElementList ')'
            OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges
                {
                    CreateStmt *n = makeNode(CreateStmt);
                    n->exists_ok = FALSE;
                    $5->temptype = $3;
                    n->relation = $5;
                    n->tableElts = $7;
                    n->inhRelations = $9;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = $11;
                    n->tablespacename = $12.str;
                    n->copyMode = $13;
                    n->projStmt = $14;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->partitionExpr = $15.partnExpr;
                    n->partnGroupExpr = $15.groupExpr;
                    n->activePartitionCount = $15.activePartitionCount;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->inheritPrivileges = $16;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    $$ = (Node *)n;
                }
        |     CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')'
            OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges
                {
                    CreateStmt *n = makeNode(CreateStmt);
                    n->exists_ok = TRUE;
                    $8->temptype = $3;
                    n->relation = $8;
                    n->tableElts = $10;
                    n->inhRelations = $12;
                    n->constraints = NIL;
                    n->hasoids = $13;
                    n->oncommit = $14;
                    n->tablespacename = $15.str;
                    n->copyMode = $16;
                    n->projStmt = $17;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->partitionExpr = $18.partnExpr;
                    n->partnGroupExpr = $18.groupExpr;
                    n->activePartitionCount = $18.activePartitionCount;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->inheritPrivileges = $19;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    $$ = (Node *)n;
                }
        |     CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')'
            OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges
                {
                    CreateStmt *n = makeNode(CreateStmt);
                    n->exists_ok = TRUE;
                    $8->temptype = $3;
                    n->relation = $8;
                    n->tableElts = $10;
                    n->inhRelations = $12;
                    n->constraints = NIL;
                    n->hasoids = $13;
                    n->oncommit = $14;
                    n->tablespacename = $15.str;
                    n->copyMode = $16;
                    n->projStmt = $17;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->partitionExpr = $18.partnExpr;
                    n->partnGroupExpr = $18.groupExpr;
                    n->activePartitionCount = $18.activePartitionCount;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->inheritPrivileges = $19;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    $$ = (Node *)n;
                }
        | CREATE OptTemp TABLE qualified_name OF qualified_name
            '(' OptTableElementList ')' OptWithOids OnCommitOption OptTableSpace OptCopy AutoProjectionDef VPartition OptInheritPrivileges
                {
                    /* SQL99 CREATE TABLE OF <UDT> (cols) seems to be satisfied
                     * by our inheritance capabilities. Let's try it...
                     */
                    CreateStmt *n = makeNode(CreateStmt);
                    n->exists_ok = FALSE;
                    $4->temptype = $2;
                    n->relation = $4;
                    n->tableElts = $8;
                    n->inhRelations = list_make1($6);
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = $11;
                    n->tablespacename = $12.str;
                    n->copyMode = $13;
                    n->projStmt = $14;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->partitionExpr = $15.partnExpr;
                    n->partnGroupExpr = $15.groupExpr;
                    n->activePartitionCount = $15.activePartitionCount;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = $16;
                    $$ = (Node *)n;
                }
                | CREATE OptTemp TABLE qualified_name TableLikeClause OptCopy OptInheritPrivileges
                {
                    CreateStmt *n = makeNode(CreateStmt);
                    n->exists_ok = FALSE;
                    $4->temptype = $2; // only NO_TEMP is supported, but parser complaints if OptTemp is removed...
                    n->relation = $4;
                    n->replicate_from = $5;
                    n->selectStmt = NULL;
                    n->projStmt = NULL;
                    n->copyMode = $6;
                    n->inheritPrivileges = $7;
                    n->skip_permissions = false;
                    // others not important as we don't use them
                    $$ = (Node *)n;
                }
                | CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name TableLikeClause OptCopy OptInheritPrivileges
                {
                    CreateStmt *n = makeNode(CreateStmt);
                    n->exists_ok = TRUE;
                    $7->temptype = $2; // only NO_TEMP is supported, but parser complaints if OptTemp is removed...
                    n->relation = $7;
                    n->replicate_from = $8;
                    n->selectStmt = NULL;
                    n->projStmt = NULL;
                    n->copyMode = $9;
                    n->inheritPrivileges = $10;
                    n->skip_permissions = false;
                    // others not important as we don't use them
                    $$ = (Node *)n;
                }
        ;

VPartition:
            PARTITION BY b_expr GROUP_P BY b_expr ACTIVEPARTITIONCOUNT active_partition_count
            {
                $$.partnExpr = $3;
                $$.groupExpr = $6;
                $$.activePartitionCount = $8;
            }
          | PARTITION BY b_expr GROUP_P BY b_expr
            {
                $$.partnExpr = $3;
                $$.groupExpr = $6;
                $$.activePartitionCount = VINT_NULL;
            }
          | PARTITION BY b_expr ACTIVEPARTITIONCOUNT active_partition_count
            {
                $$.partnExpr = $3;
                $$.groupExpr = NIL;
                $$.activePartitionCount = $5;
            }
          | PARTITION BY b_expr
            {
                $$.partnExpr = $3;
                $$.groupExpr = NIL;
                $$.activePartitionCount = VINT_NULL;
            }
          | /*EMPTY*/
            {
                $$.partnExpr = NIL;
                $$.groupExpr = NIL;
                $$.activePartitionCount = VINT_NULL;
            }

        ;

OptInheritPrivileges:
            INCLUDE SCHEMA PRIVILEGES { $$ = INHERIT_PRIVILEGES; }
            | INCLUDE PRIVILEGES { $$ = INHERIT_PRIVILEGES; }
            | EXCLUDE SCHEMA PRIVILEGES { $$ = NOT_INHERIT_PRIVILEGES; }
            | EXCLUDE PRIVILEGES { $$ = NOT_INHERIT_PRIVILEGES; }
            | /* EMPTY */ { $$ = DEFAULT_INHERIT_PRIVILEGES; }
        ;

/*
 * Redundancy here is needed to avoid shift/reduce conflicts,
 * since TEMP is not a reserved word.  See also OptTempTableName.
 */
OptTemp:    TEMPORARY                        { $$ = DEFAULT_TEMP; }
            | TEMP                            { $$ = DEFAULT_TEMP; }
            | LOCAL TEMPORARY                { $$ = LOCAL_TEMP; }
            | LOCAL TEMP                    { $$ = LOCAL_TEMP; }
            | GLOBAL TEMPORARY                { $$ = GLOBAL_TEMP; }
            | GLOBAL TEMP                    { $$ = GLOBAL_TEMP; }
            | /*EMPTY*/                        { $$ = NOT_TEMP; }
        ;

OptLocalTempOnly:    LOCAL TEMPORARY                { $$ = LOCAL_TEMP; }
            | LOCAL TEMP                    { $$ = LOCAL_TEMP; }
            | /*EMPTY*/                        { $$ = NOT_TEMP; }
        ;

OptTableElementList:
            TableElementList                    { $$ = $1; }
            | /*EMPTY*/                            { $$ = NIL; }
        ;

TableElementList:
            TableElement
                {
                    $$ = list_make1($1);
                }
            | TableElementList ',' TableElement
                {
                    $$ = lappend($1, $3);
                }
        ;

TableElement:
            columnDef encode_type index_type opt_access_rank
                {
                    ColumnDef *n = (ColumnDef*)$1;
                    VColumnElem *projProp = makeNode(VColumnElem);
                    projProp->colId=n->colname;
                    projProp->encodeType=$2;
                    projProp->accTypes=$3;
                    projProp->group=-1;
                    projProp->accessRank=$4;
                    n->projProp = projProp;
                    $$ = (Node *)n;
                }
            | TableLikeClause                    { $$ = $1; }
            | TableConstraint                    { $$ = $1; }
        ;

columnDef:    ColId TypenameWithTypmod ColQualList
                {
                    ColumnDef *n = makeNode(ColumnDef);
                    n->colname = $1.str;
                    n->typeInfo = $2;
                    n->constraints = $3;
                    n->is_local = true;
                    n->projProp = NULL;
                    $$ = (Node *)n;
                }
              | ColId IDENT '(' Iconst ')' ColQualList
                {
                    ColumnDef *n = makeNode(ColumnDef);
                    n->colname = $1.str;
                    TypeName *t = SystemTypeName($2.str);
                    t->typmod = VARHDRSZ + $4;
                    n->typeInfo = t;
                    n->constraints = $6;
                    n->is_local = true;
                    n->projProp = NULL;
                    $$ = (Node *)n;
                }
        ;

ColQualList:
            ColQualList ColConstraint                { $$ = lappend($1, $2); }
            | /*EMPTY*/                                { $$ = NIL; }
        ;

ColConstraint:
            CONSTRAINT name ColConstraintElem
                {
                    switch (nodeTag($3))
                    {
                        case T_Constraint:
                            {
                                Constraint *n = (Constraint *)$3;
                                n->name = $2.str;
                            }
                            break;
                        case T_FkConstraint:
                            {
                                FkConstraint *n = (FkConstraint *)$3;
                                n->constr_name = $2.str;
                            }
                            break;
                        default:
                            break;
                    }
                    $$ = $3;
                }
            | ColConstraintElem                        { $$ = $1; }
            | ConstraintAttr                        { $$ = $1; }
        ;

/* DEFAULT NULL is already the default for Postgres.
 * But define it here and carry it forward into the system
 * to make it explicit.
 * - thomas 1998-09-13
 *
 * WITH NULL and NULL are not SQL92-standard syntax elements,
 * so leave them out. Use DEFAULT NULL to explicitly indicate
 * that a column may have that value. WITH NULL leads to
 * shift/reduce conflicts with WITH TIME ZONE anyway.
 * - thomas 1999-01-08
 *
 * DEFAULT expression must be b_expr not a_expr to prevent shift/reduce
 * conflict on NOT (since NOT might start a subsequent NOT NULL constraint,
 * or be part of a_expr NOT LIKE or similar constructs).
 */
ColConstraintElem:
            NOT NULL_P
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_NOTNULL;
                    n->name = NULL;
                    n->raw_expr = NULL;
                    n->cooked_expr = NULL;
                    n->keys = NULL;
                    n->indexspace = NULL;
                    n->status = CONSTR_STAT_NULL;
                    $$ = (Node *)n;
                }
            | NULL_P
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_NULL;
                    n->name = NULL;
                    n->raw_expr = NULL;
                    n->cooked_expr = NULL;
                    n->keys = NULL;
                    n->indexspace = NULL;
                    n->status = CONSTR_STAT_NULL;
                    $$ = (Node *)n;
                }
            | UNIQUE OptConsTableSpace OptConsStatus
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_UNIQUE;
                    n->name = NULL;
                    n->raw_expr = NULL;
                    n->cooked_expr = NULL;
                    n->keys = NULL;
                    n->indexspace = $2.str;
                    n->status = $3;
                    $$ = (Node *)n;
                }
            | PRIMARY KEY OptConsTableSpace OptConsStatus
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_PRIMARY;
                    n->name = NULL;
                    n->raw_expr = NULL;
                    n->cooked_expr = NULL;
                    n->keys = NULL;
                    n->indexspace = $3.str;
                    n->status = $4;
                    $$ = (Node *)n;
                }
            | CHECK '(' a_expr ')' OptConsStatus
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_CHECK;
                    n->name = NULL;
                    n->raw_expr = $3;
                    n->cooked_expr = NULL;
                    n->keys = NULL;
                    n->indexspace = NULL;
                    n->status = $5;
                    $$ = (Node *)n;
                }
            | DEFAULT b_expr
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_DEFAULT;
                    n->name = NULL;
                    n->raw_expr = $2;
                    n->cooked_expr = NULL;
                    n->keys = NULL;
                    n->indexspace = NULL;
                    n->status = CONSTR_STAT_NULL;
                    $$ = (Node *)n;
                }
            | SET USING b_expr
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_SETUSING;
                    n->name = NULL;
                    n->raw_expr = $3;
                    n->cooked_expr = NULL;
                    n->keys = NULL;
                    n->indexspace = NULL;
                    n->status = CONSTR_STAT_NULL;
                    $$ = (Node *)n;
                }
            | DEFAULT USING b_expr
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_DEFUSING;
                    n->name = NULL;
                    n->raw_expr = $3;
                    n->cooked_expr = NULL;
                    n->keys = NULL;
                    n->indexspace = NULL;
                    n->status = CONSTR_STAT_NULL;
                    $$ = (Node *)n;
                }
            | REFERENCES qualified_name opt_column_list key_match key_actions
                {
                    FkConstraint *n = makeNode(FkConstraint);
                    n->constr_name        = NULL;
                    n->pktable            = $2;
                    n->fk_attrs            = NIL;
                    n->pk_attrs            = $3;
                    n->fk_matchtype        = $4;
                    n->fk_upd_action    = (char) ($5 >> 8);
                    n->fk_del_action    = (char) ($5 & 0xFF);
                    n->deferrable        = FALSE;
                    n->initdeferred        = FALSE;
                    $$ = (Node *)n;
                }
        ;

/*
 * ConstraintAttr represents constraint attributes, which we parse as if
 * they were independent constraint clauses, in order to avoid shift/reduce
 * conflicts (since NOT might start either an independent NOT NULL clause
 * or an attribute).  analyze.c is responsible for attaching the attribute
 * information to the preceding "real" constraint node, and for complaining
 * if attribute clauses appear in the wrong place or wrong combinations.
 *
 * See also ConstraintAttributeSpec, which can be used in places where
 * there is no parsing conflict.
 */
ConstraintAttr:
            DEFERRABLE
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_ATTR_DEFERRABLE;
                    $$ = (Node *)n;
                }
            | NOT DEFERRABLE
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_ATTR_NOT_DEFERRABLE;
                    $$ = (Node *)n;
                }
            | INITIALLY DEFERRED
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_ATTR_DEFERRED;
                    $$ = (Node *)n;
                }
            | INITIALLY IMMEDIATE
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_ATTR_IMMEDIATE;
                    $$ = (Node *)n;
                }
        ;


/*
 * SQL99 supports wholesale borrowing of a table definition via the LIKE clause.
 * This seems to be a poor man's inheritance capability, with the resulting
 * tables completely decoupled except for the original commonality in definitions.
 *
 * This is very similar to CREATE TABLE AS except for the INCLUDING DEFAULTS extension
 * which is a part of SQL 200N
 */
TableLikeClause:
                LIKE qualified_name like_including_projections
                {
                    InhRelation *n = makeNode(InhRelation);
                    n->relation = $2;
                    n->including_defaults = FALSE; // not supported
                    n->including_projections = $3;

                    $$ = (Node *)n;
                }
        ;

like_including_projections:
                INCLUDING PROJECTIONS        { $$ = true; }
                | EXCLUDING PROJECTIONS        { $$ = false; }
                | /* EMPTY */                { $$ = false; }
        ;

/* ConstraintElem specifies constraint syntax which is not embedded into
 *    a column definition. ColConstraintElem specifies the embedded form.
 * - thomas 1997-12-03
 */
TableConstraint:
            CONSTRAINT name ConstraintElem
                {
                    switch (nodeTag($3))
                    {
                        case T_Constraint:
                            {
                                Constraint *n = (Constraint *)$3;
                                n->name = $2.str;
                            }
                            break;
                        case T_FkConstraint:
                            {
                                FkConstraint *n = (FkConstraint *)$3;
                                n->constr_name = $2.str;
                            }
                            break;
                        case T_CorrelationConstraint:
                            {
                                FkConstraint *n = (FkConstraint *)$3;
                                n->constr_name = $2.str;
                            }
                            break;
                        default:
                            break;
                    }
                    $$ = $3;
                }
            | ConstraintElem                        { $$ = $1; }
        ;

ConstraintElem:
            CHECK '(' a_expr ')' OptConsStatus
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_CHECK;
                    n->name = NULL;
                    n->raw_expr = $3;
                    n->cooked_expr = NULL;
                    n->indexspace = NULL;
                    n->status = $5;
                    $$ = (Node *)n;
                }
            | UNIQUE '(' columnList ')' OptConsTableSpace OptConsStatus
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_UNIQUE;
                    n->name = NULL;
                    n->raw_expr = NULL;
                    n->cooked_expr = NULL;
                    n->keys = $3;
                    n->indexspace = $5.str;
                    n->status = $6;
                    $$ = (Node *)n;
                }
            | PRIMARY KEY '(' columnList ')' OptConsTableSpace OptConsStatus
                {
                    Constraint *n = makeNode(Constraint);
                    n->contype = CONSTR_PRIMARY;
                    n->name = NULL;
                    n->raw_expr = NULL;
                    n->cooked_expr = NULL;
                    n->keys = $4;
                    n->indexspace = $6.str;
                    n->status = $7;
                    $$ = (Node *)n;
                }
            | FOREIGN KEY '(' columnList ')' REFERENCES qualified_name
                opt_column_list key_match key_actions ConstraintAttributeSpec
                {
                    FkConstraint *n = makeNode(FkConstraint);
                    n->constr_name        = NULL;
                    n->pktable            = $7;
                    n->fk_attrs            = $4;
                    n->pk_attrs            = $8;
                    n->fk_matchtype        = $9;
                    n->fk_upd_action    = (char) ($10 >> 8);
                    n->fk_del_action    = (char) ($10 & 0xFF);
                    n->deferrable        = ($11 & 1) != 0;
                    n->initdeferred        = ($11 & 2) != 0;
                    $$ = (Node *)n;
                }
            | CORRELATION '(' columnList ')' opt_determines_clause OptionalStrengthValue
                {
                    CorrelationConstraint* n = makeNode(CorrelationConstraint);
                    n->correlationType = CORREL_DETERMINES;
                    n->name = NULL;
                    n->left_attrs = $3;
                    n->right_attrs = $5;
                    n->strength = (Node *)$6;
                    $$ = (Node*)n;
                }
        ;

opt_column_list:
            '(' columnList ')'                        { $$ = $2; }
            | /*EMPTY*/                                { $$ = NIL; }
        ;

columnList:
            columnElem                                { $$ = list_make1(makeStr($1)); }
            | columnList ',' columnElem                { $$ = lappend($1, makeStr($3)); }
        ;

opt_determines_clause:
            DETERMINES '(' columnElem ')'           { $$ = list_make1(makeStr($3)); }
            | /*EMPTY*/                             { $$ = NIL; }
        ;

OptionalStrengthValue:
            STRENGTH opt_minus FCONST
                {
                    Value *f = makeFloat($3);
                    if ($2)
                        doNegateFloat(f);
                    $$ = f;
                }
            | STRENGTH opt_minus ICONST
                {   $$ = makeInteger($2 ? -$3 : $3);
                }
            | /*EMPTY*/                           { $$ = NIL; }
        ;
columnElem: ColId
                {
                    /*disallow improper use of epoch column: (VER-18543)*/
                    /*(in table constraint, view column defintion, copy target etc)*/
                    if (isEpochCol($1.str))
                        ereport(ERROR, (errcode(ERRCODE_RESERVED_NAME),
                                errmsg("Invalid use of reserved the column name \"%s\"", $1.str)));
                    $$ = $1;
                }
        ;

key_match:  MATCH FULL
            {
                $$ = FKCONSTR_MATCH_FULL;
            }
        | MATCH PARTIAL
            {
                ereport(ERROR,
                        (errcode(ERRCODE_FEATURE_NOT_SUPPORTED),
                         errmsg("MATCH PARTIAL is not supported")));
                $$ = FKCONSTR_MATCH_PARTIAL;
            }
        | MATCH SIMPLE
            {
                $$ = FKCONSTR_MATCH_UNSPECIFIED;
            }
        | /*EMPTY*/
            {
                $$ = FKCONSTR_MATCH_UNSPECIFIED;
            }
        ;

/*
 * We combine the update and delete actions into one value temporarily
 * for simplicity of parsing, and then break them down again in the
 * calling production.  update is in the left 8 bits, delete in the right.
 * Note that NOACTION is the default.
 */
key_actions:
            key_update
                { $$ = ($1 << 8) | (FKCONSTR_ACTION_NOACTION & 0xFF); }
            | key_delete
                { $$ = (FKCONSTR_ACTION_NOACTION << 8) | ($1 & 0xFF); }
            | key_update key_delete
                { $$ = ($1 << 8) | ($2 & 0xFF); }
            | key_delete key_update
                { $$ = ($2 << 8) | ($1 & 0xFF); }
            | /*EMPTY*/
                { $$ = (FKCONSTR_ACTION_NOACTION << 8) | (FKCONSTR_ACTION_NOACTION & 0xFF); }
        ;

key_update: ON UPDATE key_action        { $$ = $3; }
        ;

key_delete: ON DELETE_P key_action        { $$ = $3; }
        ;

key_action:
            NO ACTION                    { $$ = FKCONSTR_ACTION_NOACTION; }
            | RESTRICT                    { $$ = FKCONSTR_ACTION_RESTRICT; }
            | CASCADE                    { $$ = FKCONSTR_ACTION_CASCADE; }
            | SET NULL_P                { $$ = FKCONSTR_ACTION_SETNULL; }
            | SET DEFAULT                { $$ = FKCONSTR_ACTION_SETDEFAULT; }
        ;

OptInherit: INHERITS '(' qualified_name_list ')'    { $$ = $3; }
            | /*EMPTY*/                                { $$ = NIL; }
        ;

OptWithOids:
            WITH OIDS                                { $$ = MUST_HAVE_OIDS; }
            | WITHOUT OIDS                            { $$ = MUST_NOT_HAVE_OIDS; }
            | /*EMPTY*/                                { $$ = DEFAULT_OIDS; }
        ;

OnCommitOption:  ON COMMIT DROP                { $$ = ONCOMMIT_DROP; }
            | ON COMMIT DELETE_P ROWS        { $$ = ONCOMMIT_DELETE_ROWS; }
            | ON COMMIT PRESERVE ROWS        { $$ = ONCOMMIT_PRESERVE_ROWS; }
            | /*EMPTY*/                        { $$ = ONCOMMIT_NOOP; }
        ;

OptTableSpace:   TABLESPACE name                    { $$ = $2; }
            | /*EMPTY*/                                { $$ = ctNULL; }
        ;

OptConsTableSpace:   USING INDEX TABLESPACE name    { $$ = $4; }
            | /*EMPTY*/                                { $$ = ctNULL; }
        ;

OptConsStatus:   ENABLED                          { $$ = CONSTR_STAT_ENABLED; }
            |    DISABLED                         { $$ = CONSTR_STAT_DISABLED; }
            | /*EMPTY*/                           { $$ = CONSTR_STAT_NULL; }
        ;

/*
 * Note: CREATE TABLE ... AS SELECT ... is just another spelling for
 * SELECT ... INTO.
 */

CreateAsStmt:
            CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses

                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                                        n->exists_ok = TRUE;
                    $7->temptype = $2;
                    n->relation = $7;
                    n->tableElts = $8;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $9;
                    n->oncommit = $10;
                    n->tablespacename = NULL;
                    n->copyMode = $11;
                    n->selectStmt = $14;
                    n->hintClause = $13;
                    n->projStmt = $15;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses

                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $8->temptype = $3;
                    n->relation = $8;
                    n->tableElts = $9;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = $11;
                    n->tablespacename = NULL;
                    n->copyMode = $12;
                    n->selectStmt = $15;
                    n->hintClause = $14;
                    n->projStmt = $16;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    // Materialize specified columns in n->tableElts, or
                    // all query columns (i.e., aggresive materialization)
                    // if none was provided in n->tableElts
                    n->flexMaterializeAll = (list_length(n->tableElts) == 0) ? true : false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AS hint_clause VSelectStmt ProjectionClauses
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                    n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $8->temptype = $3;
                    n->relation = $8;
                    n->tableElts = $10;
                    n->inhRelations = $12;
                    n->constraints = NULL;
                    n->hasoids = $13;
                    n->oncommit = $14;
                    n->tablespacename = $15.str;
                    n->copyMode = $16;
                    n->hintClause = $18;
                    n->selectStmt = $19;
                    n->projStmt = $20;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    // With the '(' columns ')' syntax, the user cannot implicitly materialize
                    // all columns except when they explicitly list all columns
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses

                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $8->temptype = $3;
                    n->relation = $8;
                    n->tableElts = $9;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = $11;
                    n->tablespacename = NULL;
                    n->copyMode = $12;
                    n->selectStmt = $15;
                    n->hintClause = $14;
                    n->projStmt = $16;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    // Materialize specified columns in n->tableElts, or
                    // all query columns (i.e., aggresive materialization)
                    // if none was provided in n->tableElts
                    n->flexMaterializeAll = (list_length(n->tableElts) == 0) ? true : false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AS hint_clause VSelectStmt ProjectionClauses

                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                    n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $8->temptype = $3;
                    n->relation = $8;
                    n->tableElts = $10;
                    n->inhRelations = $12;
                    n->constraints = NULL;
                    n->hasoids = $13;
                    n->oncommit = $14;
                    n->tablespacename = $15.str;
                    n->copyMode = $16;
                    n->hintClause = $18;
                    n->selectStmt = $19;
                    n->projStmt = $20;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    // With the '(' columns ')' syntax, the user cannot implicitly materialize
                    // all columns except when they explicitly list all columns
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClausesNoKsafe
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $4->temptype = $2;
                    n->relation = $4;
                    n->tableElts = $5;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $6;
                    n->oncommit = $7;
                    n->tablespacename = NULL;
                    n->copyMode = $8;
                    n->selectStmt = $11;
                    n->hintClause = $10;
                    n->projStmt = $12;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
// Can't have VPartition follow a VSelectStmt directly, because "PARTITION" isn't a reserved keyword,
// so "SELECT * FROM t PARTITION" might mean 't AS "PARTITION"' or it might mean "t PARTITION BY".
// But if we require the keyword 'KSAFE' to be used between the two, it means the same thing,
// and is deterministically parseable.
            | CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClausesRequireKsafe VPartition
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $4->temptype = $2;
                    n->relation = $4;
                    n->tableElts = $5;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $6;
                    n->oncommit = $7;
                    n->tablespacename = NULL;
                    n->copyMode = $8;
                    n->selectStmt = $11;
                    n->hintClause = $10;
                    n->projStmt = $12;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = $13.partnExpr;
                    n->partnGroupExpr = $13.groupExpr;
                    n->activePartitionCount = $13.activePartitionCount;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEX OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $5->temptype = $3;
                    n->relation = $5;
                    n->tableElts = $6;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $7;
                    n->oncommit = $8;
                    n->tablespacename = NULL;
                    n->copyMode = $9;
                    n->selectStmt = $12;
                    n->hintClause = $11;
                    n->projStmt = $13;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    // Materialize specified columns in n->tableElts, or
                    // all query columns (i.e., aggresive materialization)
                    // if none was provided in n->tableElts
                    n->flexMaterializeAll = (list_length(n->tableElts) == 0) ? true : false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEX OptTemp TABLE qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AS hint_clause VSelectStmt ProjectionClauses
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                    n->exists_ok = FALSE;
                    $5->temptype = $3;
                    n->relation = $5;
                    n->tableElts = $7;
                    n->inhRelations = $9;
                    n->constraints = NULL;
                    n->hasoids = $10;
                    n->oncommit = $11;
                    n->tablespacename = $12.str;
                    n->copyMode = $13;
                    n->hintClause = $15;
                    n->selectStmt = $16;
                    n->projStmt = $17;
                    n->partitionExpr = NULL;
                    n->partnGroupExpr = NULL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    // With the '(' columns ')' syntax, the user cannot implicitly materialize
                    // all columns except when they explicitly list all columns
                    n->flexMaterializeAll = false;
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    addFlexTableColumns(n);
                    $$ = (Node *)n;
                }
             | CREATE FLEXIBLE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS hint_clause VSelectStmt ProjectionClauses
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $5->temptype = $3;
                    n->relation = $5;
                    n->tableElts = $6;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $7;
                    n->oncommit = $8;
                    n->tablespacename = NULL;
                    n->copyMode = $9;
                    n->selectStmt = $12;
                    n->hintClause = $11;
                    n->projStmt = $13;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    // Materialize specified columns in n->tableElts, or
                    // all query columns (i.e., aggresive materialization)
                    // if none was provided in n->tableElts
                    n->flexMaterializeAll = (list_length(n->tableElts) == 0) ? true : false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
             | CREATE FLEXIBLE OptTemp TABLE qualified_name '(' OptTableElementList ')' OptInherit OptWithOids OnCommitOption OptTableSpace OptCopy AS hint_clause VSelectStmt ProjectionClauses
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                    n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $5->temptype = $3;
                    n->relation = $5;
                    n->tableElts = $7;
                    n->inhRelations = $9;
                    n->constraints = NULL;
                    n->hasoids = $10;
                    n->oncommit = $11;
                    n->tablespacename = $12.str;
                    n->copyMode = $13;
                    n->hintClause = $15;
                    n->selectStmt = $16;
                    n->projStmt = $17;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NULL;
                    n->partnGroupExpr = NULL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    // With the '(' columns ')' syntax, the user cannot implicitly materialize
                    // all columns except when they explicitly list all columns
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
/* External Tables: CREATE TABLE AS COPY.
 */
            | CREATE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $8->temptype = $3;
                    n->relation = $8;
                    n->tableElts = $10;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $12;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $14;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE MANAGED EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = TRUE;
                    n->exists_ok = TRUE;
                    $9->temptype = $4;
                    n->relation = $9;
                    n->tableElts = $11;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $13;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $15;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEX EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $9->temptype = $4;
                    n->relation = $9;
                    n->tableElts = $11;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $13;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $15;                   
                    n->skip_permissions = false;
                    confirmFlexNotUsingHive((CopyStmt*)n->external_source);
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEXIBLE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $9->temptype = $4;
                    n->relation = $9;
                    n->tableElts = $11;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $13;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $15;
                    n->skip_permissions = false;
                    confirmFlexNotUsingHive((CopyStmt*)n->external_source);
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $5->temptype = $3;
                    n->relation = $5;
                    n->tableElts = $7;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $9;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $11;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE MANAGED EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = TRUE;
                    n->exists_ok = FALSE;
                    $6->temptype = $4;
                    n->relation = $6;
                    n->tableElts = $8;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $12;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEX EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $6->temptype = $4;
                    n->relation = $6;
                    n->tableElts = $8;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $12;
                    n->skip_permissions = false;
                    confirmFlexNotUsingHive((CopyStmt*)n->external_source);
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEXIBLE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $6->temptype = $4;
                    n->relation = $6;
                    n->tableElts = $8;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $12;
                    n->skip_permissions = false;
                    confirmFlexNotUsingHive((CopyStmt*)n->external_source);
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
        ;

// Support for inherited privileges. Can't have two adjacent optional terms, so write it all out...
CreateAsStmt:
            CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses

                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                                        n->exists_ok = TRUE;
                    $7->temptype = $2;
                    n->relation = $7;
                    n->tableElts = $8;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $9;
                    n->oncommit = $10;
                    n->copyMode = $11;
                    n->tablespacename = NULL;
                    n->selectStmt = $17;
                    n->hintClause = $16;
                    n->projStmt = $18;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses

                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                                        n->exists_ok = TRUE;
                    $7->temptype = $2;
                    n->relation = $7;
                    n->tableElts = $8;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $9;
                    n->oncommit = $10;
                    n->copyMode = $11;
                    n->tablespacename = NULL;
                    n->selectStmt = $17;
                    n->hintClause = $16;
                    n->projStmt = $18;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses

                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $8->temptype = $3;
                    n->relation = $8;
                    n->tableElts = $9;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = $11;
                    n->copyMode = $12;
                    n->tablespacename = NULL;
                    n->selectStmt = $18;
                    n->hintClause = $17;
                    n->projStmt = $19;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEX OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses

                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $8->temptype = $3;
                    n->relation = $8;
                    n->tableElts = $9;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = $11;
                    n->copyMode = $12;
                    n->tablespacename = NULL;
                    n->selectStmt = $18;
                    n->hintClause = $17;
                    n->projStmt = $19;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses

                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $8->temptype = $3;
                    n->relation = $8;
                    n->tableElts = $9;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = $11;
                    n->copyMode = $12;
                    n->tablespacename = NULL;
                    n->selectStmt = $18;
                    n->hintClause = $17;
                    n->projStmt = $19;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEXIBLE OptTemp TABLE IF_P NOT EXISTS qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses

                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $8->temptype = $3;
                    n->relation = $8;
                    n->tableElts = $9;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = $11;
                    n->copyMode = $12;
                    n->tablespacename = NULL;
                    n->selectStmt = $18;
                    n->hintClause = $17;
                    n->projStmt = $19;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClausesNoKsafe
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $4->temptype = $2;
                    n->relation = $4;
                    n->tableElts = $5;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $6;
                    n->oncommit = $7;
                    n->copyMode = $8;
                    n->tablespacename = NULL;
                    n->selectStmt = $14;
                    n->hintClause = $13;
                    n->projStmt = $15;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClausesNoKsafe
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $4->temptype = $2;
                    n->relation = $4;
                    n->tableElts = $5;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $6;
                    n->oncommit = $7;
                    n->copyMode = $8;
                    n->tablespacename = NULL;
                    n->selectStmt = $14;
                    n->hintClause = $13;
                    n->projStmt = $15;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
// Can't have VPartition follow a VSelectStmt directly, because "PARTITION" isn't a reserved keyword,
// so "SELECT * FROM t PARTITION" might mean 't AS "PARTITION"' or it might mean "t PARTITION BY".
// But if we require the keyword 'KSAFE' to be used between the two, it means the same thing,
// and is deterministically parseable.
            | CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClausesRequireKsafe VPartition
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $4->temptype = $2;
                    n->relation = $4;
                    n->tableElts = $5;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $6;
                    n->oncommit = $7;
                    n->copyMode = $8;
                    n->tablespacename = NULL;
                    n->selectStmt = $14;
                    n->hintClause = $13;
                    n->projStmt = $15;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = $16.partnExpr;
                    n->partnGroupExpr = $16.groupExpr;
                    n->activePartitionCount = $16.activePartitionCount;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClausesRequireKsafe VPartition
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $4->temptype = $2;
                    n->relation = $4;
                    n->tableElts = $5;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $6;
                    n->oncommit = $7;
                    n->copyMode = $8;
                    n->tablespacename = NULL;
                    n->selectStmt = $14;
                    n->hintClause = $13;
                    n->projStmt = $15;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = $16.partnExpr;
                    n->partnGroupExpr = $16.groupExpr;
                    n->activePartitionCount = $16.activePartitionCount;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEX OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $5->temptype = $3;
                    n->relation = $5;
                    n->tableElts = $6;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $7;
                    n->oncommit = $8;
                    n->copyMode = $9;
                    n->tablespacename = NULL;
                    n->selectStmt = $15;
                    n->hintClause = $14;
                    n->projStmt = $16;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEX OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $5->temptype = $3;
                    n->relation = $5;
                    n->tableElts = $6;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $7;
                    n->oncommit = $8;
                    n->copyMode = $9;
                    n->tablespacename = NULL;
                    n->selectStmt = $15;
                    n->hintClause = $14;
                    n->projStmt = $16;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
             | CREATE FLEXIBLE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy INCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $5->temptype = $3;
                    n->relation = $5;
                    n->tableElts = $6;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $7;
                    n->oncommit = $8;
                    n->copyMode = $9;
                    n->tablespacename = NULL;
                    n->selectStmt = $15;
                    n->hintClause = $14;
                    n->projStmt = $16;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
             | CREATE FLEXIBLE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy EXCLUDE OptSchemaKeyword PRIVILEGES AS hint_clause VSelectStmt ProjectionClauses
                {
                    //CTAS will generate CreateStmt with selectStmt subquery
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $5->temptype = $3;
                    n->relation = $5;
                    n->tableElts = $6;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $7;
                    n->oncommit = $8;
                    n->copyMode = $9;
                    n->tablespacename = NULL;
                    n->selectStmt = $15;
                    n->hintClause = $14;
                    n->projStmt = $16;
                    ((VCreateProjectionStmt*)(n->projStmt))->createType = PROJ_INSTANT;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = NULL;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
/* External Tables: CREATE TABLE AS COPY.
 */
            | CREATE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $8->temptype = $3;
                    n->relation = $8;
                    n->tableElts = $10;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $12;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $17;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $8->temptype = $3;
                    n->relation = $8;
                    n->tableElts = $10;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $12;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $17;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE MANAGED EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = TRUE;
                    n->exists_ok = TRUE;
                    $9->temptype = $4;
                    n->relation = $9;
                    n->tableElts = $11;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $13;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $18;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE MANAGED EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = TRUE;
                    n->exists_ok = TRUE;
                    $9->temptype = $4;
                    n->relation = $9;
                    n->tableElts = $11;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $13;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $18;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEX EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $9->temptype = $4;
                    n->relation = $9;
                    n->tableElts = $11;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $13;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $18;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEX EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $9->temptype = $4;
                    n->relation = $9;
                    n->tableElts = $11;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $13;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $18;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEXIBLE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $9->temptype = $4;
                    n->relation = $9;
                    n->tableElts = $11;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $13;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $18;
                    n->replicate_from = NULL;
                    n->skip_permissions = false;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEXIBLE EXTERNAL OptTemp TABLE IF_P NOT EXISTS qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = TRUE;
                    $9->temptype = $4;
                    n->relation = $9;
                    n->tableElts = $11;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $13;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $18;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $5->temptype = $3;
                    n->relation = $5;
                    n->tableElts = $7;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $9;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $14;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $5->temptype = $3;
                    n->relation = $5;
                    n->tableElts = $7;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $9;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $14;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE MANAGED EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = TRUE;
                    n->exists_ok = FALSE;
                    $6->temptype = $4;
                    n->relation = $6;
                    n->tableElts = $8;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $15;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE MANAGED EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = TRUE;
                    n->exists_ok = FALSE;
                    $6->temptype = $4;
                    n->relation = $6;
                    n->tableElts = $8;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $15;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = false;
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEX EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $6->temptype = $4;
                    n->relation = $6;
                    n->tableElts = $8;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $15;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEXIBLE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids INCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $6->temptype = $4;
                    n->relation = $6;
                    n->tableElts = $8;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $15;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
            | CREATE FLEXIBLE EXTERNAL OptTemp TABLE qualified_name '(' OptTableElementList ')' OptWithOids EXCLUDE OptSchemaKeyword PRIVILEGES AS ExternalTableCopyStmt
                {
                    CreateStmt *n = makeNode(CreateStmt);
                                        n->external_managed = FALSE;
                    n->exists_ok = FALSE;
                    $6->temptype = $4;
                    n->relation = $6;
                    n->tableElts = $8;
                    n->inhRelations = NIL;
                    n->constraints = NIL;
                    n->hasoids = $10;
                    n->oncommit = ONCOMMIT_NOOP;
                    n->tablespacename = NULL;
                    n->selectStmt = NULL;
                    n->hintClause = NULL;
                    n->projStmt = NULL;
                    n->partitionExpr = NIL;
                    n->partnGroupExpr = NIL;
                    n->activePartitionCount = VINT_NULL;
                    n->external_source = $15;
                    n->skip_permissions = false;
                    n->replicate_from = NULL;
                    n->flextable = true;
                    n->flexMaterializeAll = false;
                    addFlexTableColumns(n);
                    n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                    $$ = (Node *)n;
                }
        ;


AutoProjectionDef:
            NO PROJECTION                { $$ = NIL; } /* for backward compatibility on temptable */
            | opt_sort_clause ProjectionClauses
                {
                    VCreateProjectionStmt *n = (VCreateProjectionStmt*) $2;
                    n->sortClause=$1;
                    $$ = (Node *)n;
                }
        ;

ProjectionClausesRequireKsafe:
            opt_encode_clause VSegmentation ksafe_num_required
                {
                    VCreateProjectionStmt *n = makeNode(VCreateProjectionStmt);
                    n->relation = NULL;
                    n->targetList=NULL;
                    n->sortClause=NULL;
                    n->encodeClause=$1;
                    n->segmentation=$2;
                    n->ksafe=$3;
                    $$ = (Node *)n;
                }
        ;

ProjectionClausesNoKsafe:
            opt_encode_clause VSegmentation
                {
                    VCreateProjectionStmt *n = makeNode(VCreateProjectionStmt);
                    n->relation = NULL;
                    n->targetList=NULL;
                    n->sortClause=NULL;
                    n->encodeClause=$1;
                    n->segmentation=$2;
                    n->ksafe=KSAFE_NONE;
                    $$ = (Node *)n;
                }
        ;

ProjectionClauses:
            opt_encode_clause VSegmentation ksafe_num
                {
                    VCreateProjectionStmt *n = makeNode(VCreateProjectionStmt);
                    n->relation = NULL;
                    n->targetList=NULL;
                    n->sortClause=NULL;
                    n->encodeClause=$1;
                    n->segmentation=$2;
                    n->ksafe=$3;
                    $$ = (Node *)n;
                }
        ;

opt_encode_clause:
            ENCODED BY vt_columnList                   { $$ = $3; }
            | /*EMPTY*/                                { $$ = NIL; }
        ;

OptSchemaKeyword:
            SCHEMA                                     { $$ = NIL; }
            | /*EMPTY*/                                { $$ = NIL; }
        ; 

/*****************************************************************************
 *
 *        QUERY :
 *                CREATE SEQUENCE seqname
 *                ALTER SEQUENCE seqname
 *
 *****************************************************************************/

CreateSeqStmt:
            CREATE OptTemp SEQUENCE qualified_name OptSeqList
                {
                    CreateSeqStmt *n = makeNode(CreateSeqStmt);
                    $4->temptype = $2;
                    n->sequence = $4;
                    n->options = $5;
                    n->exists_ok = FALSE;
                    $$ = (Node *)n;
                }
            | CREATE OptTemp SEQUENCE IF_P NOT EXISTS qualified_name OptSeqList
                {
                    CreateSeqStmt *n = makeNode(CreateSeqStmt);
                    $7->temptype = $2;
                    n->sequence = $7;
                    n->options = $8;
                    n->exists_ok = TRUE;
                    $$ = (Node *)n;
                }
        ;

AlterSeqStmt:
            ALTER SEQUENCE qualified_name OptSeqList
                {
                    AlterSeqStmt *n = makeNode(AlterSeqStmt);
                    n->sequence = $3;
                    n->options = $4;
                    $$ = (Node *)n;
                }
            | ALTER SEQUENCE qualified_name SET SCHEMA qualified_schema_name
                {
                    AlterSeqStmt *n = makeNode(AlterSeqStmt);
                    n->sequence = $3;
                    n->options = list_make1(makeDefElem("schema",(Node*)makeStr($6)));
                    $$ = (Node *)n;
                }
            | ALTER SEQUENCE qualified_name OWNER TO name
                {
                    AlterSeqStmt *n = makeNode(AlterSeqStmt);
                    n->sequence = $3;
                    n->options = list_make1(makeDefElem("owner",(Node*)makeStr($6)));
                    $$ = (Node *)n;
                }
        ;

OptSeqList: OptSeqList OptSeqElem                    { $$ = lappend($1, $2); }
            | /*EMPTY*/                                { $$ = NIL; }
        ;

OptSeqElem: CACHE NumericOnly
                {
                    $$ = makeDefElem("cache", (Node *)$2);
                }
            | NO CACHE
                {
                    $$ = makeDefElem("cache", NULL);
                }
            | CYCLE
                {
                    $$ = makeDefElem("cycle", (Node *)makeInteger(TRUE));
                }
            | NO CYCLE
                {
                    $$ = makeDefElem("cycle", (Node *)makeInteger(FALSE));
                }
            | ORDER
                {
                    $$ = makeDefElem("order", (Node *)makeInteger(TRUE));
                }
            | NO ORDER
                {
                    $$ = makeDefElem("order", (Node *)makeInteger(FALSE));
                }
            | INCREMENT opt_by IntegerOnly
                {
                    $$ = makeDefElem("increment", (Node *)$3);
                }
            | MAXVALUE NumericOnly
                {
                    $$ = makeDefElem("maxvalue", (Node *)$2);
                }
            | MINVALUE NumericOnly
                {
                    $$ = makeDefElem("minvalue", (Node *)$2);
                }
            | NO MAXVALUE
                {
                    $$ = makeDefElem("maxvalue", NULL);
                }
            | NO MINVALUE
                {
                    $$ = makeDefElem("minvalue", NULL);
                }
            | START opt_with IntegerOnly
                {
                    $$ = makeDefElem("start", (Node *)$3);
                }
            | RESTART opt_with IntegerOnly
                {
                    $$ = makeDefElem("restart", (Node *)$3);
                }
        ;

opt_by:        BY                {}
            | /* empty */    {}
      ;

NumericOnly:
            IntegerOnly                            { $$ = $1; }
            | FCONST                               { $$ = makeFloat($1); }
            | '-' FCONST
                {
                    $$ = makeFloat($2);
                    doNegateFloat($$);
                }
        ;

IntegerOnly:
            Iconst
                {
                    $$ = makeInteger($1);
                }
            | '-' Iconst
                {
                    $$ = makeInteger($2);
                    $$->val.ival = - $$->val.ival;
                }
        ;

RuntimePriorityValue:
        HIGH     { $$ = makeInteger(100); }
        | MEDIUM { $$ = makeInteger(50); }
        | LOW    { $$ = makeInteger(0); }
        ;

/*****************************************************************************
 *
 *        QUERIES :
 *                CREATE PROCEDURAL LANGUAGE ...
 *                DROP PROCEDURAL LANGUAGE ...
 *
 *****************************************************************************/

CreatePLangStmt:
            CREATE opt_trusted opt_procedural LANGUAGE ColId_or_Sconst
            HANDLER handler_name opt_validator opt_lancompiler
            {
                CreatePLangStmt *n = makeNode(CreatePLangStmt);
                n->plname = $5.str;
                n->plhandler = $7;
                n->plvalidator = $8;
                n->pltrusted = $2;
                $$ = (Node *)n;
            }
        ;

opt_trusted:
            TRUSTED                                    { $$ = TRUE; }
            | /*EMPTY*/                                { $$ = FALSE; }
        ;

/* This ought to be just func_name, but that causes reduce/reduce conflicts
 * (CREATE LANGUAGE is the only place where func_name isn't followed by '(').
 * Work around by using simple names, instead.
 */
handler_name:
            name                        { $$ = list_make1(makeStr($1)); }
            | name attrs                { $$ = lcons(makeStr($1), $2); }
        ;

opt_lancompiler:
            LANCOMPILER Sconst                        { $$ = $2; }
| /*EMPTY*/                                { $$ = ctString(""); }
        ;

opt_validator:
            VALIDATOR handler_name { $$ = $2; }
            | /*EMPTY*/ { $$ = NULL; }
        ;

DropPLangStmt:
            DROP opt_procedural LANGUAGE ColId_or_Sconst opt_drop_behavior
                {
                    DropPLangStmt *n = makeNode(DropPLangStmt);
                    n->plname = $4.str;
                    n->behavior = $5;
                    $$ = (Node *)n;
                }
        ;

opt_procedural:
            PROCEDURAL                                {}
            | /*EMPTY*/                                {}
        ;

/*****************************************************************************
 *
 *         QUERY:
 *             CREATE TABLESPACE tablespace LOCATION '/path/to/tablespace/'
 *
 *****************************************************************************/

CreateTableSpaceStmt: CREATE TABLESPACE name OptTableSpaceOwner LOCATION Sconst
                {
                    CreateTableSpaceStmt *n = makeNode(CreateTableSpaceStmt);
                    n->tablespacename = $3.str;
                    n->owner = $4.str;
                    n->location = $6.str;
                    $$ = (Node *) n;
                }
        ;

OptTableSpaceOwner: OWNER name            { $$ = $2; }
            | /*EMPTY */                { $$ = ctNULL; }
        ;

/*****************************************************************************
 *
 *         QUERY :
 *                DROP TABLESPACE <tablespace>
 *
 *        No need for drop behaviour as we cannot implement dependencies for
 *        objects in other databases; we can only support RESTRICT.
 *
 ****************************************************************************/

DropTableSpaceStmt: DROP TABLESPACE name
                {
                    DropTableSpaceStmt *n = makeNode(DropTableSpaceStmt);
                    n->tablespacename = $3.str;
                    $$ = (Node *) n;
                }
        ;

/*****************************************************************************
 *
 *        QUERIES :
 *                CREATE TRIGGER ...
 *                DROP TRIGGER ...
 *
 *****************************************************************************/

CreateTrigStmt:
            CREATE TRIGGER name TriggerActionTime TriggerEvents ON
            qualified_name TriggerForSpec EXECUTE PROCEDURE
            func_name '(' TriggerFuncArgs ')'
                {
                    CreateTrigStmt *n = makeNode(CreateTrigStmt);
                    n->trigname = $3.str;
                    n->relation = $7;
                    n->funcname = $11;
                    n->args = $13;
                    n->before = $4;
                    n->row = $8;
                    memcpy(n->actions, $5.str, 4);
                    n->isconstraint  = FALSE;
                    n->deferrable     = FALSE;
                    n->initdeferred  = FALSE;
                    n->constrrel = NULL;
                    $$ = (Node *)n;
                }
            | CREATE CONSTRAINT TRIGGER name AFTER TriggerEvents ON
            qualified_name OptConstrFromTable
            ConstraintAttributeSpec
            FOR EACH ROW EXECUTE PROCEDURE
            func_name '(' TriggerFuncArgs ')'
                {
                    CreateTrigStmt *n = makeNode(CreateTrigStmt);
                    n->trigname = $4.str;
                    n->relation = $8;
                    n->funcname = $16;
                    n->args = $18;
                    n->before = FALSE;
                    n->row = TRUE;
                    memcpy(n->actions, $6.str, 4);
                    n->isconstraint  = TRUE;
                    n->deferrable = ($10 & 1) != 0;
                    n->initdeferred = ($10 & 2) != 0;

                    n->constrrel = $9;
                    $$ = (Node *)n;
                }
        ;

TriggerActionTime:
            BEFORE                                    { $$ = TRUE; }
            | AFTER                                    { $$ = FALSE; }
        ;

TriggerEvents:
            TriggerOneEvent
                {
                    char *e = palloc(4);
                    e[0] = $1; e[1] = '\0';
                    $$ = ctString(e);
                }
            | TriggerOneEvent OR TriggerOneEvent
                {
                    char *e = palloc(4);
                    e[0] = $1; e[1] = $3; e[2] = '\0';
                    $$ = ctString(e);
                }
            | TriggerOneEvent OR TriggerOneEvent OR TriggerOneEvent
                {
                    char *e = palloc(4);
                    e[0] = $1; e[1] = $3; e[2] = $5; e[3] = '\0';
                    $$ = ctString(e);
                }
        ;

TriggerOneEvent:
            INSERT                                    { $$ = 'i'; }
            | DELETE_P                                { $$ = 'd'; }
            | UPDATE                                { $$ = 'u'; }
        ;

TriggerForSpec:
            FOR TriggerForOpt TriggerForType
                {
                    $$ = $3;
                }
            | /* EMPTY */
                {
                    /*
                     * If ROW/STATEMENT not specified, default to
                     * STATEMENT, per SQL
                     */
                    $$ = FALSE;
                }
        ;

TriggerForOpt:
            EACH                                    {}
            | /*EMPTY*/                                {}
        ;

TriggerForType:
            ROW                                        { $$ = TRUE; }
            | STATEMENT                                { $$ = FALSE; }
        ;

TriggerFuncArgs:
            TriggerFuncArg                            { $$ = list_make1($1); }
            | TriggerFuncArgs ',' TriggerFuncArg    { $$ = lappend($1, $3); }
            | /*EMPTY*/                                { $$ = NIL; }
        ;

TriggerFuncArg:
            Iconst
                {
                    char buf[64];
                    snprintf(buf, sizeof(buf), "%lld", $1);
                    $$ = makeString(pstrdup(buf));
                }
            | FCONST                                { $$ = makeStr($1); }
            | Sconst                                { $$ = makeStr($1); }
            | BCONST                                { $$ = makeStr($1); }
            | XCONST                                { $$ = makeStr($1); }
            | ColId                                    { $$ = makeStr($1); }
        ;

OptConstrFromTable:
            FROM qualified_name                        { $$ = $2; }
            | /*EMPTY*/                                { $$ = NULL; }
        ;

ConstraintAttributeSpec:
            ConstraintDeferrabilitySpec
                { $$ = $1; }
            | ConstraintDeferrabilitySpec ConstraintTimeSpec
                {
                    if ($1 == 0 && $2 != 0)
                        ereport(ERROR,
                                (errcode(ERRCODE_SYNTAX_ERROR),
                                 errmsg("Constraint declared INITIALLY DEFERRED must be DEFERRABLE")));
                    $$ = $1 | $2;
                }
            | ConstraintTimeSpec
                {
                    if ($1 != 0)
                        $$ = 3;
                    else
                        $$ = 0;
                }
            | ConstraintTimeSpec ConstraintDeferrabilitySpec
                {
                    if ($2 == 0 && $1 != 0)
                        ereport(ERROR,
                                (errcode(ERRCODE_SYNTAX_ERROR),
                                 errmsg("Constraint declared INITIALLY DEFERRED must be DEFERRABLE")));
                    $$ = $1 | $2;
                }
            | /*EMPTY*/
                { $$ = 0; }
        ;

ConstraintDeferrabilitySpec:
            NOT DEFERRABLE                            { $$ = 0; }
            | DEFERRABLE                            { $$ = 1; }
        ;

ConstraintTimeSpec:
            INITIALLY IMMEDIATE                        { $$ = 0; }
            | INITIALLY DEFERRED                    { $$ = 2; }
        ;


DropTrigStmt:
            DROP TRIGGER name ON qualified_name opt_drop_behavior
                {
                    DropPropertyStmt *n = makeNode(DropPropertyStmt);
                    n->relation = $5;
                    n->property = $3.str;
                    n->behavior = $6;
                    n->removeType = OBJECT_TRIGGER;
                    $$ = (Node *) n;
                }
        ;


/*****************************************************************************
 *
 *        QUERIES :
 *                CREATE ASSERTION ...
 *                DROP ASSERTION ...
 *
 *****************************************************************************/

CreateAssertStmt:
            CREATE ASSERTION name CHECK '(' a_expr ')'
            ConstraintAttributeSpec
                {
                    CreateTrigStmt *n = makeNode(CreateTrigStmt);
                    n->trigname = $3.str;
                    n->args = list_make1($6);
                    n->isconstraint  = TRUE;
                    n->deferrable = ($8 & 1) != 0;
                    n->initdeferred = ($8 & 2) != 0;

                    ereport(ERROR,
                            (errcode(ERRCODE_FEATURE_NOT_SUPPORTED),
                             errmsg("CREATE ASSERTION is not supported")));

                    $$ = (Node *)n;
                }
        ;

DropAssertStmt:
            DROP ASSERTION name opt_drop_behavior
                {
                    DropPropertyStmt *n = makeNode(DropPropertyStmt);
                    n->relation = NULL;
                    n->property = $3.str;
                    n->behavior = $4;
                    n->removeType = OBJECT_TRIGGER; /* XXX */
                    ereport(ERROR,
                            (errcode(ERRCODE_FEATURE_NOT_SUPPORTED),
                             errmsg("DROP ASSERTION is not supported")));
                    $$ = (Node *) n;
                }
        ;


/*****************************************************************************
 *
 *        QUERY :
 *                define (aggregate,operator,type)
 *
 *****************************************************************************/

DefineStmt:
            CREATE OPERATOR any_operator definition
                {
                    DefineStmt *n = makeNode(DefineStmt);
                    n->kind = OBJECT_OPERATOR;
                    n->defnames = $3;
                    n->definition = $4;
                    $$ = (Node *)n;
                }
        ;

definition: '(' def_list ')'                        { $$ = $2; }
        ;

def_list:      def_elem                                { $$ = list_make1($1); }
            | def_list ',' def_elem                    { $$ = lappend($1, $3); }
        ;

def_elem:  ColLabel '=' def_arg
                {
                    $$ = makeDefElem($1.str, (Node *)$3);
                }
            | ColLabel
                {
                    $$ = makeDefElem($1.str, NULL);
                }
        ;

/* Note: any simple identifier will be returned as a type name! */
def_arg:    func_return                        { $$ = (Node *)$1; }
            | qual_all_Op                    { $$ = (Node *)$1; }
            | NumericOnly                    { $$ = (Node *)$1; }
            | Sconst                        { $$ = (Node *)makeStr($1); }
        ;


/*****************************************************************************
 *
 *        QUERIES :
 *                CREATE OPERATOR CLASS ...
 *                DROP OPERATOR CLASS ...
 *
 *****************************************************************************/

CreateOpClassStmt:
            CREATE OPERATOR CLASS any_name opt_default FOR TYPE_P Typename
            USING access_method AS opclass_item_list
                {
                    CreateOpClassStmt *n = makeNode(CreateOpClassStmt);
                    n->opclassname = $4;
                    n->isDefault = $5;
                    n->datatype = $8;
                    n->amname = $10.str;
                    n->items = $12;
                    $$ = (Node *) n;
                }
        ;

opclass_item_list:
            opclass_item                            { $$ = list_make1($1); }
            | opclass_item_list ',' opclass_item    { $$ = lappend($1, $3); }
        ;

opclass_item:
            OPERATOR Iconst any_operator opt_recheck
                {
                    CreateOpClassItem *n = makeNode(CreateOpClassItem);
                    n->itemtype = OPCLASS_ITEM_OPERATOR;
                    n->name = $3;
                    n->args = NIL;
                    n->number = $2;
                    n->recheck = $4;
                    $$ = (Node *) n;
                }
            | OPERATOR Iconst any_operator '(' oper_argtypes ')' opt_recheck
                {
                    CreateOpClassItem *n = makeNode(CreateOpClassItem);
                    n->itemtype = OPCLASS_ITEM_OPERATOR;
                    n->name = $3;
                    n->args = $5;
                    n->number = $2;
                    n->recheck = $7;
                    $$ = (Node *) n;
                }
            | FUNCTION Iconst func_name func_args
                {
                    CreateOpClassItem *n = makeNode(CreateOpClassItem);
                    n->itemtype = OPCLASS_ITEM_FUNCTION;
                    n->name = $3;
                    n->args = extractArgTypes($4);
                    n->number = $2;
                    $$ = (Node *) n;
                }
            | STORAGE Typename
                {
                    CreateOpClassItem *n = makeNode(CreateOpClassItem);
                    n->itemtype = OPCLASS_ITEM_STORAGETYPE;
                    n->storedtype = $2;
                    $$ = (Node *) n;
                }
        ;

opt_default:    DEFAULT    { $$ = TRUE; }
            | /*EMPTY*/    { $$ = FALSE; }
        ;

opt_recheck:    RECHECK    { $$ = TRUE; }
            | /*EMPTY*/    { $$ = FALSE; }
        ;


DropOpClassStmt:
            DROP OPERATOR CLASS any_name USING access_method opt_drop_behavior
                {
                    RemoveOpClassStmt *n = makeNode(RemoveOpClassStmt);
                    n->opclassname = $4;
                    n->amname = $6.str;
                    n->behavior = $7;
                    $$ = (Node *) n;
                }
        ;


/*****************************************************************************
 *
 *        QUERY:
 *
 *        DROP itemtype itemname [, itemname ...] [ RESTRICT | CASCADE ] [ segments ]
 *
 *****************************************************************************/

DropStmt:    DROP drop_type IF_P EXISTS any_name_list opt_drop_behavior
                {
                    DropStmt *n = makeNode(DropStmt);
                    n->removeType = $2;
                    n->missing_ok = TRUE;
                    n->objects = $5;
                    n->behavior = $6;
                    $$ = (Node *)n;
                }
             | DROP drop_type any_name_list opt_drop_behavior
                {
                    DropStmt *n = makeNode(DropStmt);
                    n->removeType = $2;
                    n->missing_ok = FALSE;
                    n->objects = $3;
                    n->behavior = $4;
                    $$ = (Node *)n;
                }
             | DROP RESOURCE POOL any_name_list
                {
                    DropStmt *n = makeNode(DropStmt);
                    n->removeType = OBJECT_RESOURCEPOOL;
                    n->missing_ok = FALSE;
                    n->objects = $4;
                    n->behavior = DROP_RESTRICT; //drop_restrict is the default drop behaviour
                    $$ = (Node *)n;
                }
              | DROP MODEL IF_P EXISTS any_name_list
                {
                    DropStmt *n = makeNode(DropStmt);
                    n->removeType = OBJECT_MODEL;
                    n->missing_ok = TRUE;
                    n->objects = $5;
                    $$ = (Node *)n;
                }
              | DROP MODEL any_name_list
                {
                    DropStmt *n = makeNode(DropStmt);
                    n->removeType = OBJECT_MODEL;
                    n->missing_ok = FALSE;
                    n->objects = $3;
                    $$ = (Node *)n;
                }
              | DROP Interface_or_address_drop IF_P EXISTS any_name_list opt_drop_behavior
                {
                    DropStmt *n = makeNode(DropStmt);
                    n->removeType = OBJECT_INTERFACE;
                    n->missing_ok = TRUE;
                    n->typeAlias = $2;
                    n->objects = $5;
                    n->behavior = $6;
                    $$ = (Node *) n;
                }
              | DROP Interface_or_address_drop any_name_list opt_drop_behavior
                {
                    DropStmt *n = makeNode(DropStmt);
                    n->removeType = OBJECT_INTERFACE;
                    n->missing_ok = FALSE;
                    n->typeAlias = $2;
                    n->objects = $3;
                    n->behavior = $4;
                    $$ = (Node *) n;
                }
        ;

drop_type:    TABLE                                 { $$ = OBJECT_TABLE; }
            | SEQUENCE                              { $$ = OBJECT_SEQUENCE; }
            | VIEW                                  { $$ = OBJECT_VIEW; }
            | TEXT INDEX                            { $$ = OBJECT_INDEX; }
            | INDEX                                 { $$ = OBJECT_INDEX; }
            | TYPE_P                                { $$ = OBJECT_TYPE; }
            | DOMAIN_P                              { $$ = OBJECT_DOMAIN; }
            | SCHEMA                                { $$ = OBJECT_SCHEMA; }
            | PROJECTION                            { $$ = OBJECT_PROJECTION; }
            | NODE                                  { $$ = OBJECT_NODE; }
            | PROFILE                               { $$ = OBJECT_PROFILE; }
            | ROLE                                  { $$ = OBJECT_ROLE; }
            | LIBRARY                               { $$ = OBJECT_LIBRARY; }
            | TUNING RULE                           { $$ = OBJECT_TUNINGRULE; }
            | SUBNET                                { $$ = OBJECT_SUBNET; }
            | LOAD BALANCE GROUP_P                  { $$ = OBJECT_LOADBALANCEGROUP; }
            | ROUTING RULE                          { $$ = OBJECT_ROUTINGRULE; }
            | FAULT GROUP_P                         { $$ = OBJECT_FAULTGROUP; }
            | AUTHENTICATION                        { $$ = OBJECT_AUTHENTICATION; }
            | NOTIFIER                              { $$ = OBJECT_NOTIFIER; }
            | BRANCH                                { $$ = OBJECT_BRANCH; }
        ;

any_name_list:
            any_name                                { $$ = list_make1($1); }
            | any_name_list ',' any_name            { $$ = lappend($1, $3); }
        ;

any_name:    ColId                        { $$ = list_make1(makeStr($1)); }
            | ColId attrs                { $$ = lcons(makeStr($1), $2); }
        ;

attrs:        '.' attr_name
                    { $$ = list_make1(makeStr($2)); }
            | attrs '.' attr_name
                    { $$ = lappend($1, makeStr($3)); }
        ;

Interface_or_address_drop:
            NETWORK INTERFACE               {$$ = DROP_TYPE_INTERFACE;}
          | NETWORK ADDRESS                 {$$ = DROP_TYPE_ADDRESS;}
          ;
/*****************************************************************************
 *
 *        QUERY:
 *                truncate table relname
 *
 *****************************************************************************/

TruncateStmt:
            TRUNCATE TABLE qualified_name
                {
                    TruncateStmt *n = makeNode(TruncateStmt);
                    n->relation = $3;
                    $$ = (Node *)n;
                }
        ;

/*****************************************************************************
 *
 *    The COMMENT ON statement can take different forms based upon the type of
 *    the object associated with the comment. The form of the statement is:
 *
 *    COMMENT ON [ [ DATABASE | DOMAIN | INDEX | SEQUENCE | TABLE | TYPE | VIEW |
 *                   LANGUAGE | OPERATOR CLASS | LARGE OBJECT |
 *                   CAST ] <objname> |
 *                 AGGREGATE <aggname> (<aggtype>) |
 *                 FUNCTION <funcname> (arg1, arg2, ...) |
 *                 OPERATOR <op> (leftoperand_typ, rightoperand_typ) |
 *                 TRIGGER <triggername> ON <relname> |
 *                 RULE <rulename> ON <relname> ]
 *               IS 'varchar'
 *
 *****************************************************************************/

CommentStmt:
            COMMENT ON comment_type any_name IS comment_text
                {
                    CommentStmt *n = makeNode(CommentStmt);
                    n->objtype = $3;
                    n->objname = $4;
                    n->objargs = NIL;
                    n->comment = $6.str;
                    $$ = (Node *) n;
                }
            | COMMENT ON FUNCTION func_name func_args IS comment_text
                {
                    CommentStmt *n = makeNode(CommentStmt);
                    n->objtype = OBJECT_FUNCTION;
                    n->objname = $4;
                    n->objargs = $5;
                    n->comment = $7.str;
                    $$ = (Node *) n;
                }
            | COMMENT ON udx_type FUNCTION func_name func_args IS comment_text
                {
                    CommentStmt *n = makeNode(CommentStmt);
                    n->objtype = $3;
                    n->objname = $5;
                    n->objargs = $6;
                    n->comment = $8.str;
                    $$ = (Node *) n;
                }
            | COMMENT ON OPERATOR any_operator '(' oper_argtypes ')'
            IS comment_text
                {
                    CommentStmt *n = makeNode(CommentStmt);
                    n->objtype = OBJECT_OPERATOR;
                    n->objname = $4;
                    n->objargs = $6;
                    n->comment = $9.str;
                    $$ = (Node *) n;
                }
            | COMMENT ON CONSTRAINT name ON any_name IS comment_text
                {
                    CommentStmt *n = makeNode(CommentStmt);
                    n->objtype = OBJECT_CONSTRAINT;
                    n->objname = lappend($6, makeStr($4));
                    n->objargs = NIL;
                    n->comment = $8.str;
                    $$ = (Node *) n;
                }
            | COMMENT ON RULE name ON any_name IS comment_text
                {
                    CommentStmt *n = makeNode(CommentStmt);
                    n->objtype = OBJECT_RULE;
                    n->objname = lappend($6, makeStr($4));
                    n->objargs = NIL;
                    n->comment = $8.str;
                    $$ = (Node *) n;
                }
            | COMMENT ON RULE name IS comment_text
                {
                    /* Obsolete syntax supported for awhile for compatibility */
                    CommentStmt *n = makeNode(CommentStmt);
                    n->objtype = OBJECT_RULE;
                    n->objname = list_make1(makeStr($4));
                    n->objargs = NIL;
                    n->comment = $6.str;
                    $$ = (Node *) n;
                }
            | COMMENT ON TRIGGER name ON any_name IS comment_text
                {
                    CommentStmt *n = makeNode(CommentStmt);
                    n->objtype = OBJECT_TRIGGER;
                    n->objname = lappend($6, makeStr($4));
                    n->objargs = NIL;
                    n->comment = $8.str;
                    $$ = (Node *) n;
                }
            | COMMENT ON OPERATOR CLASS any_name USING access_method IS comment_text
                {
                    CommentStmt *n = makeNode(CommentStmt);
                    n->objtype = OBJECT_OPCLASS;
                    n->objname = $5;
                    n->objargs = list_make1(makeStr($7));
                    n->comment = $9.str;
                    $$ = (Node *) n;
                }
            | COMMENT ON LARGE_P OBJECT_P NumericOnly IS comment_text
                {
                    CommentStmt *n = makeNode(CommentStmt);
                    n->objtype = OBJECT_LARGEOBJECT;
                    n->objname = list_make1($5);
                    n->objargs = NIL;
                    n->comment = $7.str;
                    $$ = (Node *) n;
                }
            | COMMENT ON CAST '(' Typename AS Typename ')' IS comment_text
                {
                    CommentStmt *n = makeNode(CommentStmt);
                    n->objtype = OBJECT_CAST;
                    n->objname = list_make1($5);
                    n->objargs = list_make1($7);
                    n->comment = $10.str;
                    $$ = (Node *) n;
                }
            | COMMENT ON opt_procedural LANGUAGE any_name IS comment_text
                {
                    CommentStmt *n = makeNode(CommentStmt);
                    n->objtype = OBJECT_LANGUAGE;
                    n->objname = $5;
                    n->objargs = NIL;
                    n->comment = $7.str;
                    $$ = (Node *) n;
                }
            | COMMENT ON LIBRARY func_name IS comment_text
                {
                    CommentStmt *n = makeNode(CommentStmt);
                    n->objtype = OBJECT_LIBRARY;
                    n->objname = $4;
                    n->objargs = NIL;
                    n->comment = $6.str;
                    $$ = (Node *) n;
                }
        ;

comment_type:
            COLUMN                                { $$ = OBJECT_COLUMN; }
            | DATABASE                            { $$ = OBJECT_DATABASE; }
            | SCHEMA                              { $$ = OBJECT_SCHEMA; }
            | INDEX                               { $$ = OBJECT_INDEX; }
            | SEQUENCE                            { $$ = OBJECT_SEQUENCE; }
            | TABLE                               { $$ = OBJECT_TABLE; }
            | DOMAIN_P                            { $$ = OBJECT_TYPE; }
            | TYPE_P                              { $$ = OBJECT_TYPE; }
            | VIEW                                { $$ = OBJECT_VIEW; }
            | PROJECTION                          { $$ = OBJECT_PROJECTION; }
            | NODE                                { $$ = OBJECT_NODE; }
        ;

udx_type:
            TRANSFORM                             { $$ = OBJECT_TRANSFORM; }
            | ANALYTIC                            { $$ = OBJECT_ANALYTIC; }
            | AGGREGATE                           { $$ = OBJECT_AGGREGATE; }
        ;


comment_text:
            Sconst                                { $$ = $1; }
            | NULL_P                              { $$ = ctNULL; }
        ;

/*****************************************************************************
 *
 *        QUERY:
 *            fetch/move
 *
 *****************************************************************************/

FetchStmt:    FETCH fetch_direction from_in name
                {
                    FetchStmt *n = (FetchStmt *) $2;
                    n->portalname = $4.str;
                    n->ismove = FALSE;
                    $$ = (Node *)n;
                }
            | FETCH name
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_FORWARD;
                    n->howMany = 1;
                    n->portalname = $2.str;
                    n->ismove = FALSE;
                    $$ = (Node *)n;
                }
            | MOVE fetch_direction from_in name
                {
                    FetchStmt *n = (FetchStmt *) $2;
                    n->portalname = $4.str;
                    n->ismove = TRUE;
                    $$ = (Node *)n;
                }
            | MOVE name
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_FORWARD;
                    n->howMany = 1;
                    n->portalname = $2.str;
                    n->ismove = TRUE;
                    $$ = (Node *)n;
                }
        ;

fetch_direction:
            /*EMPTY*/
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_FORWARD;
                    n->howMany = 1;
                    $$ = (Node *)n;
                }
            | NEXT
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_FORWARD;
                    n->howMany = 1;
                    $$ = (Node *)n;
                }
            | PRIOR
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_BACKWARD;
                    n->howMany = 1;
                    $$ = (Node *)n;
                }
            | FIRST_P
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_ABSOLUTE;
                    n->howMany = 1;
                    $$ = (Node *)n;
                }
            | LAST_P
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_ABSOLUTE;
                    n->howMany = -1;
                    $$ = (Node *)n;
                }
            | ABSOLUTE_P fetch_count
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_ABSOLUTE;
                    n->howMany = $2;
                    $$ = (Node *)n;
                }
            | RELATIVE_P fetch_count
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_RELATIVE;
                    n->howMany = $2;
                    $$ = (Node *)n;
                }
            | fetch_count
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_FORWARD;
                    n->howMany = $1;
                    $$ = (Node *)n;
                }
            | ALL
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_FORWARD;
                    n->howMany = FETCH_ALL;
                    $$ = (Node *)n;
                }
            | FORWARD
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_FORWARD;
                    n->howMany = 1;
                    $$ = (Node *)n;
                }
            | FORWARD fetch_count
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_FORWARD;
                    n->howMany = $2;
                    $$ = (Node *)n;
                }
            | FORWARD ALL
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_FORWARD;
                    n->howMany = FETCH_ALL;
                    $$ = (Node *)n;
                }
            | BACKWARD
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_BACKWARD;
                    n->howMany = 1;
                    $$ = (Node *)n;
                }
            | BACKWARD fetch_count
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_BACKWARD;
                    n->howMany = $2;
                    $$ = (Node *)n;
                }
            | BACKWARD ALL
                {
                    FetchStmt *n = makeNode(FetchStmt);
                    n->direction = FETCH_BACKWARD;
                    n->howMany = FETCH_ALL;
                    $$ = (Node *)n;
                }
        ;

fetch_count:
            Iconst                                    { $$ = $1; }
            | '-' Iconst                            { $$ = - $2; }
        ;

from_in:    FROM                                    {}
            | IN_P                                    {}
        ;


/*****************************************************************************
 *
 * GRANT and REVOKE statements
 *
 *****************************************************************************/

GrantStmt:  GRANT privileges_or_roles opt_on_target_clause TO grantee_list 
            opt_grant_grantadmin_option
            {
                GrantStmt *n = makeNode(GrantStmt);
                if($3 == NIL)
                {
                    n->is_grant = GRANT_ROLES;
                    n->roles = $2;
                }
                else
                {
                    n->is_grant = GRANT_PRIVILEGES;
                    n->privileges = $2;
                    n->objtype = ($3)->objtype;
                    n->objects = ($3)->objs;
                }
                n->grantees = $5;
                n->grant_option = false;
                n->admin_option = false;
                if(keywordCmp($6.str, "GRANT") == 0)
                    n->grant_option = true;
                if(keywordCmp($6.str, "ADMIN") == 0)
                    n->admin_option = true;
                $$ = (Node*)n;
            }
            | GRANT AUTHENTICATION auth_list TO grantee_list
            {
                GrantStmt *n = makeNode(GrantStmt);
                n->is_grant = GRANT_AUTH;
                n->auths = $3;
                n->grantees = $5;
                $$ = (Node*)n;
            }
        ;

RevokeStmt: REVOKE revoke_privileges_or_roles opt_on_target_clause // asymmetric from GrantStmt since ADMIN is not a reserved word
            FROM grantee_list opt_drop_behavior                    // but GRANT is
            {
                GrantStmt *n = makeNode(GrantStmt);
                n->grant_option = $2->grant_option;
                n->admin_option = $2->admin_option;
                if($3 == NIL)
                {
                    n->is_grant = REVOKE_ROLES;
                    n->roles = $2->roles;
                }
                else
                {
                    n->is_grant = REVOKE_PRIVILEGES;
                    n->privileges = $2->privileges;
                    n->objtype = ($3)->objtype;
                    n->objects = ($3)->objs;
                }
                n->grantees = $5;
                n->behavior = $6;
                $$ = (Node *)n;
            }
            | REVOKE AUTHENTICATION auth_list FROM grantee_list
            {
                GrantStmt *n = makeNode(GrantStmt);
                n->is_grant = REVOKE_AUTH;
                n->auths = $3;
                n->grantees = $5;
                $$ = (Node *)n;
            }
        ;

opt_on_target_clause: ON privilege_target { $$ = $2; }
                      | /*EMPTY*/ { $$ = NIL; }
                      ;

revoke_privileges_or_roles: privileges_or_roles
                              {
                                  GranteesWithOption *n = makeNode(GranteesWithOption);
                                  n->grant_option = false;
                                  n->admin_option = false;
                                  n->privileges = $1;
                                  n->roles = $1;
                                  $$ = n;
                              }
                            | GRANT OPTION FOR privileges_or_roles
                              {
                                  GranteesWithOption *n = makeNode(GranteesWithOption);
                                  n->grant_option = true;
                                  n->admin_option = false;
                                  n->privileges = $4;
                                  n->roles = NIL;
                                  $$ = n;
                              }
                            | ADMIN OPTION FOR privileges_or_roles
                              {
                                  GranteesWithOption *n = makeNode(GranteesWithOption);
                                  n->grant_option = false;
                                  n->admin_option = true;
                                  n->roles = $4;
                                  n->privileges = NIL;
                                  $$ = n;
                              }
        ;
/* either ALL [PRIVILEGES] or a list of individual privileges */
privileges_or_roles: privilege_or_role_list        { $$ = $1; }
                     | ALL                         { $$ = list_make1(makeString("ALL")); }
                     | ALL PRIVILEGES              { $$ = list_make1(makeString("ALL")); }
                     | ALL EXTEND             { $$ = list_make1(makeString("ALL EXTEND")); }
                     | ALL PRIVILEGES EXTEND  { $$ = list_make1(makeString("ALL EXTEND")); }
        ;

privilege_or_role_list:
        privilege_or_role                                { $$ = list_make1(makeStr($1)); }
        | privilege_or_role_list ',' privilege_or_role     { $$ = lappend($1, makeStr($3)); }
        ;

auth_list:
        name                              { $$ = list_make1(makeStr($1)); }
        | auth_list ',' name              { $$ = lappend($1, makeStr($3)); }
        ;

/* Not all of these privilege types apply to all objects, but that
 * gets sorted out later.
 */

// Hack to avoid making all privileges reserved words
privilege_or_role:    SELECT                                  { $$ = ctString(pstrdup($1)); }
                      | REFERENCES                            { $$ = ctString(pstrdup($1)); }
                      | CREATE                                { $$ = ctString(pstrdup($1)); }
                      | ColId                                 { $$ = $1; }
        ;


/* Don't bother trying to fold the first two rules into one using
   opt_table.  You're going to get conflicts. */
privilege_target:
            qualified_name_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_RELATION;
                    n->objs = $1;
                    $$ = n;
                }
            | TABLE qualified_name_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_RELATION;
                    n->objs = $2;
                    $$ = n;
                }
            | FUNCTION function_with_argtypes_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_FUNCTION;
                    n->objs = $2;
                    $$ = n;
                }
            | TRANSFORM FUNCTION function_with_argtypes_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_TRANSFORM;
                    n->objs = $3;
                    $$ = n;
                }
            | ANALYTIC FUNCTION function_with_argtypes_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_AN_FUNCTION;
                    n->objs = $3;
                    $$ = n;
                }
            | AGGREGATE FUNCTION function_with_argtypes_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_AGG_FUNCTION;
                    n->objs = $3;
                    $$ = n;
                }
            | SOURCE function_with_argtypes_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_SOURCE_FUNCTION;
                    n->objs = $2;
                    $$ = n;
                }
            | FILTER function_with_argtypes_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_FILTER_FUNCTION;
                    n->objs = $2;
                    $$ = n;
                }
            | PARSER function_with_argtypes_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_PARSER_FUNCTION;
                    n->objs = $2;
                    $$ = n;
                }
            | PROCEDURE proc_with_argtypes_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_PROC;
                    n->objs = $2;
                    $$ = n;
                }
            | DATABASE dbname_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_DATABASE;
                    n->objs = $2;
                    $$ = n;
                }
            | LANGUAGE name_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_LANGUAGE;
                    n->objs = $2;
                    $$ = n;
                }
            | SCHEMA qualified_schema_name_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_NAMESPACE;
                    n->objs = $2;
                    $$ = n;
                }
            | TABLESPACE name_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_TABLESPACE;
                    n->objs = $2;
                    $$ = n;
                }
            | SEQUENCE qualified_name_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_SEQUENCE;
                    n->objs = $2;
                    $$ = n;
                }
            | RESOURCE POOL name_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_RESOURCE_POOL;
                    n->objs = $3;
                    $$ = n;
                }
            | LIBRARY qualified_name_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_LIBRARY;
                    n->objs = $2;
                    $$ = n;
                }
            | LOCATION copy_file_list
                {
                    PrivTarget *n = makeNode(PrivTarget);
                    n->objtype = ACL_OBJECT_STORAGELOCATION;
                    n->objs = $2;
                    $$ = n;
                }
            | ALL TABLES IN_P SCHEMA qualified_schema_name_list
               {
                   PrivTarget *n = makeNode(PrivTarget);
                   n->objtype = ACL_OBJECT_ALL_RELATIONS;
                   n->objs = $5;
                   $$ = n;
               }
            | ALL FUNCTIONS IN_P SCHEMA qualified_schema_name_list
               {
                   PrivTarget *n = makeNode(PrivTarget);
                   n->objtype = ACL_OBJECT_ALL_FUNCTIONS;
                   n->objs = $5;
                   $$ = n;
               }
            | ALL SEQUENCES IN_P SCHEMA qualified_schema_name_list
               {
                   PrivTarget *n = makeNode(PrivTarget);
                   n->objtype = ACL_OBJECT_ALL_SEQUENCES;
                   n->objs = $5;
                   $$ = n;
               }
            | MODEL qualified_name_list
               {
                   PrivTarget *n = makeNode(PrivTarget);
                   n->objtype = ACL_OBJECT_MODEL;
                    n->objs = $2;
                    $$ = n;
               }
        ;


grantee_list:
            grantee                                    { $$ = list_make1($1); }
            | grantee_list ',' grantee                { $$ = lappend($1, $3); }
        ;

grantee:    ColId
                {
                    PrivGrantee *n = makeNode(PrivGrantee);
                    /* This hack lets us avoid reserving PUBLIC as a keyword*/
                    if (keywordCmp($1.str, "public") == 0)
                        n->username = NULL;
                    else
                        n->username = $1.str;
                    n->groupname = NULL;
                    $$ = (Node *)n;
                }
            | GROUP_P ColId
                {
                    PrivGrantee *n = makeNode(PrivGrantee);
                    /* Treat GROUP PUBLIC as a synonym for PUBLIC */
                    if (keywordCmp($2.str, "public") == 0)
                        n->groupname = NULL;
                    else
                        n->groupname = $2.str;
                    n->username = NULL;
                    $$ = (Node *)n;
                }
        ;

opt_grant_grantadmin_option:
            WITH GRANT OPTION { $$ = ctString("GRANT"); }
            | WITH ADMIN OPTION { $$ = ctString("ADMIN"); }
            | /*EMPTY*/ { $$ = ctString("Nil"); }
        ;

function_with_argtypes_list:
            function_with_argtypes                    { $$ = list_make1($1); }
            | function_with_argtypes_list ',' function_with_argtypes
                                                    { $$ = lappend($1, $3); }
        ;

function_with_argtypes:
            func_name func_args
                {
                    FuncWithArgs *n = makeNode(FuncWithArgs);
                    n->funcname = $1;
                    n->funcargs = $2;
                    $$ = (Node *)n;
                }
        ;

proc_with_argtypes_list:
            proc_with_argtypes                      { $$ = list_make1($1); }
            | proc_with_argtypes_list ',' proc_with_argtypes
                                                    { $$ = lappend($1, $3); }
        ;

proc_with_argtypes:
            func_name proc_args
                {
                    FuncWithArgs *n = makeNode(FuncWithArgs);
                    n->funcname = $1;
                    n->funcargs = $2;
                    $$ = (Node *)n;
                }
        ;

/*****************************************************************************
 *
 *        QUERY:
 *                create index <indexname> on <relname>
 *                  [ using <access> ] "(" ( <col> [ using <opclass> ] )+ ")"
 *                  [ tablespace <tablespacename> ] [ where <predicate> ]
 *
 * Note: we cannot put TABLESPACE clause after WHERE clause unless we are
 * willing to make TABLESPACE a fully reserved word.
 *****************************************************************************/

IndexStmt:    CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause tokenizer_clause tokenizer_args stemmer_clause stemmer_args
                {
                    IndexStmt *n = makeNode(IndexStmt);
                    n->unique = $2;
                    n->txtindex = $3;
                    n->idxname = $5;
                    n->relation = $7;
                    n->accessMethod = $8.str;
                    n->indexParams = $10;
                    n->tableSpace = $12.str;
                    n->whereClause = $13;
                    n->tokenizer_relation = $14;
                    n->tokenizer_args = $15;
                    n->stemmer_relation = $16;
                    n->stemmer_args = $17;
                    n->use_default_tokenizer = false;
                    n->use_default_stemmer = false;
                    $$ = (Node *)n;
                }
             | CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause stemmer_clause stemmer_args tokenizer_clause tokenizer_args
                {
                    IndexStmt *n = makeNode(IndexStmt);
                    n->unique = $2;
                    n->txtindex = $3;
                    n->idxname = $5;
                    n->relation = $7;
                    n->accessMethod = $8.str;
                    n->indexParams = $10;
                    n->tableSpace = $12.str;
                    n->whereClause = $13;
                    n->stemmer_relation = $14;
                    n->stemmer_args = $15;
                    n->tokenizer_relation = $16;
                    n->tokenizer_args = $17;
                    n->use_default_tokenizer = false;
                    n->use_default_stemmer = false;
                    $$ = (Node *)n;
                }
             | CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause tokenizer_clause tokenizer_args
                {
                    IndexStmt *n = makeNode(IndexStmt);
                    n->unique = $2;
                    n->txtindex = $3;
                    n->idxname = $5;
                    n->relation = $7;
                    n->accessMethod = $8.str;
                    n->indexParams = $10;
                    n->tableSpace = $12.str;
                    n->whereClause = $13;
                    n->tokenizer_relation = $14;
                    n->tokenizer_args = $15;
                    n->stemmer_relation = NULL;
                    n->stemmer_args = NULL;
                    n->use_default_tokenizer = false;
                    n->use_default_stemmer = true;
                    $$ = (Node *)n;
                }
             | CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause stemmer_clause stemmer_args
                {
                    IndexStmt *n = makeNode(IndexStmt);
                    n->unique = $2;
                    n->txtindex = $3;
                    n->idxname = $5;
                    n->relation = $7;
                    n->accessMethod = $8.str;
                    n->indexParams = $10;
                    n->tableSpace = $12.str;
                    n->whereClause = $13;
                    n->stemmer_relation = $14;
                    n->stemmer_args = $15;
                    n->tokenizer_relation = NULL;
                    n->tokenizer_args = NULL;
                    n->use_default_tokenizer = true;
                    n->use_default_stemmer = false;
                    $$ = (Node *)n;
                }
             | CREATE index_opt_unique index_opt_text INDEX index_name ON qualified_name access_method_clause '(' index_params ')' OptTableSpace where_clause
                {
                    IndexStmt *n = makeNode(IndexStmt);
                    n->unique = $2;
                    n->txtindex = $3;
                    n->idxname = $5;
                    n->relation = $7;
                    n->accessMethod = $8.str;
                    n->indexParams = $10;
                    n->tableSpace = $12.str;
                    n->whereClause = $13;
                    n->stemmer_relation = NULL;
                    n->stemmer_args = NULL;
                    n->tokenizer_relation = NULL;
                    n->tokenizer_args = NULL;
                    n->use_default_tokenizer = true;
                    n->use_default_stemmer = true;
                    $$ = (Node *)n;
                }
        ;
index_opt_unique:
            UNIQUE                                    { $$ = TRUE; }
            | /*EMPTY*/                                { $$ = FALSE; }
        ;

index_opt_text:
            TEXT                                    { $$ = TRUE; }
            | /*EMPTY*/                                { $$ = FALSE; }
        ;

access_method_clause:
            USING access_method            { $$ = $2; }
| /*EMPTY*/                                { $$ = ctNULL; }
        ;

tokenizer_clause:
            TOKENIZER udx_func_name         { $$ = $2; }
            | TOKENIZER NONE                { $$ = NULL; }
         ;

stemmer_clause:
            STEMMER udx_func_name           { $$ = $2; }
            | STEMMER NONE                  { $$ = NULL; }
         ;

tokenizer_args:
            func_args                       { $$ = $1; }
            | /*EMPTY*/                     { $$ = NULL; }
         ;

stemmer_args:
            func_args                       { $$ = $1; }
            | /*EMPTY*/                     { $$ = NULL; }
         ;

index_params:    index_elem                            { $$ = list_make1($1); }
            | index_params ',' index_elem            { $$ = lappend($1, $3); }
        ;

/*
 * Index attributes can be either simple column references, or arbitrary
 * expressions in parens.  For backwards-compatibility reasons, we allow
 * an expression that's just a function call to be written without parens.
 */
index_elem:    ColId opt_class
                {
                    $$ = makeNode(IndexElem);
                    $$->name = $1.str;
                    $$->expr = NULL;
                    $$->opclass = $2;
                }
        ;

opt_class:    any_name                                { $$ = $1; }
            | USING any_name                        { $$ = $2; }
            | /*EMPTY*/                                { $$ = NIL; }
        ;

/*****************************************************************************
 *
 *        QUERY:
 *                create [or replace] operator <fname>
 *                        [(<type-1> { , <type-n>})]
 *                        [return (<name-1> <type-1> { , <name-n> <type-n> })]
 *                        as language <lang> name <name> library <lib-name>
 *
 *
 * NOTE: This is used for UDT's, UDAn's, and UDL's because there is so much
 * overlap in what they need
 *****************************************************************************/

CreateUDXStmt:
            CREATE opt_or_replace TRANSFORM FUNCTION udx_func_name
            AS Opt_language NAME_P Sconst LIBRARY qualified_name
            createtransform_opt_list
                {
                    CreateUDXStmt *n = makeNode(CreateUDXStmt);
                    n->replace = $2;
                    n->funcname = $5;
                    n->language = $7;
                    n->implFuncName = $9.str;
                    n->libName = $11;
                    n->options = $12;
                    n->udxType = UD_TRANSFORM;
                    $$ = (Node *)n;
                }
          | CREATE opt_or_replace ANALYTIC FUNCTION udx_func_name
            AS Opt_language NAME_P Sconst LIBRARY qualified_name
            createtransform_opt_list
                {
                    CreateUDXStmt *n = makeNode(CreateUDXStmt);
                    n->replace = $2;
                    n->funcname = $5;
                    n->language = $7;
                    n->implFuncName = $9.str;
                    n->libName = $11;
                    n->options = $12;
                    n->udxType = UD_ANALYTIC;
                    $$ = (Node *)n;
                }
          | CREATE opt_or_replace SOURCE udx_func_name
            AS Opt_language NAME_P Sconst LIBRARY qualified_name
            createtransform_opt_list
                {
                    CreateUDXStmt *n = makeNode(CreateUDXStmt);
                    n->replace = $2;
                    n->funcname = $4;
                    n->language = $6;
                    n->implFuncName = $8.str;
                    n->libName = $10;
                    n->options = $11;
                    n->udxType = UD_SOURCE;
                    $$ = (Node *)n;
                }
          | CREATE opt_or_replace FILTER udx_func_name
            AS Opt_language NAME_P Sconst LIBRARY qualified_name
            createtransform_opt_list
                {
                    CreateUDXStmt *n = makeNode(CreateUDXStmt);
                    n->replace = $2;
                    n->funcname = $4;
                    n->language = $6;
                    n->implFuncName = $8.str;
                    n->libName = $10;
                    n->options = $11;
                    n->udxType = UD_FILTER;
                    $$ = (Node *)n;
                }
          | CREATE opt_or_replace UNPACKER udx_func_name
            AS Opt_language NAME_P Sconst LIBRARY qualified_name
            createtransform_opt_list
                {
                    CreateUDXStmt *n = makeNode(CreateUDXStmt);
                    n->replace = $2;
                    n->funcname = $4;
                    n->language = $6;
                    n->implFuncName = $8.str;
                    n->libName = $10;
                    n->options = $11;
                    n->udxType = UD_FILTER;
                    $$ = (Node *)n;
                }
          | CREATE opt_or_replace PARSER udx_func_name
            AS Opt_language NAME_P Sconst LIBRARY qualified_name
            createtransform_opt_list
                {
                    CreateUDXStmt *n = makeNode(CreateUDXStmt);
                    n->replace = $2;
                    n->funcname = $4;
                    n->language = $6;
                    n->implFuncName = $8.str;
                    n->libName = $10;
                    n->options = $11;
                    n->udxType = UD_PARSER;
                    $$ = (Node *)n;
                }
          | CREATE opt_or_replace AGGREGATE FUNCTION udx_func_name
            AS Opt_language NAME_P Sconst LIBRARY qualified_name
                {
                    CreateUDXStmt *n = makeNode(CreateUDXStmt);
                    n->replace = $2;
                    n->funcname = $5;
                    n->language = $7;
                    n->implFuncName = $9.str;
                    n->libName = $11;
                    n->udxType = UD_AGGREGATE;
                    $$ = (Node *)n;
                }
          | CREATE opt_or_replace TYPE_P udx_func_name
            definition
                {
                    CreateUDXStmt *n = makeNode(CreateUDXStmt);
                    n->replace = $2;
                    n->funcname = $4;
                    n->parameters = $5;
                    n->udxType = UD_TYPE;
                    $$ = (Node *)n;
                }
          | CREATE opt_or_replace FILESYSTEM udx_func_name
            AS Opt_language NAME_P Sconst LIBRARY qualified_name
            //createtransform_opt_list //jhu NOTE: no fenced mode
                {
                    CreateUDXStmt *n = makeNode(CreateUDXStmt);
                    n->replace = $2;
                    n->funcname = $4;
                    n->language = $6;
                    n->implFuncName = $8.str;
                    n->libName = $10;
                    n->udxType = UD_FILESYSTEM;
                    $$ = (Node *)n;
                }
        ;

createtransform_opt_list:
            createtransform_opt_list createtransform_opt_item { $$ = lappend($1, $2); }
            | /* EMPTY */                                     { $$ = NIL; }
        ;

createtransform_opt_item:
            FENCED
                {
                    $$ = makeDefElem("fenced", (Node *)makeInteger(TRUE));
                }
            | NOT FENCED
                {
                    $$ = makeDefElem("fenced", (Node *)makeInteger(FALSE));
                }
        ;

/*****************************************************************************
 *
 *        QUERY:
 *                create [or replace] function <fname>
 *                        [(<type-1> { , <type-n>})]
 *                        returns <type-r>
 *                        as <filename or code in language as appropriate>
 *                        language <lang> [with parameters]
 *
 *****************************************************************************/

CreateFunctionStmt:
            CREATE opt_or_replace FUNCTION udx_func_name func_args
            RETURN func_return AS BEGIN_P RETURN a_expr ';' END_P
                {
                    CreateFunctionStmt *n = makeNode(CreateFunctionStmt);
                    n->replace = $2;
                    n->funcname = $4;
                    n->parameters = $5;
                    n->returnType = $7;
                    n->sqlMacroDef = $11;
                    n->options = 0;
                    $$ = (Node *)n;
                }
          | CREATE opt_or_replace FUNCTION udx_func_name
            AS Opt_language NAME_P Sconst LIBRARY qualified_name
            createfunc_opt_list
                {
                    CreateFunctionStmt *n = makeNode(CreateFunctionStmt);
                    n->replace = $2;
                    n->funcname = $4;
                    n->parameters = 0;
                    n->returnType = 0;
                    n->sqlMacroDef = 0;
                    n->language = $6;
                    n->implFuncName = $8.str;
                    n->libName = $10;
                    n->options = $11;
                    $$ = (Node *)n;
                }

//CreateFunctionStmt:
//            CREATE opt_or_replace FUNCTION func_name func_args
//            RETURN func_return createfunc_opt_list opt_definition
//                {
//                    CreateFunctionStmt *n = makeNode(CreateFunctionStmt);
//                    n->replace = $2;
//                    n->funcname = $4;
//                    n->parameters = $5;
//                    n->returnType = $7;
//                    n->options = $8;
//                    n->withClause = $9;
//                    $$ = (Node *)n;
//                }
//        ;

		;

AlterFunctionStmt:
            ALTER FUNCTION func_name func_args SET SCHEMA qualified_schema_name
            {
                AlterFunctionStmt *n = makeNode(AlterFunctionStmt);
                n->subtype = AT_AlterSchema;
                n->funcname = $3;
                n->parameters = $4;
                n->name = $7.str;
                n->udxType = UD_FUNCTION;
                $$ = (Node *)n;
            }
            | ALTER FUNCTION func_name func_args OWNER TO UserId
            {
                AlterFunctionStmt *n = makeNode(AlterFunctionStmt);
                n->subtype = AT_AlterOwner;
                n->funcname = $3;
                n->parameters = $4;
                n->name = $7.str;
                n->udxType = UD_FUNCTION;
                $$ = (Node *)n;
            }
            |ALTER TRANSFORM FUNCTION func_name func_args SET SCHEMA qualified_schema_name
            {
                AlterFunctionStmt *n = makeNode(AlterFunctionStmt);
                n->subtype = AT_AlterSchema;
                n->funcname = $4;
                n->parameters = $5;
                n->name = $8.str;
                n->udxType = UD_TRANSFORM;
                $$ = (Node *)n;
            }
            | ALTER TRANSFORM FUNCTION func_name func_args OWNER TO UserId
            {
                AlterFunctionStmt *n = makeNode(AlterFunctionStmt);
                n->subtype = AT_AlterOwner;
                n->funcname = $4;
                n->parameters = $5;
                n->name = $8.str;
                n->udxType = UD_TRANSFORM;
                $$ = (Node *)n;
            }
            |ALTER AGGREGATE FUNCTION func_name func_args SET SCHEMA qualified_schema_name
            {
                AlterFunctionStmt *n = makeNode(AlterFunctionStmt);
                n->subtype = AT_AlterSchema;
                n->funcname = $4;
                n->parameters = $5;
                n->name = $8.str;
                n->udxType = UD_AGGREGATE;
                $$ = (Node *)n;
            }
            | ALTER AGGREGATE FUNCTION func_name func_args OWNER TO UserId
            {
                AlterFunctionStmt *n = makeNode(AlterFunctionStmt);
                n->subtype = AT_AlterOwner;
                n->funcname = $4;
                n->parameters = $5;
                n->name = $8.str;
                n->udxType = UD_AGGREGATE;
                $$ = (Node *)n;
            }
            |ALTER ANALYTIC FUNCTION func_name func_args SET SCHEMA qualified_schema_name
            {
                AlterFunctionStmt *n = makeNode(AlterFunctionStmt);
                n->subtype = AT_AlterSchema;
                n->funcname = $4;
                n->parameters = $5;
                n->name = $8.str;
                n->udxType = UD_ANALYTIC;
                $$ = (Node *)n;
            }
            | ALTER ANALYTIC FUNCTION func_name func_args OWNER TO UserId
            {
                AlterFunctionStmt *n = makeNode(AlterFunctionStmt);
                n->subtype = AT_AlterOwner;
                n->funcname = $4;
                n->parameters = $5;
                n->name = $8.str;
                n->udxType = UD_ANALYTIC;
                $$ = (Node *)n;
            }
            |ALTER SOURCE func_name func_args SET SCHEMA qualified_schema_name
            {
                AlterFunctionStmt *n = makeNode(AlterFunctionStmt);
                n->subtype = AT_AlterSchema;
                n->funcname = $3;
                n->parameters = $4;
                n->name = $7.str;
                n->udxType = UD_SOURCE;
                $$ = (Node *)n;
            }
            | ALTER SOURCE func_name func_args OWNER TO UserId
            {
                AlterFunctionStmt *n = makeNode(AlterFunctionStmt);
                n->subtype = AT_AlterOwner;
                n->funcname = $3;
                n->parameters = $4;
                n->name = $7.str;
                n->udxType = UD_SOURCE;
                $$ = (Node *)n;
            }
            |ALTER FILTER func_name func_args SET SCHEMA qualified_schema_name
            {
                AlterFunctionStmt *n = makeNode(AlterFunctionStmt);
                n->subtype = AT_AlterSchema;
                n->funcname = $3;
                n->parameters = $4;
                n->name = $7.str;
                n->udxType = UD_FILTER;
                $$ = (Node *)n;
            }
            | ALTER FILTER func_name func_args OWNER TO UserId
            {
                AlterFunctionStmt *n = makeNode(AlterFunctionStmt);
                n->subtype = AT_AlterOwner;
                n->funcname = $3;
                n->parameters = $4;
                n->name = $7.str;
                n->udxType = UD_FILTER;
                $$ = (Node *)n;
            }
            |ALTER PARSER func_name func_args SET SCHEMA qualified_schema_name
            {
                AlterFunctionStmt *n = makeNode(AlterFunctionStmt);
                n->subtype = AT_AlterSchema;
                n->funcname = $3;
                n->parameters = $4;
                n->name = $7.str;
                n->udxType = UD_PARSER;
                $$ = (Node *)n;
            }
            | ALTER PARSER func_name func_args OWNER TO UserId
            {
                AlterFunctionStmt *n = makeNode(AlterFunctionStmt);
                n->subtype = AT_AlterOwner;
                n->funcname = $3;
                n->parameters = $4;
                n->name = $7.str;
                n->udxType = UD_PARSER;
                $$ = (Node *)n;
            }
        ;

AlterUDxFenceStmt:
            ALTER FUNCTION func_name func_args SET FENCED fenced_property
                {
                    AlterUDxFenceStmt *n = makeNode(AlterUDxFenceStmt);
                    n->funcname = $3;
                    n->parameters = $4;
                    n->fenced = $7;
                    n->procType = PROC_UDF;
                    $$ = (Node *)n;
                }
          | ALTER TRANSFORM FUNCTION func_name func_args SET FENCED fenced_property
                {
                    AlterUDxFenceStmt *n = makeNode(AlterUDxFenceStmt);
                    n->funcname = $4;
                    n->parameters = $5;
                    n->fenced = $8;
                    n->procType = PROC_UDT;
                    $$ = (Node *)n;
                }
          | ALTER ANALYTIC FUNCTION func_name func_args SET FENCED fenced_property
                {
                    AlterUDxFenceStmt *n = makeNode(AlterUDxFenceStmt);
                    n->funcname = $4;
                    n->parameters = $5;
                    n->fenced = $8;
                    n->procType = PROC_UDAN;
                    $$ = (Node *)n;
                }
          | ALTER SOURCE func_name func_args SET FENCED fenced_property
                {
                    AlterUDxFenceStmt *n = makeNode(AlterUDxFenceStmt);
                    n->funcname = $3;
                    n->parameters = $4;
                    n->fenced = $7;
                    n->procType = PROC_SOURCE;
                    $$ = (Node *)n;
                }
          | ALTER FILTER func_name func_args SET FENCED fenced_property
                {
                    AlterUDxFenceStmt *n = makeNode(AlterUDxFenceStmt);
                    n->funcname = $3;
                    n->parameters = $4;
                    n->fenced = $7;
                    n->procType = PROC_FILTER;
                    $$ = (Node *)n;
                }
          | ALTER PARSER func_name func_args SET FENCED fenced_property
                {
                    AlterUDxFenceStmt *n = makeNode(AlterUDxFenceStmt);
                    n->funcname = $3;
                    n->parameters = $4;
                    n->fenced = $7;
                    n->procType = PROC_PARSER;
                    $$ = (Node *)n;
                }
        ;

fenced_property:
            TRUE_P { $$ = TRUE; }
            | FALSE_P { $$ = FALSE; }
        ;

opt_or_replace:
            OR REPLACE                                { $$ = TRUE; }
            | /*EMPTY*/                                { $$ = FALSE; }
        ;

func_args:    '(' func_args_list ')'                    { $$ = $2; }
            | '(' ')'                                { $$ = NIL; }
        ;

func_args_list:
            func_arg                                { $$ = list_make1($1); }
            | func_args_list ',' func_arg            { $$ = lappend($1, $3); }
        ;

/* We can catch over-specified arguments here if we want to,
 * but for now better to silently swallow typmod, etc.
 * - thomas 2000-03-22
 */
func_arg:
            arg_class param_name func_type
                {
                    FunctionParameter *n = makeNode(FunctionParameter);
                    n->name = $2.str;
                    n->argType = $3;
                    $$ = n;
                }
            | arg_class func_type
                {
                    FunctionParameter *n = makeNode(FunctionParameter);
                    n->name = NULL;
                    n->argType = $2;
                    $$ = n;
                }
        ;

arg_class:    IN_P                                    { $$ = FALSE; }
            | OUT_P
                {
                    ereport(ERROR,
                            (errcode(ERRCODE_FEATURE_NOT_SUPPORTED),
                             errmsg("CREATE FUNCTION / OUT parameters are not supported")));
                    $$ = TRUE;
                }
            | INOUT
                {
                    ereport(ERROR,
                            (errcode(ERRCODE_FEATURE_NOT_SUPPORTED),
                             errmsg("CREATE FUNCTION / INOUT parameters are not supported")));
                    $$ = FALSE;
                }
            | /*EMPTY*/                                { $$ = FALSE; }
        ;

/*
 * Ideally param_name should be ColId, but that causes too many conflicts.
 */
param_name:    function_name
        ;

func_return:
            func_type
                {
                    /* We can catch over-specified arguments here if we want to,
                     * but for now better to silently swallow typmod, etc.
                     * - thomas 2000-03-22
                     */
                    $$ = $1;
                }
        ;

/*
 * We would like to make the second production here be ColId attrs etc,
 * but that causes reduce/reduce conflicts.  type_name is next best choice.
 */
func_type:    Typename                                { $$ = $1; }
            | type_name attrs '%' TYPE_P
                {
                    $$ = makeNode(TypeName);
                    $$->names = lcons(makeStr($1), $2);
                    $$->pct_type = true;
                    $$->typmod = -1;
                }
        ;


createfunc_opt_list:
            /* Must be at least one to prevent conflict */
            createfunc_opt_list createfunc_opt_item { $$ = lappend($1, $2); }
            | /* EMPTY */                           { $$ = NIL; }
    ;

createfunc_opt_item:
            FENCED
                {
                    $$ = makeDefElem("fenced", (Node *)makeInteger(TRUE));
                }
            | NOT FENCED
                {
                    $$ = makeDefElem("fenced", (Node *)makeInteger(FALSE));
                }
        ;
//            | EXTERNAL SECURITY DEFINER
//                {
//                    $$ = makeDefElem("security", (Node *)makeInteger(TRUE));
//                }
//            | EXTERNAL SECURITY INVOKER
//                {
//                    $$ = makeDefElem("security", (Node *)makeInteger(FALSE));
//                }
//            | SECURITY DEFINER
//                {
//                    $$ = makeDefElem("security", (Node *)makeInteger(TRUE));
//                }
//            | SECURITY INVOKER
//                {
//                    $$ = makeDefElem("security", (Node *)makeInteger(FALSE));
//                }
//        ;

//func_as:    Sconst                        { $$ = list_make1(makeStr($1)); }
//            | Sconst ',' Sconst
//                {
//                    $$ = list_make2(makeStr($1), makeStr($3));
//                }
//        ;
//
//opt_definition:
//            WITH definition                            { $$ = $2; }
//            | /*EMPTY*/                                { $$ = NIL; }
//        ;

/*****************************************************************************
 *
 *        QUERY:
 *                create library <lib_name>
 *                        as <file_name>
 *                        depends <dependencies>
 *                        language <lang> ;
 *
 *****************************************************************************/
CreateLibraryStmt:
            CREATE opt_or_replace LIBRARY qualified_name AS Sconst Opt_depends Opt_language
                {
                    CreateAlterLibraryStmt *n = makeNode(CreateAlterLibraryStmt);
                    n->replace = $2;
                    n->libName = $4;
                    n->libFileName = $6.str;
                    n->depends = $7;
                    n->libLang = $8;
                    n->alter = false;
                    $$ = (Node*)n;
                }
        ;
Opt_depends:
            DEPENDS Sconst              { $$ = $2.str;}
            | /*empty,*/                { $$ = NULL;}
        ;

Opt_language:
            LANGUAGE Sconst             { $$ = $2.str;}
            | /*empty,*/                { $$ = NULL;}
        ;

/*****************************************************************************
 *
 *        QUERY: alter library <lib_name> as <file_name> depends <dependencies>;
 *
 *****************************************************************************/
AlterLibraryStmt:
            ALTER LIBRARY qualified_name AS Sconst Opt_depends
                {
                    CreateAlterLibraryStmt *n = makeNode(CreateAlterLibraryStmt);
                    n->replace = true;
                    n->libName = $3;
                    n->libFileName = $5.str;
                    n->depends = $6;
                    n->libLang = NULL;
                    n->alter = true;
                    $$ = (Node*)n;
                }
        ;



/*****************************************************************************
 *
 *        QUERY:
 *                create procedure <proc_name>
 *                        [(<type-1> { , <type-n>})]
 *                        as <program path> on <node>
 *                        user <user name>
 *                        language <lang>
 *
 *****************************************************************************/

CreateProcStmt:
            CREATE PROCEDURE func_name proc_args createproc_opt_list
                {
                    CreateProcStmt* n = makeNode(CreateProcStmt);
                    n->procName = $3;
                    n->parameters = $4;
                    n->options = $5;
                    $$ = (Node*)n;
                }
        ;

proc_args: '(' proc_args_list ')'                    { $$ = $2; }
            | '(' ')'                                { $$ = NIL; }
        ;

proc_args_list:
            proc_arg                                 { $$ = list_make1($1); }
            | proc_args_list ',' proc_arg            { $$ = lappend($1, $3); }
        ;

proc_arg:
            proc_param_name proc_type
                {
                    FunctionParameter* n = makeNode(FunctionParameter);
                    n->name = $1.str;
                    n->argType = $2;
                    $$ = n;
                }
            | proc_type
                {
                    FunctionParameter* n = makeNode(FunctionParameter);
                    n->name = NULL;
                    n->argType = $1;
                    $$ = n;
                }
        ;

/*
 * Ideally param_name should be ColId, but that causes too many conflicts.
 */
proc_param_name:    function_name
        ;

proc_type:    Typename                                { $$ = $1; }
        ;


createproc_opt_list:
            /* Must be at least one to prevent conflict */
            createproc_opt_item                     { $$ = list_make1($1); }
            | createproc_opt_list createproc_opt_item { $$ = lappend($1, $2); }
    ;

createproc_opt_item:
            AS Sconst
                {
                    $$ = makeDefElem("as", (Node*)makeStr($2));
                }
            | ON Sconst
                {
                    $$ = makeDefElem("on", (Node*)makeStr($2));
                }

            | LANGUAGE ColId_or_Sconst
                {
                    $$ = makeDefElem("language", (Node*)makeStr($2));
                }

            | USER Sconst
                {
                    $$ = makeDefElem("user", (Node*)makeStr($2));
                }
        ;


/*****************************************************************************
 *
 *        QUERY:
 *
 *        DROP FUNCTION funcname (arg1, arg2, ...) [ RESTRICT | CASCADE ]
 *        DROP AGGREGATE aggname (aggtype) [ RESTRICT | CASCADE ]
 *        DROP OPERATOR opname (leftoperand_typ, rightoperand_typ) [ RESTRICT | CASCADE ]
 *
 *****************************************************************************/

RemoveFuncStmt:
            DROP FUNCTION IF_P EXISTS func_name func_args opt_drop_behavior
                {
                    DropProcStmt *n = makeNode(DropProcStmt);
                    n->procName = $5;
                    n->parameters = $6;
                    n->behavior = $7;
                    n->missing_ok = TRUE;
                    n->procType = PROC_UDF;
                    $$ = (Node *)n;
                }
            | DROP FUNCTION func_name func_args opt_drop_behavior
                {
                    DropProcStmt *n = makeNode(DropProcStmt);
                    n->procName = $3;
                    n->parameters = $4;
                    n->behavior = $5;
                    n->missing_ok = FALSE;
                    n->procType = PROC_UDF;
                    $$ = (Node *)n;
                }
        ;

RemoveProcStmt:
            DROP PROCEDURE IF_P EXISTS func_name proc_args opt_drop_behavior
                {
                    DropProcStmt *n = makeNode(DropProcStmt);
                    n->procName = $5;
                    n->parameters = $6;
                    n->behavior = $7;
                    n->missing_ok = TRUE;
                    n->procType = PROC_SP;
                    $$ = (Node *)n;
                }
            | DROP PROCEDURE func_name proc_args opt_drop_behavior
                {
                    DropProcStmt *n = makeNode(DropProcStmt);
                    n->procName = $3;
                    n->parameters = $4;
                    n->behavior = $5;
                    n->missing_ok = FALSE;
                    n->procType = PROC_SP;
                    $$ = (Node *)n;
                }
        ;

RemoveUDXStmt:
            DROP TRANSFORM FUNCTION IF_P EXISTS func_name func_args opt_drop_behavior
                {
                    DropProcStmt *n = makeNode(DropProcStmt);
                    n->procName = $6;
                    n->parameters = $7;
                    n->behavior = $8; /* used for text index dependencies*/
                    n->missing_ok = TRUE;
                    n->procType = PROC_UDT;
                    $$ = (Node *)n;
                }
            | DROP TRANSFORM FUNCTION func_name func_args opt_drop_behavior
                {
                    DropProcStmt *n = makeNode(DropProcStmt);
                    n->procName = $4;
                    n->parameters = $5;
                    n->behavior = $6; /* used for text index dependencies*/
                    n->missing_ok = FALSE;
                    n->procType = PROC_UDT;
                    $$ = (Node *)n;
                }
            | DROP ANALYTIC FUNCTION IF_P EXISTS func_name func_args
                {
                    DropProcStmt *n = makeNode(DropProcStmt);
                    n->procName = $6;
                    n->parameters = $7;
                    n->behavior = DROP_CASCADE; /* doesn't matter, no code to do cascade*/
                    n->missing_ok = TRUE;
                    n->procType = PROC_UDAN;
                    $$ = (Node *)n;
                }
            | DROP ANALYTIC FUNCTION func_name func_args
                {
                    DropProcStmt *n = makeNode(DropProcStmt);
                    n->procName = $4;
                    n->parameters = $5;
                    n->behavior = DROP_CASCADE; /* doesn't matter, no code to do cascade*/
                    n->missing_ok = FALSE;
                    n->procType = PROC_UDAN;
                    $$ = (Node *)n;
                }
            | DROP AGGREGATE FUNCTION IF_P EXISTS func_name func_args
                {
                    DropProcStmt *n = makeNode(DropProcStmt);
                    n->procName = $6;
                    n->parameters = $7;
                    n->behavior = DROP_CASCADE; /* doesn't matter, no code to do cascade*/
                    n->missing_ok = TRUE;
                    n->procType = PROC_UDAGG;
                    $$ = (Node *)n;
                }
            | DROP AGGREGATE FUNCTION func_name func_args
                {
                    DropProcStmt *n = makeNode(DropProcStmt);
                    n->procName = $4;
                    n->parameters = $5;
                    n->behavior = DROP_CASCADE; /* doesn't matter, no code to do cascade*/
                    n->missing_ok = FALSE;
                    n->procType = PROC_UDAGG;
                    $$ = (Node *)n;
                }
            | DROP PARSER func_name func_args
                {
                    DropProcStmt *n = makeNode(DropProcStmt);
                    n->procName = $3;
                    n->parameters = $4;
                    n->behavior = DROP_CASCADE; /* doesn't matter, no code to do cascade*/
                    n->missing_ok = FALSE;
                    n->procType = PROC_PARSER;
                    $$ = (Node *)n;
                }
            | DROP FILTER func_name func_args
                {
                    DropProcStmt *n = makeNode(DropProcStmt);
                    n->procName = $3;
                    n->parameters = $4;
                    n->behavior = DROP_CASCADE; /* doesn't matter, no code to do cascade*/
                    n->missing_ok = FALSE;
                    n->procType = PROC_FILTER;
                    $$ = (Node *)n;
                }
            | DROP UNPACKER func_name func_args
                {
                    DropProcStmt *n = makeNode(DropProcStmt);
                    n->procName = $3;
                    n->parameters = $4;
                    n->behavior = DROP_CASCADE; /* doesn't matter, no code to do cascade*/
                    n->missing_ok = FALSE;
                    n->procType = PROC_FILTER;
                    $$ = (Node *)n;
                }
            | DROP SOURCE func_name func_args
                {
                    DropProcStmt *n = makeNode(DropProcStmt);
                    n->procName = $3;
                    n->parameters = $4;
                    n->behavior = DROP_CASCADE; /* doesn't matter, no code to do cascade*/
                    n->missing_ok = FALSE;
                    n->procType = PROC_SOURCE;
                    $$ = (Node *)n;
                }
        ;

RemoveAggrStmt:
            DROP AGGREGATE func_name '(' aggr_argtype ')' opt_drop_behavior
                {
                        RemoveAggrStmt *n = makeNode(RemoveAggrStmt);
                        n->aggname = $3;
                        n->aggtype = $5;
                        n->behavior = $7;
                        $$ = (Node *)n;
                }
        ;

aggr_argtype:
            Typename                                { $$ = $1; }
            | '*'                                    { $$ = NULL; }
        ;

RemoveOperStmt:
            DROP OPERATOR any_operator '(' oper_argtypes ')' opt_drop_behavior
                {
                    RemoveOperStmt *n = makeNode(RemoveOperStmt);
                    n->opname = $3;
                    n->args = $5;
                    n->behavior = $7;
                    $$ = (Node *)n;
                }
        ;

oper_argtypes:
            Typename
                {
                   ereport(ERROR,
                           (errcode(ERRCODE_SYNTAX_ERROR),
                            errmsg("Missing argument"),
                            errhint("Use NONE to denote the missing argument of a unary operator")));
                }
            | Typename ',' Typename
                    { $$ = list_make2($1, $3); }
            | NONE ',' Typename /* left unary */
                    { $$ = list_make2(NULL, $3); }
            | Typename ',' NONE /* right unary */
                    { $$ = list_make2($1, NULL); }
        ;

any_operator:
            all_Op
                    { $$ = list_make1(makeStr($1)); }
            | ColId '.' any_operator
                    { $$ = lcons(makeStr($1), $3); }
        ;


/*****************************************************************************
 *
 *        CREATE CAST / DROP CAST
 *
 *****************************************************************************/

CreateCastStmt: CREATE CAST '(' Typename AS Typename ')'
                    WITH FUNCTION function_with_argtypes cast_context
                {
                    CreateCastStmt *n = makeNode(CreateCastStmt);
                    n->sourcetype = $4;
                    n->targettype = $6;
                    n->func = (FuncWithArgs *) $10;
                    n->context = (CoercionContext) $11;
                    $$ = (Node *)n;
                }
            | CREATE CAST '(' Typename AS Typename ')'
                    WITHOUT FUNCTION cast_context
                {
                    CreateCastStmt *n = makeNode(CreateCastStmt);
                    n->sourcetype = $4;
                    n->targettype = $6;
                    n->func = NULL;
                    n->context = (CoercionContext) $10;
                    $$ = (Node *)n;
                }
        ;

cast_context:  AS IMPLICIT_P                    { $$ = COERCION_IMPLICIT; }
        | AS ASSIGNMENT                            { $$ = COERCION_ASSIGNMENT; }
        | /*EMPTY*/                                { $$ = COERCION_EXPLICIT; }
        ;


DropCastStmt: DROP CAST '(' Typename AS Typename ')' opt_drop_behavior
                {
                    DropCastStmt *n = makeNode(DropCastStmt);
                    n->sourcetype = $4;
                    n->targettype = $6;
                    n->behavior = $8;
                    $$ = (Node *)n;
                }
        ;



/*****************************************************************************
 *
 *        QUERY:
 *
 *        REINDEX type <typename> [FORCE] [ALL]
 *
 *****************************************************************************/

ReindexStmt:
            REINDEX reindex_type qualified_name opt_force
                {
                    ReindexStmt *n = makeNode(ReindexStmt);
                    n->kind = $2;
                    n->relation = $3;
                    n->name = NULL;
                    n->force = $4;
                    $$ = (Node *)n;
                }
            | REINDEX DATABASE name opt_force
                {
                    ReindexStmt *n = makeNode(ReindexStmt);
                    n->kind = OBJECT_DATABASE;
                    n->name = $3.str;
                    n->relation = NULL;
                    n->force = $4;
                    $$ = (Node *)n;
                }
        ;

reindex_type:
            INDEX                                    { $$ = OBJECT_INDEX; }
            | TABLE                                    { $$ = OBJECT_TABLE; }
        ;

opt_force:    FORCE                                    {  $$ = TRUE; }
            | /* EMPTY */                            {  $$ = FALSE; }
        ;

/*****************************************************************************
 *
 * ALTER THING name RENAME TO newname
 *
 *****************************************************************************/

RenameStmt: ALTER AGGREGATE func_name '(' aggr_argtype ')' RENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_AGGREGATE;
                    n->object = $3;
                    n->objarg = list_make1($5);
                    n->newname = $9.str;
                    $$ = (Node *)n;
                }
            | ALTER DATABASE database_name RENAME TO database_name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_DATABASE;
                    n->subname = $3.str;
                    n->newname = $6.str;
                    $$ = (Node *)n;
                }
            | ALTER FUNCTION func_name func_args RENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_FUNCTION;
                    n->object = $3;
                    n->objarg = $4;
                    n->newname = $7.str;
                    $$ = (Node *)n;
                }
            | ALTER GROUP_P UserId RENAME TO UserId
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_GROUP;
                    n->subname = $3.str;
                    n->newname = $6.str;
                    $$ = (Node *)n;
                }
            | ALTER LANGUAGE name RENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_LANGUAGE;
                    n->subname = $3.str;
                    n->newname = $6.str;
                    $$ = (Node *)n;
                }
            | ALTER OPERATOR CLASS any_name USING access_method RENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_OPCLASS;
                    n->object = $4;
                    n->subname = $6.str;
                    n->newname = $9.str;
                    $$ = (Node *)n;
                }
            | ALTER SCHEMA qualified_schema_name_list RENAME TO name_list
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_SCHEMA;
                    n->oldnames = $3;
                    n->newnames = $6;
                    $$ = (Node *)n;
                }
            | ALTER TABLE qualified_name_list ',' qualified_name RENAME TO name_list
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_TABLE;
                    n->oldnames = lappend($3, $5);
                    n->newnames = $8;
                    $$ = (Node *)n;
                }
            /* This rule exists to avoid a reduce conflict */
            | ALTER TABLE relation_expr RENAME TO name_list
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_TABLE;
                    n->oldnames = list_make1($3);
                    n->newnames = $6;
                    $$ = (Node *)n;
                }
            | ALTER VIEW qualified_name_list RENAME TO name_list
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_VIEW;
                    n->oldnames = $3;
                    n->newnames = $6;
                    $$ = (Node *)n;
                }
            | ALTER TABLE relation_expr RENAME opt_column name TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_COLUMN;
                    n->relation = $3;
                    n->subname = $6.str;
                    n->newname = $8.str;
                    $$ = (Node *)n;
                }
            | ALTER TABLE relation_expr RENAME CONSTRAINT name TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_CONSTRAINT;
                    n->relation = $3;
                    n->subname = $6.str;
                    n->newname = $8.str;
                    $$ = (Node *)n;
                }
            | ALTER INDEX relation_expr RENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_INDEX;
                    n->relation = $3;
                    n->subname = NULL;
                    n->newname = $6.str;
                    $$ = (Node *)n;
                }
            | ALTER MODEL relation_expr RENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_MODEL;
                    n->relation = $3;
                    n->subname = NULL;
                    n->newname = $6.str;
                    $$ = (Node *)n;
                }
            | ALTER TRIGGER name ON relation_expr RENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->relation = $5;
                    n->subname = $3.str;
                    n->newname = $8.str;
                    n->renameType = OBJECT_TRIGGER;
                    $$ = (Node *)n;
                }
            | ALTER USER UserId RENAME TO UserId
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_USER;
                    n->subname = $3.str;
                    n->newname = $6.str;
                    $$ = (Node *)n;
                }
            | ALTER ROLE UserId RENAME TO UserId
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_ROLE;
                    n->subname = $3.str;
                    n->newname = $6.str;
                    $$ = (Node *)n;
                }
            | ALTER TABLESPACE name RENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_TABLESPACE;
                    n->subname = $3.str;
                    n->newname = $6.str;
                    $$ = (Node *)n;
                }
            | ALTER PROJECTION qualified_name RENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_PROJECTION;
                    n->relation = $3;
                    n->newname = $6.str;
                    $$ = (Node *)n;
                }
            | ALTER PROJECTION qualified_name SET BASENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_PROJECTION;
                    n->relation = $3;
                    n->newbasename = $7.str;
                    $$ = (Node *)n;
                }
            | ALTER SEQUENCE qualified_name RENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_SEQUENCE;
                    n->relation = $3;
                    n->newname = $6.str;
                    $$ = (Node *)n;
                }
            | ALTER PROFILE qualified_name RENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_PROFILE;
                    n->relation = $3;
                    n->newname = $6.str;
                    $$ = (Node *)n;
                }
            | ALTER SUBNET qualified_name RENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_SUBNET;
                    n->relation = $3;
                    n->newname = $6.str;
                    $$ = (Node *)n;
                }
            | ALTER NETWORK INTERFACE qualified_name RENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_INTERFACE;
                    n->relation = $4;
                    n->newname = $7.str;
                    $$ = (Node *)n;
                }
            | ALTER AUTHENTICATION qualified_name RENAME TO name
                {
                    RenameStmt *n = makeNode(RenameStmt);
                    n->renameType = OBJECT_AUTHENTICATION;
                    n->relation = $3;
                    n->newname = $6.str;
                    $$ = (Node *)n;
                }

       ;

opt_column: COLUMN                                    { $$ = COLUMN; }
            | /*EMPTY*/                                { $$ = 0; }
        ;


/*****************************************************************************
 *
 *        QUERY:    Define Rewrite Rule
 *
 *****************************************************************************/

RuleStmt:    CREATE opt_or_replace RULE name AS
            { QueryIsRule=TRUE; }
            ON event TO qualified_name where_clause
            DO opt_instead RuleActionList
                {
                    RuleStmt *n = makeNode(RuleStmt);
                    n->replace = $2;
                    n->relation = $10;
                    n->rulename = $4.str;
                    n->whereClause = $11;
                    n->event = $8;
                    n->instead = $13;
                    n->actions = $14;
                    $$ = (Node *)n;
                    QueryIsRule=FALSE;
                }
        ;

RuleActionList:
            NOTHING                                    { $$ = NIL; }
            | RuleActionStmt                        { $$ = list_make1($1); }
            | '(' RuleActionMulti ')'                { $$ = $2; }
        ;

/* the thrashing around here is to discard "empty" statements... */
RuleActionMulti:
            RuleActionMulti ';' RuleActionStmtOrEmpty
                { if ($3 != NULL)
                    $$ = lappend($1, $3);
                  else
                    $$ = $1;
                }
            | RuleActionStmtOrEmpty
                { if ($1 != NULL)
                    $$ = list_make1($1);
                  else
                    $$ = NIL;
                }
        ;

RuleActionStmt:
            SelectStmt
            | InsertStmt
            | UpdateStmt
            | DeleteStmt
            | NotifyStmt
            | ExportStmt
            | VMergeStmt
        ;

RuleActionStmtOrEmpty:
            RuleActionStmt                            { $$ = $1; }
            |    /*EMPTY*/                            { $$ = NULL; }
        ;

/* change me to select, update, etc. some day */
event:        SELECT                                    { $$ = CMD_SELECT; }
            | UPDATE                                { $$ = CMD_UPDATE; }
            | DELETE_P                                { $$ = CMD_DELETE; }
            | INSERT                                { $$ = CMD_INSERT; }
         ;

opt_instead:
            INSTEAD                                    { $$ = TRUE; }
            | ALSO                                    { $$ = FALSE; }
            | /*EMPTY*/                                { $$ = FALSE; }
        ;


DropRuleStmt:
            DROP RULE name ON qualified_name opt_drop_behavior
                {
                    DropPropertyStmt *n = makeNode(DropPropertyStmt);
                    n->relation = $5;
                    n->property = $3.str;
                    n->behavior = $6;
                    n->removeType = OBJECT_RULE;
                    $$ = (Node *) n;
                }
        ;


/*****************************************************************************
 *
 *        QUERY:
 *                NOTIFY <qualified_name> can appear both in rule bodies and
 *                as a query-level command
 *
 *****************************************************************************/

NotifyStmt: NOTIFY qualified_name
                {
                    NotifyStmt *n = makeNode(NotifyStmt);
                    n->relation = $2;
                    $$ = (Node *)n;
                }
        ;

ListenStmt: LISTEN qualified_name
                {
                    ListenStmt *n = makeNode(ListenStmt);
                    n->relation = $2;
                    $$ = (Node *)n;
                }
        ;

UnlistenStmt:
            UNLISTEN qualified_name
                {
                    UnlistenStmt *n = makeNode(UnlistenStmt);
                    n->relation = $2;
                    $$ = (Node *)n;
                }
            | UNLISTEN '*'
                {
                    UnlistenStmt *n = makeNode(UnlistenStmt);
                    n->relation = makeNode(RangeVar);
                    n->relation->relname = "*";
                    n->relation->schemaname = NULL;
                    $$ = (Node *)n;
                }
        ;


/*****************************************************************************
 *
 *        Transactions:
 *
 *        BEGIN / COMMIT / ROLLBACK / SAVEPOINT / RELEASE
 *
 *****************************************************************************/

TransactionStmt:
            ABORT_P opt_transaction
                {
                    TransactionStmt *n = makeNode(TransactionStmt);
                    n->kind = TRANS_STMT_ROLLBACK;
                    n->options = NIL;
                    $$ = (Node *)n;
                }
            | BEGIN_P opt_transaction transaction_mode_list_or_empty
                {
                    TransactionStmt *n = makeNode(TransactionStmt);
                    n->kind = TRANS_STMT_BEGIN;
                    n->options = $3;
                    $$ = (Node *)n;
                }
            | START TRANSACTION transaction_mode_list_or_empty
                {
                    TransactionStmt *n = makeNode(TransactionStmt);
                    n->kind = TRANS_STMT_START;
                    n->options = $3;
                    $$ = (Node *)n;
                }
            | COMMIT opt_transaction opt_durable
                {
                    TransactionStmt *n = makeNode(TransactionStmt);
                    n->kind = TRANS_STMT_COMMIT;
                    n->options = $3;
                    $$ = (Node *)n;
                }
            | END_P opt_transaction
                {
                    TransactionStmt *n = makeNode(TransactionStmt);
                    n->kind = TRANS_STMT_COMMIT;
                    n->options = NIL;
                    $$ = (Node *)n;
                }
            | ROLLBACK_P opt_transaction
                {
                    TransactionStmt *n = makeNode(TransactionStmt);
                    n->kind = TRANS_STMT_ROLLBACK;
                    n->options = NIL;
                    $$ = (Node *)n;
                }
            | SAVEPOINT ColId
                {
                    TransactionStmt *n = makeNode(TransactionStmt);
                    n->kind = TRANS_STMT_SAVEPOINT;
                    n->options = list_make1(makeDefElem("savepoint_name",
                                                        (Node *)makeStringConst($2,NULL)));
                    $$ = (Node *)n;
                }
            | RELEASE SAVEPOINT ColId
                {
                    TransactionStmt *n = makeNode(TransactionStmt);
                    n->kind = TRANS_STMT_RELEASE;
                    n->options = list_make1(makeDefElem("savepoint_name",
                                                        (Node *)makeStringConst($3,NULL)));
                    $$ = (Node *)n;
                }
            | RELEASE ColId
                {
                    TransactionStmt *n = makeNode(TransactionStmt);
                    n->kind = TRANS_STMT_RELEASE;
                    n->options = list_make1(makeDefElem("savepoint_name",
                                                        (Node *)makeStringConst($2,NULL)));
                    $$ = (Node *)n;
                }
            | ROLLBACK_P opt_transaction TO SAVEPOINT ColId
                {
                    TransactionStmt *n = makeNode(TransactionStmt);
                    n->kind = TRANS_STMT_ROLLBACK_TO;
                    n->options = list_make1(makeDefElem("savepoint_name",
                                                        (Node *)makeStringConst($5,NULL)));
                    $$ = (Node *)n;
                }
            | ROLLBACK_P opt_transaction TO ColId
                {
                    TransactionStmt *n = makeNode(TransactionStmt);
                    n->kind = TRANS_STMT_ROLLBACK_TO;
                    n->options = list_make1(makeDefElem("savepoint_name",
                                                        (Node *)makeStringConst($4,NULL)));
                    $$ = (Node *)n;
                }
        ;

opt_transaction:    WORK                            {}
            | TRANSACTION                            {}
            | /*EMPTY*/                                {}
        ;

transaction_mode_item:
            ISOLATION LEVEL iso_level
                    { $$ = makeDefElem("transaction_isolation",
                                       makeStringConst($3, NULL)); }
            | READ ONLY
                    { $$ = makeDefElem("transaction_read_only",
                                       makeIntConst(TRUE)); }
            | READ WRITE
                    { $$ = makeDefElem("transaction_read_only",
                                       makeIntConst(FALSE)); }
        ;

/* Syntax with commas is SQL-spec, without commas is Postgres historical */
transaction_mode_list:
            transaction_mode_item
                    { $$ = list_make1($1); }
            | transaction_mode_list ',' transaction_mode_item
                    { $$ = lappend($1, $3); }
            | transaction_mode_list transaction_mode_item
                    { $$ = lappend($1, $2); }
        ;

transaction_mode_list_or_empty:
            transaction_mode_list
            | /* EMPTY */
                    { $$ = NIL; }
        ;

opt_durable: DURABLE
                    { $$ = list_make1(makeDefElem("durable",NULL)); }
            | /* EMPTY */
                    { $$ = NIL; }
        ;

/*****************************************************************************
 *
 *        QUERY:
 *                create view <viewname> '('target-list ')' AS <query>
 *                - enumerate the OR REPLACE so we can use OptLocalTempOnly.
 *                   we cannot have two optional symbols in a row
 *****************************************************************************/
ViewStmt:    CREATE OptLocalTempOnly VIEW qualified_name opt_column_list
                AS SelectStmt
                 {
                     ViewStmt *n = makeNode(ViewStmt);
                     n->replace = FALSE;
                     $4->temptype = $2;
                     n->view = $4;
                     n->aliases = $5;
                     n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                     n->query = (Query *) $7;
                     $$ = (Node *)n;
                 }
         ;

ViewStmt:    CREATE OptLocalTempOnly VIEW qualified_name opt_column_list
                INCLUDE SCHEMA PRIVILEGES AS SelectStmt
                 {
                     ViewStmt *n = makeNode(ViewStmt);
                     n->replace = FALSE;
                     $4->temptype = $2;
                     n->view = $4;
                     n->aliases = $5;
                     n->inheritPrivileges = INHERIT_PRIVILEGES;
                     n->query = (Query *) $10;
                     $$ = (Node *)n;
                 }
         ;

ViewStmt:    CREATE OptLocalTempOnly VIEW qualified_name opt_column_list
                INCLUDE PRIVILEGES AS SelectStmt
                 {
                     ViewStmt *n = makeNode(ViewStmt);
                     n->replace = FALSE;
                     $4->temptype = $2;
                     n->view = $4;
                     n->aliases = $5;
                     n->inheritPrivileges = INHERIT_PRIVILEGES;
                     n->query = (Query *) $9;
                     $$ = (Node *)n;
                 }
         ;

ViewStmt:    CREATE OptLocalTempOnly VIEW qualified_name opt_column_list
                EXCLUDE SCHEMA PRIVILEGES AS SelectStmt
                 {
                     ViewStmt *n = makeNode(ViewStmt);
                     n->replace = FALSE;
                     $4->temptype = $2;
                     n->view = $4;
                     n->aliases = $5;
                     n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                     n->query = (Query *) $10;
                     $$ = (Node *)n;
                 }
         ;

ViewStmt:    CREATE OptLocalTempOnly VIEW qualified_name opt_column_list
                EXCLUDE PRIVILEGES AS SelectStmt
                 {
                     ViewStmt *n = makeNode(ViewStmt);
                     n->replace = FALSE;
                     $4->temptype = $2;
                     n->view = $4;
                     n->aliases = $5;
                     n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                     n->query = (Query *) $9;
                     $$ = (Node *)n;
                 }
         ;

ViewStmt:    CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list
                AS SelectStmt
                 {
                     ViewStmt *n = makeNode(ViewStmt);
                     n->replace = TRUE;
                     $6->temptype = $4;
                     n->view = $6;
                     n->aliases = $7;
                     n->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;
                     n->query = (Query *) $9;
                     $$ = (Node *)n;
                 }
         ;

ViewStmt:    CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list
                INCLUDE SCHEMA PRIVILEGES AS SelectStmt
                 {
                     ViewStmt *n = makeNode(ViewStmt);
                     n->replace = TRUE;
                     $6->temptype = $4;
                     n->view = $6;
                     n->aliases = $7;
                     n->inheritPrivileges = INHERIT_PRIVILEGES;
                     n->query = (Query *) $12;
                     $$ = (Node *)n;
                 }
         ;

ViewStmt:    CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list
                INCLUDE PRIVILEGES AS SelectStmt
                 {
                     ViewStmt *n = makeNode(ViewStmt);
                     n->replace = TRUE;
                     $6->temptype = $4;
                     n->view = $6;
                     n->aliases = $7;
                     n->inheritPrivileges = INHERIT_PRIVILEGES;
                     n->query = (Query *) $11;
                     $$ = (Node *)n;
                 }
         ;

ViewStmt:    CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list
                EXCLUDE SCHEMA PRIVILEGES AS SelectStmt
                 {
                     ViewStmt *n = makeNode(ViewStmt);
                     n->replace = TRUE;
                     $6->temptype = $4;
                     n->view = $6;
                     n->aliases = $7;
                     n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                     n->query = (Query *) $12;
                     $$ = (Node *)n;
                 }
         ;

ViewStmt:    CREATE OR REPLACE OptLocalTempOnly VIEW qualified_name opt_column_list
                EXCLUDE PRIVILEGES AS SelectStmt
                 {
                     ViewStmt *n = makeNode(ViewStmt);
                     n->replace = TRUE;
                     $6->temptype = $4;
                     n->view = $6;
                     n->aliases = $7;
                     n->inheritPrivileges = NOT_INHERIT_PRIVILEGES;
                     n->query = (Query *) $11;
                     $$ = (Node *)n;
                 }
         ;

/*****************************************************************************
 *
 *        QUERY:
 *                load "filename"
 *
 *****************************************************************************/

LoadStmt:    LOAD file_name
                {
                    LoadStmt *n = makeNode(LoadStmt);
                    n->filename = $2.str;
                    $$ = (Node *)n;
                }
        ;


/*****************************************************************************
 *
 *        CREATE DATABASE
 *
 *****************************************************************************/

CreatedbStmt:
            CREATE DATABASE database_name opt_with createdb_opt_list
                {
                    CreatedbStmt *n = makeNode(CreatedbStmt);
                    n->dbname = $3.str;
                    n->options = $5;
                    $$ = (Node *)n;
                }
        ;

createdb_opt_list:
            createdb_opt_list createdb_opt_item        { $$ = lappend($1, $2); }
            | /* EMPTY */                            { $$ = NIL; }
        ;

createdb_opt_item:
            TABLESPACE opt_equal name
                {
                    $$ = makeDefElem("tablespace", (Node *)makeStr($3));
                }
            | TABLESPACE opt_equal DEFAULT
                {
                    $$ = makeDefElem("tablespace", NULL);
                }
            | LOCATION opt_equal Sconst
                {
                    $$ = makeDefElem("location", (Node *)makeStr($3));
                }
            | LOCATION opt_equal DEFAULT
                {
                    $$ = makeDefElem("location", NULL);
                }
            | TEMPLATE opt_equal name
                {
                    $$ = makeDefElem("template", (Node *)makeStr($3));
                }
            | TEMPLATE opt_equal DEFAULT
                {
                    $$ = makeDefElem("template", NULL);
                }
            | OWNER opt_equal name
                {
                    $$ = makeDefElem("owner", (Node *)makeStr($3));
                }
            | OWNER opt_equal DEFAULT
                {
                    $$ = makeDefElem("owner", NULL);
                }
        ;

/*
 *    Though the equals sign doesn't match other WITH options, pg_dump uses
 *    equals for backward compability, and it doesn't seem worth removing it.
 *    2002-02-25
 */
opt_equal:    '='                                        {}
            | /*EMPTY*/                                {}
        ;

knob_list:
            name                        { $$ = list_make1((Node *)makeStr($1)); }
            | knob_list ',' name { $$ = lappend($1,(Node *)makeStr($3)); }
        ;

/*****************************************************************************
 *
 *        ALTER DATABASE
 *
 *****************************************************************************/

AlterDatabaseSetStmt:
/*            ALTER DATABASE database_name SET set_rest
                {
                    AlterDatabaseSetStmt *n = makeNode(AlterDatabaseSetStmt);
                    n->dbname = $3.str;
                    n->variable = $5->name;
                    n->value = $5->args;
                    $$ = (Node *)n;
                }
            | ALTER DATABASE database_name VariableResetStmt
                {
                    AlterDatabaseSetStmt *n = makeNode(AlterDatabaseSetStmt);
                    n->dbname = $3.str;
                    n->variable = ((VariableResetStmt *)$4)->name;
                    n->value = NIL;
                    $$ = (Node *)n;
                }*/
            ALTER DATABASE database_name EXPORT ON name
                {
                    AlterDatabaseSetStmt *n = makeNode(AlterDatabaseSetStmt);
                    n->dbname = $3.str;
                    n->subtype = AD_Export;
                    n->value = list_make1((Node *)makeStr($6));
                    $$ = (Node *)n;
                }
           | ALTER DATABASE database_name EXPORT ON DEFAULT
                {
                    AlterDatabaseSetStmt *n = makeNode(AlterDatabaseSetStmt);
                    n->dbname = $3.str;
                    n->subtype = AD_Export;
                    n->value = NIL;
                    $$ = (Node *)n;
                }
           | ALTER DATABASE database_name DROP ALL FAULT GROUP_P
                {
                    AlterDatabaseSetStmt *n = makeNode(AlterDatabaseSetStmt);
                    n->dbname = $3.str;
                    n->subtype = AD_DropAllFaultGroups;
                    n->value = NIL;
                    $$ = (Node *)n;
                }
           | ALTER DATABASE database_name DROP ALL AUTO FAULT GROUP_P
                {
                    AlterDatabaseSetStmt *n = makeNode(AlterDatabaseSetStmt);
                    n->dbname = $3.str;
                    n->subtype = AD_DropAllAutoFaultGroups;
                    n->value = NIL;
                    $$ = (Node *)n;
                }
           | ALTER DATABASE database_name SET PARAMETER paramarg_list
                {
                    AlterDatabaseSetStmt *n = makeNode(AlterDatabaseSetStmt);
                    n->dbname = $3.str;
                    n->subtype = AD_SetParam;
                    n->params = $6;
                    $$ = (Node *)n;
                }
           | ALTER DATABASE database_name SET paramarg_list
                {
                    AlterDatabaseSetStmt *n = makeNode(AlterDatabaseSetStmt);
                    n->dbname = $3.str;
                    n->subtype = AD_SetParam;
                    n->params = $5;
                    $$ = (Node *)n;
                }
           | ALTER DATABASE database_name CLEAR PARAMETER knob_list
                {
                    AlterDatabaseSetStmt *n = makeNode(AlterDatabaseSetStmt);
                    n->dbname = $3.str;
                    n->subtype = AD_ClearParam;
                    n->params = $6;
                    $$ = (Node *)n;
                }
           | ALTER DATABASE database_name CLEAR knob_list
                {
                    AlterDatabaseSetStmt *n = makeNode(AlterDatabaseSetStmt);
                    n->dbname = $3.str;
                    n->subtype = AD_ClearParam;
                    n->params = $5;
                    $$ = (Node *)n;
                }
           | ALTER DATABASE database_name RESET STANDBY
                {
                    AlterDatabaseSetStmt *n = makeNode(AlterDatabaseSetStmt);
                    n->dbname = $3.str;
                    n->subtype = AD_ResetStandby;
                    n->value = NIL;
                    $$ = (Node *)n;
                }
        ;
/*****************************************************************************
 *
 *        SHOW DATABASE
 *
 *****************************************************************************/
ShowDatabaseStmt: SHOW DATABASE database_name knob_list
                {
                    ShowDatabaseStmt *n = makeNode(ShowDatabaseStmt);
                    n->dbname = $3.str;
                    n->params = $4;
                    n->all = false;
                    $$ = (Node *)n;
                }
           | SHOW DATABASE database_name PARAMETER knob_list
                {
                    ShowDatabaseStmt *n = makeNode(ShowDatabaseStmt);
                    n->dbname = $3.str;
                    n->params = $5;
                    n->all = false;
                    $$ = (Node *)n;
                }
           | SHOW DATABASE database_name ALL
                {
                    ShowDatabaseStmt *n = makeNode(ShowDatabaseStmt);
                    n->dbname = $3.str;
                    n->all = true;
                    $$ = (Node *)n;
                }
           | SHOW DATABASE database_name PARAMETER ALL
                {
                    ShowDatabaseStmt *n = makeNode(ShowDatabaseStmt);
                    n->dbname = $3.str;
                    n->all = true;
                    $$ = (Node *)n;
                }
        ;

/*****************************************************************************
 *
 *        DROP DATABASE
 *
 * This is implicitly CASCADE, no need for drop behavior
 *****************************************************************************/

DropdbStmt: DROP DATABASE database_name
                {
                    DropdbStmt *n = makeNode(DropdbStmt);
                    n->dbname = $3.str;
                    $$ = (Node *)n;
                }
        ;

/*****************************************************************************
 *
 *        CREATE SUBNET
 *
 *****************************************************************************/

CreateSubnetStmt:
            CREATE SUBNET name opt_with Sconst opt_force
                {
                    CreateSubnetStmt *n = makeNode(CreateSubnetStmt);
                    n->name = $3.str;
                    n->mask = $5.str;
					n->force = $6;
                    $$ = (Node *)n;
                }
        ;

/*****************************************************************************
 *
 * Manipulate a domain
 *
 *****************************************************************************/

CreateDomainStmt:
            CREATE DOMAIN_P any_name opt_as Typename ColQualList
                {
                    CreateDomainStmt *n = makeNode(CreateDomainStmt);
                    n->domainname = $3;
                    n->typeInfo = $5;
                    n->constraints = $6;
                    $$ = (Node *)n;
                }
        ;

AlterDomainStmt:
            /* ALTER DOMAIN <domain> {SET DEFAULT <expr>|DROP DEFAULT} */
            ALTER DOMAIN_P any_name alter_column_default
                {
                    AlterDomainStmt *n = makeNode(AlterDomainStmt);
                    n->subtype = 'T';
                    n->typeInfo = $3;
                    n->def = $4;
                    $$ = (Node *)n;
                }
            /* ALTER DOMAIN <domain> DROP NOT NULL */
            | ALTER DOMAIN_P any_name DROP NOT NULL_P
                {
                    AlterDomainStmt *n = makeNode(AlterDomainStmt);
                    n->subtype = 'N';
                    n->typeInfo = $3;
                    $$ = (Node *)n;
                }
            /* ALTER DOMAIN <domain> SET NOT NULL */
            | ALTER DOMAIN_P any_name SET NOT NULL_P
                {
                    AlterDomainStmt *n = makeNode(AlterDomainStmt);
                    n->subtype = 'O';
                    n->typeInfo = $3;
                    $$ = (Node *)n;
                }
            /* ALTER DOMAIN <domain> ADD CONSTRAINT ... */
            | ALTER DOMAIN_P any_name ADD TableConstraint
                {
                    AlterDomainStmt *n = makeNode(AlterDomainStmt);
                    n->subtype = 'C';
                    n->typeInfo = $3;
                    n->def = $5;
                    $$ = (Node *)n;
                }
            /* ALTER DOMAIN <domain> DROP CONSTRAINT <name> [RESTRICT|CASCADE] */
            | ALTER DOMAIN_P any_name DROP CONSTRAINT name opt_drop_behavior
                {
                    AlterDomainStmt *n = makeNode(AlterDomainStmt);
                    n->subtype = 'X';
                    n->typeInfo = $3;
                    n->name = $6.str;
                    n->behavior = $7;
                    $$ = (Node *)n;
                }
            ;

opt_as:        AS                                        {}
            | /* EMPTY */                            {}
        ;

/*****************************************************************************
 *
 * Manipulate a storage location -- trying to replace nasty location PGCalls
 *
 *****************************************************************************/

CreateLocationStmt:
            CREATE LOCATION Sconst OptNodes OptShared OptUsage OptLabel OptSize
                {
                    CreateAlterLocationStmt *n = makeNode(CreateAlterLocationStmt);
                    n->path = $3.str;
                    n->nodes = $4.str;
                    n->sharingType = $5;
                    n->usage = $6.str;
                    n->tier = $7.str; // actually label
                    n->alter = false; // jhu TODO
                    n->max_size = $8.str;
                    $$ = (Node *)n;
                }
        ;
        
OptUsage:
            USAGE Sconst                 { $$ = $2; }
            | /*EMPTY*/                  { $$ = ctString("DATA,TEMP"); }
        ;

OptNodes:
            ALL NODES                    { $$ = ctNULL; } // null == default == all nodes
            | NODE Sconst                { $$ = $2; }
            | /*EMPTY*/                  { $$ = ctNULL; }
        ;

OptShared:
            SHARED                       { $$ = SHARING_TYPE_SHARED;   }
            | COMMUNAL                   { $$ = SHARING_TYPE_COMMUNAL; }
            | /*EMPTY*/                  { $$ = SHARING_TYPE_NONE;     }
        ;

OptLabel:
            LABEL Sconst                  { $$ = $2; }
            | /*EMPTY*/                  { $$ = ctNULL; }
        ;

OptSize:
            LIMIT Sconst               { $$ = $2; }
            | /*EMPTY*/                  { $$ = ctNULL; }
        ;
/*****************************************************************************
 *
 *        QUERY:
 *                cluster <index_name> on <qualified_name>
 *                cluster <qualified_name>
 *                cluster
 *
 *****************************************************************************/

ClusterStmt:
            CLUSTER index_name ON qualified_name
                {
                   ClusterStmt *n = makeNode(ClusterStmt);
                   n->relation = $4;
                   n->indexname = $2->relname;
                   $$ = (Node*)n;
                }
            | CLUSTER qualified_name
                {
                   ClusterStmt *n = makeNode(ClusterStmt);
                   n->relation = $2;
                   n->indexname = NULL;
                   $$ = (Node*)n;
                }
            | CLUSTER
                {
                   ClusterStmt *n = makeNode(ClusterStmt);
                   n->relation = NULL;
                   n->indexname = NULL;
                   $$ = (Node*)n;
                }
        ;

/*****************************************************************************
 *
 *        QUERY:
 *                vacuum
 *                analyze
 *
 *****************************************************************************/

/*
VacuumStmt: VACUUM opt_full opt_freeze opt_verbose
                {
                    VacuumStmt *n = makeNode(VacuumStmt);
                    n->vacuum = true;
                    n->analyze = false;
                    n->full = $2;
                    n->freeze = $3;
                    n->verbose = $4;
                    n->relation = NULL;
                    n->va_cols = NIL;
                    $$ = (Node *)n;
                }
            | VACUUM opt_full opt_freeze opt_verbose qualified_name
                {
                    VacuumStmt *n = makeNode(VacuumStmt);
                    n->vacuum = true;
                    n->analyze = false;
                    n->full = $2;
                    n->freeze = $3;
                    n->verbose = $4;
                    n->relation = $5;
                    n->va_cols = NIL;
                    $$ = (Node *)n;
                }
            | VACUUM opt_full opt_freeze opt_verbose AnalyzeStmt
                {
                    VacuumStmt *n = (VacuumStmt *) $5;
                    n->vacuum = true;
                    n->full = $2;
                    n->freeze = $3;
                    n->verbose |= $4;
                    $$ = (Node *)n;
                }
        ;
*/

AnalyzeStmt:
            analyze_keyword
                {
                    VacuumStmt *n = makeNode(VacuumStmt);
                    n->vacuum = false;
                    n->analyze = true;
                    n->full = false;
                    n->freeze = false;
                    n->verbose = false;
                    n->relation = NULL;
                    n->va_cols = NIL;
                    $$ = (Node *)n;
                }
            | analyze_keyword qualified_name opt_name_list
                {
                    VacuumStmt *n = makeNode(VacuumStmt);
                    n->vacuum = false;
                    n->analyze = true;
                    n->full = false;
                    n->freeze = false;
                    n->verbose = false;
                    n->relation = $2;
                    n->va_cols = $3;
                    $$ = (Node *)n;
                }
            /* Vertica added ANALYZE CONSTRAINT ... */
            | analyze_keyword CONSTRAINT qualified_name opt_name_list
                {
                    VAnalyzeStmt *n = makeNode(VAnalyzeStmt);
                    n->constraint = true;
                    n->relation = $3;
                    n->va_cols = $4;
                    $$ = (Node *)n;
                }
            /* Vertica added ANALYZE ALL CONSTRAINT */
            | analyze_keyword ALL CONSTRAINT
                {
                    VAnalyzeStmt *n = makeNode(VAnalyzeStmt);
                    n->constraint = true;
                    n->relation = NULL;
                    n->va_cols = NIL;
                    $$ = (Node *)n;
                }
        ;

analyze_keyword:
            ANALYZE                                    {}
            | ANALYSE /* British */                    {}
        ;
        
opt_json:
            JSON                                    { $$ = TRUE; }
            | /*EMPTY*/                                { $$ = FALSE; }
        ;

opt_verbose:
            VERBOSE                                    { $$ = TRUE; }
            | /*EMPTY*/                                { $$ = FALSE; }
        ;

opt_name_list:
            '(' name_list ')'                        { $$ = $2; }
            | /*EMPTY*/                                { $$ = NIL; }
        ;
opt_local:
            LOCAL                                      { $$ = TRUE; }
            | /*EMPTY*/                                { $$ = FALSE; }
        ;
opt_hint_list:
            '(' hint_list ')'                        { $$ = $2; }
            | /*EMPTY*/                                { $$ = NIL; }
		;
/**
 *
 * PLAN STABILITY, SAVE QUERY.
 * SAVE QUERY SQL
 *
 */
PlanStabilitySavePlanStmt:
    SAVE QUERY PlanStabilitySupportedStmt
    {
        PlanStabilitySavePlanStmt *n = makeNode(PlanStabilitySavePlanStmt);
        n->query = (Query*) $3;
        $$ = (Node *) n;
    }
;

/**
 * PLAN STABILITY, CREATE DIRECTED QUERY.
 * CREATE DIRECTED QUERY { OPTIMIZER | OPT | CUSTOM } dirQueryName
 *          [COMMENT 'comments'] SQL.
 */
PlanStabilityAssociatePlanStmt:
    CREATE DIRECTED QUERY OptPlan PlanIdentifier PlanDescription
            OptimizerVersion DirectedQueryCreationDate
                    PlanStabilitySupportedStmt
    {
        PlanStabilityAssociatePlanStmt *n =
                makeNode(PlanStabilityAssociatePlanStmt);
        n->optPlan = true;
        n->identifier = $5.str;
        n->description = $6.str;
        n->optversion = $7.str;
        n->creationDate = $8.str;
        n->query = (Query*) $9;
        $$ = (Node *) n;
    } |
    CREATE DIRECTED QUERY CUSTOM PlanIdentifier PlanDescription OptimizerVersion
            DirectedQueryCreationDate PlanStabilitySupportedStmt
    {
        PlanStabilityAssociatePlanStmt *n =
                makeNode(PlanStabilityAssociatePlanStmt);
        n->optPlan = false;
        n->identifier = $5.str;
        n->description = $6.str;
        n->optversion = $7.str;
        n->creationDate = $8.str;
        n->query = (Query*) $9;
        $$ = (Node *) n;
    }
;

/**
 *
 * PLAN STABILITY, DROP DIRECTED QUERY.
 * DROP DIRECTED QUERY dirQueryName 
 *
 */
PlanStabilityRemovePlanStmt:
    DROP DIRECTED QUERY PlanIdentifierList
    {
        PlanStabilityRemovePlanStmt *n = makeNode(PlanStabilityRemovePlanStmt);
        n->identifiers = $4;
        $$ = (Node *) n;
    }
;

/**
 *
 * PLAN STABILITY, GET DIRECTED QUERY.
 * Usage: GET DIRECTED QUERY SQL
 *
 * PLAN STABILITY, GET UNINDEXED DIRECTED QUERY.
 * Usage: GET UNINDEXED DIRECTED QUERY SQL
 *
 */
PlanStabilityGetPlanStmt:
    GET DIRECTED QUERY PlanStabilitySupportedStmt
    {
        PlanStabilityGetPlanStmt *n = makeNode(PlanStabilityGetPlanStmt);
        n->query = (Query *) $4;
        $$ = (Node *) n;
    }
    |
    GET UNINDEXED DIRECTED QUERY
    {
        PlanStabilityGetPlanStmt *n = makeNode(PlanStabilityGetPlanStmt);
        n->query = NULL;
        $$ = (Node *) n;
    }
;

/**
 *
 * PLAN STABILITY, ACTIVATE/DEACTIVATE DIRECTED QUERY.
 * Usage: ACTIVATE DIRECTED QUERY dirQueryName
 *        DEACTIVATE DIRECTED QUERY SQL
 *        DEACTIVATE DIRECTEDQUERY dirQueryName
 *
 */
PlanStabilityActivatePlanStmt:
    ACTIVATE DIRECTED QUERY PlanIdentifier
    {
        PlanStabilityActivatePlanStmt *n =
                makeNode(PlanStabilityActivatePlanStmt);
        n->query = NIL;
        n->activate = true;
        n->identifier = $4.str;
        $$ = (Node *) n;
    } |
    DEACTIVATE DIRECTED QUERY PlanIdentifier
    {
        PlanStabilityActivatePlanStmt *n =
                makeNode(PlanStabilityActivatePlanStmt);
        n->query = NIL;
        n->activate = false;
        n->identifier = $4.str;
        $$ = (Node *) n;
    } |
    DEACTIVATE DIRECTED QUERY PlanStabilitySupportedStmt
    {
        PlanStabilityActivatePlanStmt *n =
                makeNode(PlanStabilityActivatePlanStmt);
        n->query = (Query *) $4;
        n->activate = false;
        n->identifier = 0;
        $$ = (Node *) n;
    }
;

PlanStabilitySupportedStmt:
        VSelectStmt;

PlanIdentifier:
        ColLabel
        {
            $$ = $1;
        }
;

PlanIdentifierList:
        PlanIdentifierList ',' PlanIdentifier {
            $$ = lappend($1, makeStr($3));
        }
        | PlanIdentifier { $$ = list_make1(makeStr($1)); }
;

PlanDescription:
        COMMENT Sconst { $$ = $2; }
        |  /* EMPTY */  { $$ = ctNULL; }
;

OptimizerVersion:
        OPTVER Sconst { $$ = $2; }
        |  /* EMPTY */  { $$ = ctNULL; }
;

DirectedQueryCreationDate:
        PSDATE Sconst { $$ = $2; }
        |  /* EMPTY */  { $$ = ctNULL; }
;

OptPlan:
        OPTIMIZER { $$ = TRUE; }
        |
        OPT { $$ = TRUE; }
;

/*****************************************************************************
 *
 *        QUERY:
 *                EXPLAIN [ANALYZE] [LOCAL] [VERBOSE] [JSON] query
 *
 *****************************************************************************/
/*VER-50473: Add opt_annotated for feature "explain directed query"*/
ExplainStmt: EXPLAIN hint_clause opt_analyze opt_local opt_verbose opt_json opt_annotated ExplainableStmt
                {
                    ExplainStmt *n = makeNode(ExplainStmt);

                    n->hintClause = $2;
                    n->analyze = $3;
                    n->localized = $4;
                    n->verbose = $5;
                    n->json = $6;
                    n->annotated = $7;
                    n->query = (Query*)$8;
                    n->allNodesUp = FALSE;

                    $$ = (Node *)n;
                }
        ;

ExplainableStmt:
            VSelectStmt
            | InsertStmt
            | UpdateStmt
            | DeleteStmt
            | CopyStmt
            | DeclareCursorStmt
            | ExecuteStmt                    /* by default all are $$=$1 */
            | ExportStmt
            | VMergeStmt
        ;

opt_analyze:
            analyze_keyword            { $$ = TRUE; }
            | /* EMPTY */            { $$ = FALSE; }
        ;
/*VER-50473: to indicate whether to explain directed query or whole plan*/
opt_annotated:
            ANNOTATED			{ $$ = TRUE; }
            | /* EMPTY */		{ $$ = FALSE;}
        ;

/*****************************************************************************
 *
 *        QUERY:
 *                PROFILE query
 *
 *****************************************************************************/

ProfileStmt: PROFILE ProfileableStmt
                {
                    ProfileStmt *n = makeNode(ProfileStmt);
                    n->query = (Query*)$2;
                    $$ = (Node *)n;
                }
        ;

ProfileableStmt:
            VSelectStmt
            | InsertStmt
            | UpdateStmt
            | DeleteStmt
            | CopyStmt
            | ExportStmt
            | VMergeStmt
        ;

/*****************************************************************************
 *
 *        QUERY:
 *                PREPARE <plan_name> [(args, ...)] AS <query>
 *
 *****************************************************************************/

PrepareStmt: PREPARE name prep_type_clause AS PreparableStmt
                {
                    PrepareStmt *n = makeNode(PrepareStmt);
                    n->name = $2.str;
                    n->argtypes = $3;
                    n->query = (Query *) $5;
                    $$ = (Node *) n;
                }
        ;

prep_type_clause: '(' prep_type_list ')'    { $$ = $2; }
                | /* EMPTY */                { $$ = NIL; }
        ;

prep_type_list: Typename            { $$ = list_make1($1); }
              | IDENT '(' Iconst ')'
                {
                    TypeName *t = SystemTypeName($1.str);
                    t->typmod = VARHDRSZ + $3;
                    $$ = list_make1((Node *)t);
                }
              | prep_type_list ',' Typename
                                    { $$ = lappend($1, $3); }
              | prep_type_list ',' IDENT '(' Iconst ')'
                {
                    TypeName *t = SystemTypeName($3.str);
                    t->typmod = VARHDRSZ + $5;
                    $$ = lappend($1, (Node *)t);
                }
        ;

PreparableStmt:
            SelectStmt
            | InsertStmt
            | UpdateStmt
            | DeleteStmt                    /* by default all are $$=$1 */
            | ExportStmt
            | VMergeStmt
        ;

/*****************************************************************************
 *
 * EXECUTE <plan_name> [(params, ...)]
 * CREATE TABLE <name> AS EXECUTE <plan_name> [(params, ...)]
 *
 *****************************************************************************/

ExecuteStmt: EXECUTE name execute_param_clause
                {
                    ExecuteStmt *n = makeNode(ExecuteStmt);
                    n->name = $2.str;
                    n->params = $3;
                    n->into = NULL;
                    $$ = (Node *) n;
                }
            | CREATE OptTemp TABLE qualified_name opt_vt_columnGroupList OptWithOids OnCommitOption OptCopy AS EXECUTE name execute_param_clause
                {
                    ExecuteStmt *n = makeNode(ExecuteStmt);
                    n->copyMode = $8;
                    n->name = $11.str;
                    n->params = $12;
                    $4->temptype = $2;
                    n->into = $4;
                    if ($5)
                        ereport(ERROR,
                                (errcode(ERRCODE_FEATURE_NOT_SUPPORTED),
                                 errmsg("Column name list is not allowed in CREATE TABLE / AS EXECUTE")));
                    /* ... because it's not implemented, but it could be */
                    $$ = (Node *) n;
                }
        ;

execute_param_clause: '(' expr_list ')'                { $$ = $2; }
                    | /* EMPTY */                    { $$ = NIL; }
                    ;

/*****************************************************************************
 *
 *        QUERY:
 *                DEALLOCATE [PREPARE] <plan_name>
 *
 *****************************************************************************/

DeallocateStmt: DEALLOCATE name
                    {
                        DeallocateStmt *n = makeNode(DeallocateStmt);
                        n->name = $2.str;
                        $$ = (Node *) n;
                    }
                | DEALLOCATE PREPARE name
                    {
                        DeallocateStmt *n = makeNode(DeallocateStmt);
                        n->name = $3.str;
                        $$ = (Node *) n;
                    }
        ;

/*****************************************************************************
 *
 *        QUERY:
 *                MERGE STATEMENTS (Vertica's Merge Upsert)
 *
 *****************************************************************************/

/* MERGE statement */
VMergeStmt:
            MERGE hint_clause INTO merge_table_tgt_ref
            USING merge_table_src_ref ON a_expr
            merge_clause_list
                {
                    // get tgt and src tables
                    RangeVar *tgtRel = (RangeVar *) $4;
                    Node *srcRelNode = $6;
                                    
                    RangeSubselect *srcSubSelect;
                    
                    bool srcIsSubqry;
                
                    // If src is a relation, make a dummy RangeSubSelect (original logic)
                    if (IsA(srcRelNode, RangeVar)) {
                
                        RangeVar *srcRel = (RangeVar*)srcRelNode;
                                        
                        if (srcRel->alias == NULL)
                        {
                            Alias *alias = makeNode(Alias);
                
                            // Alias must be the full name, not only the short relName
                            int l = strlen(srcRel->relname) + 1;
                            if (srcRel->schemaname != NULL)
                                l += strlen(srcRel->schemaname) + 1;
                            if (srcRel->catalogname !=NULL)
                                l += strlen(srcRel->catalogname) + 1;
                
                            char* strAlias = palloc(l);
                            strcpy(strAlias, "\0");
                            if (srcRel->schemaname != NULL)
                            {
                                strcat(strAlias, srcRel->schemaname);
                                strcat(strAlias, ".");
                            }
                            if (srcRel->catalogname !=NULL)
                            {
                                strcat(strAlias, srcRel->catalogname);
                                strcat(strAlias, ".");
                            }
                            strcat(strAlias, srcRel->relname);
                            alias->aliasname = strAlias;
                
                            srcRel->alias = alias;
                        }
                        
                        // Target alias
						bool mustQualifyTargetFullName = (strcasecmp(tgtRel->relname, srcRel->relname) == 0);
                        
	                    if (tgtRel->alias == NULL && mustQualifyTargetFullName)
	                    {
	                        Alias *alias = makeNode(Alias);
	                
	                        // Alias must be the full name, not only the short relName
	                        int l = strlen(tgtRel->relname) + 1;
	                        if (tgtRel->schemaname != NULL)
	                            l += strlen(tgtRel->schemaname) + 1;
	                        if (tgtRel->catalogname !=NULL)
	                            l += strlen(tgtRel->catalogname) + 1;
	                
	                        char *strAlias = palloc(l);
	                        strcpy(strAlias, "\0");
	                        if (tgtRel->schemaname != NULL)
	                        {
	                            strcat(strAlias, tgtRel->schemaname);
	                            strcat(strAlias, ".");
	                        }
	                        if (tgtRel->catalogname !=NULL)
	                        {
	                            strcat(strAlias, tgtRel->catalogname);
	                            strcat(strAlias, ".");
	                        }
	                        strcat(strAlias, tgtRel->relname);
	                        alias->aliasname = strAlias;
	                        tgtRel->alias = alias;
	                    }
                
                        // ------------------------------------------------------------------
                        // Make the subQry of the update stmt first
                        SelectStmt *selQry =  makeNode(SelectStmt);
                        selQry->fromClause =  list_make1(srcRel);             // srcRelation
                
                        // Make select '*, true' for the subquery
                        // Noet that 'true' is a placeholder for the 'matched' column out of the join
                
                        // Make '*' node
                        ColumnRef *starNode = makeNode(ColumnRef);
                        starNode->fields = list_make1(makeString("*"));
                        ResTarget *starTarget = makeNode(ResTarget);
                        starTarget->name = NULL;
                        starTarget->indirection = NIL;
                        starTarget->val = (Node *) starNode;
                
                        // Make '*'
                        List *tgtList = NIL;
                        tgtList = lappend(tgtList, starTarget);
                        selQry->targetList = tgtList;
                
                        // Make subqery for this selQry to be able to assign it to from clause of update stmt
                        srcSubSelect = makeNode(RangeSubselect);
                        srcSubSelect->subquery = (Node *) selQry;
                        // Alias of the subquery will be the same alias of the src if provided
                        Alias *alias = makeNode(Alias);
                        if (srcRel->alias)
                            alias->aliasname = srcRel->alias->aliasname;
                        else
                            alias->aliasname = "SelQry";
                        srcSubSelect->alias = alias;
                        srcIsSubqry = false;
                    }
                    // Otherwise, already a RangeSubselect, must have a alias
                    else {
                        VIAssert(IsA(srcRelNode, RangeSubselect));
                        srcSubSelect = (RangeSubselect*) srcRelNode;
                        srcIsSubqry = true;
                    }
                
                    // build VMergeStmt node
                    VMergeStmt *n = makeNode(VMergeStmt);
                    n->mergeTargetRel = tgtRel;
                    n->mergeSourceRel = list_make1(srcSubSelect);
                    n->mergeMatchCond = $8;
                    n->mergeClauses = $9;
                    n->hintClause = $2;
                    n->srcIsSubqry = srcIsSubqry;
                    
                    $$ = (Node *) n;
                }
       ;

merge_clause_list:
            merge_clause
            {
                $$ = list_make1($1);
            }
            |
            merge_clause_list merge_clause
            {
                $$ = lappend($1, $2);
            }
        ;

merge_clause:
            merge_update_clause
                {
                    $$ = (Node *) $1;
                }
            |
            merge_insert_clause
                {
                    $$ = (Node *) $1;
                }
       ;


merge_update_clause:
            WHEN MATCHED THEN UPDATE SET update_target_list where_clause
                {
                    VMergeClause *n = makeNode(VMergeClause);
                    n->clauseType = MERGE_UPDATE_CLAUSE;
                    n->guard = $7;
                    n->targetList = $6;
                    n->cols = NIL;
                    $$ = (Node *) n;
                }
            |
            WHEN MATCHED AND a_expr THEN UPDATE SET update_target_list
                {
                    VMergeClause *n = makeNode(VMergeClause);
                    n->clauseType = MERGE_UPDATE_CLAUSE;
                    n->guard = $4;
                    n->targetList = $8;
                    n->cols = NIL;
                    $$ = (Node *) n;
                }
        ;
        
merge_insert_clause:
            WHEN NOT MATCHED THEN INSERT merge_insert_target_list where_clause
                {
                    VMergeClause *n = (VMergeClause *) $6;
                    n->guard = $7;
                    $$ = (Node *) n;
                }
            |
            WHEN NOT MATCHED AND a_expr THEN INSERT merge_insert_target_list
                {
                    VMergeClause *n = (VMergeClause *) $8;
                    n->guard = $5;
                    $$ = (Node *) n;
                }
        ;
        
merge_insert_target_list:
            VALUES '(' insert_target_list ')'
                {
                    VMergeClause *n = makeNode(VMergeClause);
                    n->clauseType = MERGE_INSERT_CLAUSE;
                    n->cols = NIL; 
                    n->targetList = $3;
                    $$ = (Node *) n;
                }
            | DEFAULT VALUES
                {
                    VMergeClause *n = makeNode(VMergeClause);
                    n->clauseType = MERGE_INSERT_CLAUSE;
                    n->cols = NIL;
                    n->targetList = NIL;
                    $$ = (Node *) n;
                }
            | select_with_parens
                {
                    ereport(ERROR,
                           (errcode(ERRCODE_SYNTAX_ERROR),
                            errmsg("Subquery in MERGE statement are allowed at SOURCE only")));
                    $$ = NULL;
                }
            | '(' insert_column_list ')' VALUES '(' insert_target_list ')'
                {
                    VMergeClause *n = makeNode(VMergeClause);
                    n->clauseType = MERGE_INSERT_CLAUSE;
                    n->cols = $2;
                    n->targetList = $6;
                    $$ = (Node *) n;
                }
            | '(' insert_column_list ')' select_with_parens
                {
                    ereport(ERROR,
                           (errcode(ERRCODE_SYNTAX_ERROR),
                            errmsg("Subquery in MERGE statement are allowed at SOURCE only")));
                    $$ = NULL;
                }
        ;

merge_table_tgt_ref:
              relation_expr
                {
                    $$ = (Node *) $1;
                }
            | relation_expr alias_clause
                {
                    $1->alias = $2;
                    $$ = (Node *) $1;
                }
            | select_with_parens
                {
                    /*
                     * Does not support subquery in MERGE stmt
                     */
                    ereport(ERROR,
                            (errcode(ERRCODE_SYNTAX_ERROR),
                             errmsg("Subquery in MERGE statement are allowed at SOURCE only")));
                    $$ = NULL;
                }
            | select_with_parens alias_clause
                {
                    /*
                     * Does not support subquery in MERGE stmt
                     */
                    ereport(ERROR,
                            (errcode(ERRCODE_SYNTAX_ERROR),
                             errmsg("Subquery in MERGE statement are allowed at SOURCE only")));
                    $$ = NULL;
                }
     ;
merge_table_src_ref:
              relation_expr
                {
                    $$ = (Node *) $1;
                }
            | relation_expr alias_clause
                {
                    $1->alias = $2;
                    $$ = (Node *) $1;
                }
            | select_with_parens
                {
                    ereport(ERROR,
                            (errcode(ERRCODE_SYNTAX_ERROR),
                             errmsg("Subquery in FROM must have an alias"),
                             errhint("For example, FROM (SELECT ...) [AS] foo")));
                    $$ = NULL;
                }
            | select_with_parens alias_clause
                {
                    RangeSubselect *n = makeNode(RangeSubselect);
                    n->subquery = $1;
                    n->alias = $2;
                    $$ = (Node *) n;
                }
     ;

/*****************************************************************************
 *
 *        QUERY:
 *                INSERT STATEMENTS
 *
 *****************************************************************************/

InsertStmt:
            INSERT hint_clause INTO qualified_name insert_rest
                {
                    $5->hintClause = $2;
                    $5->relation = $4;
                    $$ = (Node *) $5;
                }
        ;

insert_rest:
            VALUES '(' insert_target_list ')'
                {
                    $$ = makeNode(InsertStmt);
                    $$->cols = NIL;
                    $$->targetList = $3;
                    $$->selectStmt = NULL;
                }
            | DEFAULT VALUES
                {
                    $$ = makeNode(InsertStmt);
                    $$->cols = NIL;
                    $$->targetList = NIL;
                    $$->selectStmt = NULL;
                }
            | VSelectStmt 
                {
                    $$ = makeNode(InsertStmt);
                    $$->cols = NIL;
                    $$->targetList = NIL;
                    $$->selectStmt = $1;
                }
            | '(' insert_column_list ')' VALUES '(' insert_target_list ')'
                {
                    $$ = makeNode(InsertStmt);
                    $$->cols = $2;
                    $$->targetList = $6;
                    $$->selectStmt = NULL;
                }
            | '(' insert_column_list ')' VSelectStmt
                {
                    $$ = makeNode(InsertStmt);
                    $$->cols = $2;
                    $$->targetList = NIL;
                    $$->selectStmt = $4;
                }
        ;

insert_column_list:
            insert_column_item
                    { $$ = list_make1($1); }
            | insert_column_list ',' insert_column_item
                    { $$ = lappend($1, $3); }
        ;

insert_column_item:
            ColId opt_indirection
                {
                    $$ = makeNode(ResTarget);
                    $$->name = $1.str;
                    $$->indirection = $2;
                    $$->val = NULL;
                }
        ;


/*****************************************************************************
 *
 *        CONNECT TO DATABASE
 *
 *****************************************************************************/

opt_connect_addr_family:
            ',' Sconst                                     {$$ = $2;}
            | /*EMPTY*/                                    {$$ = ctNULL;}
        ;

opt_connect_tls_mode:
            TLSMODE PREFER                                 {$$ = true;}
            | /*EMPTY*/                                    {$$ = false;}
        ;

ConnectStmt:
            CONNECT TO VERTICA database_name USER UserId PASSWORD Sconst ON Sconst ',' Iconst opt_connect_addr_family opt_connect_tls_mode
                {
                    ConnectStmt *n = makeNode(ConnectStmt);
                    n->dbname = $4.str;
                    n->user = $6.str;
                    n->password = $8.str;
                    n->host = $10.str;
                    n->port = $12;
                    n->addressFamily = $13.str;
                    n->tlsmode_override_prefer = $14;
                    $$ = (Node *)n;
                }
        ;
/*****************************************************************************
 *
 *        DISCONNECT DATABASE
 *
 *****************************************************************************/

DisconnectStmt: DISCONNECT database_name
                {
                    DisconnectStmt *n = makeNode(DisconnectStmt);
                    n->dbname = $2.str;
                    $$ = (Node *)n;
                }
        ;


/*****************************************************************************
 *
 *                EXPORT STATEMENTS
 *
 *****************************************************************************/

ExportStmt:
            EXPORT TO VERTICA export_relation opt_export_column_list export_select export_segmentation
                {
                    ExportStmt* e = makeNode(ExportStmt);
                    e->exportType = EXPORT_VERTICA;
                    e->relation = $4;
                    e->columns = $5;
                    e->selectStmt = (Node*)$6;
                    e->segExpr = $7;
                    $$ = (Node *) e;
                }
            | EXPORT TO STDOUT export_select
                {
                    ExportStmt* e = makeNode(ExportStmt);
                    e->exportType = EXPORT_STDOUT;
                    e->selectStmt = (Node*)$4;
                    $$ = (Node *) e;
                }
            | EXPORT TO PARQUET '(' paramarg_list ')' opt_export_over_clause AS SelectStmt 
                {
                    ExportStmt* e = makeNode(ExportStmt);
                    e->exportType = EXPORT_PARQUET;
                    e->parquetArgs = (List *)$5;
                    e->analyticClause = (Node *)$7;
                    e->selectStmt = (Node *)$9;

                    $$ = (Node *) e;
                }
        ;


opt_export_over_clause:
            over_clause                                   { $$ = $1; }
            | /*EMPTY*/                                   { $$ = NIL; }
        ;

opt_export_column_list:
            '(' export_column_list ')'                    { $$ = $2; }
            | /*EMPTY*/                                   { $$ = NIL; }
        ;

export_column_list:
            columnref                                          { $$ = list_make1($1); }
            | export_column_list ',' columnref                 { $$ = lappend($1, $3); }
        ;

export_segmentation:
            SEGMENTED BY b_expr                            {$$ = $3;}
            | /*EMPTY*/                                    {$$ =NIL;}
        ;

opt_export_target_list:
            '(' target_list ')'                    { $$ = $2; } |
            /*EMPTY*/
            {
                ColumnRef *c = makeNode(ColumnRef);
                c->fields = list_make1(makeString("*"));

                ResTarget* r= makeNode(ResTarget);
                r->name = NULL;
                r->indirection = NIL;
                r->val = (Node *)c;
                $$ = list_make1((Node*)r);
            }
        ;
export_select:
            AS SelectStmt                                  {$$ = $2;}
            | AS VHistoricalSelectStmt                     {$$ = $2;}
            | FROM qualified_name opt_export_target_list
              {
                  SelectStmt *n = makeNode(SelectStmt);
                  n->targetList = $3;
                  RangeVar* rv = (RangeVar*) $2;
                  rv->inhOpt = INH_DEFAULT;
                  rv->alias = NULL;
                  n->fromClause = list_make1((Node*)rv);
                  $$ = (Node*)n;
              }
        ;
export_relation: any_name
              {
                    RangeVar *r = makeNode(RangeVar);

                    /* can't use qualified_name, sigh */
                    switch (list_length($1))
                    {
                        case 1:
                            ereport(ERROR,
                                (errcode(ERRCODE_SYNTAX_ERROR),
                                     errmsg("Database name is required (too few dotted names): %s",
                                     NameListToString($1))));
                            break;
                        case 2:
                            r->catalogname = strVal(linitial($1));
                            r->schemaname = NULL;
                            r->relname = strVal(lsecond($1));
                            break;
                        case 3:
                            r->catalogname = strVal(linitial($1));
                            r->schemaname = strVal(lsecond($1));
                            r->relname = strVal(lthird($1));
                            break;
                        default:
                            ereport(ERROR,
                                    (errcode(ERRCODE_SYNTAX_ERROR),
                                     errmsg("Improper qualified name (too many dot): %s",
                                            NameListToString($1))));
                            break;
                    }
                    $$ = r;
              }
        ;



/*****************************************************************************
 *
 *        QUERY:
 *                DELETE STATEMENTS
 *
 *****************************************************************************/

DeleteStmt: DELETE_P hint_clause FROM relation_expr where_clause
                {
                    DeleteStmt *n = makeNode(DeleteStmt);
                    n->hintClause = $2;
                    n->relation = $4;
                    n->whereClause = $5;
                    $$ = (Node *)n;
                }
        ;

LockStmt:    LOCK_P opt_table qualified_name_list opt_lock opt_nowait
                {
                    LockStmt *n = makeNode(LockStmt);

                    n->relations = $3;
                    n->mode = $4;
                    n->nowait = $5;
                    $$ = (Node *)n;
                }
        ;

opt_lock:    IN_P lock_type MODE             { $$ = $2; }
            | /*EMPTY*/                        { $$ = LK_X; }
        ;

lock_type:  SHARE                  { $$ = LK_S; }
            | INSERT               { $$ = LK_I; }
            | INSERT VALIDATE      { $$ = LK_IV; }
            | SHARE INSERT         { $$ = LK_SI; }
            | EXCLUSIVE            { $$ = LK_X; }
            | NOT DELETE_P         { $$ = LK_T; }
            | USAGE                { $$ = LK_U; }
            | OWNER                { $$ = LK_O; }
        ;

opt_nowait:    NOWAIT             { $$ = TRUE; }
            | /*EMPTY*/                        { $$ = FALSE; }
        ;


/*****************************************************************************
 *
 *        QUERY:
 *                UpdateStmt (UPDATE)
 *
 *****************************************************************************/

UpdateStmt: UPDATE      hint_clause relation_expr_opt_alias
            SET update_target_list
            from_clause
            where_clause
                {
                    UpdateStmt *n = makeNode(UpdateStmt);
                    n->hintClause = $2;
                    n->relation = $3;
                    n->targetList = $5;
                    n->fromClause = $6;
                    n->whereClause = $7;
                    $$ = (Node *)n;
                }
        ;


/*****************************************************************************
 *
 *        QUERY:
 *                CURSOR STATEMENTS
 *
 *****************************************************************************/
DeclareCursorStmt: DECLARE name cursor_options CURSOR opt_hold FOR SelectStmt
                {
                    DeclareCursorStmt *n = makeNode(DeclareCursorStmt);
                    n->portalname = $2.str;
                    n->options = $3;
                    n->query = $7;
                    if ($5)
                        n->options |= CURSOR_OPT_HOLD;
                    $$ = (Node *)n;
                }
        ;

cursor_options: /*EMPTY*/                    { $$ = 0; }
            | cursor_options NO SCROLL        { $$ = $1 | CURSOR_OPT_NO_SCROLL; }
            | cursor_options SCROLL            { $$ = $1 | CURSOR_OPT_SCROLL; }
            | cursor_options BINARY            { $$ = $1 | CURSOR_OPT_BINARY; }
            | cursor_options INSENSITIVE    { $$ = $1 | CURSOR_OPT_INSENSITIVE; }
        ;

opt_hold: /* EMPTY */                        { $$ = FALSE; }
            | WITH HOLD                        { $$ = TRUE; }
            | WITHOUT HOLD                    { $$ = FALSE; }
        ;

/*****************************************************************************
 *
 *        QUERY:
 *                SELECT STATEMENTS
 *
 *****************************************************************************/

/* A complete SELECT statement looks like this.
 *
 * The rule returns either a single SelectStmt node or a tree of them,
 * representing a set-operation tree.
 *
 * There is an ambiguity when a sub-SELECT is within an a_expr and there
 * are excess parentheses: do the parentheses belong to the sub-SELECT or
 * to the surrounding a_expr?  We don't really care, but yacc wants to know.
 * To resolve the ambiguity, we are careful to define the grammar so that
 * the decision is staved off as long as possible: as long as we can keep
 * absorbing parentheses into the sub-SELECT, we will do so, and only when
 * it's no longer possible to do that will we decide that parens belong to
 * the expression.    For example, in "SELECT (((SELECT 2)) + 3)" the extra
 * parentheses are treated as part of the sub-select.  The necessity of doing
 * it that way is shown by "SELECT (((SELECT 2)) UNION SELECT 2)".    Had we
 * parsed "((SELECT 2))" as an a_expr, it'd be too late to go back to the
 * SELECT viewpoint when we see the UNION.
 *
 * This approach is implemented by defining a nonterminal select_with_parens,
 * which represents a SELECT with at least one outer layer of parentheses,
 * and being careful to use select_with_parens, never '(' SelectStmt ')',
 * in the expression grammar.  We will then have shift-reduce conflicts
 * which we can resolve in favor of always treating '(' <select> ')' as
 * a select_with_parens.  To resolve the conflicts, the productions that
 * conflict with the select_with_parens productions are manually given
 * precedences lower than the precedence of ')', thereby ensuring that we
 * shift ')' (and then reduce to select_with_parens) rather than trying to
 * reduce the inner <select> nonterminal to something else.  We use UMINUS
 * precedence for this, which is a fairly arbitrary choice.
 *
 * To be able to define select_with_parens itself without ambiguity, we need
 * a nonterminal select_no_parens that represents a SELECT structure with no
 * outermost parentheses.  This is a little bit tedious, but it works.
 *
 * In non-expression contexts, we use SelectStmt which can represent a SELECT
 * with or without outer parentheses.
 */

SelectStmt: select_no_parens            %prec UMINUS
            | select_with_parens        %prec UMINUS
        ;

select_with_parens:
            '(' select_no_parens ')'                { $$ = $2; }
            | '(' select_with_parens ')'            { $$ = $2; }
        ;

/*
 *    FOR UPDATE may be before or after LIMIT/OFFSET.
 *    In <=7.2.X, LIMIT/OFFSET had to be after FOR UPDATE
 *    We now support both orderings, but prefer LIMIT/OFFSET before FOR UPDATE
 *    2002-08-28 bjm
 */
select_no_parens:
            simple_select                        { $$ = $1; }
            | select_clause sort_clause
                {
                    insertSelectOptions((SelectStmt *) $1, $2, NIL,
                                        NULL, NULL, NULL, NULL, NULL);
                    $$ = $1;
                    }
            | select_clause opt_sort_clause for_update_clause opt_select_limit
                {
                    insertSelectOptions((SelectStmt *) $1, $2, $3,
                                        list_nth($4, 0), list_nth($4, 1),
                                        list_nth($4, 2), list_nth($4, 3), NULL);
                    $$ = $1;
                }
            | select_clause opt_sort_clause select_limit opt_for_update_clause
                {
                    insertSelectOptions((SelectStmt *) $1, $2, $4,
                                        list_nth($3, 0), list_nth($3, 1),
                                        list_nth($3, 2), list_nth($3, 3), NULL);
                    $$ = $1;
                }
           | with_clause select_clause
               {
                   insertSelectOptions((SelectStmt *) $2, NULL, NIL,
                                       NULL, NULL, NULL, NULL, $1);
                   $$ = $2;
               }
           | with_clause select_clause select_limit
               {
                   insertSelectOptions((SelectStmt *) $2, NULL, NIL,
                                       list_nth($3, 0), list_nth($3, 1),
                                       list_nth($3, 2), list_nth($3, 3), $1);
                   $$ = $2;
               }
           | with_clause select_clause sort_clause
               {
                   insertSelectOptions((SelectStmt *) $2, $3, NIL,
                                       NULL, NULL, NULL, NULL, $1);
                   $$ = $2;
           }
          | with_clause select_clause sort_clause select_limit
               {
                   insertSelectOptions((SelectStmt *) $2, $3, NIL,
                                       list_nth($4, 0), list_nth($4, 1),
                                       list_nth($4, 2), list_nth($4, 3), $1);
                   $$ = $2;
           }
            // | select_clause opt_sort_clause select_sample_storage
            //     {




            //         insertSelectOptions((SelectStmt *) $1, $2, NIL,
            //                             NULL, NULL, NULL, NULL);
            //         insertSamplingOptions((SelectStmt *) $1, list_nth($3, 0), list_nth($3, 1), list_nth($3, 2));
            //         $$ = $1;
            //     }

        ;


select_clause:
            simple_select                            { $$ = $1; }
            | select_with_parens                    { $$ = $1; }
        ;

/*
 * This rule parses SELECT statements that can appear within set operations,
 * including UNION, INTERSECT and EXCEPT.  '(' and ')' can be used to specify
 * the ordering of the set operations.    Without '(' and ')' we want the
 * operations to be ordered per the precedence specs at the head of this file.
 *
 * As with select_no_parens, simple_select cannot have outer parentheses,
 * but can have parenthesized subclauses.
 *
 * Note that sort clauses cannot be included at this level --- SQL92 requires
 *        SELECT foo UNION SELECT bar ORDER BY baz
 * to be parsed as
 *        (SELECT foo UNION SELECT bar) ORDER BY baz
 * not
 *        SELECT foo UNION (SELECT bar ORDER BY baz)
 * Likewise FOR UPDATE and LIMIT.  Therefore, those clauses are described
 * as part of the select_no_parens production, not simple_select.
 * This does not limit functionality, because you can reintroduce sort and
 * limit clauses inside parentheses.
 *
 * Select stmt with INTO clause is defined in SelectInfoStmt. It must be used alone.
 */
simple_select:
            SELECT hint_clause opt_distinct target_list select_clauses
                {
                    SelectStmt *n = (SelectStmt*)$5;
                    n->hintClause = list_concat($2, n->hintClause);
                    n->distinctClause = $3;
                    n->targetList = $4;
                    n->into = NIL;
                    n->intoColNames = NIL;
                    n->intoHasOids = DEFAULT_OIDS;
                    n->aliascolnames = NIL;

                    $$ = (Node *)n;
                }
            | select_clause UNION opt_all hint_clause select_clause
                {
                    $$ = makeSetOp(SETOP_UNION, $3, $4, $1, $5, yyloc);
                }
            | select_clause INTERSECT opt_all hint_clause select_clause
                {
                    $$ = makeSetOp(SETOP_INTERSECT, $3, $4, $1, $5, yyloc);
                }
            | select_clause EXCEPT opt_all hint_clause select_clause
                {
                    $$ = makeSetOp(SETOP_EXCEPT, $3, $4, $1, $5, yyloc);
                }
            | select_clause MINUS opt_all hint_clause select_clause
                {
                    $$ = makeSetOp(SETOP_EXCEPT, $3, $4, $1, $5, yyloc);
                }

        ;

/*
 * SQL standard WITH clause looks like:
 *
 * WITH [ RECURSIVE ] <query name> [ (<column>,...) ]
 *        AS (query)
 */
with_clause:
        WITH hint_clause RECURSIVE cte_list
             {
                 ereport(ERROR,
                        (errcode(ERRCODE_SYNTAX_ERROR),
                         errmsg("Recursive With is not supported")));
             }
       | WITH hint_clause cte_list
          {
                  $$ = makeNode(WithClause);
                  $$->hintClause = $2;
                  $$->ctes = $3;
                  $$->recursive = false;
                  $$->materialized = false;
              }
     ;

cte_list:
        common_table_expr                       { $$ = list_make1($1); }
      | cte_list ',' common_table_expr        { $$ = lappend($1, $3); }
      ;

common_table_expr:  name opt_name_list AS '(' SelectStmt ')'
     {
         CommonTableExpr *n = makeNode(CommonTableExpr);
         n->ctename = $1.str;
         n->aliascolnames = $2;
         n->ctequery = $5;
         $$ = (Node *) n;
     }
    ;

/*
 * select_clauses include all clauses after FROM in the query
 *   it's shared by SELECT query and SELECT INTO query
 */
select_clauses:
            from_clause
            where_clause
            timeseries_clause
            group_clause
            having_clause
            window_clause
            pattern_clause
                {
                    SelectStmt *n = makeNode(SelectStmt);
                    n->fromClause = $1;
                    n->whereClause = $2;
                    n->timeseriesClause = $3;
                    n->hintClause = $4.vhints;
                    n->groupClause = $4.grouping_clause;
                    n->havingClause = $5;
                    n->windowClause = $6;
                    n->matchClause = $7;
                    $$ = (Node *)n;
                }
		;
/*
 * Note: SELECT ... INTO ... is another spelling for CREATE TABLE ... AS SELECT ...
 * SELECT ... INTO ... should be used stand-alone, can not be used in subquery or union with others
 */
VSelectIntoStmt:
        SelectIntoStmt { $$ = $1; }
        | EpochOrTime SelectIntoStmt
        {
            CreateStmt* createStmt = (CreateStmt*)$2;
            Node* selectStmt = createStmt->selectStmt;
            VHistoricalSelectStmt* n = makeNode(VHistoricalSelectStmt);
            n->epochSpec = $1;
            n->selectStmt = selectStmt;
            createStmt->selectStmt = (Node*)n;
            $$ = (Node*)createStmt;
        }
        ;

SelectIntoStmt:
            simple_select_into
                { $$ = $1; }
            | simple_select_into sort_clause
                {
                    SelectStmt* selectStmt = (SelectStmt*)((CreateStmt*)$1)->selectStmt;
                    insertSelectOptions(selectStmt, $2, NIL,
                                        NULL, NULL, NULL, NULL, NULL);
                    $$ = $1;
                }
            | simple_select_into opt_sort_clause for_update_clause opt_select_limit
                {
                    SelectStmt* selectStmt = (SelectStmt*)((CreateStmt*)$1)->selectStmt;
                    insertSelectOptions(selectStmt, $2, $3,
                                        list_nth($4, 0), list_nth($4, 1),
                                        list_nth($4, 2), list_nth($4, 3), NULL);
                    $$ = $1;
                }
            | simple_select_into opt_sort_clause select_limit opt_for_update_clause
                {
                    SelectStmt* selectStmt = (SelectStmt*)((CreateStmt*)$1)->selectStmt;
                    insertSelectOptions(selectStmt, $2, $4,
                                        list_nth($3, 0), list_nth($3, 1),
                                        list_nth($3, 2), list_nth($3, 3), NULL);
                    $$ = $1;
                }
        ;

simple_select_into:
            SELECT hint_clause opt_distinct target_list
            INTO OptTempTableName OnCommitOption select_clauses
                {
                    //select query
                    SelectStmt *n = (SelectStmt*)$8;
                    n->hintClause = list_concat($2, n->hintClause);
                    n->distinctClause = $3;
                    n->targetList = $4;
                    n->into = NIL;
                    n->intoColNames = NIL;
                    n->intoHasOids = DEFAULT_OIDS;
                    n->aliascolnames = NIL;

                    //add selectQuery into CreateStmt, convert to CTAS
                    CreateStmt *c = makeNode(CreateStmt);
                    c->exists_ok = FALSE;
                    c->relation = $6;
                    c->tableElts = NIL;
                    c->inhRelations = NIL;
                    c->constraints = NIL;
                    c->hasoids = NIL;
                    c->oncommit = $7;
                    c->tablespacename = NULL;
                    c->selectStmt = (Node *)n;
                    c->hintClause = NULL;
                    c->partitionExpr = NIL;
                    c->partnGroupExpr = NIL;
                    c->skip_permissions = false;
                    c->flextable = false;
                    c->inheritPrivileges = DEFAULT_INHERIT_PRIVILEGES;

                    //add default projection
                    VCreateProjectionStmt *v = makeNode(VCreateProjectionStmt);
                    v->relation = NULL;
                    v->sortClause=NULL;
                    v->encodeClause=NULL;
                    v->segmentation=NULL;
                    v->ksafe=KSAFE_NONE;
                    v->createType = PROJ_INSTANT;
                    c->projStmt = (Node *)v;

                    $$ = (Node *)c;
                }
        ;

/*
 * Redundancy here is needed to avoid shift/reduce conflicts,
 * since TEMP is not a reserved word.  See also OptTemp.
 */
OptTempTableName:
            TEMPORARY opt_table qualified_name
                {
                    $$ = $3;
                    $$->temptype = DEFAULT_TEMP;
                }
            | TEMP opt_table qualified_name
                {
                    $$ = $3;
                    $$->temptype = DEFAULT_TEMP;
                }
            | LOCAL TEMPORARY opt_table qualified_name
                {
                    $$ = $4;
                    $$->temptype = LOCAL_TEMP;
                }
            | LOCAL TEMP opt_table qualified_name
                {
                    $$ = $4;
                    $$->temptype = LOCAL_TEMP;
                }
            | GLOBAL TEMPORARY opt_table qualified_name
                {
                    $$ = $4;
                    $$->temptype = GLOBAL_TEMP;
                }
            | GLOBAL TEMP opt_table qualified_name
                {
                    $$ = $4;
                    $$->temptype = GLOBAL_TEMP;
                }
            | TABLE qualified_name
                {
                    $$ = $2;
                    $$->temptype = NOT_TEMP;
                }
            | qualified_name
                {
                    $$ = $1;
                    $$->temptype = NOT_TEMP;
                }
        ;

opt_table:    TABLE                                    {}
            | /*EMPTY*/                                {}
        ;

opt_all:    ALL                                        { $$ = TRUE; }
            | DISTINCT                                { $$ = FALSE; }
            | /*EMPTY*/                                { $$ = FALSE; }
        ;

/* We use (NIL) as a placeholder to indicate that all target expressions
 * should be placed in the DISTINCT list during parsetree analysis.
 */
opt_distinct:
            DISTINCT                                { $$ = list_make1(NIL); }
            | DISTINCT ON '(' expr_list ')'            { $$ = $4; }
            | ALL                                    { $$ = NIL; }
            | /*EMPTY*/                                { $$ = NIL; }
        ;

opt_sort_clause:
            sort_clause                                { $$ = $1;}
            | /*EMPTY*/                                { $$ = NIL; }
        ;

sort_clause:
            ORDER BY sortby_list                    { $$ = $3; }
        ;

sortby_list: sortby                       { $$ = list_make1($1);  }
             |sortby_list ',' sortby      { $$ = lappend($1, $3); }
        ;

sortby:        a_expr USING qual_all_Op
                {
                    $$ = makeNode(SortBy);
                    $$->node = $1;
                    $$->sortby_kind = SORT_USING;
                    $$->useOp = $3;
                }
             | a_expr asc_desc
                {
                    $$ = makeNode(SortBy);
                    $$->node = $1;
                    $$->sortby_kind = $2;
                    $$->useOp = NIL;
                }
       ;

asc_desc:     ASC                        { $$ = SORT_ASCEND;  }
              | DESC                     { $$ = SORT_DESCEND; }
              | /* empty, use default */ { $$ = SORT_ASCEND;  }
  ;

// NOTE: whenever this is re-enabled, update the sample_storage.sql and sample_storage_3nodes.sql tests to not use optimizer directives but use this syntax instead. available at SVN r56927.
// select_sample_storage:
//             SAMPLE STORAGE select_sample_storage_count
//                 { $$ = list_make3($3,NULL,NULL); }
//             | SAMPLE STORAGE select_sample_storage_percent PERCENT
//                { $$ = list_make3(NULL,$3,NULL); }
//             | SAMPLE STORAGE select_sample_storage_count ',' select_sample_storage_band_count
//                 { $$ = list_make3($3,NULL,$5); }
//             | SAMPLE STORAGE select_sample_storage_percent PERCENT ',' select_sample_storage_band_count
//                 { $$ = list_make3(NULL,$3,$6); }

//         ;

// opt_select_sample_storage:
//             select_sample_storage                            { $$ = $1; }
//             | /* EMPTY */
//                     { $$ = list_make3(NULL,NULL,NULL); }
//         ;

// select_sample_storage_count:
//             a_expr                                    { $$ = $1; }
//         ;

// select_sample_storage_percent:
//             a_expr                                    { $$ = $1; }
//         ;

// select_sample_storage_band_count:
//             a_expr                                    { $$ = $1; }
//         ;

select_limit:
            LIMIT select_limit_value OFFSET select_offset_value
                { $$ = list_make4($4, $2, NULL, NULL); }
            | OFFSET select_offset_value LIMIT select_limit_value
                { $$ = list_make4($2, $4, NULL, NULL); }
            | LIMIT select_limit_value
                { $$ = list_make4(NULL, $2, NULL, NULL); }
            | OFFSET select_offset_value
                { $$ = list_make4($2, NULL, NULL, NULL); }
            | LIMIT select_limit_value ',' select_offset_value
                {
                    /* Disabled because it was too confusing, bjm 2002-02-18 */
                    ereport(ERROR,
                            (errcode(ERRCODE_SYNTAX_ERROR),
                             errmsg("LIMIT #,# syntax is not supported"),
                             errhint("Use separate LIMIT and OFFSET clauses")));
                }
             // Top-k
             | LIMIT IntegerOnly OVER '(' partition_clause orderby_clause ')'
                {
                    if ($2->val.ival <= 0)
                        ereport (ERROR,
                                 (errcode(ERRCODE_SYNTAX_ERROR),
                                  errmsg("Limit in Top-K query must be a positive number")));

                    if (IsA(linitial($5), VPartitionBatch) ||
                        IsA(linitial($5), VPartitionPrepass))
                        ereport (ERROR,
                                 (errcode(ERRCODE_SYNTAX_ERROR),
                                  errmsg("Batch/Prepass may only be used in the over(...) clause of a user defined transform in a Live Aggregate Projection")));

                    $$ = list_make4(NULL, makeIntConst($2->val.ival), $5, $6);
                }
        ;

opt_select_limit:
            select_limit                            { $$ = $1; }
            | /* EMPTY */
                    { $$ = list_make4(NULL,NULL,NULL,NULL); }
        ;

select_limit_value:
            a_expr                                    { $$ = $1; }
            | ALL
                {
                    /* LIMIT ALL is represented as a NULL constant */
                    A_Const *n = makeNode(A_Const);
                    n->val.type = T_Null;
                    $$ = (Node *)n;
                }
        ;

select_offset_value:
            a_expr                                    { $$ = $1; }
        ;

/*
 *    jimmy bell-style recursive queries aren't supported in the
 *    current system.
 *
 *    ...however, recursive addattr and rename supported.  make special
 *    cases for these.
 */

group_clause:
            GROUP_P BY hint_clause groupby_expr_list {
				$$.vhints = $3; 
            	$$.grouping_clause = $4;
			}	
            | /*EMPTY*/                                { 
            	$$.vhints = NIL; 
            	$$.grouping_clause = NIL; 
            	}
        ;

having_clause:
            HAVING a_expr                            { $$ = $2; }
            | /*EMPTY*/                                { $$ = NULL; }
        ;

for_update_clause:
            FOR UPDATE update_list                    { $$ = $3; }
            | FOR READ ONLY                            { $$ = NULL; }
        ;

opt_for_update_clause:
            for_update_clause                        { $$ = $1; }
            | /* EMPTY */                            { $$ = NULL; }
        ;

update_list:
            OF qualified_name_list                            { $$ = $2; }
            | /* EMPTY */                            { $$ = list_make1(NULL); }
        ;

hint_clause:
            HINT_BEGIN hint_rest                    { $$ = $2; }
            | /* EMPTY */                           { $$ = NIL; }
        ;

hint_rest:
            hints HINT_END                           { $$ = $1; }
            | error HINT_END                         { $$ = NIL; }
            ;

hints:
            hint                                     { if ($1 != NULL)
                                                         $$ = list_make1($1);
                                                       else
                                                         $$ = NIL; }
            | hints ',' hint                         { if ($3 != NIL)
                                                         $$ = lappend($1, $3); 
                                                       else
                                                         $$ = $1; }
            ;

hint:
            hint_name opt_hint_list
            {
                VHint* n = makeNode(VHint);
                n->hintName = $1.str;
                n->argList = $2;
                $$ = (Node*)n;
            }
            | /* EMPTY */                           { $$ = NULL; }
        ;

groupby_expr_list:
            groupby_expr                          { $$ = list_make1($1); }
            | groupby_expr_list ',' groupby_expr  { $$ = lappend($1, $3); }
            ;

groupby_expr:
            a_expr { $$ = $1;}
            |  rollup_clause  { $$ = $1; }
            |  cube_clause  { $$ = $1; }
            |  grouping_sets_clause { $$ = $1; }
        ;

rollup_clause: 
            ROLLUP '(' grouping_expr_list ')' 
            {
                MultiLevelAgg *n = makeNode(MultiLevelAgg);
                n->clauseType = ROLLUP_MLA_TYPE;
                n->groupinglist = $3;
                $$ = (Node *) n;
            }
        ;

cube_clause: 
            CUBE '(' grouping_expr_list ')' 
            {
                MultiLevelAgg *n = makeNode(MultiLevelAgg);
                n->clauseType = CUBE_MLA_TYPE;
                n->groupinglist = $3;
                $$ = (Node *) n;
            }
        ;

grouping_sets_clause: GROUPING SETS '(' grouping_set_expr_list ')'
            {
                MultiLevelAgg *n = makeNode(MultiLevelAgg);
                n->clauseType = GROUPING_SETS_MLA_TYPE;
                n->groupinglist = $4;
                $$ = (Node *) n;
            }
        ;

grouping_expr_list:
           grouping_expr  { $$ = list_make1($1); }
           | grouping_expr_list ',' grouping_expr  { $$ = lappend($1, $3); }
           ;

grouping_expr:
            ad_expr { $$ = list_make1($1); }
            | '(' expr_list ')' { $$ = $2; }  %prec IS
            ;

grouping_set_expr_list:
           grouping_set_expr  { $$ = list_make1($1); }
           | grouping_set_expr_list ',' grouping_set_expr  { $$ = lappend($1, $3); }
           ;

grouping_set_expr:
            ad_expr { $$ = list_make1($1); }
            | rollup_clause  { $$ = list_make1($1); }
            | cube_clause  { $$ = list_make1($1); }
            | '(' ')' { $$ = NIL; }
            | '(' expr_list ')' { $$ = $2; }  %prec IS
            ;


/*****************************************************************************
 *
 *    clauses common to all Optimizable Stmts:
 *        from_clause        - allow list of both JOIN expressions and table names
 *        where_clause    - qualifications for joins or restrictions
 *
 *****************************************************************************/

from_clause:
            FROM from_list                            { $$ = $2; }
            | /*EMPTY*/                                { $$ = NIL; }
        ;

from_list:
            table_ref                                { $$ = list_make1($1); }
            | from_list ',' table_ref                { $$ = lappend($1, $3); }
        ;

/*
 * table_ref is where an alias clause can be attached.    Note we cannot make
 * alias_clause have an empty production because that causes parse conflicts
 * between table_ref := '(' joined_table ')' alias_clause
 * and joined_table := '(' joined_table ')'.  So, we must have the
 * redundant-looking productions here instead.
 */
table_ref:    relation_expr hint_clause
                {
                    $1->optHints = $2;
                    $$ = (Node *) $1;
                }
            | relation_expr table_sample hint_clause
                {
                    $1->optHints = $3;
                    $1->tablesample = (Node *)$2;
                    $$ = (Node *) $1;
                }
            | relation_expr alias_clause hint_clause
                {
                    $1->alias = $2;
                    $1->optHints = $3;
                    $$ = (Node *) $1;
                }
           | relation_expr table_sample alias_clause hint_clause
                {
                    $1->alias = $3;
                    $1->optHints = $4;
                    $1->tablesample = (Node *)$2;
                    $$ = (Node *) $1;
                }

            | func_table
                {
                    RangeFunction *n = makeNode(RangeFunction);
                    n->funccallnode = $1;
                    n->coldeflist = NIL;
                    $$ = (Node *) n;
                }
            | func_table alias_clause
                {
                    RangeFunction *n = makeNode(RangeFunction);
                    n->funccallnode = $1;
                    n->alias = $2;
                    n->coldeflist = NIL;
                    $$ = (Node *) n;
                }
            | func_table AS '(' TableFuncElementList ')'
                {
                    RangeFunction *n = makeNode(RangeFunction);
                    n->funccallnode = $1;
                    n->coldeflist = $4;
                    $$ = (Node *) n;
                }
            | func_table AS ColId '(' TableFuncElementList ')'
                {
                    RangeFunction *n = makeNode(RangeFunction);
                    Alias *a = makeNode(Alias);
                    n->funccallnode = $1;
                    a->aliasname = $3.str;
                    n->alias = a;
                    n->coldeflist = $5;
                    $$ = (Node *) n;
                }
            | func_table AliasColId '(' TableFuncElementList ')'
                {
                    RangeFunction *n = makeNode(RangeFunction);
                    Alias *a = makeNode(Alias);
                    n->funccallnode = $1;
                    a->aliasname = $2.str;
                    n->alias = a;
                    n->coldeflist = $4;
                    $$ = (Node *) n;
                }
            | select_with_parens
                {
                    /*
                     * The SQL spec does not permit a subselect
                     * (<derived_table>) without an alias clause,
                     * so we don't either.  This avoids the problem
                     * of needing to invent a unique refname for it.
                     * That could be surmounted if there's sufficient
                     * popular demand, but for now let's just implement
                     * the spec and see if anyone complains.
                     * However, it does seem like a good idea to emit
                     * an error message that's better than "syntax error".
                     */
                    ereport(ERROR,
                            (errcode(ERRCODE_SYNTAX_ERROR),
                             errmsg("Subquery in FROM must have an alias"),
                             errhint("For example, FROM (SELECT ...) [AS] foo")));
                    $$ = NULL;
                }
            | select_with_parens alias_clause
                {
                    RangeSubselect *n = makeNode(RangeSubselect);
                    n->subquery = $1;
                    n->alias = $2;
                    $$ = (Node *) n;
                }
            | joined_table
                {
                    $$ = (Node *) $1;
                }
            | '(' joined_table ')' alias_clause
                {
                    $2->alias = $4;
                    $$ = (Node *) $2;
                }
        ;

table_sample:
           TABLESAMPLE '(' FCONST ')'
             {
                 A_Const *n = makeNode(A_Const);
                 n->val.type = T_Float;
                 n->val.val.str = $3;
                 n->typeInfo = SystemTypeName("float8");
                 $$ = (Node *)n;
             }
            | TABLESAMPLE '(' Iconst ')'
             {
                 A_Const *n = makeNode(A_Const);
                 n->val.type = T_Integer;
                 n->val.val.ival = $3;
                 n->typeInfo = SystemTypeName("int8");
                 $$ = (Node *)n;
             }
        ;

/*
 * It may seem silly to separate joined_table from table_ref, but there is
 * method in SQL92's madness: if you don't do it this way you get reduce-
 * reduce conflicts, because it's not clear to the parser generator whether
 * to expect alias_clause after ')' or not.  For the same reason we must
 * treat 'JOIN' and 'join_type JOIN' separately, rather than allowing
 * join_type to expand to empty; if we try it, the parser generator can't
 * figure out when to reduce an empty join_type right after table_ref.
 *
 * Note that a CROSS JOIN is the same as an unqualified
 * INNER JOIN, and an INNER JOIN/ON has the same shape
 * but a qualification expression to limit membership.
 * A NATURAL JOIN implicitly matches column names between
 * tables and the shape is determined by which columns are
 * in common. We'll collect columns during the later transformations.
 */

joined_table:
            '(' joined_table ')'
                {
                    $$ = $2;
                }
            | table_ref CROSS JOIN hint_clause table_ref
                {
                    /* CROSS JOIN is same as unqualified inner join */
                    JoinExpr *n = makeNode(JoinExpr);
                    n->origJoinType = n->jointype = JOIN_INNER;
                    n->isNatural = FALSE;
                    n->isComplex = FALSE;
                    n->isSwapped = FALSE;
                    n->larg = $1;
                    n->rarg = $5;
                    n->optHints = $4;
                    n->vertica_using = NIL;
                    n->quals = NULL;
                    $$ = n;
                }
            | table_ref CROSS COMPLEX JOIN hint_clause table_ref
                {
                    /* CROSS JOIN is same as unqualified inner join */
                    JoinExpr *n = makeNode(JoinExpr);
                    n->origJoinType = n->jointype = JOIN_INNER;
                    n->isNatural = FALSE;
                    n->isComplex = TRUE;
                    n->isSwapped = FALSE;
                    n->larg = $1;
                    n->rarg = $6;
                    n->optHints = $5;
                    n->vertica_using = NIL;
                    n->quals = NULL;
                    $$ = n;
                }
            | table_ref UNIONJOIN hint_clause table_ref
                {
                    /* UNION JOIN is made into 1 token to avoid shift/reduce
                     * conflict against regular UNION keyword.
                     */
                    JoinExpr *n = makeNode(JoinExpr);
                    n->origJoinType = n->jointype = JOIN_UNION;
                    n->isNatural = FALSE;
                    n->isComplex = FALSE;
                    n->isSwapped = FALSE;
                    n->larg = $1;
                    n->rarg = $4;
                    n->optHints = $3;
                    n->vertica_using = NIL;
                    n->quals = NULL;
                    $$ = n;
                }
            | table_ref join_type JOIN hint_clause table_ref join_qual
                {
                    JoinExpr *n = makeNode(JoinExpr);
                    n->origJoinType = n->jointype = $2;
                    n->isNatural = FALSE;
					n->isComplex = FALSE;
					n->isSwapped = FALSE;
                    n->larg = $1;
                    n->rarg = $5;
                    n->optHints = $4;
                    if ($6 != NULL && IsA($6, List))
                        n->vertica_using = (List *) $6; /* USING clause */
                    else
                        n->quals = $6; /* ON clause */
                    $$ = n;
                }
            | table_ref JOIN hint_clause table_ref join_qual
                {
                    /* letting join_type reduce to empty doesn't work */
                    JoinExpr *n = makeNode(JoinExpr);
                    n->origJoinType = n->jointype = JOIN_INNER;
                    n->isNatural = FALSE;
					n->isComplex = FALSE;
					n->isSwapped = FALSE;
                    n->larg = $1;
                    n->rarg = $4;
                    n->optHints = $3;
                    if ($5 != NULL && IsA($5, List))
                        n->vertica_using = (List *) $5; /* USING clause */
                    else
                        n->quals = $5; /* ON clause */
                    $$ = n;
                }
            | table_ref COMPLEX JOIN hint_clause table_ref join_qual
                {
                    /* letting join_type reduce to empty doesn't work */
                    JoinExpr *n = makeNode(JoinExpr);
                    n->origJoinType = n->jointype = JOIN_INNER;
                    n->isNatural = FALSE;
                    n->isComplex = TRUE;
                    n->isSwapped = FALSE;
                    n->larg = $1;
                    n->rarg = $5;
                    n->optHints = $4;
                    if ($6 != NULL && IsA($6, List))
                        n->vertica_using = (List *) $6; /* USING clause */
                    else
                        n->quals = $6; /* ON clause */
                    $$ = n;
                }
            | table_ref NATURAL join_type JOIN hint_clause table_ref
                {
                    JoinExpr *n = makeNode(JoinExpr);
                    n->origJoinType = n->jointype = $3;
                    n->isNatural = TRUE;
					n->isComplex = FALSE;
					n->isSwapped = FALSE;
                    n->larg = $1;
                    n->rarg = $6;
                    n->optHints = $5;
                    n->vertica_using = NIL; /* figure out which columns later... */
                    n->quals = NULL; /* fill later */
                    $$ = n;
                }
            | table_ref NATURAL JOIN hint_clause table_ref
                {
                    /* letting join_type reduce to empty doesn't work */
                    JoinExpr *n = makeNode(JoinExpr);
                    n->origJoinType = n->jointype = JOIN_INNER;
                    n->isNatural = TRUE;
                    n->isComplex = FALSE;
                    n->isSwapped = FALSE;
                    n->larg = $1;
                    n->rarg = $5;
                    n->optHints = $4;
                    n->vertica_using = NIL; /* figure out which columns later... */
                    n->quals = NULL; /* fill later */
                    $$ = n;
                }
             | table_ref join_type_ext JOIN hint_clause table_ref join_qual
                {
                    JoinExpr *n = makeNode(JoinExpr);
                    n->origJoinType = n->jointype = $2;
                    n->isNatural = FALSE;
					n->isComplex = FALSE;
					n->isSwapped = FALSE;
                    n->larg = $1;
                    n->rarg = $5;
                    n->optHints = $4;
                    if ($6 != NULL && IsA($6, List))
                        n->vertica_using = (List *) $6; /* USING clause */
                    else
                        n->quals = $6; /* ON clause */
                    $$ = n;
                }
              | table_ref join_type_ext COMPLEX JOIN hint_clause table_ref join_qual
                {
                    JoinExpr *n = makeNode(JoinExpr);
                    n->origJoinType = n->jointype = $2;
                    n->isNatural = FALSE;
                    n->isComplex = TRUE;
                    n->isSwapped = FALSE;
                    n->larg = $1;
                    n->rarg = $6;
                    n->optHints = $5;
                    if ($7 != NULL && IsA($7, List))
                        n->vertica_using = (List *) $7; /* USING clause */
                    else
                        n->quals = $7; /* ON clause */
                    $$ = n;
                }
        ;

alias_clause:
            AS ColId '(' name_list ')'
                {
                    $$ = makeNode(Alias);
                    $$->aliasname = $2.str;
                    $$->colnames = $4;
                }
            | AS ColId
                {
                    $$ = makeNode(Alias);
                    $$->aliasname = $2.str;
                }
            | AliasColId '(' name_list ')'
                {
                    $$ = makeNode(Alias);
                    $$->aliasname = $1.str;
                    $$->colnames = $3;
                }
            | AliasColId
                {
                    $$ = makeNode(Alias);
                    $$->aliasname = $1.str;
                }
        ;

join_type:    FULL join_outer                            { $$ = JOIN_FULL; }
            | LEFT join_outer                        { $$ = JOIN_LEFT; }
            | RIGHT join_outer                        { $$ = JOIN_RIGHT; }
            | INNER_P                                { $$ = JOIN_INNER; }
        ;

/* OUTER is just noise... */
join_outer: OUTER_P                                    { $$ = NULL; }
            | /*EMPTY*/                                { $$ = NULL; }
        ;
        
/*extended join types: semi, uni, anti, allsemi, nullaware anti*/
join_type_ext:  SEMI  { $$ = JOIN_SEMI; }
                |LEFT SEMI {$$ = JOIN_SEMI; }
                |ANTI  {$$ = JOIN_ANTI; }
                |LEFT ANTI {$$ = JOIN_ANTI; }
                |SEMIALL {$$ = JOIN_SEMI_ALL; }
                |LEFT SEMIALL {$$ = JOIN_SEMI_ALL; }
                |NULLAWARE ANTI {$$ = JOIN_ANTI_NULL_AWARE; }
                |LEFT NULLAWARE ANTI {$$ = JOIN_ANTI_NULL_AWARE; }
                |UNI { $$ = JOIN_UNI; }
        ;
        
/* JOIN qualification clauses
 * Possibilities are:
 *    USING ( column list ) allows only unqualified column names,
 *                          which must match between tables.
 *    ON expr allows more general qualifications.
 *
 * We return USING as a List node, while an ON-expr will not be a List.
 */

join_qual:    USING '(' name_list ')'                    { $$ = (Node *) $3; }
            | ON a_expr                                { $$ = $2; }
        ;


relation_expr:
            qualified_name
                {
                    /* default inheritance */
                    $$ = $1;
                    $$->inhOpt = INH_DEFAULT;
                    $$->alias = NULL;
                }
            | qualified_name '*'
                {
                    /* inheritance query */
                    $$ = $1;
                    $$->inhOpt = INH_YES;
                    $$->alias = NULL;
                }
            | ONLY qualified_name
                {
                    /* no inheritance */
                    $$ = $2;
                    $$->inhOpt = INH_NO;
                    $$->alias = NULL;
                }
            | ONLY '(' qualified_name ')'
                {
                    /* no inheritance, SQL99-style syntax */
                    $$ = $3;
                    $$->inhOpt = INH_NO;
                    $$->alias = NULL;
                }
        ;

/*
 * Given "UPDATE foo set set ...", we have to decide without looking any
 * further ahead whether the first "set" is an alias or the UPDATE's SET
 * keyword.  Since "set" is allowed as a column name both interpretations
 * are feasible.  We resolve the shift/reduce conflict by giving the first
 * relation_expr_opt_alias production a higher precedence than the SET token
 * has, causing the parser to prefer to reduce, in effect assuming that the
 * SET is not an alias.
 */
relation_expr_opt_alias: relation_expr                                  %prec UMINUS
                                {
                                        $$ = $1;
                                }
                        | relation_expr ColId
                                {
                                        Alias *alias = makeNode(Alias);
                                        alias->aliasname = $2.str;
                                        $1->alias = alias;
                                        $$ = $1;
                                }
                        | relation_expr AS ColId
                                {
                                        Alias *alias = makeNode(Alias);
                                        alias->aliasname = $3.str;
                                        $1->alias = alias;
                                        $$ = $1;
                                }
                ;

func_table: func_expr                                { $$ = $1; }
        ;


where_clause:
            WHERE a_expr                            { $$ = $2; }
            | /*EMPTY*/                                { $$ = NULL; }
        ;


TableFuncElementList:
            TableFuncElement
                {
                    $$ = list_make1($1);
                }
            | TableFuncElementList ',' TableFuncElement
                {
                    $$ = lappend($1, $3);
                }
        ;

TableFuncElement:    ColId Typename
                {
                    ColumnDef *n = makeNode(ColumnDef);
                    n->colname = $1.str;
                    n->typeInfo = $2;
                    n->constraints = NIL;
                    n->is_local = true;
                    n->projProp = NULL;
                    $$ = (Node *)n;
                }
        ;

/*****************************************************************************
 *
 *    Type syntax
 *        SQL92 introduces a large amount of type-specific syntax.
 *        Define individual clauses to handle these cases, and use
 *         the generic case to handle regular type-extensible Postgres syntax.
 *        - thomas 1997-10-10
 *
 *****************************************************************************/
TypenameWithTypmod: Typename
                {
                    $$ = $1;
                    // supply default sizes for varchar and varbinary
                    if ($1->typmod == -1 && list_length($1->names) == 2) {
                        const char *nspace = strVal(linitial($1->names));
                        if (!keywordCmp(nspace, "catalog")) {
                            const char *typenm = strVal(lsecond($1->names));
                            if (!keywordCmp(typenm, "varchar") ||
                                !keywordCmp(typenm, "varbinary"))
                            {
                                $1->typmod = VARHDRSZ + getDfltAttrSize();
                            }
                            else if (!keywordCmp(typenm, "long varchar") ||
                                     !keywordCmp(typenm, "long varbinary"))
                            {
                                $1->typmod = VARHDRSZ + getDfltLongAttrSize();
                            }
                            else if (!keywordCmp(typenm, "numeric"))
                            {
                                // Default numeric typmod
                                $1->typmod = TYPMODFROMPRECSCALE(37,15);
                            }
                        }
                    }
                }
            | sequencetype                 {$$ = makeTypeName($1.str);}
            | sequencetype '(' IntegerOnly ')'
                {
                    $$ = makeTypeName($1.str);
                    $$->arrayBounds = list_make1($3);
                }
            | sequencetype '(' IntegerOnly ',' IntegerOnly ',' IntegerOnly ')'
                {
                    $$ = makeTypeName($1.str);
                    $$->arrayBounds = list_make3($3, $5, $7);
                }
            | sequencetype '(' IntegerOnly ',' IntegerOnly ')'
                {
                    $$ = makeTypeName($1.str);
                    $$->arrayBounds = list_make2($3, $5);
                }

        ;

Typename:    SimpleTypename opt_array_bounds
                {
                    $$ = $1;
                    $$->arrayBounds = $2;
                }
            | SETOF SimpleTypename opt_array_bounds
                {
                    $$ = $2;
                    $$->arrayBounds = $3;
                    $$->setof = TRUE;
                }
            | SimpleTypename ARRAY '[' Iconst ']'
                {
                    /* SQL99's redundant syntax */
                    $$ = $1;
                    $$->arrayBounds = list_make1(makeInteger($4));
                }
            | SETOF SimpleTypename ARRAY '[' Iconst ']'
                {
                    /* SQL99's redundant syntax */
                    $$ = $2;
                    $$->arrayBounds = list_make1(makeInteger($5));
                    $$->setof = TRUE;
                }
        ;

opt_array_bounds:
            opt_array_bounds '[' ']'
                    {  $$ = lappend($1, makeInteger(-1)); }
            | opt_array_bounds '[' Iconst ']'
                    {  $$ = lappend($1, makeInteger($3)); }
            | /*EMPTY*/
                    {  $$ = NIL; }
        ;

/*
 * XXX ideally, the production for a qualified typename should be ColId attrs
 * (there's no obvious reason why the first name should need to be restricted)
 * and should be an alternative of GenericType (so that it can be used to
 * specify a type for a literal in AExprConst).  However doing either causes
 * reduce/reduce conflicts that I haven't been able to find a workaround
 * for.  FIXME later.
 */
SimpleTypename:
            GenericType                                { $$ = $1; }
            | Numeric                                { $$ = $1; }
            | Binary                                 { $$ = $1; }
            | Bit                                    { $$ = $1; }
            | Character                                { $$ = $1; }
            | ConstDatetime                            { $$ = $1; }
            | ConstInterval interval_qualifier
                {
                    $$ = (INTERVAL_RANGE($2) & INTERVAL_YEAR2MONTH) ?
                        SystemTypeName("intervalym") : $1;

                    if (INTERVAL_RANGE($2) == 0) // if default qualifier
                        $$->typmod = INTERVAL_TYPMOD(INTERVAL_PRECISION($2),
                                                     INTERVAL_DAY2SECOND);
                    else
                        $$->typmod = $2;
                }
            | ConstIntervalYM interval_qualifier
                {
                    if (INTERVAL_RANGE($2) == 0) // if default qualifier
                        $$->typmod = INTERVALYM_DFLT;
                    else if (INTERVAL_RANGE($2) & ~INTERVAL_YEAR2MONTH)
                        ereport(ERROR,
                                (errcode(ERRCODE_SYNTAX_ERROR),
                                 errmsg("Conflicting INTERVAL subtypes")));
                    else
                        $$->typmod = $2;
                 }
            | type_name attrs
                {
                    $$ = makeNode(TypeName);
                    $$->names = lcons(makeStr($1), $2);
                    $$->typmod = -1;
                }
            | Uuid                                   { $$ = $1; }
        ;

/* We have a separate ConstTypename to allow defaulting fixed-length
 * types such as CHAR(), BINARY() and BIT() to an unspecified length.
 * SQL9x requires that these default to a length of one, but this
 * makes no sense for constructs like CHAR 'hi', BINARY '0xFF' and BIT '0101',
 * where there is an obvious better choice to make.
 * Note that ConstInterval/YM is not included here since it must
 * be pushed up higher in the rules to accomodate the postfix
 * options (e.g. INTERVAL '1' YEAR).
 */
ConstTypename:
            GenericTypeWithoutLength                 { $$ = $1; }
            | Numeric                                { $$ = $1; }
            | ConstBinary                             { $$ = $1; }
            | ConstBit                                { $$ = $1; }
            | ConstCharacter                        { $$ = $1; }
            | ConstDatetime                            { $$ = $1; }
            | Uuid                                  { $$ = $1; }
        ;

GenericType:
           GenericTypeWithLength                    { $$ = $1; }
           | GenericTypeWithoutLength                    { $$ = $1; }
       ;


GenericTypeWithLength: type_name '(' Iconst ')'
                {
                    $$ = makeTypeName($1.str);
                    $$->typmod = VARHDRSZ + $3;
                }
        ;

GenericTypeWithoutLength: type_name
                {
                    $$ = makeTypeName($1.str);
                    if(keywordCmp($1.str, "char") == 0 ||
                       keywordCmp($1.str, "varchar") == 0 ||
                       keywordCmp($1.str, "long varchar") == 0)
                        $$->typmod = VARHDRSZ + 1;
                    else if(keywordCmp($1.str, "numeric") == 0)
                        $$->typmod = TYPMODFROMPRECSCALE(37,15);
                    else if(keywordCmp($1.str, "uuid") == 0)
                        $$->typmod = UUID_LEN;
                }
        ;

/* SQL92 numeric data types
 * Check FLOAT() precision limits assuming IEEE floating types.
 * - thomas 1997-09-18
 * Provide real DECIMAL() and NUMERIC() implementations now - Jan 1998-12-30
 */
// changed INT and INTEGER to int8 - Bill Mann
Numeric:    INT_P
                {
                    $$ = SystemTypeName("int8");
                }
            | INTEGER
                {
                    $$ = SystemTypeName("int8");
                }
            | SMALLINT
                {
                    $$ = SystemTypeName("int8");
                }
            | TINYINT
                {
                    $$ = SystemTypeName("int8");
                }
            | BIGINT
                {
                    $$ = SystemTypeName("int8");
                }
            | REAL
                {
                    $$ = SystemTypeName("float8");
                }
            | FLOAT_P opt_float
                {
                    $$ = $2;
                }
            | DOUBLE_P PRECISION
                {
                    $$ = SystemTypeName("float8");
                }
            | DECIMAL_P opt_decimal
                {
                    $$ = SystemTypeName("numeric");
                    $$->typmod = $2;
                }
            | DEC opt_decimal
                {
                    $$ = SystemTypeName("numeric");
                    $$->typmod = $2;
                }
            | NUMERIC opt_numeric
                {
                    $$ = SystemTypeName("numeric");
                    $$->typmod = $2;
                }
            | MONEY opt_numeric
                {
                    $$ = SystemTypeName("numeric");
                    $$->typmod = $2 > 0 ? $2 : TYPMODFROMPRECSCALE(18,4);
                }
            | NUMBER_P opt_numeric
                {
                    $$ = SystemTypeName("numeric");
                    $$->typmod = $2 > 0 ? $2 : TYPMODFROMPRECSCALE(38,0);
                }
            | BOOLEAN_P
                {
                    $$ = SystemTypeName("bool");
                }
        ;

opt_float:    '(' Iconst ')'
                {
                    if ($2 < 1)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("Precision for type float must be at least 1 bit")));
                    else if ($2 <= 24)
                        $$ = SystemTypeName("float8");
                    else if ($2 <= 53)
                        $$ = SystemTypeName("float8");
                    else
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("Precision for type float must be less than 54 bits")));
                }
            | /*EMPTY*/
                {
                    $$ = SystemTypeName("float8");
                }
        ;

opt_numeric:
            '(' Iconst ',' Iconst ')'
                {
                    if ($2 < 1 || $2 > NUMERIC_MAX_PRECISION)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("NUMERIC precision %lld must be between 1 and %d",
                                        $2, NUMERIC_MAX_PRECISION)));
                    if ($4 < 0 || $4 > $2)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("NUMERIC scale %lld must be between 0 and precision %lld",
                                        $4, $2)));

                    $$ = (($2 << 16) | $4) + VARHDRSZ;
                }
            | '(' Iconst ')'
                {
                    if ($2 < 1 || $2 > NUMERIC_MAX_PRECISION)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("NUMERIC precision %lld must be between 1 and %d",
                                        $2, NUMERIC_MAX_PRECISION)));

                    $$ = ($2 << 16) + VARHDRSZ;
                }
            | /*EMPTY*/
                {
                    /* Insert "-1" meaning "no limit" */
                    $$ = -1;
                }
        ;

opt_decimal:
            '(' Iconst ',' Iconst ')'
                {
                    if ($2 < 1 || $2 > NUMERIC_MAX_PRECISION)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("DECIMAL precision %lld must be between 1 and %d",
                                        $2, NUMERIC_MAX_PRECISION)));
                    if ($4 < 0 || $4 > $2)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("DECIMAL scale %lld must be between 0 and precision %lld",
                                        $4, $2)));

                    $$ = (($2 << 16) | $4) + VARHDRSZ;
                }
            | '(' Iconst ')'
                {
                    if ($2 < 1 || $2 > NUMERIC_MAX_PRECISION)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("DECIMAL precision %lld must be between 1 and %d",
                                        $2, NUMERIC_MAX_PRECISION)));

                    $$ = ($2 << 16) + VARHDRSZ;
                }
            | /*EMPTY*/
                {
                    /* Insert "-1" meaning "no limit" */
                    $$ = -1;
                }
        ;


/*
 * binary-field data type
 * The following implements BINARY(), VARBINARY() and BYTEA().
 */
Binary:       BinaryWithLength
                {
                    $$ = $1;
                }
            | BinaryWithoutLength
                {
                    $$ = $1;
                }
        ;

/* ConstBinary is like Binary except "BINARY" defaults to unspecified length */
/* See notes for ConstCharacter, which addresses same issue for "CHAR" */
ConstBinary:    BinaryWithLength
                {
                    $$ = $1;
                }
              | BinaryWithoutLength
                {
                    $$ = $1;
                    $$->typmod = -1;
                }
        ;

BinaryWithLength:
            binary '(' Iconst ')'
                {
                    $$ = SystemTypeName($1.str);
                    if ($3 < 1)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("Length for type %s must be at least 1",
                                        $1.str)));
                    else {
                        uint32 MaxAttrSize;
                        if (keywordCmp($1.str, "long varbinary") == 0) {
                            MaxAttrSize = getComputedMaxLongAttrSize();
                        } else {
                            MaxAttrSize = getComputedMaxAttrSize();
                        }
                        if ($3 > MaxAttrSize) {
                            ereport(ERROR,
                                    (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                     errmsg("Length for type %s cannot exceed %d",
                                            $1.str, MaxAttrSize)));
                        }
                    }
                        $$->typmod = VARHDRSZ + $3;
                }
        ;

BinaryWithoutLength:
            binary
                {
                    $$ = SystemTypeName($1.str);
                    if (keywordCmp($1.str, "binary") == 0) {
                        // BINARY defaults to BINARY(1)
                        $$->typmod = VARHDRSZ + 1;
                    } else {
                        $$->typmod = -1;
                    }
                }
        ;

binary:     BINARY opt_varying
               { $$ = $2 ? ctString("varbinary") : ctString("binary"); }
          | VARBINARY
               { $$ = ctString("varbinary"); }
          | RAW
               { $$ = ctString("varbinary"); }
          | BYTEA
               { $$ = ctString("varbinary"); }
          | LONG VARBINARY
                 {
                   if (!getUseLongStrings()) {
                          ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("Invalid or unavailable type 'LONG VARBINARY'")));
                    }
                    $$ = ctString("long varbinary");
                }
        ;

/*
 * SQL92 bit-field data types
 * The following implements BIT() and BIT VARYING().
 */
Bit:        BitWithLength
                {
                    $$ = $1;
                }
            | BitWithoutLength
                {
                    $$ = $1;
                }
        ;

/* ConstBit is like Bit except "BIT" defaults to unspecified length */
/* See notes for ConstCharacter, which addresses same issue for "CHAR" */
ConstBit:    BitWithLength
                {
                    $$ = $1;
                }
            | BitWithoutLength
                {
                    $$ = $1;
                    $$->typmod = -1;
                }
        ;

BitWithLength:
            BIT opt_varying '(' Iconst ')'
                {
                    char *typname;

                    typname = $2 ? "varbit" : "bit";
                    $$ = SystemTypeName(typname);
                    if ($4 < 1)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("Length for type %s must be at least 1",
                                        typname)));
                    else if ($4 > (getComputedMaxAttrSize() * BITS_PER_BYTE))
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("Length for type %s cannot exceed %d",
                                        typname, getComputedMaxAttrSize() * BITS_PER_BYTE)));
                    $$->typmod = $4;
                }
        ;

BitWithoutLength:
            BIT opt_varying
                {
                    /* bit defaults to bit(1), varbit to no limit */
                    if ($2)
                    {
                        $$ = SystemTypeName("varbit");
                        $$->typmod = -1;
                    }
                    else
                    {
                        $$ = SystemTypeName("bit");
                        $$->typmod = 1;
                    }
                }
        ;


/*
 * SQL92 character data types
 * The following implements CHAR() and VARCHAR[2]().
 */
Character:  CharacterWithLength
                {
                    $$ = $1;
                }
            | CharacterWithoutLength
                {
                    $$ = $1;
                }
        ;

ConstCharacter:  CharacterWithLength
                {
                    $$ = $1;
                }
            | CharacterWithoutLength
                {
                    /* Length was not specified so allow to be unrestricted.
                     * This handles problems with fixed-length (bpchar) strings
                     * which in column definitions must default to a length
                     * of one, but should not be constrained if the length
                     * was not specified.
                     */
                    $$ = $1;
                    $$->typmod = -1;
                }
        ;

CharacterWithLength:  character '(' Iconst ')'
                {
                    $$ = SystemTypeName($1.str);

                    if ($3 < 1)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("Length for type %s must be at least 1",
                                        $1.str)));
                    else {
                        uint32 MaxAttrSize;
                        if (keywordCmp($1.str, "long varchar") == 0) {
                            MaxAttrSize = getComputedMaxLongAttrSize();
                        } else {
                            MaxAttrSize = getComputedMaxAttrSize();
                        }
                        if ($3 > MaxAttrSize)
                            ereport(ERROR,
                                    (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                     errmsg("Length for type %s cannot exceed %d",
                                            $1.str, MaxAttrSize)));
                                }
                    /* we actually implement these like a varlen, so
                     * the first 4 bytes is the length. (the difference
                     * between these and "varchar" is that we blank-pad and
                     * truncate where necessary)
                     */
                    $$->typmod = VARHDRSZ + $3;
                }
        ;

CharacterWithoutLength:     character
                {
                    $$ = SystemTypeName($1.str);

                    /* char defaults to char(1) */
                    if (keywordCmp($1.str, "char") == 0)
                        $$->typmod = VARHDRSZ + 1;
                    else {
                        $$->typmod = -1;
                    }
                }
        ;

character:    CHARACTER opt_varying
                  { $$ = $2 ? ctString("varchar"): ctString("char"); }
            | CHAR_P opt_varying
                  { $$ = $2 ? ctString("varchar"): ctString("char"); }
            | VARCHAR
                  { $$ = ctString("varchar"); }
            | VARCHAR2
                  { $$ = ctString("varchar"); }
            /* Shipa wants 3.5 compatibility for N'...' */
            | NCHAR opt_varying
                  { $$ = $2 ? ctString("varchar"): ctString("char"); }
            | LONG VARCHAR
                  {
                      if (!getUseLongStrings()) {
                          ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("Invalid or unavailable type 'LONG VARCHAR'")));
                      }
                      $$ = ctString("long varchar");
                  }
        ;

sequencetype:  IDENTITY_P
                    { $$ = ctString("identity"); }
               | AUTO_INC
                    { $$ = ctString("identity"); }
        ;

opt_varying:
            VARYING                                    { $$ = TRUE; }
            | /*EMPTY*/                                { $$ = FALSE; }
        ;

ConstDatetime:
            TIMESTAMP '(' Iconst ')' opt_timezone
                {
                    if ($5)
                        $$ = SystemTypeName("timestamptz");
                    else
                        $$ = SystemTypeName("timestamp");
                    if ($3 < 0)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("TIMESTAMP(%lld)%s precision must not be negative",
                                        $3, ($5 ? " WITH TIME ZONE": ""))));
                    if ($3 > MAX_SECONDS_PRECISION)
                    {
                        ereport(WARNING,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("TIMESTAMP(%lld)%s precision reduced to maximum allowed, %d",
                                        $3, ($5 ? " WITH TIME ZONE": ""),
                                        MAX_SECONDS_PRECISION)));
                        $3 = MAX_SECONDS_PRECISION;
                    }
                    $$->typmod = $3;
                }
            | TIMESTAMP opt_timezone
                {
                    if ($2)
                        $$ = SystemTypeName("timestamptz");
                    else
                        $$ = SystemTypeName("timestamp");
                    /* SQL99 specified a default precision of six
                     * for schema definitions. But for timestamp
                     * literals we don't want to throw away precision
                     * so leave this as unspecified for now.
                     * Later, we may want a different production
                     * for schemas. - thomas 2001-12-07
                     */
                    $$->typmod = -1;
                }
            | DATETIME
                {
                    $$ = SystemTypeName("timestamp");
                    $$->typmod = -1;
                }
            | SMALLDATETIME
                {
                    $$ = SystemTypeName("timestamp");
                    $$->typmod = -1;
                }
            | TIMESTAMPTZ '(' Iconst ')'
                {
                    $$ = SystemTypeName("timestamptz");
                    if ($3 < 0)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("TIMESTAMPTZ(%lld) precision must not be negative",
                                        $3)));
                    if ($3 > MAX_SECONDS_PRECISION)
                    {
                        ereport(WARNING,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("TIMESTAMP(%lld) precision reduced to maximum allowed, %d",
                                        $3, MAX_SECONDS_PRECISION)));
                        $3 = MAX_SECONDS_PRECISION;
                    }
                    $$->typmod = $3;
                }
            | TIMESTAMPTZ
                {
                    $$ = SystemTypeName("timestamptz");
                    /* SQL99 specified a default precision of six
                     * for schema definitions. But for timestamp
                     * literals we don't want to throw away precision
                     * so leave this as unspecified for now.
                     * Later, we may want a different production
                     * for schemas. - thomas 2001-12-07
                     */
                    $$->typmod = -1;
                }
            | TIME '(' Iconst ')' opt_timezone
                {
                    if ($5)
                        $$ = SystemTypeName("timetz");
                    else
                        $$ = SystemTypeName("time");
                    if ($3 < 0)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("TIME(%lld)%s precision must not be negative",
                                        $3, ($5 ? " WITH TIME ZONE": ""))));
                    if ($3 > MAX_SECONDS_PRECISION)
                    {
                        ereport(WARNING,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("TIME(%lld)%s precision reduced to maximum allowed, %d",
                                        $3, ($5 ? " WITH TIME ZONE": ""),
                                        MAX_SECONDS_PRECISION)));
                        $3 = MAX_SECONDS_PRECISION;
                    }
                    $$->typmod = $3;
                }
            | TIME opt_timezone
                {
                    if ($2)
                        $$ = SystemTypeName("timetz");
                    else
                        $$ = SystemTypeName("time");
                    /* SQL99 specified a default precision of zero.
                     * See comments for timestamp above on why we will
                     * leave this unspecified for now. - thomas 2001-12-07
                     */
                    $$->typmod = -1;
                }
            | TIMETZ '(' Iconst ')'
                {
                    $$ = SystemTypeName("timetz");
                    if ($3 < 0)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("TIMETZ(%lld) precision must not be negative",
                                        $3)));
                    if ($3 > MAX_SECONDS_PRECISION)
                    {
                        ereport(WARNING,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("TIMETZ(%lld) precision reduced to maximum allowed, %d",
                                        $3, MAX_SECONDS_PRECISION)));
                        $3 = MAX_SECONDS_PRECISION;
                    }
                    $$->typmod = $3;
                }
            | TIMETZ
                {
                    $$ = SystemTypeName("timetz");
                    /* SQL99 specified a default precision of zero.
                     * See comments for timestamp above on why we will
                     * leave this unspecified for now. - thomas 2001-12-07
                     */
                    $$->typmod = -1;
                }
        ;

ConstInterval:
            INTERVAL                    { $$ = SystemTypeName("interval"); }
        ;

ConstIntervalYM:
            INTERVALYM                  { $$ = SystemTypeName("intervalym"); }
        ;
        
Uuid:
            UUID                        
                {
                    $$ = SystemTypeName("uuid");
                    $$->typmod = UUID_LEN;
                }
        ;

opt_timezone:
            WITH timezone                            { $$ = TRUE; }
            | WITHOUT timezone                       { $$ = FALSE; }
            | /*EMPTY*/                              { $$ = FALSE; }
        ;

opt_minus: '-'                          { $$ = TRUE; }
           | '+'                        { $$ = FALSE; }
           | /*EMPTY*/                  { $$ = FALSE; }
        ;

/* leading_precision limits are enforced here, but the result is ignored */
leading_precision: '(' Iconst ')'
               {   $$ = $2;
                   if ($$ > MAX_LEADING_PRECISION) {
                       $$ = MAX_LEADING_PRECISION;
                       ereport(WARNING,
                               (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                errmsg("INTERVAL leading field precision reduced to %lld", $$)));
                   }
                   if ($$ < 2) {
                       $$ = 2;
                       ereport(WARNING,
                               (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                errmsg("INTERVAL leading field precision increased to %lld", $$)));
                   }
               }
           | /*EMPTY*/ { $$ = -1; }
        ;

seconds_precision: '(' Iconst ')'
               {   if ($2 > MAX_SECONDS_PRECISION) {
                       $2 = MAX_SECONDS_PRECISION;
                       ereport(WARNING,
                               (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                errmsg("INTERVAL SECOND precision reduced to %lld",
                                       $2)));
                   }
                   $$ = INTERVAL_TYPMOD($2, INTERVAL_DAY2SECOND);
               }
            | /*EMPTY*/ { $$ = MAX_SECONDS_PRECISION; }
        ;

/* leading field precision is ignored, */
interval_qualifier:
            YEAR_P leading_precision
                { $$ = INTERVAL_TYPMOD(0, INTERVAL_MASK(YEAR)); }
            | MONTH_P leading_precision
                { $$ = INTERVAL_TYPMOD(0, INTERVAL_MASK(MONTH)); }
            | DAY_P leading_precision
                { $$ = INTERVAL_TYPMOD(0, INTERVAL_MASK(DAY)); }
            | HOUR_P leading_precision
                { $$ = INTERVAL_TYPMOD(0, INTERVAL_MASK(HOUR)); }
            | MINUTE_P leading_precision
                { $$ = INTERVAL_TYPMOD(0, INTERVAL_MASK(MINUTE)); }
            | SECOND_P seconds_precision
                { $$ = INTERVAL_TYPMOD($2, INTERVAL_MASK(SECOND)); }
            | YEAR_P leading_precision TO MONTH_P
                { $$ = INTERVAL_TYPMOD(0, INTERVAL_MASK(YEAR) |
                                       INTERVAL_MASK(MONTH)); }
            | DAY_P leading_precision TO HOUR_P
                { $$ = INTERVAL_TYPMOD(0, INTERVAL_MASK(DAY) |
                                       INTERVAL_MASK(HOUR)); }
            | DAY_P leading_precision TO MINUTE_P
                { $$ = INTERVAL_TYPMOD(0, INTERVAL_MASK(DAY) |
                                       INTERVAL_MASK(HOUR) |
                                       INTERVAL_MASK(MINUTE)); }
            | DAY_P leading_precision TO SECOND_P seconds_precision
                { $$ = INTERVAL_TYPMOD($5, INTERVAL_MASK(DAY) |
                                       INTERVAL_MASK(HOUR) |
                                       INTERVAL_MASK(MINUTE) |
                                       INTERVAL_MASK(SECOND)); }
            | HOUR_P leading_precision TO MINUTE_P
                { $$ = INTERVAL_TYPMOD(0, INTERVAL_MASK(HOUR) |
                                       INTERVAL_MASK(MINUTE)); }
            | HOUR_P leading_precision TO SECOND_P seconds_precision
                { $$ = INTERVAL_TYPMOD($5, INTERVAL_MASK(HOUR) |
                                       INTERVAL_MASK(MINUTE) |
                                       INTERVAL_MASK(SECOND)); }
            | MINUTE_P leading_precision TO SECOND_P seconds_precision
                { $$ = INTERVAL_TYPMOD($5, INTERVAL_MASK(MINUTE) |
                                       INTERVAL_MASK(SECOND)); }
            | seconds_precision
                { $$ = $1; }
        ;


/*****************************************************************************
 *
 *    expression grammar
 *
 *****************************************************************************/

/*
 * General expressions
 * This is the heart of the expression syntax.
 *
 * We have two expression types: a_expr is the unrestricted kind, and
 * b_expr is a subset that must be used in some places to avoid shift/reduce
 * conflicts.  For example, we can't do BETWEEN as "BETWEEN a_expr AND a_expr"
 * because that use of AND conflicts with AND as a boolean operator.  So,
 * b_expr is used in BETWEEN and we remove boolean keywords from b_expr.
 *
 * Note that '(' a_expr ')' is a b_expr, so an unrestricted expression can
 * always be used by surrounding it with parens.
 *
 * c_expr is all the productions that are common to a_expr and b_expr;
 * it's factored out just to eliminate redundant coding.
 */
a_expr:        c_expr                                    { $$ = $1; }
            | interpolate_expr                          { $$ = $1; }
            | a_expr TYPECAST Typename hint_clause
            { $$ = makeTypeCastWithHints($1, $3, $4, false); }
            | a_expr SOFTTYPECAST Typename hint_clause
            { $$ = makeTypeCastWithHints($1, $3, $4, true); }
            | a_expr AT timezone c_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("timezone");
                    // SQL-2008 6.30-6: force to INTERVAL HOUR TO MINUTE
                    if (IsA($4, A_Const)) { // look for an interval constant
                        TypeName *tn = ((A_Const *)$4)->typeInfo;
                        if (tn != NULL) // if an explict interval constant
                            tn->typmod &=
                                INTERVAL_TYPMOD(0,
                                                INTERVAL_MASK(HOUR) |
                                                INTERVAL_MASK(MINUTE) |
                                                INTERVAL_MASK(NEG_INTERVAL));
                    }
                    n->args = list_make2($4, $1);
                    $$ = (Node *) n;
                }
            | a_expr AT LOCAL
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("timezone");
                    n->args = list_make1($1);
                    $$ = (Node *) n;
                }
        /*
         * These operators must be called out explicitly in order to make use
         * of yacc/bison's automatic operator-precedence handling.  All other
         * operator names are handled by the generic productions using "Op",
         * below; and all those operators will have the same precedence.
         *
         * If you add more explicitly-known operators, be sure to add them
         * also to b_expr and to the MathOp list above.
         */
            | '+' a_expr                    %prec UMINUS
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "+", NULL, $2); }
            | '-' a_expr                    %prec UMINUS
                { $$ = doNegate($2); }
/* removed to match PG 8.2.2 and fix 6 ^ -3  -Bill
            | '%' a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "%", NULL, $2); }
            | '^' a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "^", NULL, $2); }
            | a_expr '%'
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "%", $1, NULL); }
            | a_expr '^'
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "^", $1, NULL); }
*/
            | a_expr '+' a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "+", $1, $3); }
            | a_expr '-' a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "-", $1, $3); }
            | a_expr '*' a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "*", $1, $3); }
            | a_expr '/' a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "/", $1, $3); }
            | a_expr Op_SS a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "//", $1, $3); }
            | a_expr '%' a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "%", $1, $3); }
            | a_expr '^' a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "^", $1, $3); }
            | a_expr '<' a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "<", $1, $3); }
            | a_expr '>' a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, ">", $1, $3); }
            | a_expr '=' a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "=", $1, $3); }
            | a_expr Op_Cmp a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, $2.str, $1, $3); }
            | a_expr '|' a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "|", $1, $3); }

            | a_expr qual_Op a_expr                %prec Op
                { $$ = (Node *) makeA_Expr(AEXPR_OP, $2, $1, $3); }
            | qual_Op a_expr                    %prec Op
                { $$ = (Node *) makeA_Expr(AEXPR_OP, $1, NULL, $2); }
            | a_expr '!'
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!", $1, NULL); }

            | a_expr AND a_expr
                { $$ = (Node *) makeA_Expr(AEXPR_AND, NIL, $1, $3); }
            | a_expr OR a_expr
                { $$ = (Node *) makeA_Expr(AEXPR_OR, NIL, $1, $3); }
            | NOT a_expr
                {
                    if (IsA($2, SubLink) && ((SubLink *)$2)->subLinkType == EXISTS_SUBLINK)
                    {
                        /* Make an NOT EXISTS node */
                        /* for EXISTS opername will not be populated, but for NOT EXISTS it would */
                        SubLink *n = (SubLink*)$2;
                        if (n->operName)
                            n->operName = NULL;
                        else
                            n->operName = list_make1(makeString("<>"));
                        $$ = (Node *)n;
                    }
                    else
                    {
                        $$ = (Node *) makeA_Expr(AEXPR_NOT, NIL, NULL, $2);
                    }
                }

            | a_expr LIKE a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "~~", $1, $3); }
            | a_expr NOT LIKE a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!~~", $1, $4); }
            | a_expr ILIKE a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "~~*", $1, $3); }
            | a_expr NOT ILIKE a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!~~*", $1, $4); }
            | a_expr LIKE a_expr ESCAPE a_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("like");
                    n->args = list_make3($1,$3,$5);
                    $$ = (Node *)n;
                }
            | a_expr NOT LIKE a_expr ESCAPE a_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("nlike");
                    n->args = list_make3($1,$4,$6);
                    $$ = (Node *)n;
                }
            | a_expr ILIKE a_expr ESCAPE a_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("ilike");
                    n->args = list_make3($1,$3,$5);
                    $$ = (Node *)n;
                }
            | a_expr NOT ILIKE a_expr ESCAPE a_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("nilike");
                    n->args = list_make3($1,$4,$6);
                    $$ = (Node *)n;
                }

            | a_expr LIKEB a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "~#", $1, $3); }
            | a_expr NOT LIKEB a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!~#", $1, $4); }
            | a_expr ILIKEB a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "~#*", $1, $3); }
            | a_expr NOT ILIKEB a_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!~#*", $1, $4); }
            | a_expr LIKEB a_expr ESCAPE a_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("likeb");
                    n->args = list_make3($1,$3,$5);
                    $$ = (Node *)n;
                }
            | a_expr NOT LIKEB a_expr ESCAPE a_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("nlikeb");
                    n->args = list_make3($1,$4,$6);
                    $$ = (Node *)n;
                }
            | a_expr ILIKEB a_expr ESCAPE a_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("ilikeb");
                    n->args = list_make3($1,$3,$5);
                    $$ = (Node *)n;
                }
            | a_expr NOT ILIKEB a_expr ESCAPE a_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("nilike");
                    n->args = list_make3($1,$4,$6);
                    $$ = (Node *)n;
                }

            | a_expr SIMILAR TO a_expr                %prec SIMILAR
                {
                    A_Const *c = makeNode(A_Const);
                    FuncCall *n = makeNode(FuncCall);
                    c->val.type = T_Null;
                    n->funcname = SystemFuncName("similar_escape");
                    n->args = list_make2($4, (Node *) c);
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "~", $1, (Node *) n);
                }
            | a_expr SIMILAR TO a_expr ESCAPE a_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("similar_escape");
                    n->args = list_make2($4, $6);
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "~", $1, (Node *) n);
                }
            | a_expr NOT SIMILAR TO a_expr            %prec SIMILAR
                {
                    A_Const *c = makeNode(A_Const);
                    FuncCall *n = makeNode(FuncCall);
                    c->val.type = T_Null;
                    n->funcname = SystemFuncName("similar_escape");
                    n->args = list_make2($5, (Node *) c);
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!~", $1, (Node *) n);
                }
            | a_expr NOT SIMILAR TO a_expr ESCAPE a_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("similar_escape");
                    n->args = list_make2($5, $7);
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!~", $1, (Node *) n);
                }

            /* NullTest clause
             * Define SQL92-style Null test clause.
             * Allow two forms described in the standard:
             *    a IS NULL
             *    a IS NOT NULL
             * Allow two SQL extensions
             *    a ISNULL
             *    a NOTNULL
             */
            | a_expr ISNULL
                {
                    if (IsA($1, RowExpr))
                        $$ = makeRowNullTest(IS_NULL, (RowExpr *) $1);
                    else
                    {
                        NullTest *n = makeNode(NullTest);
                        n->arg = (Expr *) $1;
                        n->nulltesttype = IS_NULL;
                        $$ = (Node *)n;
                    }
                }
            | a_expr IS NULL_P
                {
                    if (IsA($1, RowExpr))
                        $$ = makeRowNullTest(IS_NULL, (RowExpr *) $1);
                    else
                    {
                        NullTest *n = makeNode(NullTest);
                        n->arg = (Expr *) $1;
                        n->nulltesttype = IS_NULL;
                        $$ = (Node *)n;
                    }
                }
            | a_expr NOTNULL
                {
                    if (IsA($1, RowExpr))
                        $$ = makeRowNullTest(IS_NOT_NULL, (RowExpr *) $1);
                    else
                    {
                        NullTest *n = makeNode(NullTest);
                        n->arg = (Expr *) $1;
                        n->nulltesttype = IS_NOT_NULL;
                        $$ = (Node *)n;
                    }
                }
            | a_expr IS NOT NULL_P
                {
                    if (IsA($1, RowExpr))
                        $$ = makeRowNullTest(IS_NOT_NULL, (RowExpr *) $1);
                    else
                    {
                        NullTest *n = makeNode(NullTest);
                        n->arg = (Expr *) $1;
                        n->nulltesttype = IS_NOT_NULL;
                        $$ = (Node *)n;
                    }
                }
            | row OVERLAPS row
                {
                    $$ = (Node *)makeOverlaps($1, $3);
                }
            | a_expr IS TRUE_P
                {
                    BooleanTest *b = makeNode(BooleanTest);
                    b->arg = (Expr *) $1;
                    b->booltesttype = IS_TRUE;
                    $$ = (Node *)b;
                }
            | a_expr IS NOT TRUE_P
                {
                    BooleanTest *b = makeNode(BooleanTest);
                    b->arg = (Expr *) $1;
                    b->booltesttype = IS_NOT_TRUE;
                    $$ = (Node *)b;
                }
            | a_expr IS FALSE_P
                {
                    BooleanTest *b = makeNode(BooleanTest);
                    b->arg = (Expr *) $1;
                    b->booltesttype = IS_FALSE;
                    $$ = (Node *)b;
                }
            | a_expr IS NOT FALSE_P
                {
                    BooleanTest *b = makeNode(BooleanTest);
                    b->arg = (Expr *) $1;
                    b->booltesttype = IS_NOT_FALSE;
                    $$ = (Node *)b;
                }
            | a_expr IS UNKNOWN
                {
                    BooleanTest *b = makeNode(BooleanTest);
                    b->arg = (Expr *) $1;
                    b->booltesttype = IS_UNKNOWN;
                    $$ = (Node *)b;
                }
            | a_expr IS NOT UNKNOWN
                {
                    BooleanTest *b = makeNode(BooleanTest);
                    b->arg = (Expr *) $1;
                    b->booltesttype = IS_NOT_UNKNOWN;
                    $$ = (Node *)b;
                }
            | a_expr IS DISTINCT FROM a_expr            %prec IS
                {
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_DISTINCT, "=", $1, $5);
                }
            | a_expr IS OF '(' type_list ')'            %prec IS
                {
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OF, "=", $1, (Node *) $5);
                }
            | a_expr IS NOT OF '(' type_list ')'        %prec IS
                {
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OF, "!=", $1, (Node *) $6);
                }
            | a_expr BETWEEN b_expr AND b_expr            %prec BETWEEN
                {
                    $$ = (Node *) makeA_Expr(AEXPR_AND, NIL,
                        (Node *) makeSimpleA_Expr(AEXPR_OP, ">=", $1, $3),
                        (Node *) makeSimpleA_Expr(AEXPR_OP, "<=", $1, $5));
                }
            | a_expr NOT BETWEEN b_expr AND b_expr        %prec BETWEEN
                {
                    $$ = (Node *) makeA_Expr(AEXPR_OR, NIL,
                        (Node *) makeSimpleA_Expr(AEXPR_OP, "<", $1, $4),
                        (Node *) makeSimpleA_Expr(AEXPR_OP, ">", $1, $6));
                }
            | a_expr IN_P in_expr
                {
                    /* in_expr returns a SubLink or a list of a_exprs */
                    if (IsA($3, SubLink))
                    {
                            SubLink *n = (SubLink *)$3;
                            n->subLinkType = ANY_SUBLINK;
                            if (IsA($1, RowExpr))
                                n->lefthand = ((RowExpr *) $1)->args;
                            else
                                n->lefthand = list_make1($1);
                            n->operName = list_make1(makeString("="));
                            $$ = (Node *)n;
                    }
                    else
                    {
                        /* generate scalar IN expression */
                        // from PG 8.3.0
                        $$ = (Node *) makeSimpleA_Expr(AEXPR_IN, "=", $1, $3);
                    }
                }
            | a_expr NOT IN_P in_expr
                {
                    /* in_expr returns a SubLink or a list of a_exprs */
                    if (IsA($4, SubLink))
                    {
                        /* Make an IN node */
                        SubLink *n = (SubLink *)$4;
                        n->subLinkType = ANY_SUBLINK;
                        if (IsA($1, RowExpr))
                            n->lefthand = ((RowExpr *) $1)->args;
                        else
                            n->lefthand = list_make1($1);
                        n->operName = list_make1(makeString("<>"));
                        $$ = (Node *)n;
                        /* Stick a NOT on top; not for vertica */
                        /* $$ = (Node *) makeA_Expr(AEXPR_NOT, NIL, NULL, (Node *) n); */
                    }
                    else
                    {
                        /* generate scalar NOT IN expression */
                        // from PG 8.3.0
                        $$ = (Node *) makeSimpleA_Expr(AEXPR_IN, "<>", $1, $4);
                    }
                }
            | a_expr subquery_Op sub_type select_with_parens %prec Op
                {
                    SubLink *n = makeNode(SubLink);
                    n->subLinkType = $3;
                    if (IsA($1, RowExpr))
                        n->lefthand = ((RowExpr *) $1)->args;
                    else
                        n->lefthand = list_make1($1);
                    n->operName = $2;
                    n->subselect = $4;
                    if (n->subLinkType == ANY_SUBLINK &&
                        list_length(n->operName) == 1 &&
                        strcmp(strVal(llast(n->operName)), "<>") == 0)
                        n->subLinkType = NE_ANY_SUBLINK;
                    $$ = (Node *)n;
                }
            | a_expr subquery_Op sub_type '(' a_expr ')' %prec Op
                {
                    if ($3 == ANY_SUBLINK)
                        $$ = (Node *) makeA_Expr(AEXPR_OP_ANY, $2, $1, $5);
                    else
                        $$ = (Node *) makeA_Expr(AEXPR_OP_ALL, $2, $1, $5);
                }
            | UNIQUE select_with_parens %prec Op
                {
                    /* Not sure how to get rid of the parentheses
                     * but there are lots of shift/reduce errors without them.
                     *
                     * Should be able to implement this by plopping the entire
                     * select into a node, then transforming the target expressions
                     * from whatever they are into count(*), and testing the
                     * entire result equal to one.
                     * But, will probably implement a separate node in the executor.
                     */
                    ereport(ERROR,
                            (errcode(ERRCODE_FEATURE_NOT_SUPPORTED),
                             errmsg("UNIQUE predicate is not supported")));
                }
        ;
interpolate_expr:
             columnref INTERPOLATE PREVIOUS_P VALUE_P columnref
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("_interpolated_prev_value");
                    n->args = list_make2($1,$5);
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
        ;

ad_expr:    d_expr                                    { $$ = $1; }
            | interpolate_expr                          { $$ = $1; }
            | ad_expr TYPECAST Typename
                { $$ = makeTypeCast($1, $3, false); }
            | ad_expr SOFTTYPECAST Typename
                { $$ = makeTypeCast($1, $3, true); }
            | ad_expr AT timezone d_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("timezone");
                    // SQL-2008 6.30-6: force to INTERVAL HOUR TO MINUTE
                    if (IsA($4, A_Const)) { // look for an interval constant
                        TypeName *tn = ((A_Const *)$4)->typeInfo;
                        if (tn != NULL) // if an explict interval constant
                            tn->typmod &=
                                INTERVAL_TYPMOD(0,
                                                INTERVAL_MASK(HOUR) |
                                                INTERVAL_MASK(MINUTE) |
                                                INTERVAL_MASK(NEG_INTERVAL));
                    }
                    n->args = list_make2($4, $1);
                    $$ = (Node *) n;
                }
            | ad_expr AT LOCAL
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("timezone");
                    n->args = list_make1($1);
                    $$ = (Node *) n;
                }
        /*
         * These operators must be called out explicitly in order to make use
         * of yacc/bison's automatic operator-precedence handling.  All other
         * operator names are handled by the generic productions using "Op",
         * below; and all those operators will have the same precedence.
         *
         * If you add more explicitly-known operators, be sure to add them
         * also to b_expr and to the MathOp list above.
         */
            | '+' ad_expr                    %prec UMINUS
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "+", NULL, $2); }
            | '-' ad_expr                    %prec UMINUS
                { $$ = doNegate($2); }
            | ad_expr '+' ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "+", $1, $3); }
            | ad_expr '-' ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "-", $1, $3); }
            | ad_expr '*' ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "*", $1, $3); }
            | ad_expr '/' ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "/", $1, $3); }
            | ad_expr Op_SS ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "//", $1, $3); }
            | ad_expr '%' ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "%", $1, $3); }
            | ad_expr '^' ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "^", $1, $3); }
            | ad_expr '<' ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "<", $1, $3); }
            | ad_expr '>' ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, ">", $1, $3); }
            | ad_expr '=' ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "=", $1, $3); }
            | ad_expr Op_Cmp ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, $2.str, $1, $3); }
            | ad_expr '|' ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "|", $1, $3); }

            | ad_expr qual_Op ad_expr                %prec Op
                { $$ = (Node *) makeA_Expr(AEXPR_OP, $2, $1, $3); }
            | qual_Op ad_expr                    %prec Op
                { $$ = (Node *) makeA_Expr(AEXPR_OP, $1, NULL, $2); }
            | ad_expr '!'
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!", $1, NULL); }

            | ad_expr AND ad_expr
                { $$ = (Node *) makeA_Expr(AEXPR_AND, NIL, $1, $3); }
            | ad_expr OR ad_expr
                { $$ = (Node *) makeA_Expr(AEXPR_OR, NIL, $1, $3); }
            | NOT ad_expr
                {
                    if (IsA($2, SubLink) && ((SubLink *)$2)->subLinkType == EXISTS_SUBLINK)
                    {
                        /* Make an NOT EXISTS node */
                        /* for EXISTS opername will not be populated, but for NOT EXISTS it would */
                        SubLink *n = (SubLink*)$2;
                        if (n->operName)
                            n->operName = NULL;
                        else
                            n->operName = list_make1(makeString("<>"));
                        $$ = (Node *)n;
                    }
                    else
                    {
                        $$ = (Node *) makeA_Expr(AEXPR_NOT, NIL, NULL, $2);
                    }
                }

            | ad_expr LIKE ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "~~", $1, $3); }
            | ad_expr NOT LIKE ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!~~", $1, $4); }
            | ad_expr ILIKE ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "~~*", $1, $3); }
            | ad_expr NOT ILIKE ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!~~*", $1, $4); }
            | ad_expr LIKE ad_expr ESCAPE ad_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("like");
                    n->args = list_make3($1,$3,$5);
                    $$ = (Node *)n;
                }
            | ad_expr NOT LIKE ad_expr ESCAPE ad_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("nlike");
                    n->args = list_make3($1,$4,$6);
                    $$ = (Node *)n;
                }
            | ad_expr ILIKE ad_expr ESCAPE ad_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("ilike");
                    n->args = list_make3($1,$3,$5);
                    $$ = (Node *)n;
                }
            | ad_expr NOT ILIKE ad_expr ESCAPE ad_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("nilike");
                    n->args = list_make3($1,$4,$6);
                    $$ = (Node *)n;
                }

            | ad_expr LIKEB ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "~#", $1, $3); }
            | ad_expr NOT LIKEB ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!~#", $1, $4); }
            | ad_expr ILIKEB ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "~#*", $1, $3); }
            | ad_expr NOT ILIKEB ad_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!~#*", $1, $4); }
            | ad_expr LIKEB ad_expr ESCAPE ad_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("likeb");
                    n->args = list_make3($1,$3,$5);
                    $$ = (Node *)n;
                }
            | ad_expr NOT LIKEB ad_expr ESCAPE ad_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("nlikeb");
                    n->args = list_make3($1,$4,$6);
                    $$ = (Node *)n;
                }
            | ad_expr ILIKEB ad_expr ESCAPE ad_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("ilikeb");
                    n->args = list_make3($1,$3,$5);
                    $$ = (Node *)n;
                }
            | ad_expr NOT ILIKEB ad_expr ESCAPE ad_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("nilike");
                    n->args = list_make3($1,$4,$6);
                    $$ = (Node *)n;
                }

            | ad_expr SIMILAR TO ad_expr                %prec SIMILAR
                {
                    A_Const *c = makeNode(A_Const);
                    FuncCall *n = makeNode(FuncCall);
                    c->val.type = T_Null;
                    n->funcname = SystemFuncName("similar_escape");
                    n->args = list_make2($4, (Node *) c);
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "~", $1, (Node *) n);
                }
            | ad_expr SIMILAR TO ad_expr ESCAPE ad_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("similar_escape");
                    n->args = list_make2($4, $6);
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "~", $1, (Node *) n);
                }
            | ad_expr NOT SIMILAR TO ad_expr            %prec SIMILAR
                {
                    A_Const *c = makeNode(A_Const);
                    FuncCall *n = makeNode(FuncCall);
                    c->val.type = T_Null;
                    n->funcname = SystemFuncName("similar_escape");
                    n->args = list_make2($5, (Node *) c);
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!~", $1, (Node *) n);
                }
            | ad_expr NOT SIMILAR TO ad_expr ESCAPE ad_expr
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("similar_escape");
                    n->args = list_make2($5, $7);
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!~", $1, (Node *) n);
                }

            /* NullTest clause
             * Define SQL92-style Null test clause.
             * Allow two forms described in the standard:
             *    a IS NULL
             *    a IS NOT NULL
             * Allow two SQL extensions
             *    a ISNULL
             *    a NOTNULL
             */
            | ad_expr ISNULL
                {
                    if (IsA($1, RowExpr))
                        $$ = makeRowNullTest(IS_NULL, (RowExpr *) $1);
                    else
                    {
                        NullTest *n = makeNode(NullTest);
                        n->arg = (Expr *) $1;
                        n->nulltesttype = IS_NULL;
                        $$ = (Node *)n;
                    }
                }
            | ad_expr IS NULL_P
                {
                    if (IsA($1, RowExpr))
                        $$ = makeRowNullTest(IS_NULL, (RowExpr *) $1);
                    else
                    {
                        NullTest *n = makeNode(NullTest);
                        n->arg = (Expr *) $1;
                        n->nulltesttype = IS_NULL;
                        $$ = (Node *)n;
                    }
                }
            | ad_expr NOTNULL
                {
                    if (IsA($1, RowExpr))
                        $$ = makeRowNullTest(IS_NOT_NULL, (RowExpr *) $1);
                    else
                    {
                        NullTest *n = makeNode(NullTest);
                        n->arg = (Expr *) $1;
                        n->nulltesttype = IS_NOT_NULL;
                        $$ = (Node *)n;
                    }
                }
            | ad_expr IS NOT NULL_P
                {
                    if (IsA($1, RowExpr))
                        $$ = makeRowNullTest(IS_NOT_NULL, (RowExpr *) $1);
                    else
                    {
                        NullTest *n = makeNode(NullTest);
                        n->arg = (Expr *) $1;
                        n->nulltesttype = IS_NOT_NULL;
                        $$ = (Node *)n;
                    }
                }
            | ad_expr IS TRUE_P
                {
                    BooleanTest *b = makeNode(BooleanTest);
                    b->arg = (Expr *) $1;
                    b->booltesttype = IS_TRUE;
                    $$ = (Node *)b;
                }
            | ad_expr IS NOT TRUE_P
                {
                    BooleanTest *b = makeNode(BooleanTest);
                    b->arg = (Expr *) $1;
                    b->booltesttype = IS_NOT_TRUE;
                    $$ = (Node *)b;
                }
            | ad_expr IS FALSE_P
                {
                    BooleanTest *b = makeNode(BooleanTest);
                    b->arg = (Expr *) $1;
                    b->booltesttype = IS_FALSE;
                    $$ = (Node *)b;
                }
            | ad_expr IS NOT FALSE_P
                {
                    BooleanTest *b = makeNode(BooleanTest);
                    b->arg = (Expr *) $1;
                    b->booltesttype = IS_NOT_FALSE;
                    $$ = (Node *)b;
                }
            | ad_expr IS UNKNOWN
                {
                    BooleanTest *b = makeNode(BooleanTest);
                    b->arg = (Expr *) $1;
                    b->booltesttype = IS_UNKNOWN;
                    $$ = (Node *)b;
                }
            | ad_expr IS NOT UNKNOWN
                {
                    BooleanTest *b = makeNode(BooleanTest);
                    b->arg = (Expr *) $1;
                    b->booltesttype = IS_NOT_UNKNOWN;
                    $$ = (Node *)b;
                }
            | ad_expr IS DISTINCT FROM ad_expr            %prec IS
                {
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_DISTINCT, "=", $1, $5);
                }
            | ad_expr IS OF '(' type_list ')'            %prec IS
                {
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OF, "=", $1, (Node *) $5);
                }
            | ad_expr IS NOT OF '(' type_list ')'        %prec IS
                {
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OF, "!=", $1, (Node *) $6);
                }
            | ad_expr BETWEEN bd_expr AND bd_expr            %prec BETWEEN
                {
                    $$ = (Node *) makeA_Expr(AEXPR_AND, NIL,
                        (Node *) makeSimpleA_Expr(AEXPR_OP, ">=", $1, $3),
                        (Node *) makeSimpleA_Expr(AEXPR_OP, "<=", $1, $5));
                }
            | ad_expr NOT BETWEEN bd_expr AND bd_expr        %prec BETWEEN
                {
                    $$ = (Node *) makeA_Expr(AEXPR_OR, NIL,
                        (Node *) makeSimpleA_Expr(AEXPR_OP, "<", $1, $4),
                        (Node *) makeSimpleA_Expr(AEXPR_OP, ">", $1, $6));
                }
            | ad_expr subquery_Op sub_type select_with_parens %prec Op
                {
                    SubLink *n = makeNode(SubLink);
                    n->subLinkType = $3;
                    if (IsA($1, RowExpr))
                        n->lefthand = ((RowExpr *) $1)->args;
                    else
                        n->lefthand = list_make1($1);
                    n->operName = $2;
                    n->subselect = $4;
                    if (n->subLinkType == ANY_SUBLINK &&
                        list_length(n->operName) == 1 &&
                        strcmp(strVal(llast(n->operName)), "<>") == 0)
                        n->subLinkType = NE_ANY_SUBLINK;
                    $$ = (Node *)n;
                }
            | ad_expr subquery_Op sub_type '(' ad_expr ')' %prec Op
                {
                    if ($3 == ANY_SUBLINK)
                        $$ = (Node *) makeA_Expr(AEXPR_OP_ANY, $2, $1, $5);
                    else
                        $$ = (Node *) makeA_Expr(AEXPR_OP_ALL, $2, $1, $5);
                }
        ;
/*
 * Restricted expressions
 *
 * b_expr is a subset of the complete expression syntax defined by a_expr.
 *
 * Presently, AND, NOT, IS, and IN are the a_expr keywords that would
 * cause trouble in the places where b_expr is used.  For simplicity, we
 * just eliminate all the boolean-keyword-operator productions from b_expr.
 */
b_expr:        c_expr
                { $$ = $1; }
            | b_expr TYPECAST Typename
                { $$ = makeTypeCast($1, $3, false); }
            | b_expr SOFTTYPECAST Typename
                { $$ = makeTypeCast($1, $3, true); }
            | '+' b_expr                    %prec UMINUS
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "+", NULL, $2); }
            | '-' b_expr                    %prec UMINUS
                { $$ = doNegate($2); }
/* removed to match PG 8.2.2 and fix 6 ^ -3  -Bill
            | '%' b_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "%", NULL, $2); }
            | '^' b_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "^", NULL, $2); }
            | b_expr '%'
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "%", $1, NULL); }
            | b_expr '^'
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "^", $1, NULL); }
*/
            | b_expr '+' b_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "+", $1, $3); }
            | b_expr '-' b_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "-", $1, $3); }
            | b_expr '*' b_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "*", $1, $3); }
            | b_expr '/' b_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "/", $1, $3); }
            | b_expr Op_SS b_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "//", $1, $3); }
            | b_expr '%' b_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "%", $1, $3); }
            | b_expr '^' b_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "^", $1, $3); }
            | b_expr '<' b_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "<", $1, $3); }
            | b_expr '>' b_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, ">", $1, $3); }
            | b_expr '=' b_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "=", $1, $3); }
            | b_expr Op_Cmp b_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, $2.str, $1, $3); }
            | b_expr '|' b_expr
                 { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "|", $1, $3); }

            | b_expr qual_Op b_expr                %prec Op
                { $$ = (Node *) makeA_Expr(AEXPR_OP, $2, $1, $3); }
            | qual_Op b_expr                    %prec Op
                { $$ = (Node *) makeA_Expr(AEXPR_OP, $1, NULL, $2); }
            | b_expr '!'
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!", $1, NULL); }
            | b_expr IS DISTINCT FROM b_expr    %prec IS
                {
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_DISTINCT, "=", $1, $5);
                }
            | b_expr IS OF '(' type_list ')'    %prec IS
                {
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OF, "=", $1, (Node *) $5);
                }
            | b_expr IS NOT OF '(' type_list ')'    %prec IS
                {
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OF, "!=", $1, (Node *) $6);
                }
        ;

bd_expr:        d_expr
                { $$ = $1; }
            | bd_expr TYPECAST Typename
                { $$ = makeTypeCast($1, $3, false); }
            | bd_expr SOFTTYPECAST Typename
                { $$ = makeTypeCast($1, $3, true); }
            | '+' bd_expr                    %prec UMINUS
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "+", NULL, $2); }
            | '-' bd_expr                    %prec UMINUS
                { $$ = doNegate($2); }
            | bd_expr '+' bd_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "+", $1, $3); }
            | bd_expr '-' bd_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "-", $1, $3); }
            | bd_expr '*' bd_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "*", $1, $3); }
            | bd_expr '/' bd_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "/", $1, $3); }
            | bd_expr Op_SS bd_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "//", $1, $3); }
            | bd_expr '%' bd_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "%", $1, $3); }
            | bd_expr '^' bd_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "^", $1, $3); }
            | bd_expr '<' bd_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "<", $1, $3); }
            | bd_expr '>' bd_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, ">", $1, $3); }
            | bd_expr '=' bd_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "=", $1, $3); }
            | bd_expr Op_Cmp bd_expr
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, $2.str, $1, $3); }
            | bd_expr '|' bd_expr
                 { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "|", $1, $3); }
            | bd_expr qual_Op bd_expr                %prec Op
                { $$ = (Node *) makeA_Expr(AEXPR_OP, $2, $1, $3); }
            | qual_Op bd_expr                    %prec Op
                { $$ = (Node *) makeA_Expr(AEXPR_OP, $1, NULL, $2); }
            | bd_expr '!'
                { $$ = (Node *) makeSimpleA_Expr(AEXPR_OP, "!", $1, NULL); }
            | bd_expr IS DISTINCT FROM bd_expr    %prec IS
                {
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_DISTINCT, "=", $1, $5);
                }
            | bd_expr IS OF '(' type_list ')'    %prec IS
                {
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OF, "=", $1, (Node *) $5);
                }
            | bd_expr IS NOT OF '(' type_list ')'    %prec IS
                {
                    $$ = (Node *) makeSimpleA_Expr(AEXPR_OF, "!=", $1, (Node *) $6);
                }
        ;


/*
 * Productions that can be used in both a_expr and b_expr.
 *
 * Note: productions that refer recursively to a_expr or b_expr mostly
 * cannot appear here.    However, it's OK to refer to a_exprs that occur
 * inside parentheses, such as function arguments; that cannot introduce
 * ambiguity to the b_expr syntax.
 */
c_expr:        columnref                                { $$ = $1; }
            | AexprConst                            { $$ = $1; }
            | PARAM opt_indirection
                {
                    ParamRef *p = makeNode(ParamRef);
                    p->number = $1;
                    if ($2)
                    {
                        A_Indirection *n = makeNode(A_Indirection);
                        n->arg = (Node *) p;
                        n->indirection = $2;
                        $$ = (Node *) n;
                    }
                    else
                        $$ = (Node *) p;
                }
            | '(' a_expr ')' indirection
                {
                    A_Indirection *n = makeNode(A_Indirection);
                    n->arg = $2;
                    n->indirection = $4;
                    $$ = (Node *)n;
                }
            | '(' a_expr ')'
                { $$ = $2; }
            | '(' a_expr '-' a_expr ')' interval_qualifier
                {
                    A_Expr *n = makeSimpleA_Expr(AEXPR_OP, "-", $2, $4);
                    if (INTERVAL_RANGE($6) != 0) /* else i_q is EMPTY */
                        n->typmod = $6;
                    $$ = (Node *)n;
                }
            | case_expr
                { $$ = $1; }
            | func_expr
                { $$ = $1; }
            | select_with_parens            %prec UMINUS
                {
                    SubLink *n = makeNode(SubLink);
                    n->subLinkType = EXPR_SUBLINK;
                    n->lefthand = NIL;
                    n->operName = NIL;
                    n->subselect = $1;
                    $$ = (Node *)n;
                }
            | EXISTS select_with_parens
                {
                    SubLink *n = makeNode(SubLink);
                    n->subLinkType = EXISTS_SUBLINK;
                    n->lefthand = NIL;
                    n->operName = NIL;
                    n->subselect = $2;
                    $$ = (Node *)n;
                }
            | ARRAY select_with_parens
                {
                    SubLink *n = makeNode(SubLink);
                    n->subLinkType = ARRAY_SUBLINK;
                    n->lefthand = NIL;
                    n->operName = NIL;
                    n->subselect = $2;
                    $$ = (Node *)n;
                }
            | ARRAY array_expr
                {    $$ = $2;    }
            | row
                {
                    RowExpr *r = makeNode(RowExpr);
                    r->args = $1;
                    r->row_typeid = InvalidOid;    /* not analyzed yet */
                    $$ = (Node *)r;
                }
        ;

d_expr:       columnref                                { $$ = $1; }
            | AexprConst                            { $$ = $1; }
            | PARAM opt_indirection
                {
                    ParamRef *p = makeNode(ParamRef);
                    p->number = $1;
                    if ($2)
                    {
                        A_Indirection *n = makeNode(A_Indirection);
                        n->arg = (Node *) p;
                        n->indirection = $2;
                        $$ = (Node *) n;
                    }
                    else
                        $$ = (Node *) p;
                }
             | '(' a_expr '-' a_expr ')' interval_qualifier
                {
                    A_Expr *n = makeSimpleA_Expr(AEXPR_OP, "-", $2, $4);
                    if (INTERVAL_RANGE($6) != 0) /* else i_q is EMPTY */
                        n->typmod = $6;
                    $$ = (Node *)n;
                }
            | case_expr
                { $$ = $1; }
            | func_expr
                { $$ = $1; }
            | select_with_parens            %prec UMINUS
                {
                    SubLink *n = makeNode(SubLink);
                    n->subLinkType = EXPR_SUBLINK;
                    n->lefthand = NIL;
                    n->operName = NIL;
                    n->subselect = $1;
                    $$ = (Node *)n;
                }
            | EXISTS select_with_parens
                {
                    SubLink *n = makeNode(SubLink);
                    n->subLinkType = EXISTS_SUBLINK;
                    n->lefthand = NIL;
                    n->operName = NIL;
                    n->subselect = $2;
                    $$ = (Node *)n;
                }
            | ARRAY select_with_parens
                {
                    SubLink *n = makeNode(SubLink);
                    n->subLinkType = ARRAY_SUBLINK;
                    n->lefthand = NIL;
                    n->operName = NIL;
                    n->subselect = $2;
                    $$ = (Node *)n;
                }
            | ARRAY array_expr
                {    $$ = $2;    }
        ;

/*
 * func_expr is split out from c_expr just so that we have a classification
 * for "everything that is a function call or looks like one".  This isn't
 * very important, but it saves us having to document which variants are
 * legal in the backwards-compatible functional-index syntax for CREATE INDEX.
 * (Note that many of the special SQL functions wouldn't actually make any
 * sense as functional index entries, but we ignore that consideration here.)
 */
func_expr: non_analytic_function { $$ = $1; }
           | analytic_function { $$ = $1; }
       ;

non_analytic_function:    func_name '(' ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = $1;
                    n->args = NIL;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | func_name '(' expr_list ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = $1;
                    n->args = $3;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | func_name '(' ALL expr_list ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = $1;
                    n->args = $4;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = TRUE;
                    $$ = (Node *)n;
                }
            | func_name '(' USING PARAMETERS paramarg_list ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = $1;
                    n->args = NIL;
                    n->kwargs = $5;
                    n->parameters = NULL;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | func_name '(' expr_list USING PARAMETERS paramarg_list ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = $1;
                    n->args = $3;
                    n->kwargs = $6;
                    n->parameters = NULL;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | func_name '(' DISTINCT expr_list USING PARAMETERS paramarg_list ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = $1;
                    n->args = $4;
                    n->kwargs = $7;
                    n->parameters = NULL;
                    n->agg_star = FALSE;
                    n->agg_distinct = TRUE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | func_name '(' '*' USING PARAMETERS paramarg_list ')'
               {
                   FuncCall *n = makeNode(FuncCall);
                   A_Const *star = makeNode(A_Const);

                   star->val.type = T_Integer;
                   star->val.val.ival = 1;
                   n->funcname = $1;
                   n->args = list_make1(star);
                   n->kwargs = $6;
                   n->parameters = NULL;
                   n->agg_star = TRUE;
                   n->agg_distinct = FALSE;
                   n->agg_all = FALSE;
                   $$ = (Node *) n;
               }
            | func_name '(' DISTINCT expr_list ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = $1;
                    n->args = $4;
                    n->agg_star = FALSE;
                    n->agg_distinct = TRUE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | func_name '(' expr_list IGNORE NULLS ')'
                {
                    FuncCall *func = makeNode(FuncCall);
                    isFirstLastValueFunc($1);
                    func->funcname = $1;
                    func->args = lappend($3, (Node *)makeBoolAConst(TRUE));
                    func->agg_star = FALSE;
                    func->agg_distinct = FALSE;
                    func->agg_all = FALSE;
                    $$ = (Node *) func;
                }
            | func_name '(' expr_list IGNORE NULLS ',' a_expr ')'
              {
                  /* this is primarily for TSA functions
                   * i.e. first_value(bidprice ignore nulls, 'LINEAR'), ...
                   * first_value(bidprice, 'LINEAR') would be matched above
                   * with func_name '(' expr_list ')' first_value(bidprice
                   * ignore nulls) would be matched above with func_name '('
                   * a_expr IGNORE NULLS ')' the key word IGNORE NULLS causes
                   * this difficultly.
                   */
                    FuncCall *func = makeNode(FuncCall);
                    isFirstLastValueFunc($1);
                    func->funcname = $1;
                    func->args = lappend(lappend($3, (Node *)makeBoolAConst(TRUE)), $7);
                    func->agg_star = FALSE;
                    func->agg_distinct = FALSE;
                    func->agg_all = FALSE;
                    $$ = (Node *) func;
              }
            | func_name '(' '*' ')'
                {
                    /*
                     * For now, we transform AGGREGATE(*) into AGGREGATE(1).
                     *
                     * This does the right thing for COUNT(*) (in fact,
                     * any certainly-non-null expression would do for COUNT),
                     * and there are no other aggregates in SQL92 that accept
                     * '*' as parameter.
                     *
                     * The FuncCall node is also marked agg_star = true,
                     * so that later processing can detect what the argument
                     * really was.
                     */
                    FuncCall *n = makeNode(FuncCall);
                    A_Const *star = makeNode(A_Const);

                    star->val.type = T_Integer;
                    star->val.val.ival = 1;
                    n->funcname = $1;
                    n->args = list_make1(star);
                    n->agg_star = TRUE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | CURRENT_DATE opt_parens
                {
                    /*
                     * Translate as "'now()'::varchar::date".
                     *
                     * We cannot use "'now'::date" because coerce_type() will
                     * immediately reduce that to a constant representing
                     * today's date.  We need to delay the conversion until
                     * runtime, else the wrong things will happen when
                     * CURRENT_DATE is used in a column default value or rule.
                     *
                     * This could be simplified if we had a way to generate
                     * an expression tree representing runtime application
                     * of type-input conversion functions...
                     */
                    A_Const *s = makeNode(A_Const);
                    TypeName *d;

                    s->val.type = T_String;
                    s->val.val.str = ctString("now()");
                    s->typeInfo = SystemTypeName("varchar");

                    d = SystemTypeName("date");

                    $$ = (Node *)makeTypeCast((Node *)s, d, false);
                }
            | CURRENT_TIME
                {
                    /*
                     * Translate as "'now()'::varchar::timetz".
                     * See comments for CURRENT_DATE.
                     */
                    A_Const *s = makeNode(A_Const);
                    TypeName *d;

                    s->val.type = T_String;
                    s->val.val.str = ctString("now()");
                    s->typeInfo = SystemTypeName("varchar");

                    d = SystemTypeName("timetz");
                    /* SQL99 mandates a default precision of zero for TIME
                     * fields in schemas. However, for CURRENT_TIME
                     * let's preserve the microsecond precision we
                     * might see from the system clock. - thomas 2001-12-07
                     */
                    d->typmod = 6;

                    $$ = (Node *)makeTypeCast((Node *)s, d, false);
                }
            | CURRENT_TIME '(' Iconst ')'
                {
                    /*
                     * Translate as "'now()'::varchar::timetz(n)".
                     * See comments for CURRENT_DATE.
                     */
                    A_Const *s = makeNode(A_Const);
                    TypeName *d;

                    s->val.type = T_String;
                    s->val.val.str = ctString("now()");
                    s->typeInfo = SystemTypeName("varchar");
                    d = SystemTypeName("timetz");
                    if ($3 < 0)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("CURRENT_TIME(%lld) precision must not be negative",
                                        $3)));
                    if ($3 > MAX_SECONDS_PRECISION)
                    {
                        ereport(WARNING,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("CURRENT_TIME(%lld) precision reduced to maximum allowed, %d",
                                        $3, MAX_SECONDS_PRECISION)));
                        $3 = MAX_SECONDS_PRECISION;
                    }
                    d->typmod = $3;

                    $$ = (Node *)makeTypeCast((Node *)s, d, false);
                }
            | CURRENT_TIMESTAMP
                {
                    /*
                     * Translate as "'now()'::varchar::timestamptz".
                     * See comments for CURRENT_DATE.
                     */
                    A_Const *s = makeNode(A_Const);
                    TypeName *d;

                    s->val.type = T_String;
                    s->val.val.str = ctString("now()");
                    s->typeInfo = SystemTypeName("varchar");

                    d = SystemTypeName("timestamptz");
                    /* SQL99 mandates a default precision of 6 for timestamp.
                     * Also, that is about as precise as we will get since
                     * we are using a microsecond time interface.
                     * - thomas 2001-12-07
                     */
                    d->typmod = 6;

                    $$ = (Node *)makeTypeCast((Node *)s, d, false);
                }
            | CURRENT_TIMESTAMP '(' Iconst ')'
                {
                    /*
                     * Translate as "'now()'::varchar::timestamptz(n)".
                     * See comments for CURRENT_DATE.
                     */
                    A_Const *s = makeNode(A_Const);
                    TypeName *d;

                    s->val.type = T_String;
                    s->val.val.str = ctString("now()");
                    s->typeInfo = SystemTypeName("varchar");

                    d = SystemTypeName("timestamptz");
                    if ($3 < 0)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("CURRENT_TIMESTAMP(%lld) precision must not be negative",
                                        $3)));
                    if ($3 > MAX_SECONDS_PRECISION)
                    {
                        ereport(WARNING,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("CURRENT_TIMESTAMP(%lld) precision reduced to maximum allowed, %d",
                                        $3, MAX_SECONDS_PRECISION)));
                        $3 = MAX_SECONDS_PRECISION;
                    }
                    d->typmod = $3;

                    $$ = (Node *)makeTypeCast((Node *)s, d, false);
                }
            | LOCALTIME
                {
                    /*
                     * Translate as "'now()'::varchar::time".
                     * See comments for CURRENT_DATE.
                     */
                    A_Const *s = makeNode(A_Const);
                    TypeName *d;

                    s->val.type = T_String;
                    s->val.val.str = ctString("now()");
                    s->typeInfo = SystemTypeName("varchar");

                    d = SystemTypeName("time");
                    /* SQL99 mandates a default precision of zero for TIME
                     * fields in schemas. However, for LOCALTIME
                     * let's preserve the microsecond precision we
                     * might see from the system clock. - thomas 2001-12-07
                     */
                    d->typmod = 6;

                    $$ = (Node *)makeTypeCast((Node *)s, d, false);
                }
            | LOCALTIME '(' Iconst ')'
                {
                    /*
                     * Translate as "'now()'::varchar::time(n)".
                     * See comments for CURRENT_DATE.
                     */
                    A_Const *s = makeNode(A_Const);
                    TypeName *d;

                    s->val.type = T_String;
                    s->val.val.str = ctString("now()");
                    s->typeInfo = SystemTypeName("varchar");
                    d = SystemTypeName("time");
                    if ($3 < 0)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("LOCALTIME(%lld) precision must not be negative",
                                        $3)));
                    if ($3 > MAX_SECONDS_PRECISION)
                    {
                        ereport(WARNING,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("LOCALTIME(%lld) precision reduced to maximum allowed, %d",
                                        $3, MAX_SECONDS_PRECISION)));
                        $3 = MAX_SECONDS_PRECISION;
                    }
                    d->typmod = $3;

                    $$ = (Node *)makeTypeCast((Node *)s, d, false);
                }
            | LOCALTIMESTAMP
                {
                    /*
                     * Translate as "'now()'::varchar::timestamp".
                     * See comments for CURRENT_DATE.
                     */
                    A_Const *s = makeNode(A_Const);
                    TypeName *d;

                    s->val.type = T_String;
                    s->val.val.str = ctString("now()");
                    s->typeInfo = SystemTypeName("varchar");

                    d = SystemTypeName("timestamp");
                    /* SQL99 mandates a default precision of 6 for timestamp.
                     * Also, that is about as precise as we will get since
                     * we are using a microsecond time interface.
                     * - thomas 2001-12-07
                     */
                    d->typmod = 6;

                    $$ = (Node *)makeTypeCast((Node *)s, d, false);
                }
            | LOCALTIMESTAMP '(' Iconst ')'
                {
                    /*
                     * Translate as "'now()'::varchar::timestamp(n)".
                     * See comments for CURRENT_DATE.
                     */
                    A_Const *s = makeNode(A_Const);
                    TypeName *d;

                    s->val.type = T_String;
                    s->val.val.str = ctString("now()");
                    s->typeInfo = SystemTypeName("varchar");

                    d = SystemTypeName("timestamp");
                    if ($3 < 0)
                        ereport(ERROR,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("LOCALTIMESTAMP(%lld) precision must not be negative",
                                        $3)));
                    if ($3 > MAX_SECONDS_PRECISION)
                    {
                        ereport(WARNING,
                                (errcode(ERRCODE_INVALID_PARAMETER_VALUE),
                                 errmsg("LOCALTIMESTAMP(%lld) precision reduced to maximum allowed, %d",
                                        $3, MAX_SECONDS_PRECISION)));
                        $3 = MAX_SECONDS_PRECISION;
                    }
                    d->typmod = $3;

                    $$ = (Node *)makeTypeCast((Node *)s, d, false);
                }
            | CURRENT_DATABASE opt_parens
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("current_database");
                    n->args = NIL;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | CURRENT_SCHEMA opt_parens
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("current_schema");
                    n->args = NIL;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | CURRENT_USER opt_parens
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("current_user");
                    n->args = NIL;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | SESSION_USER opt_parens
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("session_user");
                    n->args = NIL;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | SYSDATE opt_parens
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("sysdate");
                    n->args = NIL;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | USER opt_parens
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("current_user");
                    n->args = NIL;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | CAST '(' a_expr AS Typename ')'
                { $$ = makeTypeCast($3, $5, false); }
            | DATEDIFF '(' datediff_list ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("datediff");
                    n->args = $3;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | EXTRACT '(' extract_list ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("date_part");
                    n->args = $3;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | CHAR_LENGTH '(' a_expr using_octets ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    if ($4)
                        n->funcname = SystemFuncName("octet_length");
                    else
                        n->funcname = SystemFuncName("char_length");
                    n->args = list_make1($3);
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | CHARACTER_LENGTH '(' a_expr using_octets ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    if ($4)
                        n->funcname = SystemFuncName("octet_length");
                    else
                        n->funcname = SystemFuncName("character_length");
                    n->args = list_make1($3);
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | OVERLAY '(' overlay_list using_octets ')'
                {
                    /* overlay(A PLACING B FROM C FOR D) is converted to
                     * substring(A, 1, C-1) || B || substring(A, C+1, C+D)
                     * overlay(A PLACING B FROM C) is converted to
                     * substring(A, 1, C-1) || B || substring(A, C+1, C+char_length(B))
                     */
                    FuncCall *n = makeNode(FuncCall);
                    if ($4)
                        n->funcname = SystemFuncName("overlayb");
                    else
                        n->funcname = SystemFuncName("overlay");
                    n->args = $3;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | POSITION '(' position_list using_octets ')'
                {
                    /* position(A in B) is converted to position(B, A) */
                    FuncCall *n = makeNode(FuncCall);
                    if ($4)
                        n->funcname = SystemFuncName("positionb");
                    else
                        n->funcname = SystemFuncName("position");
                    n->args = $3;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | SUBSTRING '(' substr_list using_octets ')'
                {
                    /* substring(A from B for C) is converted to
                     * substring(A, B, C) - thomas 2000-11-28
                     */
                    FuncCall *n = makeNode(FuncCall);
                    if ($4)
                        n->funcname = SystemFuncName("substrb"); // oracle func
                    else
                        n->funcname = SystemFuncName("substring");
                    n->args = $3;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | TIMESTAMPADD '(' datediff_list ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("timestampadd");
                    n->args = $3;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | TIMESTAMPDIFF '(' datediff_list ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("timestampdiff");
                    n->args = $3;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | TREAT '(' a_expr AS Typename ')'
                {
                    /* TREAT(expr AS target) converts expr of a particular type to target,
                     * which is defined to be a subtype of the original expression.
                     * In SQL99, this is intended for use with structured UDTs,
                     * but let's make this a generally useful form allowing stronger
                     * coersions than are handled by implicit casting.
                     */
                    FuncCall *n = makeNode(FuncCall);
                    /* Convert SystemTypeName() to SystemFuncName() even though
                     * at the moment they result in the same thing.
                     */
                    n->funcname = SystemFuncName(((Value *)llast($5->names))->val.str.str);
                    n->args = list_make1($3);
                    $$ = (Node *)n;
                }
            | TRIM '(' BOTH trim_list ')'
                {
                    /* various trim expressions are defined in SQL92
                     * - thomas 1997-07-19
                     */
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("btrim");
                    n->args = $4;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | TRIM '(' LEADING trim_list ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("ltrim");
                    n->args = $4;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | TRIM '(' TRAILING trim_list ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("rtrim");
                    n->args = $4;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | TRIM '(' trim_list ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = SystemFuncName("btrim");
                    n->args = $3;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = (Node *)n;
                }
            | DECODE '(' a_expr ',' decode_search_result_list decode_default ')'
                {
                    CaseExpr *c = makeNode(CaseExpr);
                    c->casetype = InvalidOid; /* not analyzed yet */
                    c->arg = (Expr *) $3;
                    c->args = $5;
                    c->defresult = (Expr *) $6;
                    $$ = (Node *)c;
                }
      ;

opt_parens: '(' ')'                                    {}
            | /*EMPTY*/                                {}
        ;
paramarg:
            name '=' a_expr
                {
                    DefElem *arg = makeDefElem($1.str, (Node *) $3);
                    $$ = arg;
                }
        ;


paramarg_list:
            paramarg
                {
                    $$ = list_make1($1);
                }
            | paramarg_list ',' paramarg
                {
                    $$ = lappend($1, $3);
                }
        ;

load_function:
                func_name '(' PARAMETERS Sconst ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = $1;
                    n->args = NULL;
                    n->kwargs = NULL;
                    A_Const *params = makeNode(A_Const);
                    params->val.type = T_String;
                    params->val.val.str = $4;
                    n->parameters = list_make1((Node *)params);
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = n;
                }
                | func_name '(' paramarg_list ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = $1;
                    n->args = NULL;
                    n->kwargs = $3;
                    n->parameters = NULL;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = n;
                }
                | func_name '(' ')'
                {
                    FuncCall *n = makeNode(FuncCall);
                    n->funcname = $1;
                    n->args = NULL;
                    n->kwargs = NULL;
                    n->parameters = NULL;
                    n->agg_star = FALSE;
                    n->agg_distinct = FALSE;
                    n->agg_all = FALSE;
                    $$ = n;
                }
                ;

/*
 * Supporting nonterminals for expressions.
 */

/* Explicit row production.
 *
 * SQL99 allows an optional ROW keyword, so we can now do single-element rows
 * without conflicting with the parenthesized a_expr production.  Without the
 * ROW keyword, there must be more than one a_expr inside the parens.
 */
row:        ROW '(' expr_list ')'                    { $$ = $3; }
            | ROW '(' ')'                            { $$ = NIL; }
            | '(' expr_list ',' a_expr ')'            { $$ = lappend($2, $4); }
        ;

sub_type:    ANY                                        { $$ = ANY_SUBLINK; }
            | SOME                                    { $$ = ANY_SUBLINK; }
            | ALL                                    { $$ = ALL_SUBLINK; }
        ;

all_Op:        Op                                        { $$ = $1; }
            | MathOp                                { $$ = $1; }
        ;

MathOp:       '+'                                    { $$ = ctString("+"); }
            | '-'                                    { $$ = ctString("-"); }
            | '*'                                    { $$ = ctString("*"); }
            | '/'                                    { $$ = ctString("/"); }
            | Op_SS                                  { $$ = ctString("//"); }
            | '%'                                    { $$ = ctString("%"); }
            | '^'                                    { $$ = ctString("^"); }
            | '<'                                    { $$ = ctString("<"); }
            | '>'                                    { $$ = ctString(">"); }
            | '='                                    { $$ = ctString("="); }
            | Op_Cmp                                 { $$ = $1; }
        ;

qual_Op:    Op
                    { $$ = list_make1(makeStr($1)); }
            | OPERATOR '(' any_operator ')'
                    { $$ = $3; }
        ;

qual_all_Op:
            all_Op
                    { $$ = list_make1(makeStr($1)); }
            | OPERATOR '(' any_operator ')'
                    { $$ = $3; }
        ;

subquery_Op:
            all_Op
                    { $$ = list_make1(makeStr($1)); }
            | OPERATOR '(' any_operator ')'
                    { $$ = $3; }
            | LIKE
                    { $$ = list_make1(makeString("~~")); }
            | NOT LIKE
                    { $$ = list_make1(makeString("!~~")); }
            | ILIKE
                    { $$ = list_make1(makeString("~~*")); }
            | NOT ILIKE
                    { $$ = list_make1(makeString("!~~*")); }
            | LIKEB
                    { $$ = list_make1(makeString("~#")); }
            | NOT LIKEB
                    { $$ = list_make1(makeString("!~#")); }
            | ILIKEB
                    { $$ = list_make1(makeString("~#*")); }
            | NOT ILIKEB
                    { $$ = list_make1(makeString("!~#*")); }
/* cannot put SIMILAR TO here, because SIMILAR TO is a hack.
 * the regular expression is preprocessed by a function (similar_escape),
 * and the ~ operator for posix regular expressions is used.
 *        x SIMILAR TO y     ->    x ~ similar_escape(y)
 * this transformation is made on the fly by the parser upwards.
 * however the SubLink structure which handles any/some/all stuff
 * is not ready for such a thing.
 */
            ;

expr_list:    a_expr
                {
                    $$ = list_make1($1);
                }
            | expr_list ',' a_expr
                {
                    $$ = lappend($1, $3);
                }
        ;

datediff_list:
              extract_arg ',' expr_list
                {
                    A_Const *n = makeNode(A_Const);
                    n->val.type = T_String;
                    n->val.val.str = $1;
                    $$ = lcons(n, $3);
                }
            | '(' a_expr ')' ',' expr_list
                {
                    $$ = lcons($2, $5);
                }
        ;

extract_list:
            extract_arg FROM a_expr
                {
                    A_Const *n = makeNode(A_Const);
                    n->val.type = T_String;
                    n->val.val.str = $1;
                    $$ = list_make2((Node *) n, $3);
                }
        ;

type_list:  type_list ',' Typename
                {
                    $$ = lappend($1, $3);
                }
            | Typename
                {
                    $$ = list_make1($1);
                }
        ;

array_expr_list: array_expr
                {    $$ = list_make1($1);        }
            | array_expr_list ',' array_expr
                {    $$ = lappend($1, $3);    }
        ;

array_expr: '[' expr_list ']'
                {
                    ArrayExpr *n = makeNode(ArrayExpr);
                    n->elements = $2;
                    $$ = (Node *)n;
                }
            | '[' array_expr_list ']'
                {
                    ArrayExpr *n = makeNode(ArrayExpr);
                    n->elements = $2;
                    $$ = (Node *)n;
                }
        ;

/* Allow delimited string SCONST in extract_arg as an SQL extension.
 * - thomas 2001-04-12
 * Also used for datediff_list
 *
 * This needs to include all entries in keywords.c which are also found in
 * Datetime.cpp deltatktbl which are marked UNITS, plus epoch.
 */
extract_arg:
              IDENT                                 { $$ = $1; }
            | DAY_P                                 { $$ = ctString("day"); }
            | DEC                                   { $$ = ctString("dec"); }
            | EPOCH_P                               { $$ = ctString("epoch"); }
            | HOUR_P                                { $$ = ctString("hour"); }
            | HOURS_P                               { $$ = ctString("hours"); }
            | MICROSECONDS_P                        { $$ = ctString("microseconds"); }
            | MILLISECONDS_P                        { $$ = ctString("milliseconds"); }
            | MINUTE_P                              { $$ = ctString("minute"); }
            | MINUTES_P                             { $$ = ctString("minutes"); }
            | MONTH_P                               { $$ = ctString("month"); }
            | SECOND_P                              { $$ = ctString("second"); }
            | SECONDS_P                             { $$ = ctString("seconds"); }
            | timezone                              { $$ = ctString("timezone"); }
            | YEAR_P                                { $$ = ctString("year"); }
            | SCONST                                { $$ = $1; }
        ;

/* OVERLAY() arguments
 * SQL99 defines the OVERLAY() function:
 * o overlay(text placing text from int for int)
 * o overlay(text placing text from int)
 */
overlay_list:
            a_expr overlay_placing substr_from substr_for
                {
                    $$ = list_make4($1, $2, $3, $4);
                }
            | a_expr overlay_placing substr_from
                {
                    $$ = list_make3($1, $2, $3);
                }
        ;

overlay_placing:
            PLACING a_expr
                { $$ = $2; }
        ;

/* position_list uses b_expr not a_expr to avoid conflict with general IN */

position_list:
            b_expr IN_P b_expr                        { $$ = list_make2($3, $1); }
            | /*EMPTY*/                                { $$ = NIL; }
        ;

/*
 * DECODE arguments
 * Support 0racle compatibility
 * VER-4601
 */
decode_search_result_list:
                         decode_search_result
                             {
                                 $$ = list_make1($1);
                             }
                         | decode_search_result_list ',' decode_search_result
                               {
                                 $$ = lappend($1, $3);
                               }
                         ;

decode_search_result:
                    a_expr ',' a_expr
                        {
                            /* use CaseWhen from case expressions */
                            CaseWhen *w = makeNode(CaseWhen);
                            w->expr = (Expr *) $1;
                            w->result = (Expr *) $3;
                            w->treatnullsequal = true;
                            $$ = (Node *)w;
                        }
                    ;

decode_default:
              ',' a_expr            { $$ = $2; }
              | /* EMPTY */         { $$ = NULL; }
		;

/* SUBSTRING() arguments
 * SQL9x defines a specific syntax for arguments to SUBSTRING():
 * o substring(text from int for int)
 * o substring(text from int) get entire string from starting point "int"
 * o substring(text from pattern) get entire string matching pattern
 * o substring(text for int) get first "int" characters of string
 * We also want to implement generic substring functions which accept
 * the usual generic list of arguments. So we will accept both styles
 * here, and convert the SQL9x style to the generic list for further
 * processing. - thomas 2000-11-28
 */
substr_list:
            a_expr substr_from substr_for
                {
                    $$ = list_make3($1, $2, $3);
                }
            | a_expr substr_for substr_from
                {
                    $$ = list_make3($1, $3, $2);
                }
            | a_expr substr_from
                {
                    $$ = list_make2($1, $2);
                }
            | a_expr substr_for
                {
                    A_Const *n = makeNode(A_Const);
                    n->val.type = T_Integer;
                    n->val.val.ival = 1;
                    $$ = list_make3($1, (Node *)n, $2);
                }
            | expr_list
                {
                    $$ = $1;
                }
            | /*EMPTY*/
                { $$ = NIL; }
        ;

substr_from:
            FROM a_expr                                { $$ = $2; }
        ;

substr_for: FOR a_expr                                { $$ = $2; }
        ;

using_octets:
            USING OCTETS                             { $$ = TRUE; }
            | USING CHARACTERS                       { $$ = FALSE; }
            | /* EMPTY */                            { $$ = FALSE; }
        ;

trim_list:  a_expr FROM expr_list                    { $$ = lappend($3, $1); }
            | FROM expr_list                         { $$ = $2; }
	    | a_expr                                 { $$ = list_make1($1); }
        ;
in_expr:    select_with_parens
                {
                    SubLink *n = makeNode(SubLink);
                    n->subselect = $1;
                    /* other fields will be filled later */
                    $$ = (Node *)n;
                }
            | '(' expr_list ')'                        { $$ = (Node *)$2; }
        ;

/*
 * Define SQL92-style case clause.
 * - Full specification
 *    CASE WHEN a = b THEN c ... ELSE d END
 * - Implicit argument
 *    CASE a WHEN b THEN c ... ELSE d END
 */
case_expr:    CASE case_arg when_clause_list case_default END_P
                {
                    CaseExpr *c = makeNode(CaseExpr);
                    c->casetype = InvalidOid; /* not analyzed yet */
                    c->arg = (Expr *) $2;
                    c->args = $3;
                    c->defresult = (Expr *) $4;
                    $$ = (Node *)c;
                }
        ;

when_clause_list:
            /* There must be at least one */
            when_clause                                { $$ = list_make1($1); }
            | when_clause_list when_clause            { $$ = lappend($1, $2); }
        ;

when_clause:
            WHEN nullsequal a_expr THEN a_expr
                {
                    CaseWhen *w = makeNode(CaseWhen);
                    w->expr = (Expr *) $3;
                    w->result = (Expr *) $5;
                    w->treatnullsequal = $2;
                    $$ = (Node *)w;
                }
        ;

case_default:
            ELSE a_expr                                { $$ = $2; }
            | /*EMPTY*/                                { $$ = NULL; }
        ;

case_arg:   a_expr                                     { $$ = $1; }
            | /*EMPTY*/                                { $$ = NULL; }
        ;

nullsequal: NULLSEQUAL                                  { $$ = true; }
            | /* EMPTY */                           { $$ = false; }
		;
/*
 * columnref starts with relation_name not ColId, so that OLD and NEW
 * references can be accepted.    Note that when there are more than two
 * dotted names, the first name is not actually a relation name...
 */
columnref:    relation_name
                {
                    $$ = makeColumnRef($1.str, NIL);
                }
            | relation_name indirection
                {
                    $$ = makeColumnRef($1.str, $2);
                }
        ;

indirection_el:
            '.' attr_name
                {
                    $$ = (Node *) makeStr($2);
                }
            | '.' '*'
                {
                    $$ = (Node *) makeString("*");
                }
            | '[' a_expr ']'
                {
                    A_Indices *ai = makeNode(A_Indices);
                    ai->lidx = NULL;
                    ai->uidx = $2;
                    $$ = (Node *) ai;
                }
            | '[' a_expr ':' a_expr ']'
                {
                    A_Indices *ai = makeNode(A_Indices);
                    ai->lidx = $2;
                    ai->uidx = $4;
                    $$ = (Node *) ai;
                }
        ;

indirection:
            indirection_el                            { $$ = list_make1($1); }
            | indirection indirection_el            { $$ = lappend($1, $2); }
        ;

opt_indirection:
            /*EMPTY*/                                { $$ = NIL; }
            | opt_indirection indirection_el        { $$ = lappend($1, $2); }
        ;


/*****************************************************************************
 *
 *    target lists for SELECT, UPDATE, INSERT
 *
 *****************************************************************************/

target_list:
            target_el                                  { $$ = list_make1($1);  }
            | target_list ',' target_el                { $$ = lappend($1, $3); }
       ;

/* AS is not optional because shift/red conflict with unary ops (PG comment).
 * Vertica got rid of user-defined postfix operators, making AS
 * optional in many cases.  [User-defined casts (in ConstTypename)
 * cause problems with keywords and with SCONST; there are other
 * undiagnosed problems with allowing anything but IDENT.]
 */
target_el:    a_expr AS ColLabel
                {
                    $$ = makeNode(ResTarget);
                    $$->name = $3.str;
                    $$->indirection = NIL;
                    $$->val = (Node *)$1;
                }
            | a_expr BareColLabel
                {
                    $$ = makeNode(ResTarget);
                    $$->name = $2.str;
                    $$->indirection = NIL;
                    $$->val = (Node *)$1;
                }
            | a_expr
                {
                    $$ = makeNode(ResTarget);
                    $$->name = NULL;
                    $$->indirection = NIL;
                    $$->val = (Node *)$1;
                }
            | '*'
                {
                    ColumnRef *n = makeNode(ColumnRef);
                    n->fields = list_make1(makeString("*"));

                    $$ = makeNode(ResTarget);
                    $$->name = NULL;
                    $$->indirection = NIL;
                    $$->val = (Node *)n;
                }
            | a_expr AS '(' columnList ')'
                {
                    VAnalyticFunc *vf = (VAnalyticFunc *) $1;
                    if (IsA(vf, VAnalyticFunc))
                        vf->aliases = $4;

                    $$ = makeNode(ResTarget);
                    $$->name = NULL;
                    $$->indirection = NIL;
                    $$->val = (Node *)vf;
                }

             ;

/*
 * Timeseries Clause
 */
timeseries_clause: TIMESERIES ColId AS AexprConst OVER '(' opt_partition_clause ORDER BY a_expr')'
                   {
                       TimeseriesClause *t = makeNode(TimeseriesClause);
                       t->alias = $2.str;
                       t->slice_expr = $4;
                       t->partitionClause = $7;

                       SortBy *s = makeNode(SortBy);
                       s->node = $10;
                       s->sortby_kind = SORT_ASCEND_NULLS_FIRST;
                       s->useOp = NIL;

                       t->sortClause = list_make1(s);

                       $$ = (Node *) t;
                   }
                   | /*EMPTY*/ { $$ = NIL; }
                   ;

/*
 * Pattern Clause
 */
pattern_clause: MATCH '(' opt_partition_clause
                          orderby_clause
                          pattern_define_clause
                          pattern_in_clause
                          pattern_match_options_clause
                          pattern_results_clause ')'
{
    PatternMatch *p = makeNode(PatternMatch);
    p->partitionClause = $3;
    p->sortClause = $4;
    p->eventDefinitions = $5;
    p->patterns = $6;
    p->matchOptions = MATCHOPTION_NONDEFAULT | $7;
    p->matchOptions = p->matchOptions | $8;

    $$ = (Node *) p;
}
| /*EMPTY*/ { $$ = NIL; }
;

pattern_define_clause: DEFINE event_definition_list { $$ = $2; }
;

event_definition_list:
event_definition { $$ = list_make1($1); }
| event_definition_list ',' event_definition { $$ = lappend($1, $3); }
;

event_definition: ColId AS a_expr
{
    PatternEvent *e = makeNode(PatternEvent);
    e->name = $1.str;
    e->qual = $3;

    $$ = (Node*) e;
}
;

pattern_in_clause: PATTERN pattern_list { $$ = $2; }
;

pattern_list:
pattern { $$ = list_make1($1); }
| pattern_list ',' pattern { $$ = lappend($1, $3); }
;

pattern: ColId AS '(' regexp ')'
{
    PatternDef *def = makeNode(PatternDef);
    def->name = $1.str;

    if(IsA($4, PatternEventRef))
    {
        // wrap in PatternRegExpr if a single PatternEventRef
        // just make this a concat operator so we can wrap it
        PatternRegExpr *regex = makeNode(PatternRegExpr);
        regex->type = PATTERN_OP_CONCATENATION;
        regex->operName = pstrdup("o");
        regex->args = list_make1($4);
        regex->greedy = false;
        regex->possessive = false;
        regex->grouped = false;

        def->regexpr = (Node *) regex;
    }
    else
        def->regexpr = $4;

    $$ = (Node *) def;
}
;

regexp: regexp regexpprime
{

    PatternRegExpr *regex = makeNode(PatternRegExpr);
    regex->type = PATTERN_OP_CONCATENATION;
    regex->operName = pstrdup("o");
    regex->args = list_make1($1);
    regex->args = lappend(regex->args, $2);
    regex->greedy = false;
    regex->possessive = false;
    regex->grouped = false;

    $$ = (Node *) regex;

}
| regexp '|' regexpprime
{

    PatternRegExpr *regex = makeNode(PatternRegExpr);
    regex->type = PATTERN_OP_ALTERNATION;
    regex->operName = pstrdup("|");
    regex->args = list_make1($1);
    regex->args = lappend(regex->args, $3);
    regex->greedy = false;
    regex->possessive = false;
    regex->grouped = false;

    $$ = (Node *) regex;

}
| regexpprime
{
    $$ = $1;
}
;

regexpprime:
'(' regexp ')' pattern_quantifier
{

    if($4.str != NULL)
    {
        PatternRegExpr *regex = makeNode(PatternRegExpr);
        const char *n = convertPercentageToQuestionMark($4.str);
        regex->type = getPatternRegExprType(n);
        regex->operName = n;
        regex->args = list_make1($2);
        regex->greedy = !isPatternOpLazy(n);
        regex->possessive = isPatternOpPossessive(n);
        regex->grouped = true;

        $$ = (Node *) regex;
    }
    else
    {
        // just make this a concat operator so we can mark it
        // as a group -- it has ( )
        PatternRegExpr *regex = makeNode(PatternRegExpr);
        regex->type = PATTERN_OP_CONCATENATION;
        regex->operName = pstrdup("o");
        regex->args = list_make1($2);
        regex->greedy = false;
        regex->possessive = false;
        regex->grouped = true; // so we know this has parentheses
        $$ = (Node *) regex;
    }

}
| ColId pattern_quantifier
{

    PatternEventRef *eref = makeNode(PatternEventRef);
    eref->name = $1.str;
    eref->eventref = ANY_ROW_REF; // filled in later during parse analysis

    if($2.str != NULL)
    {
        PatternRegExpr *regex = makeNode(PatternRegExpr);
        const char *n = convertPercentageToQuestionMark($2.str);
        regex->type = getPatternRegExprType(n);
        regex->operName = n;
        regex->args = list_make1((Node *) eref);
        regex->greedy = !isPatternOpLazy(n);
        regex->possessive = isPatternOpPossessive(n);
        regex->grouped = false;

        $$ = (Node *) regex;
    }
    else
    {
        $$ = (Node *) eref;
    }

}
;

pattern_quantifier: all_Op
{
    $$ = $1;
}
| { /* EMPTY */ $$ = ctNULL; }
        ;

pattern_results_clause: RESULTS GROUPED BY MATCH { $$ = MATCHOPTION_OUTPUT_ONE_ROW; }
| RESULTS ALL ROWS { $$ = MATCHOPTION_OUTPUT_ALL_ROWS; }
| { /* EMPTY Default */ $$ = MATCHOPTION_OUTPUT_ALL_ROWS; }
;

pattern_match_options_clause: ROWS MATCH FIRST_P EVENT_P { $$ = MATCHOPTIONS_PCRE_NON_MUTUALLY_EXCLUSIVE; }
| ROWS MATCH ALL EVENTS_P { $$ = MATCHOPTIONS_PCRE_MUTUALLY_EXCLUSIVE; }
| { /* EMPTY Default */ $$ = MATCHOPTIONS_PCRE_NON_MUTUALLY_EXCLUSIVE; }
;

/*
 * Window Definitions
 */
window_clause:
                        WINDOW window_definition_list                   { $$ = $2; }
                        | /*EMPTY*/                                     { $$ = NIL; }
                        ;

window_definition_list:
                        window_definition                               { $$ = list_make1($1); }
                        | window_definition_list ',' window_definition  { $$ = lappend($1, $3); }
                        ;

window_definition:
                        ColId AS window_specification
                        {
                            VAnalyticClause *c = $3;
                            c->name = $1.str;
                            $$ = c;
                        }
                        ;

over_clause:
                        OVER window_specification                       { $$ = $2; }
                        | OVER ColId
                        {
                            VAnalyticClause *c = makeNode(VAnalyticClause);
                            c->name = $2.str;
                            c->refname = NULL;
                            c->partitionClause = NIL;
                            c->sortClause      = NIL;
                            c->frameOptions = NIL;
                            c->start = NULL;
                            c->end = NULL;
                            c->withinGroupClause = NULL;
                            c->hasOverClause = true;
                            $$ = c;
                        }
                        ;

within_clause:          WITHIN GROUP_P '(' orderby_clause ')'
                        {
                            $$ = $4;
                        }
                        | /*EMPTY*/ { $$ = NIL; }
                        ;

window_specification:
                        '(' opt_existing_window_name opt_partition_clause opt_orderby_clause opt_frame_clause ')'
                        {
                            VAnalyticClause *c = makeNode(VAnalyticClause);
                            c->name = NULL;
                            c->refname = $2.str;
                            c->partitionClause = $3;
                            c->sortClause = $4;
                            c->frameOptions = $5->frameOptions;
                            c->start = $5->value1;
                            c->end = $5->value2;
                            c->withinGroupClause = NULL;
                            c->hasOverClause = true;

                            c->partitionAuto = AUTOPARTITION_NONE;

                            if (c->partitionClause &&
                                list_length(c->partitionClause) == 1)
                            {
                                if (IsA(linitial(c->partitionClause), VPartitionByNode))
                                {
                                    c->partitionClause = NIL;
                                    c->partitionAuto = AUTOPARTITION_BY_NODE;
                                }
                                else if (IsA(linitial(c->partitionClause), VPartitionByBest))
                                {
                                    c->partitionClause = NIL;
                                    c->partitionAuto = AUTOPARTITION_BY_BEST;
                                }
                                else if (IsA(linitial(c->partitionClause), VPartitionAuto))
                                {
                                    c->partitionClause = NIL;
                                    c->partitionAuto = AUTOPARTITION_AUTO;
                                }
                                else if (IsA(linitial(c->partitionClause), VPartitionBatch))
                                {
                                    VPartitionBatch *pb = (VPartitionBatch *)linitial(c->partitionClause);
                                    c->partitionClause = pb->xprlist;
                                    c->partitionAuto = AUTOPARTITION_BATCH;
                                }
                                else if (IsA(linitial(c->partitionClause), VPartitionPrepass))
                                {
                                    VPartitionPrepass *pp = (VPartitionPrepass *)linitial(c->partitionClause);
                                    c->partitionClause = pp->xprlist;
                                    c->partitionAuto = AUTOPARTITION_PREPASS;
                                }
                            }
                            $$ = c;
                        }
                        ;

/*
 *  analytic_function_type over_clause
 */
analytic_function:
                        non_analytic_function within_clause over_clause
                        {
                            VAnalyticFunc *afunc = makeNode(VAnalyticFunc);
                            afunc->funcExpr = (Node*)$1;

                            VAnalyticClause *analytic_clause = (VAnalyticClause *) $3;
                            analytic_clause->withinGroupClause = $2;
                            analytic_clause->hasOverClause = true;
                            afunc->analyticClause = (Node*) analytic_clause;
                            afunc->aliases = NIL;
                            $$ = (Node *)afunc;
                        }
                        ;

/*
 * If we see PARTITION, RANGE, or ROWS as the first token after the '('
 * of a window_specification, we want the assumption to be that there is
 * no existing_window_name; but those keywords are unreserved and so could
 * be ColIds.  We fix this by making them have the same precedence as IDENT
 * and giving the empty production here a slightly higher precedence, so
 * that the shift/reduce conflict is resolved in favor of reducing the rule.
 * These keywords are thus precluded from being an existing_window_name but
 * are not reserved for any other purpose.
 */
opt_existing_window_name:
                        ColId                                           { $$ = $1; }
                        | /*EMPTY*/ %prec Op                            { $$ = ctNULL; }
                        ;

/*
 * window frame ( ex. RANGE BEWTWEEN UNBOUNDED PRECEDING AND CURRENT ROW )
 */
opt_frame_clause:
                        RANGE frame_extent frame_exclusion
                        {
                            $2->frameOptions = FRAMEOPTION_NONDEFAULT | FRAMEOPTION_RANGE | $2->frameOptions | $3;
                            $$ = $2;
                        }
                        | ROWS frame_extent frame_exclusion
                        {
                            $2->frameOptions = FRAMEOPTION_NONDEFAULT | FRAMEOPTION_ROWS | $2->frameOptions | $3;
                            $$ = $2;
                        }
                        | /*EMPTY*/
                        {
                            VFrameBound *framebound = makeNode(VFrameBound);
                            framebound->frameOptions = NIL;
                            $$ = framebound;
                        }
                        ;

frame_extent:
                        frame_bound1
                        {
                            $1->frameOptions = $1->frameOptions | FRAMEOPTION_END_CURRENT_ROW;
                            $$ = $1;
                        }
                        | BETWEEN frame_bound1 AND frame_bound2
                        {
                            $2->frameOptions = FRAMEOPTION_BETWEEN | $2->frameOptions | $4->frameOptions;
                            $2->value2 = $4->value1;
                            $$ = $2;
                        }
                        ;

frame_exclusion:        EXCLUDE CURRENT_P ROW
                        {
                            $$ = FRAMEOPTION_EXCLUDE_CURRENT_ROW;
                        }
                        | EXCLUDE GROUP_P
                        {
                            $$ = FRAMEOPTION_EXCLUDE_GROUP;
                        }
                        | EXCLUDE TIES
                        {
                            $$ = FRAMEOPTION_EXCLUDE_TIES;
                        }
                        | EXCLUDE NO OTHERS
                        {
                            $$ = FRAMEOPTION_EXCLUDE_NO_OTHERS;
                        }
                        | /* EMPTY */
                        {
                            $$ = FRAMEOPTION_EXCLUDE_NO_OTHERS;
                        }
                        ;

frame_bound1:           UNBOUNDED PRECEDING
                        {
                            VFrameBound *framebound = makeNode(VFrameBound);
                            framebound->frameOptions = FRAMEOPTION_START_UNBOUNDED_PRECEDING;
                            $$ = framebound;
                        }
                        | UNBOUNDED FOLLOWING
                        {
                            VFrameBound *framebound = makeNode(VFrameBound);
                            framebound->frameOptions = FRAMEOPTION_START_UNBOUNDED_FOLLOWING;
                            $$ = framebound;
                        }
                        | a_expr PRECEDING
                        {
                            VFrameBound *framebound = makeNode(VFrameBound);
                            framebound->frameOptions = FRAMEOPTION_START_VALUE_PRECEDING;
                            framebound->value1 = $1;
                            $$ = framebound;
                        }
                        | a_expr FOLLOWING
                        {
                            VFrameBound *framebound = makeNode(VFrameBound);
                            framebound->frameOptions = FRAMEOPTION_START_VALUE_FOLLOWING;
                            framebound->value1 = $1;
                            $$ = framebound;
                        }
                        | CURRENT_P ROW
                        {
                            VFrameBound *framebound = makeNode(VFrameBound);
                            framebound->frameOptions = FRAMEOPTION_START_CURRENT_ROW;
                            framebound->value1 = NULL;
                            $$ = framebound;
                        }
                        ;

frame_bound2:           UNBOUNDED PRECEDING
                        {
                            VFrameBound *framebound = makeNode(VFrameBound);
                            framebound->frameOptions = FRAMEOPTION_END_UNBOUNDED_PRECEDING;
                            $$ = framebound;
                        }
                        | UNBOUNDED FOLLOWING
                        {
                            VFrameBound *framebound = makeNode(VFrameBound);
                            framebound->frameOptions = FRAMEOPTION_END_UNBOUNDED_FOLLOWING;
                            $$ = framebound;
                        }
                        | a_expr PRECEDING
                        {
                            VFrameBound *framebound = makeNode(VFrameBound);
                            framebound->frameOptions = FRAMEOPTION_END_VALUE_PRECEDING;
                            framebound->value1 = $1;
                            $$ = framebound;
                        }
                        | a_expr FOLLOWING
                        {
                            VFrameBound *framebound = makeNode(VFrameBound);
                            framebound->frameOptions = FRAMEOPTION_END_VALUE_FOLLOWING;
                            framebound->value1 = $1;
                            $$ = framebound;
                        }
                        | CURRENT_P ROW
                        {
                            VFrameBound *framebound = makeNode(VFrameBound);
                            framebound->frameOptions = FRAMEOPTION_END_CURRENT_ROW;
                            framebound->value1 = NULL;
                            $$ = framebound;
                        }
                        ;

/* A List of partition_clauses */
opt_partition_clause:  partition_clause  { $$ = $1; }
                       | /*EMPTY*/       { $$ = NIL; }
                       ;

partition_clause:     
                      PARTITION BY expr_list  { $$ = $3; }
                      | PARTITION BATCH BY expr_list
                      {
                          VPartitionBatch *n = makeNode(VPartitionBatch);
                          n->xprlist = $4;
                          $$ = list_make1(n);
                      }
                      | PARTITION PREPASS BY expr_list
                      {
                          VPartitionPrepass *n = makeNode(VPartitionPrepass);
                          n->xprlist = $4;
                          $$ = list_make1(n);
                      }
                      | PARTITION AUTO
                      { $$ = list_make1((Node *)makeNode(VPartitionAuto)); }
                      | PARTITION NODES
                      { $$ = list_make1((Node *)makeNode(VPartitionByNode)); }
                      | PARTITION BEST
                      { $$ = list_make1((Node *)makeNode(VPartitionByBest)); }
                      ;

/* A List of orderby_clauses */
opt_orderby_clause:   orderby_clause  { $$ = $1; }
                      | /*EMPTY*/     { $$ = NIL; }
                      ;

orderby_clause: ORDER BY orderby_list            { $$ = $3; }
        ;

orderby_list:
             orderby                           { $$ = list_make1($1); }
             | orderby_list ',' orderby        { $$ = lappend($1, $3); }
      ;

orderby:
         a_expr asc_desc_sort opt_nulls_order
         {
             $$ = makeNode(SortBy);
             $$->node = $1;
             $$->sortby_kind  = getOrderbyKind($2, $3);
             $$->useOp = NIL;
         }
     ;

asc_desc_sort:
              ASC              { $$ = SORT_ASCEND ; }
              | DESC           { $$ = SORT_DESCEND; }
              | /* EMPTY */  { $$ = SORT_ASCEND ; }
    ;


opt_nulls_order:
             NULLS FIRST_P   { $$ = NULLS_FIRST; }
             | NULLS LAST_P  { $$ = NULLS_LAST; }
             | NULLS AUTO    { $$ = NULLS_AUTO; }
             | /* EMPTY */   { $$ = NULLS_DEFAULT; }
        ;

update_target_list:
            update_target_el                        { $$ = list_make1($1); }
            | update_target_list ',' update_target_el { $$ = lappend($1,$3); }
        ;

update_target_el:
            ColId opt_indirection '=' a_expr
                {
                    $$ = makeNode(ResTarget);
                    $$->name = $1.str;
                    $$->indirection = $2;
                    $$->val = (Node *) $4;
                }
            | ColId opt_indirection '=' DEFAULT
                {
                    $$ = makeNode(ResTarget);
                    $$->name = $1.str;
                    $$->indirection = $2;
                    $$->val = (Node *) makeNode(SetToDefault);
                }

        ;

insert_target_list:
            insert_target_el                        { $$ = list_make1($1); }
            | insert_target_list ',' insert_target_el { $$ = lappend($1, $3); }
        ;

insert_target_el:
            a_expr
                {
                    $$ = makeNode(ResTarget);
                    $$->name = NULL;
                    $$->indirection = NIL;
                    $$->val = (Node *)$1;
                }
            | DEFAULT
                {
                    $$ = makeNode(ResTarget);
                    $$->name = NULL;
                    $$->indirection = NIL;
                    $$->val = (Node *) makeNode(SetToDefault);
                }
        ;


/*****************************************************************************
 *
 *    Names and constants
 *
 *****************************************************************************/

qualified_schema_name_list:
            qualified_schema_name { $$ = list_make1(makeStr($1)); }
            | qualified_schema_name_list ',' qualified_schema_name { $$ = lappend($1, makeStr($3)); }
        ;

qualified_schema_name:
            ColId { $$ = $1; }
            | ColId '.' ColId
                {
                    const char *catalogname = $1.str;
                    const char *schemaname = $3.str;
                    int cataloglen = strlen(catalogname);
                    int schemalen = strlen(schemaname);
                    char buf[cataloglen + schemalen + 4];

                    if (catalogname)
                    {
                        strcpy(buf, catalogname); // add catalog name
                        strcpy(buf+cataloglen, "~.~"); // delimit catalog from schema name
                        strcpy(buf+cataloglen+3, schemaname); // add schemna name
                    }
                    else
                        strcpy(buf, schemaname); // add schema name

                    $$ = ctString(pstrdup(buf));
                }
        ;

relation_name:
            SpecialRuleRelation                        { $$ = $1; }
            | ColId                                    { $$ = $1; }
        ;

qualified_name_list:
             qualified_name { $$ = list_make1($1); }
            | qualified_name_list ',' qualified_name { $$ = lappend($1, $3); }
        ;

relname_w_indirection:
              relation_name indirection
                {
                    check_qualified_name($2);
                    $$ = makeNode(RangeVar);
                    switch (list_length($2))
                    {
                        case 1:
                            $$->catalogname = NULL;
                            $$->schemaname = $1.str;
                            $$->relname = strVal(linitial($2));
                            break;
                        case 2:
                            $$->catalogname = $1.str;
                            $$->schemaname = strVal(linitial($2));
                            $$->relname = strVal(lsecond($2));
                            break;
                        default:
                            ereport(ERROR,
                                    (errcode(ERRCODE_SYNTAX_ERROR),
                                     errmsg("Improper qualified name (too many dots): %s",
                                            NameListToString(lcons(makeStr($1), $2)))));
                            break;
                    }
                }
        ;

hint_list:    hint_name
                    { $$ = list_make1(makeStr($1)); }
            | hint_list ',' hint_name
                    { $$ = lappend($1, makeStr($3)); }
        ;



/*
 * The syntactic rules should be the same as func_name, but the associated
 * actions are different because we want to return a RangeVar
 */
udx_func_name:
              udx_function_name
                {
                    $$ = makeNode(RangeVar);
                    $$->catalogname = NULL;
                    $$->schemaname = NULL;
                    $$->relname = $1.str;
                }
            | relname_w_indirection
                {
                    $$ = $1;
                }
        ;

/*
 * The production for a qualified relation name has to exactly match the
 * production for a qualified func_name, because in a FROM clause we cannot
 * tell which we are parsing until we see what comes after it ('(' for a
 * func_name, something else for a relation). Therefore we allow 'indirection'
 * which may contain subscripts, and reject that case in the C code.
 */
qualified_name:
            relation_name
                {
                    $$ = makeNode(RangeVar);
                    $$->catalogname = NULL;
                    $$->schemaname = NULL;
                    $$->tablesample = NULL;
                    $$->relname = $1.str;
                }
            | relname_w_indirection
                {
                    $$ = $1;
                }
        ;

name_list:    name
                    { $$ = list_make1(makeStr($1)); }
            | name_list ',' name
                    { $$ = lappend($1, makeStr($3)); }
            | name_list AND name
                    { $$ = lappend($1, makeStr($3)); }
        ;


name:        ColId                                    { $$ = $1; };

database_name:
            ColId                                    { $$ = $1; }
          | DEFAULT                                 
            { $$ = ctString(getTheDatabaseName()); }
          ;

dbname_list:
            database_name { $$ = list_make1(makeStr($1)); }
            | dbname_list ',' database_name { $$ = lappend($1, makeStr($3)); }
          ;

access_method:
            ColId                                    { $$ = $1; };

attr_name:    ColLabel                                { $$ = $1; };

index_name: qualified_name                                    { $$ = $1; };

file_name:    Sconst                                    { $$ = $1; };

/*
 * The production for a qualified func_name has to exactly match the
 * production for a qualified columnref, because we cannot tell which we
 * are parsing until we see what comes after it ('(' for a func_name,
 * anything else for a columnref).  Therefore we allow 'indirection' which
 * may contain subscripts, and reject that case in the C code.  (If we
 * ever implement SQL99-like methods, such syntax may actually become legal!)
 */
func_name:    function_name
                    { $$ = list_make1(makeStr($1)); }
            | relation_name indirection
                    { $$ = check_func_name(lcons(makeStr($1), $2)); }
        ;


/*
 * Constants
 */
AexprConst: Iconst hint_clause
                {
                    A_Const *n = makeNode(A_Const);
                    n->val.type = T_Integer;
                    n->val.val.ival = $1;
                    n->optHints = $2;
                    $$ = (Node *)n;
                }
            | FCONST hint_clause
                {
                    A_Const *n = makeNode(A_Const);
                    n->val.type = T_Float;
                    n->val.val.str = $1;
                    n->optHints = $2;
                    $$ = (Node *)n;
                }
            | Sconst hint_clause
                {
                    A_Const *n = makeNode(A_Const);
                    n->val.type = T_String;
                    n->val.val.str = $1;
                    n->optHints = $2;
                    $$ = (Node *)n;
                }
            | BCONST hint_clause
                {
                    A_Const *n = makeNode(A_Const);
                    n->val.type = T_BitString;
                    n->val.val.str = $1;
                    n->optHints = $2;
                    $$ = (Node *)n;
                }
            | XCONST hint_clause
                {
                    /* This is a varbinary constant per SQL-2008. */
                    A_Const *n = makeNode(A_Const);
                    n->val.type = T_BitString;
                    n->val.val.str = $1;
                    n->optHints = $2;
                    $$ = (Node *)n;
                }
            | ConstTypename Sconst hint_clause
                {
                    A_Const *n = makeNode(A_Const);
                    n->typeInfo = $1;
                    n->val.type = T_String;
                    n->val.val.str = $2;
                    n->optHints = $3;
                    $$ = (Node *)n;
                }
            | ConstInterval seconds_precision opt_minus Sconst hint_clause interval_qualifier
                {
                    /* seconds_precision is a PG extension */
                    A_Const *n = makeNode(A_Const);
                    n->typeInfo = (INTERVAL_RANGE($6) & INTERVAL_YEAR2MONTH) ?
                        SystemTypeName("intervalym") : $1;
                    n->val.type = T_String;
                    n->val.val.str = $4;
                    n->optHints = $5;
                    int p = Min(INTERVAL_PRECISION($2), INTERVAL_PRECISION($6));
                    int r = INTERVAL_RANGE($6);
                    if (r == 0)         // if default qualifier
                        r = INTERVAL_DAY2SECOND;
                    if ($3)
                        r |= INTERVAL_MASK(NEG_INTERVAL);
                    n->typeInfo->typmod = INTERVAL_TYPMOD(p, r);
                    $$ = (Node *)n;
                }
            | ConstIntervalYM opt_minus Sconst hint_clause interval_qualifier
                {
                    A_Const *n = makeNode(A_Const);
                    n->typeInfo = $1;
                    n->val.type = T_String;
                    n->val.val.str = $3;
                    n->optHints = $4;
                    int r = INTERVAL_RANGE($5);
                    if (r == 0)         // if default qualifier
                        r = INTERVAL_YEAR2MONTH;
                    else if (r & ~INTERVAL_YEAR2MONTH)
                        ereport(ERROR,
                                (errcode(ERRCODE_SYNTAX_ERROR),
                                 errmsg("Conflicting INTERVAL subtypes")));
                     if ($2)
                        r |= INTERVAL_MASK(NEG_INTERVAL);
                    n->typeInfo->typmod = INTERVAL_TYPMOD(0, r);
                    $$ = (Node *)n;
                }
            | TRUE_P hint_clause
                {
                    A_Const *n = makeBoolAConst(TRUE);
                    n->optHints = $2;
                    $$ = (Node *) n;
                }
            | FALSE_P hint_clause
                {
                    A_Const *n = makeBoolAConst(FALSE);
                    n->optHints = $2;
                    $$ = (Node *) n;
                }
            | NULL_P hint_clause
                {
                    A_Const *n = makeNode(A_Const);
                    n->val.type = T_Null;
                    n->optHints = $2;
                    $$ = (Node *)n;
                }
        ;

Iconst:        ICONST                                    { $$ = $1; };
Sconst:        SCONST                                    { $$ = $1; };
UserId:        ColId                                     { $$ = $1; };

ProfileId:     ColId                                     { $$ = $1; }
             | DEFAULT                                   { $$ = ctString(pstrdup($1)); }
             ;

/*
 * Name classification hierarchy.
 *
 * IDENT is the lexeme returned by the lexer for identifiers that match
 * no known keyword.  In most cases, we can accept certain keywords as
 * names, not only IDENTs.    We prefer to accept as many such keywords
 * as possible to minimize the impact of "reserved words" on programmers.
 * So, we divide names into several possible classes.  The classification
 * is chosen in part to make keywords acceptable as names wherever possible.
 */

/* Column identifier --- names that can be column, table, etc names.
 */
ColId:        IDENT                          { $$ = $1; }
            | unreserved_keyword             { $$ = ctString(pstrdup($1)); }
            | bare_col_alias_excluded_keyword{ $$ = ctString(pstrdup($1)); }
            | bare_col_rel_alias_excl_keyword{ $$ = ctString(pstrdup($1)); }
            | alias_excluded_keyword         { $$ = ctString(pstrdup($1)); }
            | col_name_keyword               { $$ = ctString(pstrdup($1)); }
            | type_excluded_keyword          { $$ = ctString(pstrdup($1)); }
            | func_excluded_keyword          { $$ = ctString(pstrdup($1)); }
        ;

/* Relation alias (bare)
 */
AliasColId:   IDENT                          { $$ = $1; }
            | unreserved_keyword             { $$ = ctString(pstrdup($1)); }
            | bare_col_alias_excluded_keyword{ $$ = ctString(pstrdup($1)); }
            | col_name_keyword               { $$ = ctString(pstrdup($1)); }
            | type_excluded_keyword          { $$ = ctString(pstrdup($1)); }
            | func_excluded_keyword          { $$ = ctString(pstrdup($1)); }
        ;
 

/* Type identifier --- names that can be type names.
 */
type_name:    IDENT                          { $$ = $1; }
            | unreserved_keyword             { $$ = ctString(pstrdup($1)); }
            | bare_col_alias_excluded_keyword{ $$ = ctString(pstrdup($1)); }
            | bare_col_rel_alias_excl_keyword{ $$ = ctString(pstrdup($1)); }
            | alias_excluded_keyword         { $$ = ctString(pstrdup($1)); }
            | func_excluded_keyword          { $$ = ctString(pstrdup($1)); }
        ;

/* Function identifier --- names that can be function names.
 */
function_name:
              IDENT                          { $$ = $1; }
            | unreserved_keyword             { $$ = ctString(pstrdup($1)); }
            | bare_col_alias_excluded_keyword{ $$ = ctString(pstrdup($1)); }
            | bare_col_rel_alias_excl_keyword{ $$ = ctString(pstrdup($1)); }
            | alias_excluded_keyword         { $$ = ctString(pstrdup($1)); }
            | func_name_keyword              { $$ = ctString(pstrdup($1)); }
        ;

/*
 * same as function_name, but gets reduce/reduce conflicts if just use function_name...
 */
udx_function_name:
              IDENT                          { $$ = $1; }
            | unreserved_keyword             { $$ = ctString(pstrdup($1)); }
            | bare_col_alias_excluded_keyword{ $$ = ctString(pstrdup($1)); }
            | bare_col_rel_alias_excl_keyword{ $$ = ctString(pstrdup($1)); }
            | alias_excluded_keyword         { $$ = ctString(pstrdup($1)); }
            | func_name_keyword              { $$ = ctString(pstrdup($1)); }
            | type_excluded_keyword          { $$ = ctString(pstrdup($1)); }
		;

/**
 * Hint identifier
 * We use this shortcut to include all keywords since ColLabel is currently
 * defined that way
 */
hint_name:
            ColLabel                                { $$ = $1; }
        ;
/**
 * argument name
 */
hive_arg_name:
            ColLabel                                { $$ = $1; }
        ;


/* Column label --- allowed labels in "AS" clauses.
 * This presently includes *all* Postgres keywords.
 */
ColLabel:     IDENT                           { $$ = $1; }
            | unreserved_keyword              { $$ = ctString(pstrdup($1)); }
            | bare_col_alias_excluded_keyword { $$ = ctString(pstrdup($1)); }
            | bare_col_rel_alias_excl_keyword{ $$ = ctString(pstrdup($1)); }
            | alias_excluded_keyword          { $$ = ctString(pstrdup($1)); }
            | col_name_keyword                { $$ = ctString(pstrdup($1)); }
            | type_excluded_keyword           { $$ = ctString(pstrdup($1)); }
            | func_excluded_keyword          { $$ = ctString(pstrdup($1)); }
            | func_name_keyword               { $$ = ctString(pstrdup($1)); }
            | reserved_keyword                { $$ = ctString(pstrdup($1)); }
            | Sconst                          { $$ = $1; }
        ;

/** Column label --- alowed without quotes or "AS" clause */
BareColLabel:  IDENT                          { $$ = $1; }
            | alias_excluded_keyword          { $$ = ctString(pstrdup($1)); }
            | type_excluded_keyword           { $$ = ctString(pstrdup($1)); }
            | func_excluded_keyword          { $$ = ctString(pstrdup($1)); }
            | unreserved_keyword              { $$ = ctString(pstrdup($1)); }
        ;

/*
 * Keyword classification lists.  Generally, every keyword present in
 * the Postgres grammar should appear in exactly one of these lists.
 *
 * Put a new keyword into the first list that it can go into without causing
 * shift or reduce conflicts.  The earlier lists define "less reserved"
 * categories of keywords.
 */
/* unreserved keyword, but not valid to be used as table alias
*/
alias_excluded_keyword: 
             ANTI
            | COMPLEX
            | CROSS
            | FULL
            | INNER_P
            | JOIN
            | LEFT
            | NATURAL
            | NULLAWARE
            | OUTER_P
            | RIGHT
            | SEMI
            | SEMIALL
            | UNI
       ;

/* "Unreserved" keywords --- available for use as any kind of name.
 */
unreserved_keyword:
              ABORT_P
            | ABSOLUTE_P
            | ACCESS
            | ACCOUNT
            | ACTION
            | ACTIVATE
            | ACTIVEPARTITIONCOUNT
            | ADD
            | ADDRESS
            | ADMIN
            | AFTER
            | AGGREGATE
            | ALSO
            | ALTER
            | ANALYSE
            | ANALYTIC
            | ANALYZE
            | ANNOTATED /*VER-50473: keyword for explain directed query*/
            | ASSIGNMENT
            | AT
            | AUTO
            | AUTHENTICATION
            | AVAILABLE
            | BACKWARD
            | BALANCE
            | BASENAME
            | BATCH
            | BEFORE
            | BEGIN_P
            | BEST
            | BLOCK
            | BLOCK_DICT
            | BLOCKDICT_COMP
            | BRANCH
            | BROADCAST
            | BY
            | BYTES
            | BZIP
            | BZIP_COMP
            | CACHE
            | CALLED
            | CASCADE
            | CATALOGPATH
            | CHAIN
            | CHARACTERISTICS
            | CHARACTERS
            | CHECKPOINT
            | CLASS
            | CLEAR
            | CLOSE
            | CLUSTER
            | COLSIZES
            | COLUMNS_COUNT
            | COMMENT
            | COMMIT
            | COMMITTED
            | COMMONDELTA_COMP
            | COMMUNAL
            | CONNECT
            | CONSTRAINTS
            | CONTROL
            | COPY
            | CPUAFFINITYMODE
            | CPUAFFINITYSET
            | CREATEDB
            | CREATEUSER
            | CSV
            | CUBE
            | CURRENT_P
            | CURSOR
            | CUSTOM
            | CUSTOM_PARTITIONS
            | CYCLE
            | DATA_P
            | DATABASE
            | DATAPATH
            | DEACTIVATE
            | DEALLOCATE
            | DECLARE
            | DEFAULTS
            | DEFERRED
            | DEFINE
            | DEFINER
            | DELETE_P
            | DELIMITER
            | DELIMITERS
            | DELTARANGE_COMP
            | DELTARANGE_COMP_SP
            | DELTAVAL
            | DEPENDS
            | DETERMINES
            | DIRECT
            | DIRECTCOLS
            | DIRECTED
            | DIRECTGROUPED
            | DIRECTPROJ
            | DISABLE
            | DISABLED
            | DISCONNECT
            | DISTVALINDEX
            | DO
            | DOMAIN_P
            | DOUBLE_P
            | DROP
            | DURABLE
            | EACH
            | ENABLE
            | ENABLED
            | ENCLOSED
            | ENCODING
            | ENCRYPTED
            | ENFORCELENGTH
            | EPHEMERAL
            | EPOCH_P
            | ERROR_P
            | ESCAPE
            | EVENT_P
            | EVENTS_P
            | EXCEPTION
            | EXCEPTIONS
            | EXCLUDE
            | EXCLUDING
            | EXCLUSIVE
            | EXECUTE
            | EXECUTIONPARALLELISM
            | EXPIRE
            | EXPLAIN
            | EXPORT
            | EXTEND
            | EXTERNAL
            | FAILED_LOGIN_ATTEMPTS
            | FAULT
            | FENCED
            | FETCH
            | FILESYSTEM
            | FILLER
            | FILTER
            | FIXEDWIDTH
            | FIRST_P
            | FLEX
            | FLEXIBLE
            | FOLLOWING
            | FORCE
            | FORMAT
            | FORWARD
            | FREEZE
            | FUNCTION
            | FUNCTIONS
            | GCDDELTA
            | GET
            | GLOBAL
            | GRACEPERIOD
            | GROUPED
            | GROUPING
            | GZIP
            | GZIP_COMP
            | HANDLER
            | HCATALOG
            | HCATALOG_CONNECTION_TIMEOUT
            | HCATALOG_DB
            | HCATALOG_SCHEMA
            | HCATALOG_SLOW_TRANSFER_LIMIT
            | HCATALOG_SLOW_TRANSFER_TIME
            | HCATALOG_USER
            | HIGH
            | HIVESERVER2_HOSTNAME
            | HOLD
            | HOST
            | HOSTNAME
            | HOURS_P
            | IDENTIFIED
	    | IDLESESSIONTIMEOUT
            | IF_P
            | IGNORE
            | IMMEDIATE
            | IMMUTABLE
            | IMPLICIT_P
            | INCLUDE
            | INCLUDING
            | INCREMENT
            | INDEX
            | INHERITS
            | INPUT_P
            | INSENSITIVE
            | INSERT
            | INSTEAD
            | INTERFACE
            | INVOKER
            | ISOLATION
            | JSON
            | KEY
            | LABEL
            | LANCOMPILER
            | LANGUAGE
            | LARGE_P
            | LAST_P
            | LATEST
            | LESS
            | LEVEL
            | LIBRARY
            | LISTEN
            | LOAD
            | LOCAL
            | LOCATION
            | LOCK_P
            | LOW
            | LZO
            | MANAGED
            | MASK
            | MATCHED
            | MATERIALIZE
            | MAXCONCURRENCY
            | MAXCONCURRENCYGRACE
            | MAXCONNECTIONS
            | MAXMEMORYSIZE
            | MAXPAYLOAD
            | MAXQUERYMEMORYSIZE
            | MAXVALUE
            | MEDIUM
            | METHOD
            | MEMORYCAP
            | MEMORYSIZE
            | MERGE
            | MERGEOUT
            | MICROSECONDS_P
            | MILLISECONDS_P
            | MINUTES_P
            | MINVALUE
            | MODE
            | MODEL
            | MOVE
            | MOVEOUT
            | NAME_P
            | NATIVE
            | NETWORK
            | NEXT
            | NO
            | NOCREATEDB
            | NOCREATEUSER
            | NODE
            | NODES
            | NOTHING
            | NOTIFIER
            | NOTIFY
            | NOWAIT
            | NULLCOLS
            | NULLS
            | OBJECT_P
            | OCTETS
            | OF
            | OFF
            | OIDS
            | OPERATOR
            | OPT
            | OPTIMIZER
            | OPTION
            | OPTVER
            | ORC
            | OTHERS
            | OWNER
            | PARAMETER
            | PARAMETERS
            | PARQUET
            | PARSER
            | PARTIAL
            | PARTITION
            | PARTITIONING
            | PASSWORD
            | PASSWORD_GRACE_TIME
            | PASSWORD_LIFE_TIME
            | PASSWORD_LOCK_TIME
            | PASSWORD_REUSE_TIME
            | PASSWORD_MAX_LENGTH
            | PASSWORD_MIN_DIGITS
            | PASSWORD_MIN_LENGTH
            | PASSWORD_MIN_LETTERS
            | PASSWORD_MIN_LOWERCASE_LETTERS
            | PASSWORD_MIN_SYMBOLS
            | PASSWORD_MIN_UPPERCASE_LETTERS
            | PASSWORD_REUSE_MAX
            | PATH
            | PATTERN
            | PERCENT
            | PERMANENT
            | PLACING
            | PLANNEDCONCURRENCY
            | POLICY
            | POOL
            | PORT
            | PRECEDING
            | PREFER
            | PREPARE
            | PREPASS
            | PRESERVE
            | PREVIOUS_P
            | PRIOR
            | PRIORITY
            | PRIVILEGES
            | PROCEDURAL
            | PROCEDURE
            | PROFILE
            | PROJECTION
            | PROJECTIONS
            | PSDATE
            | QUERY
            | QUEUETIMEOUT
            | QUOTE
            | RANDOM
            | RANGE
            | READ
            | RECHECK
            | RECORD_P
            | RECOVER
            | RECURSIVE
            | REFRESH
            | REINDEX
            | REJECTED_P
            | REJECTMAX
            | RELATIVE_P
            | RELEASE
            | REMOVE
            | RENAME
            | REORGANIZE
            | REPEATABLE
            | REPLACE
            | RESET
            | RESOURCE
            | RESTART
            | RESTRICT
            | RESULTS
            | RETURN
            | RETURNREJECTED
            | REVOKE
            | RLE
            | ROLE
            | ROLES
            | ROLLBACK_P
            | ROLLUP
            | ROUTE
            | ROUTING
            | ROWS
            | RULE
            | RUNTIMECAP
            | RUNTIMEPRIORITY
            | RUNTIMETHRESHOLD
            | SAVE
            | SAVEPOINT
            | SCROLL
            | SEARCH_PATH
            | SECONDS_P
            | SECURITY
            | SECURITY_ALGORITHM
            | SEQUENCE
            | SEQUENCES
            | SERIALIZABLE
            | SESSION
            | SET
            | SETS
            | SHARE
            | SHARED
            | SHOW
            | SIMPLE
            | SINGLEINITIATOR
            | SKIP
            | SOURCE
            | SPLIT
            | SSL_CONFIG
            | STABLE
            | STANDBY
            | START
            | STATEMENT
            | STATISTICS
            | STDIN
            | STDOUT
            | STEMMER
            | STORAGE
            | STREAM_P
            | STRENGTH
            | STRICT_P
            | SUBNET
            | SYSID
            | SYSTEM
            | TABLES
            | TABLESPACE
            | TEMP
            | TEMPLATE
            | TEMPORARY
            | TEMPSPACECAP
            | TERMINATOR_P
            | TEXT
            | THAN
            | TIES
            | TLS
            | TLSMODE
            | TOAST
            | TOLERANCE
            | TOKENIZER
            | TRANSACTION
            | TRANSFORM
            | TRICKLE
            | TRIGGER
            | TRUNCATE
            | TRUSTED
            | TUNING
            | TYPE_P
            | UDPARAMETER
            | UNCOMMITTED
            | UNCOMPRESSED
            | UNINDEXED
            | UNKNOWN
            | UNLIMITED
            | UNLISTEN
            | UNLOCK_P
            | UNPACKER
            | UPDATE
            | USAGE
            | VACUUM
            | VALIDATE
            | VALIDATOR
            | VALUE_P
            | VALUES
            | VERBOSE
            | VERTICA
            | VIEW
            | VOLATILE
            | WAIT
            | WEBHDFS_ADDRESS
            | WEBSERVICE_HOSTNAME
            | WEBSERVICE_PORT
            | WORK
            | WRITE
            | ZONE
            | ZSTD
            | ZSTD_COMP
            | ZSTD_FAST_COMP
            | ZSTD_HIGH_COMP
;

/*
 * Words that cannot be used as bare column aliases
 *  because they look like part of the expression, or
 *  something that would follow an expression.
 * These can be used with quotes or AS, of course
 */
bare_col_alias_excluded_keyword:
              ASSERTION /* Causes conflicts */
            | DAY_P /* Causes conflicts */
            | HOUR_P /* Causes conflicts */
            | ILIKE /* Causes conflics */
            | ILIKEB
            | INTERPOLATE /* Causes conflicts */
            | ISNULL
            | LIKEB
            | MINUTE_P /* Causes conflicts */
            | MONTH_P /* Causes conflicts */
            | NOTNULL
            | SECOND_P /* Causes conflicts */
            | VARYING /* Causes conflicts */
            | WITHOUT /* Causes conflicts */
            | YEAR_P /* Causes conflicts */
        ;

/*
 * Words that cannot be used as a bare column alias
 *  or as a bare relation alias because they look like
 *  set operators
 */
bare_col_rel_alias_excl_keyword:
              ENCODED /* Encoded optionally bumps up against the select list in proj definition */
            | KSAFE
            | MINUS
            | PINNED
            | SEGMENTED
            | UNSEGMENTED
;

/*
 * These are function-like but handled by parser, so can't be used as
 *  function names
 */
func_excluded_keyword:
              DATEDIFF
            | DECODE
            | TIMESTAMPADD
            | TIMESTAMPDIFF
;

/*
 * These are things we would not allow as type names,
 *  but may work as bare words elsewhere.
 */
type_excluded_keyword:
              ACCESSRANK /* Used in type modifiers */
            | AUTO_INC
            | BIGINT
            | BIT
            | BYTEA
            | BOOLEAN_P
            | CHAR_P
            | CHARACTER
            | DATETIME
            | DEC
            | DECIMAL_P
            | FLOAT_P
            | IDENTITY_P
            | INT_P
            | INTEGER
            | LONG
            | MONEY
            | NATIONAL
            | NCHAR
            | NUMBER_P
            | NUMERIC
            | RAW
            | REAL
            | SETOF
            | SMALLDATETIME
            | SMALLINT
            | TIME
            | TIMESTAMP
            | TIMESTAMPTZ
            | TIMETZ
            | TINYINT
            | UUID
            | VALINDEX
            | VARCHAR2
        ;

/* Column identifier --- keywords that can be column, table, etc names.++
 *
 * Many of these keywords will in fact be recognized as type or function
 * names too; but they have special productions for the purpose, and so
 * can't be treated as "generic" type or function names.
 *
 * The type names appearing here are not usable as function names
 * because they can be followed by '(' in typename productions, which
 * looks too much like a function call for an LR(1) parser.
 */
col_name_keyword:
              CHAR_LENGTH
            | CHARACTER_LENGTH
            | EXISTS
            | EXTRACT
            | INOUT
            | NONE
            | OUT_P
            | OVERLAY
            | POSITION
            | PRECISION
            | ROW
            | SUBSTRING
            | TIMEZONE
            | TREAT
            | TRIM
            | VARBINARY
            | VARCHAR
        ;

/* Function identifier --- keywords that can be function names.
 *
 * Most of these are keywords that are used as operators in expressions;
 * in general such keywords can't be column names because they would be
 * ambiguous with variables, but they are unambiguous as function identifiers.
 *
 * Do not include POSITION, SUBSTRING, etc here since they have explicit
 * productions in a_expr to support the goofy SQL9x argument syntax.
 * - thomas 2000-11-28
 */
func_name_keyword:
              AUTHORIZATION
            | BETWEEN
            | CORRELATION /* Fubar because ALTER TABLE ADD takes keyword or col name */
            | IS
            | LIKE
            | LIMIT
            | OVER
            | OVERLAPS
            | SIMILAR
            | TIMESERIES
            | UNBOUNDED
        ;

/* Reserved keyword --- these keywords are usable only as a ColLabel.
 *
 * Keywords appear here if they could not be distinguished from variable,
 * type, or function names in some contexts.  Don't put things here unless
 * forced to.
 */
reserved_keyword:
            ALL
            | AND
            | ANY
            | ARRAY
            | AS
            | ASC
            | BINARY
            | BOTH
            | CASE
            | CAST
            | CHECK
            | COLLATE
            | COLUMN
            | CONSTRAINT
            | CREATE
            | CURRENT_DATABASE /* Function handled by parse; parens optional */
            | CURRENT_DATE
            | CURRENT_SCHEMA
            | CURRENT_TIME
            | CURRENT_TIMESTAMP
            | CURRENT_USER
            | DEFAULT
            | DEFERRABLE
            | DESC
            | DISTINCT
            | ELSE
            | END_P
            | EXCEPT
            | FALSE_P
            | FOR
            | FOREIGN
            | FROM
            | GRANT
            | GROUP_P
            | HAVING
            | IN_P
            | INITIALLY
            | INTERSECT
            | INTERVAL
            | INTERVALYM
            | INTO
            | LEADING
            | LOCALTIME
            | LOCALTIMESTAMP
            | MATCH
            | NEW
            | NOT
            | NULL_P
            | NULLSEQUAL
            | OFFSET
            | OLD
            | ON
            | ONLY
            | OR
            | ORDER
            | PRIMARY
            | REFERENCES
            | SCHEMA
            | SELECT
            | SESSION_USER
            | SOME
            | SYSDATE
            | TABLE
            | THEN
            | TO
            | TRAILING
            | TRUE_P
            | UNION
            | UNIQUE
            | USER
            | USING
            | WHEN
            | WHERE
            | WINDOW
            | WITH
            | WITHIN
        ;


SpecialRuleRelation:
            OLD
                {
                    if (QueryIsRule)
                        $$ = ctString("*OLD*");
                    else
                        ereport(ERROR,
                                (errcode(ERRCODE_SYNTAX_ERROR),
                                 errmsg("OLD used in query that is not in a rule")));
                }
            | NEW
                {
                    if (QueryIsRule)
                        $$ = ctString("*NEW*");
                    else
                        ereport(ERROR,
                                (errcode(ERRCODE_SYNTAX_ERROR),
                                 errmsg("NEW used in query that is not in a rule")));
                }
        ;

%%

static const char *
convertPercentageToQuestionMark(const char *operName)
{
    if (strcmp(operName, "%") == 0)
        return "?";
    if (strcmp(operName, "*%") == 0)
        return "*?";
    if (strcmp(operName, "+%") == 0)
        return "+?";
    if (strcmp(operName, "%%") == 0)
        return "??";
    if (strcmp(operName, "%+") == 0)
        return "?+";
    return operName;
}

static PatternRegExprType
getPatternRegExprType(const char *operName)
{

    Assert(operName && strlen(operName) >= 1);

    if(strlen(operName) > 2 ||
       (strlen(operName) == 2 && (operName[1] != '?' && operName[1] != '+')))
    {
        ereport(ERROR,
                (errcode(ERRCODE_PATTERN_MATCH_ERROR),
                 errmsg("Unsupported pattern operator")));
    }

    if(operName[0] == '*')
    {
        return PATTERN_OP_KLEENE_CLOSURE;
    }
    else if(operName[0] == '+')
    {
        return PATTERN_OP_POSITIVE_CLOSURE;
    }
    else if(operName[0] == '?')
    {
        return PATTERN_OP_ONE_OR_ZERO;
    }
    // never called...for these operNames
    // else if(strncmp(operName, '|', 1) == 0)
    // {
    //     return PATTERN_OP_ALTERNATION;
    // }
    // else if(strncmp(operName, 'o', 1) == 0)
    // {
    //     return PATTERN_OP_CONCATENATION;
    // }
    else
    {
        ereport(ERROR,
                (errcode(ERRCODE_PATTERN_MATCH_ERROR),
                 errmsg("Unsupported pattern operator")));
    }

}

static bool
isPatternOpLazy(const char *operName)
{
    Assert(operName && strlen(operName) >= 1);

    if(strlen(operName) < 2)
        return false;

    if(operName[1] == '?')
    {
        return true;
    }
    else
    {
        return false;
    }

}

static bool
isPatternOpPossessive(const char *operName)
{
    Assert(operName && strlen(operName) >= 1);

    if(strlen(operName) < 2)
        return false;

    if(operName[1] == '+')
    {
        return true;
    }
    else
    {
        return false;
    }
}

static Node *
makeColumnRef(const char *relname, List *indirection)
{
    /*
     * Generate a ColumnRef node, with an A_Indirection node added if there
     * is any subscripting in the specified indirection list.  However,
     * any field selection at the start of the indirection list must be
     * transposed into the "fields" part of the ColumnRef node.
     */
    ColumnRef  *c = makeNode(ColumnRef);
    int        nfields = 0;
    ListCell *l;

    foreach(l, indirection)
    {
        if (IsA(lfirst(l), A_Indices))
        {
            A_Indirection *i = makeNode(A_Indirection);

            if (nfields == 0)
            {
                /* easy case - all indirection goes to A_Indirection */
                c->fields = list_make1(makeString(relname));
                i->indirection = indirection;
            }
            else
            {
                /* got to split the list in two */
                i->indirection = list_copy_tail(indirection, nfields);
                indirection = list_truncate(indirection, nfields);
                c->fields = lcons(makeString(relname), indirection);
            }
            i->arg = (Node *) c;
            return (Node *) i;
        }
        nfields++;
    }
    /* No subscripting, so all indirection gets added to field list */
    c->fields = lcons(makeString(relname), indirection);
    return (Node *) c;
}

static Node *
makeTypeCast(Node *arg, TypeName *typeInfo, bool soft)
{
    /*
     * Simply generate a TypeCast node.
     *
     * Earlier we would determine whether an A_Const would
     * be acceptable, however Domains require coerce_type()
     * to process them -- applying constraints as required.
     */
    TypeCast *n = makeNode(TypeCast);
    n->arg = arg;
    n->typeInfo = typeInfo;
    n->isFailSoft = soft;
    return (Node *) n;
}

/**
 * Const hints cannot be parsed in the correct spot if they contain cast
 * information. This method generates a TypeCast node, and adds hintclause if
 * the input node is a Const.
 */
static Node *
makeTypeCastWithHints(Node *arg, TypeName *typeInfo, List* hintClause, bool soft)
{
    if (hintClause) {
        if (!IsA(arg, A_Const)) {
            ereport(ERROR, (errcode(ERRCODE_SYNTAX_ERROR),
                    errmsg("Unsupported hint for input expr")));
        }
        ((A_Const *) arg)->optHints = hintClause;
    }
    return makeTypeCast(arg, typeInfo, soft);
}

static Node *
makeStringConst(ctStr str, TypeName *typeInfo)
{
    A_Const *n = makeNode(A_Const);

    n->val.type = T_String;
    n->val.val.str = str;
    n->typeInfo = typeInfo;

    return (Node *)n;
}

static Node *
makeIntConst(int64 val)
{
    A_Const *n = makeNode(A_Const);
    n->val.type = T_Integer;
    n->val.val.ival = val;
    n->typeInfo = SystemTypeName("int8");

    return (Node *)n;
}

static Node *
makeFloatConst(const char *str)
{
    A_Const *n = makeNode(A_Const);

    n->val.type = T_Float;
    n->val.val.str = ctString(str);
    n->typeInfo = SystemTypeName("float8");

    return (Node *)n;
}

static Node *
makeAConst(Value *v)
{
    Node *n;

    switch (v->type)
    {
        case T_Float:
            n = makeFloatConst(v->val.str.str);
            break;

        case T_Integer:
            n = makeIntConst(v->val.ival);
            break;

        case T_String:
        default:
            n = makeStringConst(v->val.str, NULL);
            break;
    }

    return n;
}


/* makeMapElem()
 * Create a MapElem node and set contents.
 * MapElem has integer index instead of string in DefElem
 */
static MapElem *
makeMapElem(int64 ind, Node *arg)
{
    MapElem *f = makeNode(MapElem);
    f->ind = ind;
    f->arg = arg;
    return f;
}

/* makeBoolAConst()
 * Create an A_Const node and initialize to a boolean constant.
 */
static A_Const *
makeBoolAConst(bool state)
{
    A_Const *n = makeNode(A_Const);
    n->val.type = T_String;
    n->val.val.str = (state ? ctString("t") : ctString("f"));
    n->typeInfo = SystemTypeName("bool");
    return n;
}

/* makeRowNullTest()
 * Generate separate operator nodes for a single row descriptor test.
 *
 * Eventually this should be eliminated in favor of making the NullTest
 * node type capable of handling it directly.
 */
static Node *
makeRowNullTest(NullTestType test, RowExpr *row)
{
    Node        *result = NULL;
    ListCell    *arg;

    foreach(arg, row->args)
    {
        NullTest *n;

        n = makeNode(NullTest);
        n->arg = (Expr *) lfirst(arg);
        n->nulltesttype = test;

        if (result == NULL)
            result = (Node *) n;
        else if (test == IS_NOT_NULL)
            result = (Node *) makeA_Expr(AEXPR_OR, NIL, result, (Node *)n);
        else
            result = (Node *) makeA_Expr(AEXPR_AND, NIL, result, (Node *)n);
    }

    if (result == NULL)
    {
        /* zero-length rows?  Generate constant TRUE or FALSE */
        result = (Node *) makeBoolAConst(test == IS_NULL);
    }

    return result;
}

/* makeOverlaps()
 * Create and populate a FuncCall node to support the OVERLAPS operator.
 */
static FuncCall *
makeOverlaps(List *largs, List *rargs)
{
    FuncCall *n = makeNode(FuncCall);
    n->funcname = SystemFuncName("overlaps");
    if (list_length(largs) == 1)
        largs = lappend(largs, largs);
    else if (list_length(largs) != 2)
        ereport(ERROR,
                (errcode(ERRCODE_SYNTAX_ERROR),
                 errmsg("Wrong number of parameters on left side of OVERLAPS expression")));
    if (list_length(rargs) == 1)
        rargs = lappend(rargs, rargs);
    else if (list_length(rargs) != 2)
        ereport(ERROR,
                (errcode(ERRCODE_SYNTAX_ERROR),
                 errmsg("Wrong number of parameters on right side of OVERLAPS expression")));
    n->args = list_concat(largs, rargs);
    n->agg_star = FALSE;
    n->agg_distinct = FALSE;
    n->agg_all = FALSE;
    return n;
}

/* check_qualified_name --- check the result of qualified_name production
 *
 * It's easiest to let the grammar production for qualified_name allow
 * subscripts and '*', which we then must reject here.
 */
static void
check_qualified_name(List *names)
{
    ListCell   *i;

    foreach(i, names)
    {
        if (!IsA(lfirst(i), String))
            yyerror("syntax error");
        /*else if (strcmp(strVal(lfirst(i)), "*") == 0)
            yyerror("syntax error");*/
    }
}

/* check_func_name --- check the result of func_name production
 *
 * It's easiest to let the grammar production for func_name allow subscripts
 * and '*', which we then must reject here.
 */
static List *
check_func_name(List *names)
{
    ListCell   *i;

    foreach(i, names)
    {
        if (!IsA(lfirst(i), String))
            yyerror("syntax error");
        else if (strcmp(strVal(lfirst(i)), "*") == 0)
            yyerror("syntax error");
    }
    return names;
}

/* extractArgTypes()
 * Given a list of FunctionParameter nodes, extract a list of just the
 * argument types (TypeNames).  Most of the productions using func_args
 * don't currently want the full FunctionParameter data, so we use this
 * rather than having two sets of productions.
 */
static List *
extractArgTypes(List *parameters)
{
    List       *result = NIL;
    ListCell   *i;

    foreach(i, parameters)
    {
        FunctionParameter *p = (FunctionParameter *) lfirst(i);

        result = lappend(result, p->argType);
    }
    return result;
}

/* findLeftmostSelect()
 * Find the leftmost component SelectStmt in a set-operation parsetree.
 */
/*
static SelectStmt *
findLeftmostSelect(SelectStmt *node)
{
    while (node && node->op != SETOP_NONE)
        node = node->larg;
    Assert(node && IsA(node, SelectStmt) && node->larg == NULL);
    return node;
}
*/

/* insertSelectOptions()
 * Insert ORDER BY, etc into an already-constructed SelectStmt.
 *
 * This routine is just to avoid duplicating code in SelectStmt productions.
 */
static void
insertSelectOptions(SelectStmt *stmt,
                    List *sortClause, List *forUpdate,
                    Node *limitOffset, Node *limitCount,
                    List *limitPartition, List *limitSort,
                    WithClause *withClause)
{
    /*
     * Tests here are to reject constructs like
     *    (SELECT foo ORDER BY bar) ORDER BY baz
     */
    if (sortClause)
    {
        if (stmt->sortClause)
            ereport(ERROR,
                    (errcode(ERRCODE_SYNTAX_ERROR),
                     errmsg("Multiple ORDER BY clauses are not allowed")));
        stmt->sortClause = sortClause;
    }
    if (forUpdate)
    {
        if (stmt->forUpdate)
            ereport(ERROR,
                    (errcode(ERRCODE_SYNTAX_ERROR),
                     errmsg("Multiple FOR UPDATE clauses are not allowed")));
        stmt->forUpdate = forUpdate;
    }
    if (limitOffset)
    {
        if (stmt->limitOffset)
            ereport(ERROR,
                    (errcode(ERRCODE_SYNTAX_ERROR),
                     errmsg("Multiple OFFSET clauses are not allowed")));
        stmt->limitOffset = limitOffset;
    }
    if (limitCount)
    {
        if (stmt->limitCount)
            ereport(ERROR,
                    (errcode(ERRCODE_SYNTAX_ERROR),
                     errmsg("Multiple LIMIT clauses are not allowed")));
        stmt->limitCount = limitCount;
    }
    if (limitPartition)
    {
        if (stmt->limitPartition)
            ereport(ERROR,
                    (errcode(ERRCODE_SYNTAX_ERROR),
                     errmsg("Multiple PARTITION clauses in TopK/Limit query are not allowed")));
        stmt->limitPartition = limitPartition;
    }
    if (limitSort)
    {
        if (stmt->limitSort)
            ereport(ERROR,
                    (errcode(ERRCODE_SYNTAX_ERROR),
                     errmsg("Multiple ORDER BY clauses in partition TopK/Limit query are not allowed")));
        stmt->limitSort = limitSort;
    }
    if (withClause)
    {
        if (stmt->withClause)
            ereport(ERROR,
                    (errcode(ERRCODE_SYNTAX_ERROR),
                     errmsg("multiple WITH clauses not allowed")));

        stmt->withClause = withClause;
        tmpSetColumnAliasForWithQueries(stmt);
    }
}

/* insertSamplingOptions()
 * Insert sampling instructions into an already-constructed SelectStmt.
 *
 * This routine is just to avoid duplicating code in SelectStmt productions.
 */
// static void
// insertSamplingOptions(SelectStmt *stmt, Node *sampleStorageCount, Node *sampleStoragePercent, Node *sampleStorageBandCount)
// {
//     /*
//      * Tests here are to reject constructs like
//      *    (SELECT foo ORDER BY bar) ORDER BY baz
//      */
//     if (sampleStorageCount)
//     {
//         if (stmt->sampleStorageCount)
//             ereport(ERROR,
//                     (errcode(ERRCODE_SYNTAX_ERROR),
//                      errmsg("Multiple SAMPLE clauses are not allowed")));
//         stmt->sampleStorageCount = sampleStorageCount;
//     }
//     if (sampleStoragePercent)
//     {
//         if (stmt->sampleStoragePercent)
//             ereport(ERROR,
//                     (errcode(ERRCODE_SYNTAX_ERROR),
//                      errmsg("Multiple SAMPLE clauses are not allowed")));
//         stmt->sampleStoragePercent = sampleStoragePercent;
//     }
//     if (sampleStorageBandCount)
//     {
//         if (stmt->sampleStorageBandCount)
//             ereport(ERROR,
//                     (errcode(ERRCODE_SYNTAX_ERROR),
//                      errmsg("Multiple SAMPLE clauses are not allowed")));
//         stmt->sampleStorageBandCount = sampleStorageBandCount;
//     }

// }

static Node *
makeSetOp(SetOperation op, bool all, List *setopHints, Node *larg, Node *rarg, int loc)
{
    SelectStmt *n = makeNode(SelectStmt);
    n->op = op;
    n->setopHints = setopHints;
    n->all = all;
    n->larg = (SelectStmt *) larg;
    n->rarg = (SelectStmt *) rarg;
    return (Node *) n;
}

/* SystemFuncName()
 * Build a properly-qualified reference to a built-in function.
 */
List *
SystemFuncName(const char *name)
{
    return list_make2(makeString("catalog"), makeString(name));
}

/* SystemTypeName()
 * Build a properly-qualified reference to a built-in type.
 *
 * typmod is defaulted, but may be changed afterwards by caller.
 */
TypeName *
SystemTypeName(const char *name)
{
    TypeName   *n = makeNode(TypeName);

    n->names = list_make2(makeString("catalog"), makeString(name));
    n->typmod = -1;
    return n;
}

/* parser_init()
 * Initialize to parse one query string
 */
void



parser_init(void)
{
    QueryIsRule = FALSE;
}

/* exprIsNullConstant()
 * Test whether an a_expr is a plain NULL constant or not.
 */
bool
exprIsNullConstant(Node *arg)
{
    if (arg && IsA(arg, A_Const))
    {
        A_Const *con = (A_Const *) arg;

        if (con->val.type == T_Null &&
            con->typeInfo == NULL)
            return TRUE;
    }
    return FALSE;
}

/* doNegate()
 * Handle negation of a numeric constant.
 *
 * Formerly, we did this here because the optimizer couldn't cope with
 * indexquals that looked like "var = -4" --- it wants "var = const"
 * and a unary minus operator applied to a constant didn't qualify.
 * As of Postgres 7.0, that problem doesn't exist anymore because there
 * is a constant-subexpression simplifier in the optimizer.  However,
 * there's still a good reason for doing this here, which is that we can
 * postpone committing to a particular internal representation for simple
 * negative constants.    It's better to leave "-123.456" in string form
 * until we know what the desired type is.
 */
static Node *
doNegate(Node *n)
{
    if (IsA(n, A_Const))
    {
        A_Const *con = (A_Const *)n;

        if (con->val.type == T_Integer)
        {
            con->val.val.ival = -con->val.val.ival;
            return n;
        }
        if (con->val.type == T_Float)
        {
            doNegateFloat(&con->val);
            return n;
        }
    }

    return (Node *) makeSimpleA_Expr(AEXPR_OP, "-", NULL, n);
}

static void
doNegateFloat(Value *v)
{
    const char *oldval = v->val.str.str;

    Assert(IsA(v, Float));
    if (*oldval == '+')
        oldval++;
    if (*oldval == '-')
        v->val.str = ctString(oldval+1);    /* just strip the '-' */
    else
    {
        char   *newval = (char *) palloc(strlen(oldval) + 2);

        *newval = '-';
        strcpy(newval+1, oldval);
        v->val.str = ctString(newval);
    }
}

SortOpType getOrderbyKind(SortOpType ascDecs, SortNullsMask nullsFirstLastAuto)
{
    SortOpType sorttype = SORT_INVALID;
    if(nullsFirstLastAuto == NULLS_DEFAULT)
    {
        switch(ascDecs)
        {
        case SORT_ASCEND:
            sorttype = SORT_ASCEND_NULLS_LAST;
            break;
        case SORT_DESCEND:
            sorttype = SORT_DESCEND_NULLS_FIRST;
            break;
        default:
            break;
        }
    }
    else
        sorttype = ascDecs | nullsFirstLastAuto;

    return sorttype;
}


void isFirstLastValueFunc(List *name)
{
    const char *schemaname;
    const char *funcname;

    /* deconstruct the name list */
    DeconstructQualifiedName(name, &schemaname, &funcname);

    /* The max size of str we want to compare is strlen("first_value") + 1
     * If the funcname is bigger than that its not first_value or last_value
     */
    const size_t strcopysize = 15; /* aka strlen("ts_first_value") + 1 */
    size_t max = strlen(funcname);
    int i;
    if(max < strcopysize)
    {
        char strcopy[strcopysize];
        for(i = 0; i < max; ++i)
            strcopy[i] = tolower(funcname[i]);

        strcopy[i] = 0;

        if((strncmp(strcopy, "first_value", max) == 0) ||
           (strncmp(strcopy, "last_value",  max) == 0) ||
           (strncmp(strcopy, "nth_value",  max) == 0) ||
           (strncmp(strcopy, "ts_first_value",  max) == 0) ||
           (strncmp(strcopy, "ts_last_value",  max) == 0))
        {
            return; /* all is well */
        }
    }

    /* If we reach here error out */
    ereport(ERROR,
            (errcode(ERRCODE_SYNTAX_ERROR),
             errmsg("IGNORE NULLS can only be used with FIRST_VALUE or LAST_VALUE or NTH_VALUE")));

}

// Add flex table implicit columns.
// Done this early to ensure it correctly creates auto projections.
static void addFlexTableColumns(CreateStmt *stmt)
{
    // Adds columns in reverse order due to using lcons
    ereport(LOG, (errmsg("Adding flex table column(s)")));
    int sz = getFlexTableFieldWidth();
    addImplicitFlexTableColumn(stmt, getFlexTableRawColName(), false, sz);
    if (stmt->tableElts->length == 1 && !stmt->flexMaterializeAll)  // Only add the __identity__ column if the __raw__ column is the only other
        addImplicitFlexTableColumn(stmt, getFlexTableIdColName(), true, sz);
}

void confirmHiveFormatLimits(CopyStmt* stmt)
{
    const char* format = (strcmp(stmt->format, "parquet") == 0) ? "PARQUET" : "ORC"; 
    if ((strcmp(stmt->format, "parquet") == 0 || strcmp(stmt->format, "orc") == 0)) {
       // Should be error message in attempt to copy ORC or PARQUET files using UDSource (VER-45584)
       if (stmt->userdefined_copy->source != NULL) {
        ereport(ERROR, (errmsg("Cannot use an UDSource with %s files", format),
                        errcode(ERRCODE_SYNTAX_ERROR)));
       }
       // Check that no compression specified for ORC files (VER-37260)
       if (stmt->sources != NIL) {
           ListCell* lc = list_head(stmt->sources->sources);
           while (lc != NIL) {
             const char* comp = ((VCopySource*)lfirst(lc))->compression;
             if (strcmp(comp, "UNCOMPRESSED") != 0) { 
                ereport(ERROR, (errmsg("Cannot use %s compression with %s files", comp, format),
                        errcode(ERRCODE_SYNTAX_ERROR)));
             }
             lc = lnext(lc);
           }
       }
    }
}

// Check that ORC is not used with FLEX (VER-43723)
void confirmFlexNotUsingHive(CopyStmt* stmt) {
    if (strcmp(stmt->format, "orc") == 0) {
        ereport(ERROR, (errmsg("Cannot use ORC format with FLEX tables"),
                        errcode(ERRCODE_SYNTAX_ERROR)));
    } else if (strcmp(stmt->format, "parquet") == 0) {
        ereport(ERROR, (errmsg("Cannot use PARQUET format with FLEX tables"),
                        errcode(ERRCODE_SYNTAX_ERROR)));
    }
}

/*
 * Must undefine base_yylex before including scan.c, since we want it
 * to create the function base_yylex not filtered_base_yylex.
 */
#undef base_yylex

#include "scan.c"
