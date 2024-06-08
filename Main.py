from Gramatica_em_dicionario import *
from analisador_sintatico import *

class GLC():
    def __init__(self, NTs, Ts, Ps, S):
        self.NTs = NTs
        self.Ts = Ts
        self.Ps = Ps
        self.S = S

Trab = GLC(NTs, Terminais, Producoes, "PROGRAM")

codigo = [
    "def", "ident", "(", "int", "ident", ",", "int", "ident", ")", "{", 
        "int", "ident", ";",
        "ident", "=", "ident", "+", "ident", ";",
        "return", "ident", ";", 
    "}",
    "def", "ident", "(", ")", "{", 
        "int", "ident", ";", 
        "int", "ident", ";", 
        "ident", "=", "int_constant", ";", 
        "ident", "=", "int_constant", ";", 
        "int", "ident", ";", 
        "ident", "=", "ident", "(", "ident", ",", "ident", ")", ";", 
    "}"
]

result = analisador_sintatico(Trab, LL1Predict, LL1Action, codigo)
print(result)

