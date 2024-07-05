import re

INVALID_TYPES_ERROR = "Erro semântico: Tipos inválidos!"
NAME_ALREADY_DECLARED_ERROR = "Erro semântico: Nome já declarado no mesmo escopo!"
BREAK_OUTSIDE_FOR_ERROR = "Erro semântico: Break fora do escopo de um comando de repetição!"

contador_rotulo = 0
contador_registrador = 0

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
    if attr_list[0].vars[attr_list[1]][-1] in table:
        return NAME_ALREADY_DECLARED_ERROR
    table[attr_list[0].vars[attr_list[1]][-1]] = 1

def close_TS(attr_list, _1, _2, _3, tables_stack):
    tables_stack.pop(-1)

def set_var_based_on_another(attr_list, _1, _2, _3, _4):
    # TYPE.vars["type"] = IDENT.vars["type"]
    attr_list[0].vars[attr_list[1]] = attr_list[2].vars[attr_list[3]]

def insert_type_into_table_with_index(attr_list, _1, symbol_table, _2, _3):
    # symbol_table[IDENT.vars["lexeme"]]["type"] = TYPE.vars["type"] -> int 0
    symbol_table[attr_list[0].vars[attr_list[1]][-1]][attr_list[2]] = f"{attr_list[3].vars[attr_list[4]]} {attr_list[5].vars[attr_list[6]]}"

def insert_type_into_table_without_index(attr_list, _1, symbol_table, _2, _3):
    symbol_table[attr_list[0].vars[attr_list[1]][-1]][attr_list[2]] = f"{attr_list[3].vars[attr_list[4]]} 0"

def set_lexeme(attr_list, lexeme, _1, _2, _3):
    # IDENT.vars["lexemes"].append("b")
    attr_list[0].vars[attr_list[1]].append(lexeme)

def reset_lexeme(attr_list, _1, _2, _3, _4):
    # IDENT.vars["lexemes"].pop()
    attr_list[0].vars[attr_list[1]].pop()

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
    # Exemplo para ação SET_LVALUE_TYPE
    # LVALUE = attr[0]
    # 1-type, 3-lexemes, 4-type, 6-depth
    # IDENT = attr[2]
    # APPNUM = attr[5]
    if attr_list[4] not in symbol_table[attr_list[2].vars[attr_list[3]][-1]]:
        # if 'type' not in symbol_table[IDENT.vars['lexemes'][-1]]
        attr_list[0].vars[attr_list[1]] = ""
        return

    type_and_depth = symbol_table[attr_list[2].vars[attr_list[3]][-1]][attr_list[4]]
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





# Criar regras semânticas e colocar elas na gramática depois

def Tree_Look(node, codigo):
    if node == None:
        return
    if node.lexeme in ['+', '-']:
        Tree_Look(node.left, codigo)
        Tree_Look(node.right, codigo)
        reg1 = node.left.resultReg
        if node.right == None:
            if node.lexeme == '-':
                codigo += [reg1 + ' = -' + reg1]
            node.resultReg = reg1
            return
        reg2 = node.right.resultReg

        resultReg = novoRegistrador()

        codigo += [resultReg + ' = ' + reg1 + node.lexeme + reg2]

        node.resultReg = resultReg
        return
    elif node.lexeme in ['*', '/', '%']:
        Tree_Look(node.left, codigo)
        Tree_Look(node.right, codigo)
        reg1 = node.left.resultReg
        reg2 = node.right.resultReg

        resultReg = novoRegistrador()

        codigo += [resultReg+' = ' + reg1 + node.lexeme + reg2]

        node.resultReg = resultReg
    elif node.lexeme in ['>', '<', '>=', '<=', '==', '!=']:
        Tree_Look(node.left, codigo)
        Tree_Look(node.right, codigo)
        reg1 = node.left.resultReg
        reg2 = node.right.resultReg

        comparison = reg1 + node.lexeme + reg2
        node.resultReg = comparison
        return
    elif node.lexeme == 'none':
        node.resultReg = 'none'
    else:
        reg1 = novoRegistrador()
        codigo += [reg1 + ' = ' + str(node.lexeme)]
        node.resultReg = reg1

# EXPRESSION -> NUMEXPRESSION MORENUMEXP {GCI_expression}
# ATRIBSTAT -> LVALUE = RESULT {GCI_result} {GCI_atribstat}
def GCI_math(attr_list, _1, _2, _3):
    RESULT = attr_list[0] # RESULT pode ser um EXPRESSION
    root = RESULT.vars['node']
    codigoNovo = []
    Tree_Look(root, codigoNovo)
    # To-do: Converter lista de assembly em uma única string no GCI_math
    RESULT.vars['codigo'] = codigoNovo
    RESULT.vars['lastReg'] = root.resultReg # O registrador que guarda o valor completo desse Result
    # lastReg será uma comparação em caso de EXPRESSION, então não terá um registrador. ex: "t3 > t5"

# ATRIBSTAT -> LVALUE {subir_lvalue_lexeme} = RESULT {GCI_result} {GCI_atribstat}
def GCI_atribstat(attr_list, _1, _2, _3):
    ATRIBSTAT = attr_list[0]
    LVALUE = attr_list[1]
    RESULT = attr_list[2]
    # duvida: Aparentemente o lexeme é uma lista? Como faço para pegar só o lexema inteiro daquele ident?
    codigoNovo = str(LVALUE.lexeme) + ' = ' + RESULT.vars['lastReg']
    ATRIBSTAT.vars['codigo'] = RESULT.vars['codigo'] + codigoNovo

# LVALUE -> IDENT {subir_lvalue_lexeme} APPNUM
def subir_lvalue_lexeme(attr_list, _1, _2, _3):
    LVALUE = attr_list[0]
    IDENT = attr_list[1]
    LVALUE.vars['lexeme'] = IDENT.vars['lexeme']

# PROGRAM -> STATEMENT
# PROGRAM -> FUNCLIST
def subir_program(attr_list, _1, _2, _3):
    PROGRAM = attr_list[0]
    CODSTAT = attr_list[1]
    PROGRAM.vars['codigo'] = CODSTAT.vars['codigo']

# FUNCLIST -> FUNCDEF FUNCLIST'
def subir_funclist(attr_list, _1, _2, _3):
    FUNCLIST = attr_list[0]
    FUNCDEF = attr_list[1]
    FUNCLISTX = attr_list[2]
    FUNCLIST.vars['codigo'] = FUNCDEF.vars['codigo'] + FUNCLISTX.vars['codigo']
    
# FUNCLIST' -> FUNCLIST
# FUNCLIST' -> &
def subir_funclistx(attr_list, _1, _2, _3):
    FUNCLISTX = attr_list[0]
    FUNCLIST = attr_list[1]
    #if FUNCLIST != "&":
    FUNCLISTX.vars['codigo'] = FUNCLIST.vars['codigo']
    #else
    #   FUNCLISTX.vars['codigo'] = ''

# FUNCDEF -> def ident(PARAMLIST) {STATELIST}
def subir_funcdef(attr_list, _1, _2, _3):
    FUNCDEF = attr_list[0]
    STATELIST = attr_list[1]
    FUNCDEF.vars['codigo'] = STATELIST.vars['codigo']

# STATELIST -> STATEMENT MORESTATELIST
def subir_statelist(attr_list, _1, _2, _3):
    STATELIST = attr_list[0]
    STATEMENT = attr_list[1]
    MORESTATLIST = attr_list[2]
    #if MORESTATLIST != '&':
    STATELIST.vars['codigo'] = STATEMENT.vars['codigo'] + MORESTATLIST.vars['codigo']
    #else:
    #    STATELIST.vars['codigo'] = STATEMENT.vars['codigo']
    
# MORESTATLIST -> STATELIST
# MORESTATLIST -> &
def subir_morestatlist(attr_list, _1, _2, _3):
    MORESTATLIST = attr_list[0]
    STATELIST = attr_list[1]
    #if STATELIST != "&":
    MORESTATLIST.vars['codigo'] = STATELIST.vars['codigo']
    #else
    #   MORESTATLIST.vars['codigo'] = ''

# STATEMENT -> IFSTAT; {subir_statement}
# STATEMENT -> FORSTAT; {subir_statement}
# STATEMENT -> ATRIBSTAT; {subir_statement}
def subir_statement(attr_list, _1, _2, _3):
    STATEMENT = attr_list[0]
    CODSTAT = attr_list[1]
    STATEMENT.vars['codigo'] = CODSTAT.vars['codigo']

# MORESTAT -> else STATEMENT
# MORESTAT -> &
def subir_morestat(attr_list, _1, _2, _3):
    MORESTAT = attr_list[0]
    ELSE = attr_list[1]
    #if ELSE != "&":
    MORESTAT.vars['codigo'] = ELSE.vars['codigo']
    #else:
    #    MORESTAT.vars['codigo'] = ''

# IFSTAT -> if {cria_label} (EXPRESSION) STATEMENT MORESTAT endif {GCI_if}
# def GCI_

# IFSTAT -> if (EXPRESSION) STATEMENT MORESTAT endif {GCI_if}
def GCI_if(attr_list, _1, _2, _3):
    IFSTAT = attr_list[0]
    EXPRESSION = attr_list[1]
    STATEMENT = attr_list[2]
    MORESTAT = attr_list[3]
    if_falso = novoRotulo()
    if_prox = novoRotulo()
    #se tem else
    if (MORESTAT.vars['codigo'] != ''):
        codigo = (f"{EXPRESSION.vars['codigo']}\n"
                  f"if False {EXPRESSION.vars['lastReg']} goto {if_falso}\n"
                  f"{STATEMENT.vars['codigo']}\n"
                  f"{if_falso}: {MORESTAT.vars['codigo']}\n")
    #se nao tem else
    else:
        codigo = (f"{EXPRESSION.vars['codigo']}\n"
                  f"if False {EXPRESSION.vars['lastReg']} goto {if_prox}\n"
                  f"{STATEMENT.vars['codigo']}\n"
                  f"{if_prox}: ")
        
    IFSTAT.vars['codigo'] = codigo

#FORSTAT → for ( ATRIBSTAT1 ; EXPRESSION ; ATRIBSTAT2 ) STATEMENT {GCI_for}
def GCI_for(attr_list, _1, _2, _3):
    FORSTAT = attr_list[0]
    ATRIBSTAT1 = attr_list[1]
    EXPRESSION = attr_list[2]
    ATRIBSTAT2 = attr_list[3]
    STATEMENT = attr_list[4]
    for_prox = novoRotulo()
    for_inicio = novoRotulo()
    
    codigo = (f"{ATRIBSTAT1.vars['codigo']}\n"
              f"{for_inicio}: {EXPRESSION.vars['codigo']}\n"
              f"if False {EXPRESSION.vars['lastReg']} goto {for_prox}\n"
              f"{STATEMENT.vars['codigo']}\n"
              f"{ATRIBSTAT2.vars['codigo']}\n"
              f"goto {for_inicio}\n"
              f"{for_prox}: ")
    
    FORSTAT.vars['codigo'] = codigo

def novoRegistrador():
    global contador_registrador
    registrador = f"t{contador_registrador}"
    contador_registrador += 1
    return registrador

def novoRotulo():
    global contador_rotulo
    label = f"Label{contador_rotulo}"
    contador_rotulo += 1
    return label