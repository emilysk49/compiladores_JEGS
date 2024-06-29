import re

INVALID_TYPES_ERROR = "Erro semântico: Tipos inválidos!"
NAME_ALREADY_DECLARED_ERROR = "Erro semântico: Nome já declarado no mesmo escopo!"
BREAK_OUTSIDE_FOR_ERROR = "Erro semântico: Break fora do escopo de um comando de repetição!"

class AcaoSemantica:
    def __init__(self, fn, params):
        self.name = "acao_semantica"
        self.fn = fn
        self.params = params
        self.lexeme = None
        self.symbol_table = None
        self.nodes_list = None
        self.tables_stack = None

    def exec(self):
        return self.fn(self.params, self.lexeme, self.symbol_table, self.nodes_list, self.tables_stack)

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.children = [self.left, self.right]

    def __str__(self, level=0):
        ret = "\t" * level + self.value + ":\n"
        for child in self.children:
            if type(child) is not Node:
                ret += "\t" * (level + 1) + child.__str__() + "\n"
            else:
                ret += child.__str__(level+1)
        return ret


def create_node(attr_list, _1, _2, nodes_list, _3):
    # nó("int_constant", "-", "-")
    node = Node(attr_list[2], attr_list[3], attr_list[4])
    nodes_list.append(node)
    attr_list[0].vars[attr_list[1]] = node

def create_expr_node(attr_list, _1, _2, nodes_list, _3):
    # nó("+", IDENT.ident, "-")
    node = Node(attr_list[2], attr_list[3].vars[attr_list[4]], attr_list[5])
    nodes_list.remove(attr_list[3].vars[attr_list[4]])
    nodes_list.append(node)
    attr_list[0].vars[attr_list[1]] = node

def create_term_node(attr_list, _1, _2, nodes_list, _3):
    # nó(SIGN.sign, IDENT.ident, "-")
    node = Node(attr_list[2].vars[attr_list[3]], attr_list[4].vars[attr_list[5]], attr_list[6])
    nodes_list.remove(attr_list[4].vars[attr_list[5]])
    nodes_list.append(node)
    attr_list[0].vars[attr_list[1]] = node

def create_operation_node(attr_list, _1, _2, nodes_list, _3):
    # nó(SIGN.sign, IDENT.ident, IDENT.ident)
    node = Node(attr_list[2].vars[attr_list[3]], attr_list[4].vars[attr_list[5]], attr_list[6].vars[attr_list[7]])
    nodes_list.remove(attr_list[4].vars[attr_list[5]])
    nodes_list.remove(attr_list[6].vars[attr_list[7]])
    nodes_list.append(node)
    attr_list[0].vars[attr_list[1]] = node

def create_TS(attr_list, _1, _2, _3, tables_stack):
    table = {}
    tables_stack.append(table)
    
def set_lexeme_or_throw_error(attr_list, _1, _2, _3, tables_stack):
    table = tables_stack[-1]
    # if table[IDENT.vars["lexeme"]] -> erro
    if attr_list[0].vars[attr_list[1]] in table:
        return NAME_ALREADY_DECLARED_ERROR
    table[attr_list[0].vars[attr_list[1]]] = 1

def close_TS(attr_list, _1, _2, _3, tables_stack):
    tables_stack.pop(-1)

def set_var_based_on_another(attr_list, _1, _2, _3, _4):
    # TYPE.vars["type"] = IDENT.vars["type"]
    attr_list[0].vars[attr_list[1]] = attr_list[2].vars[attr_list[3]]

def insert_type_into_table_with_index(attr_list, _1, symbol_table, _2, _3):
    # symbol_table[IDENT.vars["lexeme"]]["type"] = TYPE.vars["type"] -> int 0
    symbol_table[attr_list[0].vars[attr_list[1]]][attr_list[2]] = f"{attr_list[3].vars[attr_list[4]]} {attr_list[5].vars[attr_list[6]]}"

def insert_type_into_table_without_index(attr_list, _1, symbol_table, _2, _3):
    symbol_table[attr_list[0].vars[attr_list[1]]][attr_list[2]] = f"{attr_list[3].vars[attr_list[4]]} 0"

def set_lexeme(attr_list, lexeme, _1, _2, _3):
    # IDENT.vars["lexeme"] = "b" 
    attr_list[0].vars[attr_list[1]] = lexeme

def set_var(attr_list, _1, _2, _3, _4):
    # TYPE.vars["final_type"] = "int"
    attr_list[0].vars[attr_list[1]] = attr_list[2]

def set_var_based_on_existing(attr_list, _1, _2, _3, _4):
    # TYPE.vars["final_type"] = TYPE.vars["current_type"]
    attr_list[0].vars[attr_list[1]] = attr_list[0].vars[attr_list[2]]

def set_var_sum(attr_list, _1, _2, _3, _4):
    attr_list[0].vars[attr_list[1]] = attr_list[0].vars[attr_list[2]] + attr_list[3]

def set_type_or_throw_error(attr_list, _1, _2, _3, _4):
    if attr_list[2].vars[attr_list[3]] != "" and attr_list[2].vars[attr_list[3]] != attr_list[4].vars[attr_list[5]]:
        return INVALID_TYPES_ERROR
    attr_list[0].vars[attr_list[1]] = attr_list[4].vars[attr_list[5]]

def set_triple_type_or_throw_error(attr_list, _1, _2, _3, _4):
    if attr_list[2].vars[attr_list[3]] != "" and attr_list[4].vars[attr_list[5]] != "" and attr_list[2].vars[attr_list[3]] != attr_list[4].vars[attr_list[5]]:
        return INVALID_TYPES_ERROR

    if attr_list[4].vars[attr_list[5]] != "" and attr_list[6].vars[attr_list[7]] != "" and attr_list[4].vars[attr_list[5]] != attr_list[6].vars[attr_list[7]]:
        return INVALID_TYPES_ERROR

    if attr_list[2].vars[attr_list[3]] != "" and attr_list[6].vars[attr_list[7]] != "" and attr_list[2].vars[attr_list[3]] != attr_list[6].vars[attr_list[7]]:
        return INVALID_TYPES_ERROR

    attr_list[0].vars[attr_list[1]] = attr_list[2].vars[attr_list[3]] or attr_list[4].vars[attr_list[5]] or attr_list[6].vars[attr_list[7]]

def set_variable_type_based_on_ident(attr_list, _1, symbol_table, _2, _3):
    type_and_depth = symbol_table[attr_list[2].vars[attr_list[3]]][attr_list[4]]
    var_type, depth, _ = re.split('(\d+)', type_and_depth)

    var_depth = attr_list[5].vars[attr_list[6]]
    attr_list[0].vars[attr_list[1]] = f"{var_type}{int(depth) - var_depth}"

def set_var_of_ts_based_on_another(attr_list, _1, _2, _3, tables_stack):
    table = tables_stack[-1]
    table[attr_list[0]] = attr_list[1].vars[attr_list[2]]

def verify_ts_var_or_throw_error(attr_list, _1, _2, _3, tables_stack):
    table = tables_stack[-1]
    if attr_list[0] not in table:
        return BREAK_OUTSIDE_FOR_ERROR
