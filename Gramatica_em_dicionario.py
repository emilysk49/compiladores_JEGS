Producoes = {
"PROGRAM" : [["STATEMENT"], ["FUNCLIST"], ["&"]],
"FUNCLIST" : [["FUNCDEF", "FUNCLIST\'"]],
"FUNCLIST\'" : [["FUNCLIST"], ["&"]],
"FUNCDEF" : [["def", "ident", "(", "PARAMLIST", ")", "{", "STATELIST", "}"]],
"PARAMLIST" : [["TYPE", "ident", "PARAMLIST\'"], ["&"]],
"PARAMLIST\'" : [[",", "PARAMLIST"], ["&"]],
"STATEMENT" : [["VARDECL", ";"], ["ATRIBSTAT", ";"], ["PRINTSTAT", ";"], ["READSTAT", ";"], ["RETURNSTAT", ";"], ["IFSTAT"], ["FORSTAT"], ["{", "STATELIST", "}"], ["break", ";"], [";"]],
"TYPE" : [["int"], ["float"], ["string"]],
"VARDECL" : [["TYPE", "ident", "INDEX"]],
"INDEX" : [["[", "int_constant", "]", "INDEX"], ["&"]],
"ATRIBSTAT" : [["LVALUE", "=", "RESULT"]],
"RESULT" : [["SIGN", "FACTOR", "EXPR"], ["FACTOR'", "EXPR"], ["ident", "RESULT'"], ["ALLOCEXPRESSION"]],
"RESULT'" : [["APPNUM", "EXPR"], ["(", "PARAMLISTCALL", ")"]],
"EXPR" : [["ADDUNARY", "ADDTERM", "MORENUMEXP"]],
"FUNCCALL" : [["ident", "(", "PARAMLISTCALL", ")"]],
"PARAMLISTCALL" : [["ident", "PARAMLISTCALL\'"], ["&"]],
"PARAMLISTCALL\'" : [[",", "PARAMLISTCALL"], ["&"]],
"PRINTSTAT" : [["print", "EXPRESSION"]],
"READSTAT" : [["read", "LVALUE"]],
"RETURNSTAT" : [["return", "ident"]],
"IFSTAT" : [["if", "(", "EXPRESSION", ")",  "STATEMENT", "MORESTAT", "endif"]],
"MORESTAT" : [["else", "STATEMENT"], ["&"]],
"FORSTAT" : [["for", "(", "ATRIBSTAT;", "EXPRESSION;", "ATRIBSTAT", ")", "STATEMENT"]],
"STATELIST" : [["STATEMENT", "MORESTATELIST"]],
"MORESTATELIST" : [["STATELIST"], ["&"]],
"ALLOCEXPRESSION" : [["new", "TYPE", "NUMEXPRESSIONS"]],
"NUMEXPRESSIONS" : [["[", "NUMEXPRESSION", "]", "NUMEXPRESSIONS\'"]],
"NUMEXPRESSIONS\'" : [["NUMEXPRESSIONS"], ["&"]],
"EXPRESSION" : [["NUMEXPRESSION", "MORENUMEXP"]],
"MORENUMEXP" : [["COMPARATOR", "NUMEXPRESSION"], ["&"]],
"COMPARATOR" : [[">"], ["<"], ["<="], [">="], ["=="], ["!="]],
"NUMEXPRESSION" : [["TERM", "ADDTERM"]],
"ADDTERM" : [["SIGN", "TERM", "ADDTERM"], ["&"]],
"SIGN": [["+"], ["-"]],
"TERM" : [["UNARYEXPR", "ADDUNARY"]],
"ADDUNARY" : [["HOPERATOR", "UNARYEXPR", "ADDUNARY"], ["&"]],
"HOPERATOR": [["*"], ["/"], ["%"]],
"UNARYEXPR" : [["MOREFACTOR", "FACTOR"]],
"MOREFACTOR": [["SIGN"], ["&"]],
"FACTOR" : [["FACTOR'"], ["LVALUE"]],
"FACTOR'" : [["int_constant"], ["float_constant"], ["string_constant"], ["null"], ["(", "EXPRESSION", ")"]],
"LVALUE" : [["ident", "APPNUM"]],
"APPNUM": [["NUMEXPRESSIONS"], ["&"]],
}

NTs = [ "PROGRAM", "FUNCLIST", "FUNCLIST\'", "FUNCDEF", "PARAMLIST", "PARAMLIST\'", "STATEMENT", "TYPE", "VARDECL", "INDEX", "ATRIBSTAT", "RESULT", "RESULT'", "EXPR", "FUNCCALL", "PARAMLISTCALL", "PARAMLISTCALL\'", "PRINTSTAT", "READSTAT", "RETURNSTAT", "IFSTAT", "MORESTAT", "FORSTAT", "STATELIST", "MORESTATELIST", "ALLOCEXPRESSION", "NUMEXPRESSIONS", "NUMEXPRESSIONS\'", "EXPRESSION", "MORENUMEXP", "COMPARATOR", "NUMEXPRESSION", "ADDTERM", "SIGN", "TERM", "ADDUNARY", "HOPERATOR", "UNARYEXPR", "MOREFACTOR", "FACTOR", "FACTOR'", "LVALUE", "APPNUM"]
Terminais = ["&", "def", "ident", "(", ")", "{", "}", "[", "]", ",", ";", "break", "int", "float", "string", "tint", "tfloat", "tstring", "int_consant", "=", "print", "read", "return", "else", "for", "new", "or", "and", "not", ">", "<", "<=", ">=", "==", "!=", "+", "-", "*", "/", "%", "int_constant", "float_constant", "string_constant", "null"]
LL1Action = [
    ["STATEMENT"],
    ["FUNCLIST"],
    ["&"],
    ["FUNCDEF", "FUNCLIST\'"],
    ["FUNCLIST"],
    ["&"],
    ["def", "ident", "(", "PARAMLIST", ")", "{", "STATELIST", "}"],
    ["TYPE", "ident", "PARAMLIST\'"],
    ["&"],
    [",", "PARAMLIST"],
    ["&"],
    ["VARDECL", ";"],
    ["ATRIBSTAT", ";"],
    ["PRINTSTAT", ";"],
    ["READSTAT", ";"],
    ["RETURNSTAT", ";"],
    ["IFSTAT"],
    ["FORSTAT"],
    ["{", "STATELIST", "}"],
    ["break", ";"],
    [";"],
    ["int"],
    ["float"],
    ["string"],
    ["TYPE", "ident", "INDEX"],
    ["[", "int_constant", "],", "INDEX"],
    ["&"],
    ["LVALUE", "=", "RESULT"],
    ["SIGN", "FACTOR", "EXPR"],
    ["FACTOR'", "EXPR"],
    ["ident", "RESULT'"],
    ["ALLOCEXPRESSION"],
    ["APPNUM", "EXPR"],
    ["(", "PARAMLISTCALL", ")"],
    ["ADDUNARY", "ADDTERM", "MORENUMEXP"],
    ["ident", "(", "PARAMLISTCALL", ")"],
    ["ident", "PARAMLISTCALL\'"],
    ["&"],
    [",", "PARAMLISTCALL"],
    ["&"],
    ["print", "EXPRESSION"],
    ["read", "LVALUE"],
    ["return", "ident"],
    ["if", "(", "EXPRESSION", ")",  "STATEMENT", "MORESTAT", "endif"],
    ["else", "STATEMENT"],
    ["&"],
    ["for", "(", "ATRIBSTAT;", "EXPRESSION;", "ATRIBSTAT", ")", "STATEMENT"],
    ["STATEMENT", "MORESTATELIST"],
    ["STATELIST"],
    ["&"],
    ["new", "TYPE", "NUMEXPRESSIONS"],
    ["[", "NUMEXPRESSION", "],", "NUMEXPRESSIONS\'"],
    ["NUMEXPRESSIONS"],
    ["&"],
    ["NUMEXPRESSION", "MORENUMEXP"],
    ["COMPARATOR", "NUMEXPRESSION"],
    ["&"],
    [">"],
    ["<"],
    ["<="],
    [">="],
    ["=="],
    ["!="],
    ["TERM", "ADDTERM"],
    ["SIGN", "TERM", "ADDTERM"],
    ["&"],
    ["+"],
    ["-"],
    ["UNARYEXPR", "ADDUNARY"],
    ["HOPERATOR", "UNARYEXPR", "ADDUNARY"],
    ["&"],
    ["*"],
    ["/"],
    ["%"],
    ["MOREFACTOR", "FACTOR"],
    ["SIGN"],
    ["&"],
    ["FACTOR'"],
    ["LVALUE"],
    ["int_constant"],
    ["float_constant"],
    ["string_constant"],
    ["null"],
    ["(", "EXPRESSION", ")"],
    ["ident", "APPNUM"],
    ["NUMEXPRESSIONS"],
    ["&"]
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
    "PARAMLIST'" : {
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
    "RESULT'" : {
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
    "PARAMLISTCALL'" : {
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
    "NUMEXPRESSIONS'" : {
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
    "FACTOR'" : {
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

