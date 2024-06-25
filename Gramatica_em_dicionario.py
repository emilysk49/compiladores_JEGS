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
CREATE_EXPR_FACTOR_NODE = AcaoSemantica(create_term_node, [EXPR, "first_node", SIGN, "sign", FACTOR, "node", None])

# Inserção de tipos na tabela de símbolos
INSERT_VARIABLE_TYPE_INTO_TABLE_WITH_INDEX = AcaoSemantica(insert_type_into_table_with_index, [IDENT, "lexeme", "type", TYPE, "type", INDEX, "depth"])
INSERT_VARIABLE_TYPE_INTO_TABLE_WITHOUT_INDEX = AcaoSemantica(insert_type_into_table_without_index, [IDENT, "lexeme", "type", TYPE, "type"])
SET_IDENT_LEXEME = AcaoSemantica(set_lexeme, [IDENT, "lexeme"])
SET_INDEX_INITIAL_DEPTH_UNTIL_NOW = AcaoSemantica(set_var, [INDEX, "depth_until_now", 0])
SET_INDEX_DEPTH_UNTIL_NOW_PLUS_ONE = AcaoSemantica(set_var_sum, [INDEX, "depth_until_now", "depth_until_now", 1])
SET_INDEX_DEPTH = AcaoSemantica(set_var_based_on_existing, [INDEX, "depth", "depth"])
SET_INDEX_DEPTH_BASED_ON_UNTIL_NOW = AcaoSemantica(set_var_based_on_existing, [INDEX, "depth", "depth_until_now"])
SET_TYPE_INT = AcaoSemantica(set_var, [TYPE, "type", "int"])
SET_TYPE_FLOAT = AcaoSemantica(set_var, [TYPE, "type", "float"])
SET_TYPE_STRING = AcaoSemantica(set_var, [TYPE, "type", "string"])

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
    CREATE_EXPR_FACTOR_NODE,
    INSERT_VARIABLE_TYPE_INTO_TABLE_WITH_INDEX,
    INSERT_VARIABLE_TYPE_INTO_TABLE_WITHOUT_INDEX,
    SET_IDENT_LEXEME,
    SET_INDEX_INITIAL_DEPTH_UNTIL_NOW,
    SET_INDEX_DEPTH_UNTIL_NOW_PLUS_ONE,
    SET_INDEX_DEPTH,
    SET_INDEX_DEPTH_BASED_ON_UNTIL_NOW,
    SET_TYPE_INT,
    SET_TYPE_FLOAT,
    SET_TYPE_STRING
 ]

Producoes = {
"PROGRAM" : [[STATEMENT], [FUNCLIST], [EPSILON]],
"FUNCLIST" : [[FUNCDEF, FUNCLISTX]],
"FUNCLIST\'" : [[FUNCLIST], [EPSILON]],
"FUNCDEF" : [[DEF, IDENT, OPEN_PARENTHESIS, PARAMLIST, CLOSING_PARENTHESIS, OPEN_CURLY_BRACKET, STATELIST, CLOSING_CURLY_BRACKET]],
"PARAMLIST" : [[TYPE, SET_IDENT_LEXEME, IDENT, INSERT_VARIABLE_TYPE_INTO_TABLE_WITHOUT_INDEX, PARAMLISTX], [EPSILON]],
"PARAMLIST\'" : [[COMMA, PARAMLIST], [EPSILON]],
"STATEMENT" : [[VARDECL, SEMICOLON], [ATRIBSTAT, SEMICOLON], [PRINTSTAT, SEMICOLON], [READSTAT, SEMICOLON], [RETURNSTAT, SEMICOLON], [IFSTAT], [FORSTAT], [OPEN_CURLY_BRACKET, STATELIST, CLOSING_CURLY_BRACKET], [BREAK, SEMICOLON], [SEMICOLON]],
"TYPE" : [[INT, SET_TYPE_INT], [FLOAT, SET_TYPE_FLOAT], [STRING, SET_TYPE_STRING]],
"VARDECL" : [[SET_INDEX_INITIAL_DEPTH_UNTIL_NOW, TYPE, SET_IDENT_LEXEME, IDENT, INDEX, INSERT_VARIABLE_TYPE_INTO_TABLE_WITH_INDEX]],
"INDEX" : [[OPEN_SQUARE_BRACKET, INT_CONSTANT, CLOSING_SQUARE_BRACKET, SET_INDEX_DEPTH_UNTIL_NOW_PLUS_ONE, INDEX, SET_INDEX_DEPTH], [EPSILON, SET_INDEX_DEPTH_BASED_ON_UNTIL_NOW]],
"ATRIBSTAT" : [[LVALUE, EQUALS, RESULT]],
"RESULT" : [[SIGN, FACTOR, CREATE_EXPR_FACTOR_NODE, EXPR, SET_RESULT_NODE], [FACTORX, CREATE_EXPR_FACTORX_NODE, EXPR, SET_RESULT_NODE], [IDENT, RESULTX], [ALLOCEXPRESSION]],
"RESULT\'" : [[APPNUM, EXPR], [OPEN_PARENTHESIS, PARAMLISTCALL, CLOSING_PARENTHESIS]],
"EXPR" : [[SET_ADDUNARY_FIRST_NODE_BASED_ON_EXPR, ADDUNARY, SET_ADDTERM_FIRST_NODE_BASED_ON_ADDUNARY, ADDTERM, SET_MORENUMEXP_FIRST_NODE_BASED_ON_ADDTERM, MORENUMEXP, SET_EXPR_FINAL_NODE]],
"FUNCCALL" : [[IDENT, OPEN_PARENTHESIS, PARAMLISTCALL, CLOSING_PARENTHESIS]],
"PARAMLISTCALL" : [[IDENT, PARAMLISTCALLX], [EPSILON]],
"PARAMLISTCALL\'" : [[COMMA, PARAMLISTCALL], [EPSILON]],
"PRINTSTAT" : [[PRINT, EXPRESSION]],
"READSTAT" : [[READ, LVALUE]],
"RETURNSTAT" : [[RETURN, IDENT]],
"IFSTAT" : [[IF, OPEN_PARENTHESIS, EXPRESSION, CLOSING_PARENTHESIS,  STATEMENT, MORESTAT, ENDIF]],
"MORESTAT" : [[ELSE, STATEMENT], [EPSILON]],
"FORSTAT" : [[FOR, OPEN_PARENTHESIS, ATRIBSTAT, EXPRESSION, SEMICOLON, SEMICOLON, ATRIBSTAT, CLOSING_PARENTHESIS, STATEMENT]],
"STATELIST" : [[STATEMENT, MORESTATELIST]],
"MORESTATELIST" : [[STATELIST], [EPSILON]],
"ALLOCEXPRESSION" : [[NEW, TYPE, NUMEXPRESSIONS]],
"NUMEXPRESSIONS" : [[OPEN_SQUARE_BRACKET, NUMEXPRESSION, CLOSING_SQUARE_BRACKET, NUMEXPRESSIONSX]],
"NUMEXPRESSIONS\'" : [[NUMEXPRESSIONS], [EPSILON]],
"EXPRESSION" : [[NUMEXPRESSION, SET_MORENUMEXP_FIRST_NODE_BASED_ON_NUMEXPRESSION, MORENUMEXP, SET_EXPRESSION_FROM_MORENUMEXP_NODE]],
"MORENUMEXP" : [[COMPARATOR, NUMEXPRESSION, CREATE_MORENUMEXP_FINAL_NODE], [EPSILON, SET_MORENUMEXP_FINAL_NODE]],
"COMPARATOR" : [[GREATER, SET_COMPARATOR_GREATER_COMPARISON], [LESS, SET_COMPARATOR_LESS_COMPARISON], [LESS_EQUAL, SET_COMPARATOR_LESS_OR_EQUAL_COMPARISON], [GREATER_EQUAL, SET_COMPARATOR_GREATER_OR_EQUAL_COMPARISON], [EQUAL, SET_COMPARATOR_EQUAL_COMPARISON], [DIFFERENT, SET_COMPARATOR_DIFFERENT_COMPARISON]],
"NUMEXPRESSION" : [[TERM, SET_ADDTERM_FIRST_NODE_BASED_ON_TERM, ADDTERM, SET_NUMEXPRESSION_NODE]],
"ADDTERM" : [[SIGN, TERM, CREATE_ADDTERM_NODE, ADDTERM], [EPSILON, SET_ADDTERM_FINAL_NODE]],
"SIGN": [[PLUS, SET_PLUS_SIGN], [MINUS, SET_MINUS_SIGN]],
"TERM" : [[UNARYEXPR, SET_ADDUNARY_FIRST_NODE_BASED_ON_UNARY_EXPR, ADDUNARY, SET_TERM_NODE_BASED_ON_ADDUNARY]],
"ADDUNARY" : [[HOPERATOR, UNARYEXPR, CREATE_ADDUNARY_NODE, ADDUNARY], [EPSILON, SET_ADDUNARY_FINAL_NODE]],
"HOPERATOR": [[MULTIPLICATION, SET_MULTIPLICATION_OPERATION], [DIVISION, SET_DIVISION_OPERATION], [MODULUS, SET_MODULUS_OPERATION]],
"UNARYEXPR" : [[MOREFACTOR, FACTOR, CREATE_UNARYEXPR_NODE]],
"MOREFACTOR": [[SIGN, SET_MOREFACTOR_SIGN_FROM_SIGN], [EPSILON, SET_NO_MOREFACTOR_SIGN]],
"FACTOR" : [[FACTORX, SET_FACTOR_FROM_FACTORX_NODE], [LVALUE, SET_FACTOR_FROM_LVALUE_NODE]],
"FACTOR\'" : [[INT_CONSTANT, CREATE_INT_CONSTANT_NODE], [FLOAT_CONSTANT, CREATE_FLOAT_CONSTANT_NODE], [STRING_CONSTANT, CREATE_STRING_CONSTANT_NODE], [NULL, CREATE_NULL_NODE], [OPEN_PARENTHESIS, EXPRESSION, CLOSING_PARENTHESIS, SET_FACTORX_FROM_EXPRESSION_NODE]],
"LVALUE" : [[IDENT, APPNUM, CREATE_LVALUE_IDENT_NODE]],
"APPNUM": [[NUMEXPRESSIONS], [EPSILON]],
}

NTs = [ PROGRAM, FUNCLIST, FUNCLISTX, FUNCDEF, PARAMLIST, PARAMLISTX, STATEMENT, TYPE, VARDECL, INDEX, ATRIBSTAT, RESULT, RESULTX, EXPR, FUNCCALL, PARAMLISTCALL, PARAMLISTCALLX, PRINTSTAT, READSTAT, RETURNSTAT, IFSTAT, MORESTAT, FORSTAT, STATELIST, MORESTATELIST, ALLOCEXPRESSION, NUMEXPRESSIONS, NUMEXPRESSIONSX, EXPRESSION, MORENUMEXP, COMPARATOR, NUMEXPRESSION, ADDTERM, SIGN, TERM, ADDUNARY, HOPERATOR, UNARYEXPR, MOREFACTOR, FACTOR, FACTORX, LVALUE, APPNUM]
Terminais = [EPSILON, DEF, IDENT, OPEN_PARENTHESIS, CLOSING_PARENTHESIS, OPEN_CURLY_BRACKET, CLOSING_CURLY_BRACKET, OPEN_SQUARE_BRACKET, CLOSING_SQUARE_BRACKET, COMMA, SEMICOLON, BREAK, INT, FLOAT, STRING, INT_CONSTANT, EQUALS, PRINT, READ, RETURN, ELSE, FOR, NEW, GREATER, LESS, LESS_EQUAL, GREATER_EQUAL, EQUAL, DIFFERENT, PLUS, MINUS, MULTIPLICATION, DIVISION, MODULUS, INT_CONSTANT, FLOAT_CONSTANT, STRING_CONSTANT, NULL]
LL1Action = [
    [STATEMENT],
    [FUNCLIST],
    [EPSILON],
    [FUNCDEF, FUNCLISTX],
    [FUNCLIST],
    [EPSILON],
    [DEF, IDENT, OPEN_PARENTHESIS, PARAMLIST, CLOSING_PARENTHESIS, OPEN_CURLY_BRACKET, STATELIST, CLOSING_CURLY_BRACKET],
    [TYPE, SET_IDENT_LEXEME, IDENT, INSERT_VARIABLE_TYPE_INTO_TABLE_WITHOUT_INDEX, PARAMLISTX],
    [EPSILON],
    [COMMA, PARAMLIST],
    [EPSILON],
    [VARDECL, SEMICOLON],
    [ATRIBSTAT, SEMICOLON],
    [PRINTSTAT, SEMICOLON],
    [READSTAT, SEMICOLON],
    [RETURNSTAT, SEMICOLON],
    [IFSTAT],
    [FORSTAT],
    [OPEN_CURLY_BRACKET, STATELIST, CLOSING_CURLY_BRACKET],
    [BREAK, SEMICOLON],
    [SEMICOLON],
    [INT, SET_TYPE_INT],
    [FLOAT, SET_TYPE_FLOAT],
    [STRING, SET_TYPE_STRING],
    [SET_INDEX_INITIAL_DEPTH_UNTIL_NOW, TYPE, SET_IDENT_LEXEME, IDENT, INDEX, INSERT_VARIABLE_TYPE_INTO_TABLE_WITH_INDEX],
    [OPEN_SQUARE_BRACKET, INT_CONSTANT, CLOSING_SQUARE_BRACKET, SET_INDEX_DEPTH_UNTIL_NOW_PLUS_ONE, INDEX, SET_INDEX_DEPTH],
    [EPSILON, SET_INDEX_DEPTH_BASED_ON_UNTIL_NOW],
    [LVALUE, EQUALS, RESULT],
    [SIGN, FACTOR, CREATE_EXPR_FACTOR_NODE, EXPR, SET_RESULT_NODE],
    [FACTORX, CREATE_EXPR_FACTORX_NODE, EXPR, SET_RESULT_NODE],
    [IDENT, RESULTX],
    [ALLOCEXPRESSION],
    [APPNUM, EXPR],
    [OPEN_PARENTHESIS, PARAMLISTCALL, CLOSING_PARENTHESIS],
    [SET_ADDUNARY_FIRST_NODE_BASED_ON_EXPR, ADDUNARY, SET_ADDTERM_FIRST_NODE_BASED_ON_ADDUNARY, ADDTERM, SET_MORENUMEXP_FIRST_NODE_BASED_ON_ADDTERM, MORENUMEXP, SET_EXPR_FINAL_NODE],
    [IDENT, OPEN_PARENTHESIS, PARAMLISTCALL, CLOSING_PARENTHESIS],
    [IDENT, PARAMLISTCALLX],
    [EPSILON],
    [COMMA, PARAMLISTCALL],
    [EPSILON],
    [PRINT, EXPRESSION],
    [READ, LVALUE],
    [RETURN, IDENT],
    [IF, OPEN_PARENTHESIS, EXPRESSION, CLOSING_PARENTHESIS,  STATEMENT, MORESTAT, ENDIF],
    [ELSE, STATEMENT],
    [EPSILON],
    [FOR, OPEN_PARENTHESIS, ATRIBSTAT, SEMICOLON, EXPRESSION, SEMICOLON, ATRIBSTAT, CLOSING_PARENTHESIS, STATEMENT],
    [STATEMENT, MORESTATELIST],
    [STATELIST],
    [EPSILON],
    [NEW, TYPE, NUMEXPRESSIONS],
    [OPEN_SQUARE_BRACKET, NUMEXPRESSION, CLOSING_SQUARE_BRACKET, NUMEXPRESSIONSX],
    [NUMEXPRESSIONS],
    [EPSILON],
    [NUMEXPRESSION, SET_MORENUMEXP_FIRST_NODE_BASED_ON_NUMEXPRESSION, MORENUMEXP, SET_EXPRESSION_FROM_MORENUMEXP_NODE],
    [COMPARATOR, NUMEXPRESSION, CREATE_MORENUMEXP_FINAL_NODE],
    [EPSILON, SET_MORENUMEXP_FINAL_NODE],
    [GREATER, SET_COMPARATOR_GREATER_COMPARISON],
    [LESS, SET_COMPARATOR_LESS_COMPARISON],
    [LESS_EQUAL, SET_COMPARATOR_LESS_OR_EQUAL_COMPARISON],
    [GREATER_EQUAL, SET_COMPARATOR_GREATER_OR_EQUAL_COMPARISON],
    [EQUAL, SET_COMPARATOR_EQUAL_COMPARISON],
    [DIFFERENT, SET_COMPARATOR_DIFFERENT_COMPARISON],
    [TERM, SET_ADDTERM_FIRST_NODE_BASED_ON_TERM, ADDTERM, SET_NUMEXPRESSION_NODE],
    [SIGN, TERM, CREATE_ADDTERM_NODE, ADDTERM],
    [EPSILON, SET_ADDTERM_FINAL_NODE],
    [PLUS, SET_PLUS_SIGN],
    [MINUS, SET_MINUS_SIGN],
    [UNARYEXPR, SET_ADDUNARY_FIRST_NODE_BASED_ON_UNARY_EXPR, ADDUNARY, SET_TERM_NODE_BASED_ON_ADDUNARY],
    [HOPERATOR, UNARYEXPR, CREATE_ADDUNARY_NODE, ADDUNARY],
    [EPSILON, SET_ADDUNARY_FINAL_NODE],
    [MULTIPLICATION, SET_MULTIPLICATION_OPERATION],
    [DIVISION, SET_DIVISION_OPERATION],
    [MODULUS, SET_MODULUS_OPERATION],
    [MOREFACTOR, FACTOR, CREATE_UNARYEXPR_NODE],
    [SIGN, SET_MOREFACTOR_SIGN_FROM_SIGN],
    [EPSILON, SET_NO_MOREFACTOR_SIGN],
    [FACTORX, SET_FACTOR_FROM_FACTORX_NODE],
    [LVALUE, SET_FACTOR_FROM_LVALUE_NODE],
    [INT_CONSTANT, CREATE_INT_CONSTANT_NODE],
    [FLOAT_CONSTANT, CREATE_FLOAT_CONSTANT_NODE],
    [STRING_CONSTANT, CREATE_STRING_CONSTANT_NODE],
    [NULL, CREATE_NULL_NODE],
    [OPEN_PARENTHESIS, EXPRESSION, CLOSING_PARENTHESIS, SET_FACTORX_FROM_EXPRESSION_NODE],
    [IDENT, APPNUM, CREATE_LVALUE_IDENT_NODE],
    [NUMEXPRESSIONS],
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
    "FUNCLIST'" : {
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
        'break': 18,
        '{': 19,
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

