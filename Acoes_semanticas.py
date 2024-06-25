class AcaoSemantica:
    def __init__(self, fn, params):
        self.name = "acao_semantica"
        self.fn = fn
        self.params = params
        self.lexeme = None
        self.symbol_table = None
        self.nodes_list = None

    def exec(self):
        self.fn(self.params, self.lexeme, self.symbol_table, self.nodes_list)

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

def create_node(attr_list, _1, _2, nodes_list):
    node = Node(attr_list[2], attr_list[3], attr_list[4])
    nodes_list.append(node)
    attr_list[0].vars[attr_list[1]] = node

def create_expr_node(attr_list, _1, _2, nodes_list):
    node = Node(attr_list[2], attr_list[3].vars[attr_list[4]], attr_list[5])
    nodes_list.append(node)
    attr_list[0].vars[attr_list[1]] = node

def create_term_node(attr_list, _1, _2, nodes_list):
    node = Node(attr_list[2].vars[attr_list[3]], attr_list[4].vars[attr_list[5]], attr_list[6])
    nodes_list.append(node)
    attr_list[0].vars[attr_list[1]] = node

def create_operation_node(attr_list, _1, _2, nodes_list):
    node = Node(attr_list[2].vars[attr_list[3]], attr_list[4].vars[attr_list[5]], attr_list[6].vars[attr_list[7]])
    nodes_list.append(node)
    attr_list[0].vars[attr_list[1]] = node

def set_var_based_on_another(attr_list, _1, _2, _3):
    attr_list[0].vars[attr_list[1]] = attr_list[2].vars[attr_list[3]]

def insert_type_into_table_with_index(attr_list, _1, symbol_table, _2):
    symbol_table[attr_list[0].vars[attr_list[1]]][attr_list[2]] = f"{attr_list[3].vars[attr_list[4]]} {attr_list[5].vars[attr_list[6]]}"

def insert_type_into_table_without_index(attr_list, _1, symbol_table, _2):
    symbol_table[attr_list[0].vars[attr_list[1]]][attr_list[2]] = f"{attr_list[3].vars[attr_list[4]]}"

def set_lexeme(attr_list, lexeme, _1, _2):
    attr_list[0].vars[attr_list[1]] = lexeme

def set_var(attr_list, _1, _2, _3):
    attr_list[0].vars[attr_list[1]] = attr_list[2]

def set_var_based_on_existing(attr_list, _1, _2, _3):
    attr_list[0].vars[attr_list[1]] = attr_list[0].vars[attr_list[2]]

def set_var_sum(attr_list, _1, _2, _3):
    attr_list[0].vars[attr_list[1]] = attr_list[0].vars[attr_list[2]] + attr_list[3]
