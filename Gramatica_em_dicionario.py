from Acoes_semanticas import *
from Variaveis import *

# Construção da árvore de expressão
CREATE_INT_CONSTANT_NODE = AcaoSemantica(create_node, [FACTORX, "node", "int_constant", None, None])
CREATE_FLOAT_CONSTANT_NODE = AcaoSemantica(create_node, [FACTORX, "node", "float_constant", None, None])
CREATE_STRING_CONSTANT_NODE = AcaoSemantica(create_node, [FACTORX, "node", "string_constant", None, None])
CREATE_NULL_NODE = AcaoSemantica(create_node, [FACTORX, "node", "null", None, None])
SET_FACTORX_FROM_EXPRESSION_NODE = AcaoSemantica(set_var_based_on_another, [FACTORX, "node", EXPRESSION, "node"])
SET_MORENUMEXP_FIRST_NODE_BASED_ON_NUMEXPRESSION = AcaoSemantica(set_var_based_on_another, [MORENUMEXP, "first_node", NUMEXPRESSION, "node"])
SET_EXPRESSION_FROM_MORENUMEXP_NODE = AcaoSemantica(set_var_based_on_another, [EXPRESSION, "node", MORENUMEXP, "final_node"])
CREATE_LVALUE_IDENT_NODE = AcaoSemantica(create_node, [LVALUE, "node", "ident", None, None])
SET_FACTOR_FROM_FACTORX_NODE = AcaoSemantica(set_var_based_on_another, [FACTOR, "node", FACTORX, "node"])
SET_FACTOR_FROM_LVALUE_NODE = AcaoSemantica(set_var_based_on_another, [FACTOR, "node", LVALUE, "node"])
SET_MOREFACTOR_SIGN_FROM_SIGN = AcaoSemantica(set_var_based_on_another, [MOREFACTOR, "sign", SIGN, "sign"])
SET_NO_MOREFACTOR_SIGN = AcaoSemantica(set_var, [MOREFACTOR, "sign", "+"])
CREATE_UNARYEXPR_NODE = AcaoSemantica(create_term_node, [UNARYEXPR, "node", MOREFACTOR, "sign", FACTOR, "node", None])
SET_MULTIPLICATION_OPERATION = AcaoSemantica(set_var, [HOPERATOR, "operation", "*"])
SET_DIVISION_OPERATION = AcaoSemantica(set_var, [HOPERATOR, "operation", "/"])
SET_MODULUS_OPERATION = AcaoSemantica(set_var, [HOPERATOR, "operation", "%"])
SET_PLUS_SIGN = AcaoSemantica(set_var, [SIGN, "sign", "+"])
SET_MINUS_SIGN = AcaoSemantica(set_var, [SIGN, "sign", "-"])
SET_ADDUNARY_FINAL_NODE = AcaoSemantica(set_var_based_on_existing, [ADDUNARY, "final_node", "first_node"])
CREATE_ADDUNARY_NODE = AcaoSemantica(create_operation_node, [ADDUNARY, "first_node", HOPERATOR, "operation", ADDUNARY, "first_node", UNARYEXPR, "node"])
SET_ADDUNARY_FIRST_NODE_BASED_ON_UNARY_EXPR = AcaoSemantica(set_var_based_on_another, [ADDUNARY, "first_node", UNARYEXPR, "node"])
SET_TERM_NODE_BASED_ON_ADDUNARY = AcaoSemantica(set_var_based_on_another, [TERM, "node", ADDUNARY, "final_node"])
SET_ADDTERM_FINAL_NODE = AcaoSemantica(set_var_based_on_existing, [ADDTERM, "final_node", "first_node"])
CREATE_ADDTERM_NODE = AcaoSemantica(create_operation_node, [ADDTERM, "first_node", SIGN, "sign", ADDTERM, "first_node", TERM, "node"])
SET_ADDTERM_FIRST_NODE_BASED_ON_TERM = AcaoSemantica(set_var_based_on_another, [ADDTERM, "first_node", TERM, "node"])
SET_NUMEXPRESSION_NODE = AcaoSemantica(set_var_based_on_another, [NUMEXPRESSION, "node", ADDTERM, "final_node"])
SET_ADDUNARY_FIRST_NODE_BASED_ON_EXPR = AcaoSemantica(set_var_based_on_another, [ADDUNARY, "first_node", EXPR, "first_node"])
SET_ADDTERM_FIRST_NODE_BASED_ON_ADDUNARY = AcaoSemantica(set_var_based_on_another, [ADDTERM, "first_node", ADDUNARY, "final_node"])
SET_COMPARATOR_GREATER_COMPARISON = AcaoSemantica(set_var, [COMPARATOR, "comparison", ">"])
SET_COMPARATOR_LESS_COMPARISON = AcaoSemantica(set_var, [COMPARATOR, "comparison", "<"])
SET_COMPARATOR_LESS_OR_EQUAL_COMPARISON = AcaoSemantica(set_var, [COMPARATOR, "comparison", "<="])
SET_COMPARATOR_GREATER_OR_EQUAL_COMPARISON = AcaoSemantica(set_var, [COMPARATOR, "comparison", ">="])
SET_COMPARATOR_EQUAL_COMPARISON = AcaoSemantica(set_var, [COMPARATOR, "comparison", "=="])
SET_COMPARATOR_DIFFERENT_COMPARISON = AcaoSemantica(set_var, [COMPARATOR, "comparison", "!="])
SET_MORENUMEXP_FINAL_NODE = AcaoSemantica(set_var_based_on_existing, [MORENUMEXP, "final_node", "first_node"])
CREATE_MORENUMEXP_FINAL_NODE = AcaoSemantica(create_operation_node, [MORENUMEXP, "final_node", COMPARATOR, "comparison", MORENUMEXP, "first_node", NUMEXPRESSION, "node"])
SET_MORENUMEXP_FIRST_NODE_BASED_ON_ADDTERM = AcaoSemantica(set_var_based_on_another, [MORENUMEXP, "first_node", ADDTERM, "final_node"])
SET_EXPR_FINAL_NODE = AcaoSemantica(set_var_based_on_another, [EXPR, "final_node", MORENUMEXP, "final_node"])
CREATE_EXPR_FACTORX_NODE = AcaoSemantica(create_expr_node, [EXPR, "first_node", "+", FACTORX, "node", None])
SET_RESULT_NODE = AcaoSemantica(set_var_based_on_another, [RESULT, "final_node", EXPR, "final_node"])
CREATE_RESULTX_IDENT_NODE = AcaoSemantica(create_node, [RESULTX, "first_node", "ident", None, None])
CREATE_EXPR_RESULTX_NODE = AcaoSemantica(create_expr_node, [EXPR, "first_node", "+", RESULTX, "first_node", None])
SET_RESULTX_FINAL_NODE = AcaoSemantica(set_var_based_on_another, [RESULTX, "final_node", EXPR, "final_node"])
SET_RESULT_FROM_RESULTX_FINAL_NODE = AcaoSemantica(set_var_based_on_another, [RESULT, "final_node", RESULTX, "final_node"])
CREATE_EXPR_FACTOR_NODE = AcaoSemantica(create_term_node, [EXPR, "first_node", SIGN, "sign", FACTOR, "node", None])

# Inserção de tipos na tabela de símbolos
INSERT_VARIABLE_TYPE_INTO_TABLE_WITH_INDEX = AcaoSemantica(insert_type_into_table_with_index, [IDENT, "lexemes", "type", TYPE, "type", INDEX, "depth"])
INSERT_VARIABLE_TYPE_INTO_TABLE_WITHOUT_INDEX = AcaoSemantica(insert_type_into_table_without_index, [IDENT, "lexemes", "type", TYPE, "type"])
SET_IDENT_LEXEME = AcaoSemantica(set_lexeme, [IDENT, "lexemes"])
RESET_IDENT_LEXEME = AcaoSemantica(reset_lexeme, [IDENT, "lexemes"])
SET_INDEX_INITIAL_DEPTH_UNTIL_NOW = AcaoSemantica(set_var, [INDEX, "depth_until_now", 0])
SET_INDEX_DEPTH_UNTIL_NOW_PLUS_ONE = AcaoSemantica(set_var_sum, [INDEX, "depth_until_now", "depth_until_now", 1])
SET_INDEX_DEPTH = AcaoSemantica(set_var_based_on_existing, [INDEX, "depth", "depth"])
SET_INDEX_DEPTH_BASED_ON_UNTIL_NOW = AcaoSemantica(set_var_based_on_existing, [INDEX, "depth", "depth_until_now"])
SET_TYPE_INT = AcaoSemantica(set_var, [TYPE, "type", "int"])
SET_TYPE_FLOAT = AcaoSemantica(set_var, [TYPE, "type", "float"])
SET_TYPE_STRING = AcaoSemantica(set_var, [TYPE, "type", "string"])

# Verificacao de identificadores por escopo
CREATE_SCOPE = AcaoSemantica(create_TS, [])
CLOSE_SCOPE = AcaoSemantica(close_TS, [])
SET_TYPE_IN_LAST_TABLE = AcaoSemantica(set_lexeme_or_throw_error, [IDENT, "lexemes"])

# Verificação de tipos
SET_NUMEXPRESSIONS_PLUS_ONE = AcaoSemantica(set_var_sum, [NUMEXPRESSIONS, "depth", "depth", 1])
SET_NUMEXPRESSIONS_ZERO = AcaoSemantica(set_var, [NUMEXPRESSIONS, "depth", 0])
SET_APPNUM_DEPTH = AcaoSemantica(set_var_based_on_another, [APPNUM, "depth", NUMEXPRESSIONS, "depth"])
SET_APPNUM_DEPTH_ZERO = AcaoSemantica(set_var, [APPNUM, "depth", 0])
SET_FACTORX_INT_TYPE = AcaoSemantica(set_var, [FACTORX, "type", "int 0"])
SET_FACTORX_FLOAT_TYPE = AcaoSemantica(set_var, [FACTORX, "type", "float 0"])
SET_FACTORX_STRING_TYPE = AcaoSemantica(set_var, [FACTORX, "type", "string 0"])
SET_FACTORX_NULL_TYPE = AcaoSemantica(set_var, [FACTORX, "type", "null"])
SET_FACTORX_EXPRESSION_TYPE = AcaoSemantica(set_var_based_on_another, [FACTORX, "type", EXPRESSION, "type"])
SET_FACTOR_TYPE_BASED_ON_FACTORX_TYPE = AcaoSemantica(set_var_based_on_another, [FACTOR, "type", FACTORX, "type"])
SET_FACTOR_TYPE_BASED_ON_LVALUE_TYPE = AcaoSemantica(set_var_based_on_another, [FACTOR, "type", LVALUE, "type"])
SET_UNARYEXPR_TYPE = AcaoSemantica(set_var_based_on_another, [UNARYEXPR, "type", FACTOR, "type"])
SET_ADDUNARY_EMPTY_TYPE = AcaoSemantica(set_var, [ADDUNARY, "type", ""])
SET_ADDUNARY_TYPE_OR_THROW_ERROR = AcaoSemantica(set_type_or_throw_error, [ADDUNARY, "type", ADDUNARY, "type", UNARYEXPR, "type"])
SET_TERM_TYPE_OR_THROW_ERROR = AcaoSemantica(set_type_or_throw_error, [TERM, "type", ADDUNARY, "type", UNARYEXPR, "type"])
SET_ADDTERM_EMPTY_TYPE = AcaoSemantica(set_var, [ADDTERM, "type", ""])
SET_ADDTERM_TYPE_OR_THROW_ERROR = AcaoSemantica(set_type_or_throw_error, [ADDTERM, "type", ADDTERM, "type", TERM, "type"])
SET_NUMEXPRESSION_TYPE_OR_THROW_ERROR = AcaoSemantica(set_type_or_throw_error, [NUMEXPRESSION, "type", ADDTERM, "type", TERM, "type"])
SET_MORENUMEXP_EMPTY_TYPE = AcaoSemantica(set_var, [MORENUMEXP, "type", ""])
SET_MORENUMEXP_BOOL_TYPE = AcaoSemantica(set_var_based_on_another, [MORENUMEXP, "type", NUMEXPRESSION, "type"])
SET_EXPR_TYPE_OR_THROW_ERROR = AcaoSemantica(set_triple_type_or_throw_error, [EXPR, "type", ADDUNARY, "type", ADDTERM, "type", MORENUMEXP, "type"])
SET_EXPRESSION_TYPE_OR_THROW_ERROR = AcaoSemantica(set_type_or_throw_error, [EXPRESSION, "type", MORENUMEXP, "type", NUMEXPRESSION, "type"])
SET_RESULTX_ZERO_DEPTH = AcaoSemantica(set_var, [RESULTX, "depth", 0])
SET_RESULTX_EMPTY_TYPE = AcaoSemantica(set_var, [RESULTX, "type", ""])
SET_RESULTX_APPNUM_DEPTH = AcaoSemantica(set_var_based_on_another, [RESULTX, "depth", APPNUM, "depth"])
SET_RESULTX_EXPR_TYPE = AcaoSemantica(set_var_based_on_another, [RESULTX, "type", EXPR, "type"])
SET_RESULT_LEXEME = AcaoSemantica(set_lexeme, [RESULT, "lexemes"])
RESET_RESULT_LEXEME = AcaoSemantica(reset_lexeme, [RESULT, "lexemes"])
SET_RESULT_FIRST_TYPE = AcaoSemantica(set_variable_type_based_on_ident, [RESULT, "first_type", RESULT, "lexemes", "type", RESULTX, "depth"])
SET_RESULT_TYPE_OR_THROW_ERROR = AcaoSemantica(set_type_or_throw_error, [RESULT, "type", RESULTX, "type", RESULT, "first_type"])
SET_RESULT_TYPE_BASED_ON_FACTOR_OR_THROW_ERROR = AcaoSemantica(set_type_or_throw_error, [RESULT, "type", EXPR, "type", FACTOR, "type"])
SET_RESULT_TYPE_BASED_ON_FACTORX_OR_THROW_ERROR = AcaoSemantica(set_type_or_throw_error, [RESULT, "type", EXPR, "type", FACTORX, "type"])
SET_LVALUE_TYPE = AcaoSemantica(set_variable_type_based_on_ident, [LVALUE, "type", IDENT, "lexemes", "type", APPNUM, "depth"])
SET_ATRIBSTAT_FIRST_TYPE = AcaoSemantica(set_var_based_on_another, [ATRIBSTAT, "first_type", LVALUE, "type"])
SET_ATRIBSTAT_TYPE_BASED_ON_FIRST_TYPE_OR_THROW_ERROR = AcaoSemantica(set_type_or_throw_error, [ATRIBSTAT, "type", RESULT, "type", ATRIBSTAT, "first_type"])

# Comandos dentro de escopos (break no escopo de for)
SET_STATEMENT_FOR_STAT_TO_TRUE = AcaoSemantica(set_var, [STATEMENT, "for_stat", True])
SET_STATEMENT_FOR_STAT_TO_FALSE = AcaoSemantica(set_var, [STATEMENT, "for_stat", False])
SET_FOR_OF_TS = AcaoSemantica(set_var_of_ts_based_on_another, ["for", STATEMENT, "for_stat"])
VERIFY_BREAK_INSIDE_FOR = AcaoSemantica(verify_ts_var_or_throw_error, ["for"])

# Geração de Código Intermediário
GCI_MATH_result = AcaoSemantica(GCI_math, [RESULT])
GCI_MATH_expression = AcaoSemantica(GCI_math, [EXPRESSION])
GCI_ATRIBSTAT = AcaoSemantica(GCI_atribstat, [ATRIBSTAT, LVALUE, RESULT])
subir_lvalue_lexeme_IDENT = AcaoSemantica(subir_lvalue_lexeme, [LVALUE, IDENT])
codigo_subir_program_statement = AcaoSemantica(subir_program, [PROGRAM, STATEMENT])
codigo_subir_program_funclist = AcaoSemantica(subir_program, [PROGRAM, FUNCLIST])
codigo_subir_funclist = AcaoSemantica(subir_funclist, [FUNCLIST, FUNCDEF, FUNCLISTX])
codigo_subir_funclistx_funclist = AcaoSemantica(subir_funclistx, [FUNCLISTX, FUNCLIST])
codigo_subir_funclistx_epsilon = AcaoSemantica(subir_funclistx, [FUNCLISTX, ''])
codigo_subir_funcdef = AcaoSemantica(subir_funcdef, [FUNCDEF, STATELIST])
codigo_subir_statelist = AcaoSemantica(subir_statelist, [STATELIST, STATEMENT, MORESTATELIST])
codigo_subir_morestatlist_state = AcaoSemantica(subir_morestatlist, [MORESTATELIST, STATELIST])
codigo_subir_morestatlist_epsilon = AcaoSemantica(subir_morestatlist, [MORESTATELIST, ''])
codigo_subir_statement_if = AcaoSemantica(subir_statement, [STATEMENT, IFSTAT])
codigo_subir_statement_for = AcaoSemantica(subir_statement, [STATEMENT, FORSTAT])
codigo_subir_statement_atrib = AcaoSemantica(subir_statement, [STATEMENT, ATRIBSTAT])
codigo_subir_morestat_statement = AcaoSemantica(subir_morestat, [MORESTAT, STATEMENT])
codigo_subir_morestat_epsilon = AcaoSemantica(subir_morestat, [MORESTAT, ''])
GCI_IF = AcaoSemantica(GCI_if, [IFSTAT, EXPRESSION, STATEMENT, MORESTAT])
GCI_FOR = AcaoSemantica(GCI_for, [FORSTAT, ATRIBSTAT, EXPRESSION, ATRIBSTAT, STATEMENT])


program_vazio = AcaoSemantica(GCI_vazio, [PROGRAM])
statement_vazio = AcaoSemantica(GCI_vazio, [STATEMENT])
codigo_subir_statement_statelist = AcaoSemantica(subir_statement_statelist, [STATEMENT, STATELIST])







AcoesSemanticas = [
    CREATE_INT_CONSTANT_NODE,
    CREATE_FLOAT_CONSTANT_NODE,
    CREATE_STRING_CONSTANT_NODE,
    CREATE_NULL_NODE,
    SET_FACTORX_FROM_EXPRESSION_NODE,
    SET_MORENUMEXP_FIRST_NODE_BASED_ON_NUMEXPRESSION,
    SET_EXPRESSION_FROM_MORENUMEXP_NODE,
    CREATE_LVALUE_IDENT_NODE,
    SET_FACTOR_FROM_FACTORX_NODE,
    SET_FACTOR_FROM_LVALUE_NODE,
    SET_MOREFACTOR_SIGN_FROM_SIGN,
    SET_NO_MOREFACTOR_SIGN,
    CREATE_UNARYEXPR_NODE,
    SET_MULTIPLICATION_OPERATION,
    SET_DIVISION_OPERATION,
    SET_MODULUS_OPERATION,
    SET_PLUS_SIGN,
    SET_MINUS_SIGN,
    SET_ADDUNARY_FINAL_NODE,
    CREATE_ADDUNARY_NODE,
    SET_ADDUNARY_FIRST_NODE_BASED_ON_UNARY_EXPR,
    SET_TERM_NODE_BASED_ON_ADDUNARY,
    SET_ADDTERM_FINAL_NODE,
    CREATE_ADDTERM_NODE,
    SET_ADDTERM_FIRST_NODE_BASED_ON_TERM,
    SET_NUMEXPRESSION_NODE,
    SET_ADDUNARY_FIRST_NODE_BASED_ON_EXPR,
    SET_ADDTERM_FIRST_NODE_BASED_ON_ADDUNARY,
    SET_COMPARATOR_GREATER_COMPARISON,
    SET_COMPARATOR_LESS_COMPARISON,
    SET_COMPARATOR_LESS_OR_EQUAL_COMPARISON,
    SET_COMPARATOR_GREATER_OR_EQUAL_COMPARISON,
    SET_COMPARATOR_EQUAL_COMPARISON,
    SET_COMPARATOR_DIFFERENT_COMPARISON,
    SET_MORENUMEXP_FINAL_NODE,
    CREATE_MORENUMEXP_FINAL_NODE,
    SET_MORENUMEXP_FIRST_NODE_BASED_ON_ADDTERM,
    SET_EXPR_FINAL_NODE,
    CREATE_EXPR_FACTORX_NODE,
    SET_RESULT_NODE,
    CREATE_RESULTX_IDENT_NODE,
    CREATE_EXPR_RESULTX_NODE,
    SET_RESULTX_FINAL_NODE,
    SET_RESULT_FROM_RESULTX_FINAL_NODE,
    CREATE_EXPR_FACTOR_NODE,
    INSERT_VARIABLE_TYPE_INTO_TABLE_WITH_INDEX,
    INSERT_VARIABLE_TYPE_INTO_TABLE_WITHOUT_INDEX,
    SET_IDENT_LEXEME,
    RESET_IDENT_LEXEME,
    SET_INDEX_INITIAL_DEPTH_UNTIL_NOW,
    SET_INDEX_DEPTH_UNTIL_NOW_PLUS_ONE,
    SET_INDEX_DEPTH,
    SET_INDEX_DEPTH_BASED_ON_UNTIL_NOW,
    SET_TYPE_INT,
    SET_TYPE_FLOAT,
    SET_TYPE_STRING,
    CREATE_SCOPE,
    CLOSE_SCOPE,
    SET_TYPE_IN_LAST_TABLE,
    SET_NUMEXPRESSIONS_PLUS_ONE,
    SET_NUMEXPRESSIONS_ZERO,
    SET_APPNUM_DEPTH,
    SET_APPNUM_DEPTH_ZERO,
    SET_FACTORX_INT_TYPE,
    SET_FACTORX_FLOAT_TYPE,
    SET_FACTORX_STRING_TYPE,
    SET_FACTORX_NULL_TYPE,
    SET_FACTORX_EXPRESSION_TYPE,
    SET_FACTOR_TYPE_BASED_ON_FACTORX_TYPE,
    SET_FACTOR_TYPE_BASED_ON_LVALUE_TYPE,
    SET_UNARYEXPR_TYPE,
    SET_ADDUNARY_EMPTY_TYPE,
    SET_ADDUNARY_TYPE_OR_THROW_ERROR,
    SET_TERM_TYPE_OR_THROW_ERROR,
    SET_ADDTERM_EMPTY_TYPE,
    SET_ADDTERM_TYPE_OR_THROW_ERROR,
    SET_NUMEXPRESSION_TYPE_OR_THROW_ERROR,
    SET_MORENUMEXP_EMPTY_TYPE,
    SET_MORENUMEXP_BOOL_TYPE,
    SET_EXPR_TYPE_OR_THROW_ERROR,
    SET_EXPRESSION_TYPE_OR_THROW_ERROR,
    SET_RESULTX_ZERO_DEPTH,
    SET_RESULTX_EMPTY_TYPE,
    SET_RESULTX_APPNUM_DEPTH,
    SET_RESULTX_EXPR_TYPE,
    SET_RESULT_LEXEME,
    RESET_RESULT_LEXEME,
    SET_RESULT_FIRST_TYPE,
    SET_RESULT_TYPE_OR_THROW_ERROR,
    SET_RESULT_TYPE_BASED_ON_FACTOR_OR_THROW_ERROR,
    SET_RESULT_TYPE_BASED_ON_FACTORX_OR_THROW_ERROR,
    SET_LVALUE_TYPE,
    SET_ATRIBSTAT_FIRST_TYPE,
    SET_ATRIBSTAT_TYPE_BASED_ON_FIRST_TYPE_OR_THROW_ERROR,
    SET_STATEMENT_FOR_STAT_TO_TRUE,
    SET_STATEMENT_FOR_STAT_TO_FALSE,
    SET_FOR_OF_TS,
    VERIFY_BREAK_INSIDE_FOR,
    # Geração de código intermediário
    GCI_MATH_result,
    GCI_MATH_expression,
    GCI_ATRIBSTAT,
    subir_lvalue_lexeme_IDENT,
    codigo_subir_program_statement,
    codigo_subir_program_funclist,
    codigo_subir_funclist,
    codigo_subir_funclistx_funclist,
    codigo_subir_funclistx_epsilon,
    codigo_subir_funcdef,
    codigo_subir_statelist,
    codigo_subir_morestatlist_state,
    codigo_subir_morestatlist_epsilon,
    codigo_subir_statement_if,
    codigo_subir_statement_for,
    codigo_subir_statement_atrib,
    codigo_subir_morestat_statement,
    codigo_subir_morestat_epsilon,
    GCI_IF,
    GCI_FOR,

    program_vazio,
    statement_vazio,
    codigo_subir_statement_statelist
 ]

Producoes = {
"PROGRAM" : [[program_vazio, SET_STATEMENT_FOR_STAT_TO_FALSE, STATEMENT, codigo_subir_program_statement], [program_vazio, FUNCLIST, codigo_subir_program_funclist], [program_vazio, EPSILON]],
"FUNCLIST" : [[FUNCDEF, FUNCLISTX, codigo_subir_funclist]],
"FUNCLIST\'" : [[FUNCLIST, codigo_subir_funclistx_funclist], [EPSILON, codigo_subir_funclistx_epsilon]],
"FUNCDEF" : [[DEF, SET_IDENT_LEXEME, IDENT, SET_TYPE_IN_LAST_TABLE, CREATE_SCOPE, OPEN_PARENTHESIS, PARAMLIST, CLOSING_PARENTHESIS, OPEN_CURLY_BRACKET, STATELIST, CLOSE_SCOPE, CLOSING_CURLY_BRACKET, RESET_IDENT_LEXEME, codigo_subir_funcdef]],
"PARAMLIST" : [[TYPE, SET_IDENT_LEXEME, IDENT, INSERT_VARIABLE_TYPE_INTO_TABLE_WITHOUT_INDEX, PARAMLISTX, RESET_IDENT_LEXEME], [EPSILON]],
"PARAMLIST\'" : [[COMMA, PARAMLIST], [EPSILON]],
"STATEMENT" : [[VARDECL, SEMICOLON, statement_vazio], [ATRIBSTAT, SEMICOLON, codigo_subir_statement_atrib], [PRINTSTAT, SEMICOLON, statement_vazio], [READSTAT, SEMICOLON, statement_vazio], [RETURNSTAT, SEMICOLON, statement_vazio], [IFSTAT, codigo_subir_statement_if], [FORSTAT, codigo_subir_statement_for], [OPEN_CURLY_BRACKET, CREATE_SCOPE, SET_FOR_OF_TS, STATELIST, CLOSE_SCOPE, CLOSING_CURLY_BRACKET, codigo_subir_statement_statelist], [BREAK, SEMICOLON, statement_vazio], [SEMICOLON, statement_vazio]],
"TYPE" : [[INT, SET_TYPE_INT], [FLOAT, SET_TYPE_FLOAT], [STRING, SET_TYPE_STRING]],
"VARDECL" : [[SET_INDEX_INITIAL_DEPTH_UNTIL_NOW, TYPE, SET_IDENT_LEXEME, IDENT, SET_TYPE_IN_LAST_TABLE, INDEX, INSERT_VARIABLE_TYPE_INTO_TABLE_WITH_INDEX, RESET_IDENT_LEXEME]],
"INDEX" : [[OPEN_SQUARE_BRACKET, INT_CONSTANT, CLOSING_SQUARE_BRACKET, SET_INDEX_DEPTH_UNTIL_NOW_PLUS_ONE, INDEX, SET_INDEX_DEPTH], [EPSILON, SET_INDEX_DEPTH_BASED_ON_UNTIL_NOW]],
"ATRIBSTAT" : [[LVALUE, SET_ATRIBSTAT_FIRST_TYPE, subir_lvalue_lexeme_IDENT, EQUALS, RESULT, GCI_MATH_result, SET_ATRIBSTAT_TYPE_BASED_ON_FIRST_TYPE_OR_THROW_ERROR, GCI_atribstat]],
"RESULT" : [[SIGN, FACTOR, CREATE_EXPR_FACTOR_NODE, EXPR, SET_RESULT_NODE, SET_RESULT_TYPE_BASED_ON_FACTOR_OR_THROW_ERROR], [FACTORX, CREATE_EXPR_FACTORX_NODE, EXPR, SET_RESULT_NODE, SET_RESULT_TYPE_BASED_ON_FACTORX_OR_THROW_ERROR], [SET_RESULT_LEXEME, IDENT, CREATE_RESULTX_IDENT_NODE, RESULTX, SET_RESULT_FIRST_TYPE, SET_RESULT_FROM_RESULTX_FINAL_NODE, SET_RESULT_TYPE_OR_THROW_ERROR, RESET_RESULT_LEXEME], [ALLOCEXPRESSION]],
"RESULT\'" : [[SET_APPNUM_DEPTH_ZERO, APPNUM, SET_RESULTX_APPNUM_DEPTH, CREATE_EXPR_RESULTX_NODE, EXPR, SET_RESULTX_FINAL_NODE, SET_RESULTX_EXPR_TYPE], [OPEN_PARENTHESIS, PARAMLISTCALL, CLOSING_PARENTHESIS, SET_RESULTX_ZERO_DEPTH, SET_RESULTX_EMPTY_TYPE]],
"EXPR" : [[SET_ADDUNARY_FIRST_NODE_BASED_ON_EXPR, ADDUNARY, SET_ADDTERM_FIRST_NODE_BASED_ON_ADDUNARY, ADDTERM, SET_MORENUMEXP_FIRST_NODE_BASED_ON_ADDTERM, MORENUMEXP, SET_EXPR_FINAL_NODE, SET_EXPR_TYPE_OR_THROW_ERROR]],
"FUNCCALL" : [[IDENT, OPEN_PARENTHESIS, PARAMLISTCALL, CLOSING_PARENTHESIS]],
"PARAMLISTCALL" : [[IDENT, PARAMLISTCALLX], [EPSILON]],
"PARAMLISTCALL\'" : [[COMMA, PARAMLISTCALL], [EPSILON]],
"PRINTSTAT" : [[PRINT, EXPRESSION]],
"READSTAT" : [[READ, LVALUE]],
"RETURNSTAT" : [[RETURN, IDENT]],
"IFSTAT" : [[IF, OPEN_PARENTHESIS, EXPRESSION, CLOSING_PARENTHESIS, SET_STATEMENT_FOR_STAT_TO_FALSE, STATEMENT, MORESTAT, ENDIF, GCI_IF]],
"MORESTAT" : [[ELSE, SET_STATEMENT_FOR_STAT_TO_FALSE, STATEMENT, codigo_subir_morestat_statement], [EPSILON, codigo_subir_morestat_epsilon]],
"FORSTAT" : [[FOR, OPEN_PARENTHESIS, ATRIBSTAT, SEMICOLON, EXPRESSION, SEMICOLON, ATRIBSTAT, CLOSING_PARENTHESIS, SET_STATEMENT_FOR_STAT_TO_TRUE, STATEMENT, GCI_FOR]],
"STATELIST" : [[SET_STATEMENT_FOR_STAT_TO_FALSE, STATEMENT, MORESTATELIST, codigo_subir_statelist]],
"MORESTATELIST" : [[STATELIST, codigo_subir_morestatlist_state], [EPSILON, codigo_subir_morestatlist_epsilon]],
"ALLOCEXPRESSION" : [[NEW, TYPE, NUMEXPRESSIONS]],
"NUMEXPRESSIONS" : [[OPEN_SQUARE_BRACKET, NUMEXPRESSION, CLOSING_SQUARE_BRACKET, NUMEXPRESSIONSX, SET_NUMEXPRESSIONS_PLUS_ONE]],
"NUMEXPRESSIONS\'" : [[NUMEXPRESSIONS], [EPSILON]],
"EXPRESSION" : [[NUMEXPRESSION, SET_MORENUMEXP_FIRST_NODE_BASED_ON_NUMEXPRESSION, MORENUMEXP, SET_EXPRESSION_FROM_MORENUMEXP_NODE, SET_EXPRESSION_TYPE_OR_THROW_ERROR, GCI_MATH_expression]],
"MORENUMEXP" : [[COMPARATOR, NUMEXPRESSION, CREATE_MORENUMEXP_FINAL_NODE, SET_MORENUMEXP_BOOL_TYPE], [EPSILON, SET_MORENUMEXP_FINAL_NODE, SET_MORENUMEXP_EMPTY_TYPE]],
"COMPARATOR" : [[GREATER, SET_COMPARATOR_GREATER_COMPARISON], [LESS, SET_COMPARATOR_LESS_COMPARISON], [LESS_EQUAL, SET_COMPARATOR_LESS_OR_EQUAL_COMPARISON], [GREATER_EQUAL, SET_COMPARATOR_GREATER_OR_EQUAL_COMPARISON], [EQUAL, SET_COMPARATOR_EQUAL_COMPARISON], [DIFFERENT, SET_COMPARATOR_DIFFERENT_COMPARISON]],
"NUMEXPRESSION" : [[TERM, SET_ADDTERM_FIRST_NODE_BASED_ON_TERM, ADDTERM, SET_NUMEXPRESSION_NODE, SET_NUMEXPRESSION_TYPE_OR_THROW_ERROR]],
"ADDTERM" : [[SIGN, TERM, CREATE_ADDTERM_NODE, ADDTERM, SET_ADDTERM_TYPE_OR_THROW_ERROR], [EPSILON, SET_ADDTERM_FINAL_NODE, SET_ADDTERM_EMPTY_TYPE]],
"SIGN": [[PLUS, SET_PLUS_SIGN], [MINUS, SET_MINUS_SIGN]],
"TERM" : [[UNARYEXPR, SET_ADDUNARY_FIRST_NODE_BASED_ON_UNARY_EXPR, ADDUNARY, SET_TERM_NODE_BASED_ON_ADDUNARY, SET_TERM_TYPE_OR_THROW_ERROR]],
"ADDUNARY" : [[HOPERATOR, UNARYEXPR, CREATE_ADDUNARY_NODE, ADDUNARY, SET_ADDUNARY_TYPE_OR_THROW_ERROR], [EPSILON, SET_ADDUNARY_FINAL_NODE, SET_ADDUNARY_EMPTY_TYPE]],
"HOPERATOR": [[MULTIPLICATION, SET_MULTIPLICATION_OPERATION], [DIVISION, SET_DIVISION_OPERATION], [MODULUS, SET_MODULUS_OPERATION]],
"UNARYEXPR" : [[MOREFACTOR, FACTOR, CREATE_UNARYEXPR_NODE, SET_UNARYEXPR_TYPE]],
"MOREFACTOR": [[SIGN, SET_MOREFACTOR_SIGN_FROM_SIGN], [EPSILON, SET_NO_MOREFACTOR_SIGN]],
"FACTOR" : [[FACTORX, SET_FACTOR_FROM_FACTORX_NODE, SET_FACTOR_TYPE_BASED_ON_FACTORX_TYPE], [LVALUE, SET_FACTOR_FROM_LVALUE_NODE, SET_FACTOR_TYPE_BASED_ON_LVALUE_TYPE]],
"FACTOR\'" : [[INT_CONSTANT, CREATE_INT_CONSTANT_NODE, SET_FACTORX_INT_TYPE], [FLOAT_CONSTANT, CREATE_FLOAT_CONSTANT_NODE, SET_FACTORX_FLOAT_TYPE], [STRING_CONSTANT, CREATE_STRING_CONSTANT_NODE, SET_FACTORX_STRING_TYPE], [NULL, CREATE_NULL_NODE, SET_FACTORX_NULL_TYPE], [OPEN_PARENTHESIS, EXPRESSION, CLOSING_PARENTHESIS, SET_FACTORX_FROM_EXPRESSION_NODE, SET_FACTORX_EXPRESSION_TYPE]],
"LVALUE" : [[SET_IDENT_LEXEME, IDENT, subir_lvalue_lexeme_IDENT, SET_APPNUM_DEPTH_ZERO, APPNUM, CREATE_LVALUE_IDENT_NODE, SET_LVALUE_TYPE, RESET_IDENT_LEXEME]],
"APPNUM": [[SET_NUMEXPRESSIONS_ZERO, NUMEXPRESSIONS, SET_APPNUM_DEPTH], [EPSILON]],
}

NTs = [ PROGRAM, FUNCLIST, FUNCLISTX, FUNCDEF, PARAMLIST, PARAMLISTX, STATEMENT, TYPE, VARDECL, INDEX, ATRIBSTAT, RESULT, RESULTX, EXPR, FUNCCALL, PARAMLISTCALL, PARAMLISTCALLX, PRINTSTAT, READSTAT, RETURNSTAT, IFSTAT, MORESTAT, FORSTAT, STATELIST, MORESTATELIST, ALLOCEXPRESSION, NUMEXPRESSIONS, NUMEXPRESSIONSX, EXPRESSION, MORENUMEXP, COMPARATOR, NUMEXPRESSION, ADDTERM, SIGN, TERM, ADDUNARY, HOPERATOR, UNARYEXPR, MOREFACTOR, FACTOR, FACTORX, LVALUE, APPNUM]
Terminais = [EPSILON, DEF, IDENT, OPEN_PARENTHESIS, CLOSING_PARENTHESIS, OPEN_CURLY_BRACKET, CLOSING_CURLY_BRACKET, OPEN_SQUARE_BRACKET, CLOSING_SQUARE_BRACKET, COMMA, SEMICOLON, BREAK, INT, FLOAT, STRING, INT_CONSTANT, EQUALS, PRINT, READ, RETURN, ELSE, FOR, NEW, GREATER, LESS, LESS_EQUAL, GREATER_EQUAL, EQUAL, DIFFERENT, PLUS, MINUS, MULTIPLICATION, DIVISION, MODULUS, INT_CONSTANT, FLOAT_CONSTANT, STRING_CONSTANT, NULL]
LL1Action = [
    [program_vazio, SET_STATEMENT_FOR_STAT_TO_FALSE, STATEMENT, codigo_subir_program_statement],
    [program_vazio, FUNCLIST, codigo_subir_program_funclist],
    [program_vazio, EPSILON],
    [FUNCDEF, FUNCLISTX, codigo_subir_funclist],
    [FUNCLIST, codigo_subir_funclistx_funclist],
    [EPSILON, codigo_subir_funclistx_epsilon],
    [DEF, SET_IDENT_LEXEME, IDENT, SET_TYPE_IN_LAST_TABLE, CREATE_SCOPE, OPEN_PARENTHESIS, PARAMLIST, CLOSING_PARENTHESIS, OPEN_CURLY_BRACKET, STATELIST, CLOSE_SCOPE, CLOSING_CURLY_BRACKET, RESET_IDENT_LEXEME, codigo_subir_funcdef],
    [TYPE, SET_IDENT_LEXEME, IDENT, SET_TYPE_IN_LAST_TABLE, INSERT_VARIABLE_TYPE_INTO_TABLE_WITHOUT_INDEX, PARAMLISTX, RESET_IDENT_LEXEME],
    [EPSILON],
    [COMMA, PARAMLIST],
    [EPSILON],
    [VARDECL, SEMICOLON, statement_vazio],
    [ATRIBSTAT, SEMICOLON, codigo_subir_statement_atrib],
    [PRINTSTAT, SEMICOLON, statement_vazio],
    [READSTAT, SEMICOLON, statement_vazio],
    [RETURNSTAT, SEMICOLON, statement_vazio],
    [IFSTAT, codigo_subir_statement_if],
    [FORSTAT, codigo_subir_statement_for],
    [OPEN_CURLY_BRACKET, CREATE_SCOPE, SET_FOR_OF_TS, STATELIST, CLOSE_SCOPE, CLOSING_CURLY_BRACKET, codigo_subir_statement_statelist],
    [BREAK, VERIFY_BREAK_INSIDE_FOR, SEMICOLON, statement_vazio],
    [SEMICOLON, statement_vazio],
    [INT, SET_TYPE_INT],
    [FLOAT, SET_TYPE_FLOAT],
    [STRING, SET_TYPE_STRING],
    [SET_INDEX_INITIAL_DEPTH_UNTIL_NOW, TYPE, SET_IDENT_LEXEME, IDENT, SET_TYPE_IN_LAST_TABLE, INDEX, INSERT_VARIABLE_TYPE_INTO_TABLE_WITH_INDEX, RESET_IDENT_LEXEME],
    [OPEN_SQUARE_BRACKET, INT_CONSTANT, CLOSING_SQUARE_BRACKET, SET_INDEX_DEPTH_UNTIL_NOW_PLUS_ONE, INDEX, SET_INDEX_DEPTH],
    [EPSILON, SET_INDEX_DEPTH_BASED_ON_UNTIL_NOW],
    [LVALUE, SET_ATRIBSTAT_FIRST_TYPE, subir_lvalue_lexeme_IDENT, EQUALS, RESULT, GCI_MATH_result, SET_ATRIBSTAT_TYPE_BASED_ON_FIRST_TYPE_OR_THROW_ERROR, GCI_ATRIBSTAT],
    [SIGN, FACTOR, CREATE_EXPR_FACTOR_NODE, EXPR, SET_RESULT_NODE, SET_RESULT_TYPE_BASED_ON_FACTOR_OR_THROW_ERROR],
    [FACTORX, CREATE_EXPR_FACTORX_NODE, EXPR, SET_RESULT_NODE, SET_RESULT_TYPE_BASED_ON_FACTORX_OR_THROW_ERROR],
    [SET_RESULT_LEXEME, IDENT, CREATE_RESULTX_IDENT_NODE, RESULTX, SET_RESULT_FROM_RESULTX_FINAL_NODE, SET_RESULT_FIRST_TYPE, SET_RESULT_TYPE_OR_THROW_ERROR, RESET_RESULT_LEXEME],
    [ALLOCEXPRESSION],
    [SET_APPNUM_DEPTH_ZERO, APPNUM, SET_RESULTX_APPNUM_DEPTH, CREATE_EXPR_RESULTX_NODE, EXPR, SET_RESULTX_FINAL_NODE, SET_RESULTX_EXPR_TYPE],
    [OPEN_PARENTHESIS, PARAMLISTCALL, CLOSING_PARENTHESIS, SET_RESULTX_ZERO_DEPTH, SET_RESULTX_EMPTY_TYPE],
    [SET_ADDUNARY_FIRST_NODE_BASED_ON_EXPR, ADDUNARY, SET_ADDTERM_FIRST_NODE_BASED_ON_ADDUNARY, ADDTERM, SET_MORENUMEXP_FIRST_NODE_BASED_ON_ADDTERM, MORENUMEXP, SET_EXPR_FINAL_NODE, SET_EXPR_TYPE_OR_THROW_ERROR],
    [IDENT, OPEN_PARENTHESIS, PARAMLISTCALL, CLOSING_PARENTHESIS],
    [IDENT, PARAMLISTCALLX],
    [EPSILON],
    [COMMA, PARAMLISTCALL],
    [EPSILON],
    [PRINT, EXPRESSION],
    [READ, LVALUE],
    [RETURN, IDENT],
    [IF, OPEN_PARENTHESIS, EXPRESSION, CLOSING_PARENTHESIS, SET_STATEMENT_FOR_STAT_TO_FALSE, STATEMENT, MORESTAT, ENDIF, GCI_IF],
    [ELSE, SET_STATEMENT_FOR_STAT_TO_FALSE, STATEMENT, codigo_subir_morestat_statement],
    [EPSILON, codigo_subir_morestat_epsilon],
    [FOR, OPEN_PARENTHESIS, ATRIBSTAT, SEMICOLON, EXPRESSION, SEMICOLON, ATRIBSTAT, CLOSING_PARENTHESIS, SET_STATEMENT_FOR_STAT_TO_TRUE, STATEMENT, GCI_FOR],
    [SET_STATEMENT_FOR_STAT_TO_FALSE, STATEMENT, MORESTATELIST, codigo_subir_statelist],
    [STATELIST, codigo_subir_morestatlist_state],
    [EPSILON, codigo_subir_morestatlist_epsilon],
    [NEW, TYPE, NUMEXPRESSIONS],
    [OPEN_SQUARE_BRACKET, NUMEXPRESSION, CLOSING_SQUARE_BRACKET, NUMEXPRESSIONSX, SET_NUMEXPRESSIONS_PLUS_ONE],
    [NUMEXPRESSIONS],
    [EPSILON],
    [NUMEXPRESSION, SET_MORENUMEXP_FIRST_NODE_BASED_ON_NUMEXPRESSION, MORENUMEXP, SET_EXPRESSION_FROM_MORENUMEXP_NODE, SET_EXPRESSION_TYPE_OR_THROW_ERROR, GCI_MATH_expression],
    [COMPARATOR, NUMEXPRESSION, CREATE_MORENUMEXP_FINAL_NODE, SET_MORENUMEXP_BOOL_TYPE],
    [EPSILON, SET_MORENUMEXP_FINAL_NODE, SET_MORENUMEXP_EMPTY_TYPE],
    [GREATER, SET_COMPARATOR_GREATER_COMPARISON],
    [LESS, SET_COMPARATOR_LESS_COMPARISON],
    [LESS_EQUAL, SET_COMPARATOR_LESS_OR_EQUAL_COMPARISON],
    [GREATER_EQUAL, SET_COMPARATOR_GREATER_OR_EQUAL_COMPARISON],
    [EQUAL, SET_COMPARATOR_EQUAL_COMPARISON],
    [DIFFERENT, SET_COMPARATOR_DIFFERENT_COMPARISON],
    [TERM, SET_ADDTERM_FIRST_NODE_BASED_ON_TERM, ADDTERM, SET_NUMEXPRESSION_NODE, SET_NUMEXPRESSION_TYPE_OR_THROW_ERROR],
    [SIGN, TERM, CREATE_ADDTERM_NODE, ADDTERM, SET_ADDTERM_TYPE_OR_THROW_ERROR],
    [EPSILON, SET_ADDTERM_FINAL_NODE, SET_ADDTERM_EMPTY_TYPE],
    [PLUS, SET_PLUS_SIGN],
    [MINUS, SET_MINUS_SIGN],
    [UNARYEXPR, SET_ADDUNARY_FIRST_NODE_BASED_ON_UNARY_EXPR, ADDUNARY, SET_TERM_NODE_BASED_ON_ADDUNARY, SET_TERM_TYPE_OR_THROW_ERROR],
    [HOPERATOR, UNARYEXPR, CREATE_ADDUNARY_NODE, ADDUNARY, SET_ADDUNARY_TYPE_OR_THROW_ERROR],
    [EPSILON, SET_ADDUNARY_FINAL_NODE, SET_ADDUNARY_EMPTY_TYPE],
    [MULTIPLICATION, SET_MULTIPLICATION_OPERATION],
    [DIVISION, SET_DIVISION_OPERATION],
    [MODULUS, SET_MODULUS_OPERATION],
    [MOREFACTOR, FACTOR, CREATE_UNARYEXPR_NODE, SET_UNARYEXPR_TYPE],
    [SIGN, SET_MOREFACTOR_SIGN_FROM_SIGN],
    [EPSILON, SET_NO_MOREFACTOR_SIGN],
    [FACTORX, SET_FACTOR_FROM_FACTORX_NODE, SET_FACTOR_TYPE_BASED_ON_FACTORX_TYPE],
    [LVALUE, SET_FACTOR_FROM_LVALUE_NODE, SET_FACTOR_TYPE_BASED_ON_LVALUE_TYPE],
    [INT_CONSTANT, CREATE_INT_CONSTANT_NODE, SET_FACTORX_INT_TYPE],
    [FLOAT_CONSTANT, CREATE_FLOAT_CONSTANT_NODE, SET_FACTORX_FLOAT_TYPE],
    [STRING_CONSTANT, CREATE_STRING_CONSTANT_NODE, SET_FACTORX_STRING_TYPE],
    [NULL, CREATE_NULL_NODE, SET_FACTORX_NULL_TYPE],
    [OPEN_PARENTHESIS, EXPRESSION, CLOSING_PARENTHESIS, SET_FACTORX_FROM_EXPRESSION_NODE, SET_FACTORX_EXPRESSION_TYPE],
    [SET_IDENT_LEXEME, IDENT, subir_lvalue_lexeme_IDENT, SET_APPNUM_DEPTH_ZERO, APPNUM, CREATE_LVALUE_IDENT_NODE, SET_LVALUE_TYPE, RESET_IDENT_LEXEME],
    [SET_NUMEXPRESSIONS_ZERO, NUMEXPRESSIONS, SET_APPNUM_DEPTH],
    [EPSILON]
]

LL1Predict = {
    "PROGRAM" : {
        '{': 0, 
        'break': 0, 
        ';': 0, 
        'int': 0, 
        'float': 0,
        'string': 0,
        'print': 0,
        'return': 0,
        'for': 0,
        'ident': 0,
        'if': 0,
        'read': 0,
        'def': 1,
        '$': 2
    },
    "FUNCLIST" : {
        'def': 3,
    },
    "FUNCLIST\'" : {
        'def': 4,
        '$': 5
    },
    "FUNCDEF" : {
        'def': 6
    },
    "PARAMLIST" : {
        'int': 7,
        'float': 7,
        'string': 7,
        ')': 8
    },
    "PARAMLIST\'" : {
        ',': 9,
        ')': 10
    },
    "STATEMENT" : {
        'int': 11,
        'float': 11,
        'string': 11,
        'ident': 12,
        'print': 13,
        'read': 14,
        'return': 15,
        'if': 16,
        'for': 17,
        'break': 19,
        '{': 18,
        ';': 20
    },
    "TYPE" : {
        'int': 21,
        'float': 22,
        'string': 23
    },
    "VARDECL" : {
        'int': 24,
        'float': 24,
        'string': 24
    },
    "INDEX" : {
        '[': 25,
        ';': 26
    },
    "ATRIBSTAT" : {
        'ident': 27
    },
    "RESULT" : {
        '+': 28,
        '-': 28,
        'int_constant': 29,
        'float_constant': 29,
        'string_constant': 29,
        'null': 29,
        '(': 29,
        'ident': 30,
        'new': 31
    },
    "RESULT\'" : {
        '[': 32,
        '*': 32,
        '/': 32,
        '%': 32,
        '>': 32,
        '<': 32,
        '<=': 32,
        '>=': 32,
        '==': 32,
        '!=': 32,
        '+': 32,
        '-': 32,
        '(': 33,
        ';': 32,
        ')': 32
    },
    "EXPR" : {
        '*': 34,
        '/': 34,
        '%': 34,
        '>': 34,
        '<': 34,
        '<=': 34,
        '>=': 34,
        '==': 34,
        '!=': 34,
        '+': 34,
        '-': 34,
        ';': 34,
        ')': 34,
    },
    "FUNCALL" : {
        'ident': 35
    },
    "PARAMLISTCALL" : {
        'ident': 36,
        ')': 37
    },
    "PARAMLISTCALL\'" : {
        ',': 38,
        ')': 39
    },
    "PRINTSTAT" : {
        'print': 40
    },
    "READSTAT" : {
        'read': 41
    },
    "RETURNSTAT" : {
        'return': 42
    },
    "IFSTAT" : {
        'if': 43
    },
    "MORESTAT" : {
        'else': 44,
        'endif': 45
    },
    "FORSTAT" : {
        'for': 46
    },
    "STATELIST" : {
        '{': 47,
        'break': 47,
        ';': 47,
        'int': 47,
        'float': 47,
        'string': 47,
        'print': 47,
        'return': 47,
        'for': 47,
        'ident': 47,
        'if': 47,
        'read': 47
    },
    "MORESTATELIST" : {
        '{': 48,
        'break': 48,
        ';': 48,
        'int': 48,
        'float': 48,
        'string': 48,
        'print': 48,
        'return': 48,
        'for': 48,
        'ident': 48,
        'if': 48,
        'read': 48,
        '}': 49
    },
    "ALLOCEXPRESSION" : {
        'new': 50
    },
    "NUMEXPRESSIONS" : {
        '[': 51
    },
    "NUMEXPRESSIONS\'" : {
        '[': 52,
        '*': 53,
        '/': 53,
        '%': 53,
        '>': 53,
        '<': 53,
        '<=': 53,
        '>=': 53,
        '==': 53,
        '!=': 53,
        '+': 53,
        '-': 53,
        ';': 53,
        ')': 53,
        '=': 53,
        ']': 53
    },
    "EXPRESSION" : {
        '+': 54,
        '-': 54,
        'int_constant': 54,
        'float_constant': 54,
        'string_constant': 54,
        'null': 54,
        '(': 54,
        'ident': 54,
    },
    "MORENUMEXP" : {
        '>': 55,
        '<': 55,
        '<=': 55,
        '>=': 55,
        '==': 55,
        '!=': 55,
        ')': 56,
        ';': 56
    },
    "COMPARATOR" : {
        '>': 57,
        '<': 58,
        '<=': 59,
        '>=': 60,
        '==': 61,
        '!=': 62,
    },
    "NUMEXPRESSION" : {
        '+': 63,
        '-': 63,
        'int_constant': 63,
        'float_constant': 63,
        'string_constant': 63,
        'null': 63,
        '(': 63,
        'ident': 63
    },
    "ADDTERM" : {
        '+': 64,
        '-': 64,
        '>': 65,
        '<': 65,
        '<=': 65,
        '>=': 65,
        '==': 65,
        '!=': 65,
        ']': 65,
        ')': 65,
        ';': 65
    },
    "SIGN" : {
        '+': 66,
        '-': 67
    },
    "TERM" : {
        '+': 68,
        '-': 68,
        'int_constant': 68,
        'float_constant': 68,
        'string_constant': 68,
        'null': 68,
        '(': 68,
        'ident': 68
    },
    "ADDUNARY" : {
        '*': 69,
        '/': 69,
        '%': 69,
        '>': 70,
        '<': 70,
        '<=': 70,
        '>=': 70,
        '==': 70,
        '!=': 70,
        '+': 70,
        '-': 70,
        ']': 70,
        ')': 70,
        ';': 70
    },
    "HOPERATOR" : {
        '*': 71,
        '/': 72,
        '%': 73
    },
    "UNARYEXPR" : {
        '+': 74,
        '-': 74,
        'int_constant': 74,
        'float_constant': 74,
        'string_constant': 74,
        'null': 74,
        '(': 74,
        'ident': 74
    },
    "MOREFACTOR" : {
        '+': 75,
        '-': 75,
        'int_constant': 76,
        'float_constant': 76,
        'string_constant': 76,
        'null': 76,
        '(': 76,
        'ident': 76
    },
    "FACTOR" : {
        'int_constant': 77,
        'float_constant': 77,
        'string_constant': 77,
        'null': 77,
        '(': 77,
        'ident': 78
    },
    "FACTOR\'" : {
        'int_constant': 79,
        'float_constant': 80,
        'string_constant': 81,
        'null': 82,
        '(': 83,
    },
    "LVALUE" : {
        'ident': 84
    },
    "APPNUM" : {
        '[': 85,
        '*': 86,
        '/': 86,
        '%': 86,
        '>': 86,
        '<': 86,
        '<=': 86,
        '>=': 86,
        '==': 86,
        '!=': 86,
        '+': 86,
        '-': 86,
        '=': 86,
        ']': 86,
        ')': 86,
        ';': 86
    }
}

