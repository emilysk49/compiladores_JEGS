from Gramatica_em_dicionario import *
from analisador_sintatico import *
from analisador_lexico import *

class GLC():
    def __init__(self, NTs, Ts, Ps, As, S, cifrao, epsilon):
        self.NTs = NTs
        self.Ts = Ts
        self.Ps = Ps
        self.As = As
        self.S = S
        self.cifrao = cifrao
        self.epsilon = epsilon

AL = AnalisadorLexico()
AL.executar("testeInsercaoTipo.txt")

Trab = GLC(NTs, Terminais, Producoes, AcoesSemanticas, PROGRAM, CIFRAO, EPSILON)

result = analisador_sintatico(Trab, LL1Predict, LL1Action, AL.tokens, AL.posicoesLexemasDaTabelaDeSimbolos, AL.tabelaDeSimbolos)
print(result)
print(AL.tabelaDeSimbolos)