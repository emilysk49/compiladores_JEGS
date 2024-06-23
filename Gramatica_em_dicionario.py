class Variable:
    def __init__(self, name):
        self.name = name
        self.vars = {}

PROGRAM = Variable("PROGRAM")
CIFRAO = Variable("$")
STATEMENT = Variable("STATEMENT")
FUNCLIST = Variable("FUNCLIST")
FUNCDEF = Variable("FUNCDEF")
FUNCLISTX = Variable("FUNCLIST\'")
FUNCCALL = Variable("FUNCCALL")
PARAMLIST = Variable("PARAMLIST")
STATELIST = Variable("STATELIST")
TYPE = Variable("TYPE")
PARAMLISTX = Variable("PARAMLIST\'")
VARDECL = Variable("VARDECL")
ATRIBSTAT = Variable("ATRIBSTAT")
PRINTSTAT = Variable("PRINTSTAT")
READSTAT = Variable("READSTAT")
RETURNSTAT = Variable("RETURNSTAT")
IFSTAT = Variable("IFSTAT")
FORSTAT = Variable("FORSTAT")
INDEX = Variable("INDEX")
LVALUE = Variable("LVALUE")
RESULT = Variable("RESULT")
SIGN = Variable("SIGN")
FACTOR = Variable("FACTOR")
EXPR = Variable("EXPR")
RESULTX = Variable("RESULT\'")
ALLOCEXPRESSION = Variable("ALLOCEXPRESSION")
APPNUM = Variable("APPNUM")
PARAMLISTCALL = Variable("PARAMLISTCALL")
ADDTERM = Variable("ADDTERM")
MORENUMEXP = Variable("MORENUMEXP")
FACTORX = Variable("FACTOR\'")
ADDUNARY = Variable("ADDUNARY")
PARAMLISTCALLX = Variable("PARAMLISTCALL\'")
EXPRESSION = Variable("EXPRESSION")
MORESTAT = Variable("MORESTAT")
MORESTATELIST = Variable("MORESTATELIST")
NUMEXPRESSIONS = Variable("NUMEXPRESSIONS")
NUMEXPRESSIONSX = Variable("NUMEXPRESSIONS\'")
NUMEXPRESSION = Variable("NUMEXPRESSION")
COMPARATOR = Variable("COMPARATOR")
TERM = Variable("TERM")
UNARYEXPR = Variable("UNARYEXPR")
HOPERATOR = Variable("HOPERATOR")
MOREFACTOR = Variable("MOREFACTOR")

PRINT = Variable("print")
READ = Variable("read")
RETURN = Variable("return")
IF = Variable("if")
ELSE = Variable("else")
FOR = Variable("for")
GREATER = Variable(">")
LESS = Variable("<")
LESS_EQUAL = Variable("<=")
GREATER_EQUAL = Variable(">=")
EQUAL = Variable("==")
DIFFERENT = Variable("!=")
PLUS = Variable("+")
MINUS = Variable("-")
MULTIPLICATION = Variable("*")
DIVISION = Variable("/")
MODULUS = Variable("%")
NULL = Variable("null")
INT = Variable("int")
FLOAT = Variable("float")
STRING = Variable("string")
INT_CONSTANT = Variable("int_constant")
FLOAT_CONSTANT = Variable("float_constant")
STRING_CONSTANT = Variable("string_constant")
BREAK = Variable("break")
DEF = Variable("def")
IDENT = Variable("ident")
NEW = Variable("new") 
ENDIF = ("endif")
EPSILON = Variable("&")

OPEN_SQUARE_BRACKET = Variable("[")
CLOSING_SQUARE_BRACKET = Variable("]")
OPEN_CURLY_BRACKET = Variable("{")
CLOSING_CURLY_BRACKET = Variable("}")
OPEN_PARENTHESIS = Variable("(")
CLOSING_PARENTHESIS = Variable(")")
EQUALS = Variable("=")
COMMA = Variable(",")
SEMICOLON = Variable(";")

class AcaoSemantica:
    def __init__(self, fn, params):
        self.name = "acao_semantica"
        self.fn = fn
        self.params = params
        self.lexeme = None
        self.symbol_table = None

    def exec(self):
        self.fn(self.params, self.lexeme, self.symbol_table)

def insert_type_into_table_with_index(attr_list, _1, symbol_table):
    symbol_table[attr_list[0].vars[attr_list[1]]][attr_list[2]] = f"{attr_list[3].vars[attr_list[4]]} {attr_list[5].vars[attr_list[6]]}"

def insert_type_into_table_without_index(attr_list, _1, symbol_table):
    symbol_table[attr_list[0].vars[attr_list[1]]][attr_list[2]] = f"{attr_list[3].vars[attr_list[4]]}"

def set_lexeme(attr_list, lexeme, _1):
    attr_list[0].vars[attr_list[1]] = lexeme

def set_var(attr_list, _1, _2):
    attr_list[0].vars[attr_list[1]] = attr_list[2]

def set_var_based_on_existing(attr_list, _1, _2):
    attr_list[0].vars[attr_list[1]] = attr_list[0].vars[attr_list[2]]

def set_var_sum(attr_list, _1, _2):
    attr_list[0].vars[attr_list[1]] = attr_list[0].vars[attr_list[2]] + attr_list[3]

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
"RESULT" : [[SIGN, FACTOR, EXPR], [FACTORX, EXPR], [IDENT, RESULTX], [ALLOCEXPRESSION]],
"RESULT\'" : [[APPNUM, EXPR], [OPEN_PARENTHESIS, PARAMLISTCALL, CLOSING_PARENTHESIS]],
"EXPR" : [[ADDUNARY, ADDTERM, MORENUMEXP]],
"FUNCCALL" : [[IDENT, OPEN_PARENTHESIS, PARAMLISTCALL, CLOSING_PARENTHESIS]],
"PARAMLISTCALL" : [[IDENT, PARAMLISTCALLX], [EPSILON]],
"PARAMLISTCALL\'" : [[COMMA, PARAMLISTCALL], [EPSILON]],
"PRINTSTAT" : [[PRINT, EXPRESSION]],
"READSTAT" : [[READ, LVALUE]],
"RETURNSTAT" : [[RETURN, IDENT]],
"IFSTAT" : [[IF, OPEN_PARENTHESIS, EXPRESSION, CLOSING_PARENTHESIS,  STATEMENT, MORESTAT, ENDIF]],
"MORESTAT" : [[ELSE, STATEMENT], [EPSILON]],
"FORSTAT" : [[FOR, OPEN_PARENTHESIS, ATRIBSTAT, SEMICOLON, EXPRESSION, SEMICOLON, ATRIBSTAT, CLOSING_PARENTHESIS, STATEMENT]],
"STATELIST" : [[STATEMENT, MORESTATELIST]],
"MORESTATELIST" : [[STATELIST], [EPSILON]],
"ALLOCEXPRESSION" : [[NEW, TYPE, NUMEXPRESSIONS]],
"NUMEXPRESSIONS" : [[OPEN_SQUARE_BRACKET, NUMEXPRESSION, CLOSING_SQUARE_BRACKET, NUMEXPRESSIONSX]],
"NUMEXPRESSIONS\'" : [[NUMEXPRESSIONS], [EPSILON]],
"EXPRESSION" : [[NUMEXPRESSION, MORENUMEXP]],
"MORENUMEXP" : [[COMPARATOR, NUMEXPRESSION], [EPSILON]],
"COMPARATOR" : [[GREATER], [LESS], [LESS_EQUAL], [GREATER_EQUAL], [EQUAL], [DIFFERENT]],
"NUMEXPRESSION" : [[TERM, ADDTERM]],
"ADDTERM" : [[SIGN, TERM, ADDTERM], [EPSILON]],
"SIGN": [[PLUS], [MINUS]],
"TERM" : [[UNARYEXPR, ADDUNARY]],
"ADDUNARY" : [[HOPERATOR, UNARYEXPR, ADDUNARY], [EPSILON]],
"HOPERATOR": [[MULTIPLICATION], [DIVISION], [MODULUS]],
"UNARYEXPR" : [[MOREFACTOR, FACTOR]],
"MOREFACTOR": [[SIGN], [EPSILON]],
"FACTOR" : [[FACTORX], [LVALUE]],
"FACTOR\'" : [[INT_CONSTANT], [FLOAT_CONSTANT], [STRING_CONSTANT], [NULL], [OPEN_PARENTHESIS, EXPRESSION, CLOSING_PARENTHESIS]],
"LVALUE" : [[IDENT, APPNUM]],
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
    [SIGN, FACTOR, EXPR],
    [FACTORX, EXPR],
    [IDENT, RESULTX],
    [ALLOCEXPRESSION],
    [APPNUM, EXPR],
    [OPEN_PARENTHESIS, PARAMLISTCALL, CLOSING_PARENTHESIS],
    [ADDUNARY, ADDTERM, MORENUMEXP],
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
    [NUMEXPRESSION, MORENUMEXP],
    [COMPARATOR, NUMEXPRESSION],
    [EPSILON],
    [GREATER],
    [LESS],
    [LESS_EQUAL],
    [GREATER_EQUAL],
    [EQUAL],
    [DIFFERENT],
    [TERM, ADDTERM],
    [SIGN, TERM, ADDTERM],
    [EPSILON],
    [PLUS],
    [MINUS],
    [UNARYEXPR, ADDUNARY],
    [HOPERATOR, UNARYEXPR, ADDUNARY],
    [EPSILON],
    [MULTIPLICATION],
    [DIVISION],
    [MODULUS],
    [MOREFACTOR, FACTOR],
    [SIGN],
    [EPSILON],
    [FACTORX],
    [LVALUE],
    [INT_CONSTANT],
    [FLOAT_CONSTANT],
    [STRING_CONSTANT],
    [NULL],
    [OPEN_PARENTHESIS, EXPRESSION, CLOSING_PARENTHESIS],
    [IDENT, APPNUM],
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

