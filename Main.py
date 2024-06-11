from Gramatica_em_dicionario import *
from analisador_sintatico import *
from analisador_lexico import *

class GLC():
    def __init__(self, NTs, Ts, Ps, S):
        self.NTs = NTs
        self.Ts = Ts
        self.Ps = Ps
        self.S = S

AL = AnalisadorLexico()
AL.executar("testeSimples.txt")

Trab = GLC(NTs, Terminais, Producoes, "PROGRAM")

result = analisador_sintatico(Trab, LL1Predict, LL1Action, AL.tokens)
print(result)

