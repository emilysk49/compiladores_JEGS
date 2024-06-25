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
AL.executar("testeArvoreExpressao.txt")

Trab = GLC(NTs, Terminais, Producoes, AcoesSemanticas, PROGRAM, CIFRAO, EPSILON)

lista_de_nodos = []
result = analisador_sintatico(Trab, LL1Predict, LL1Action, AL.tokens, AL.posicoesLexemasDaTabelaDeSimbolos, AL.tabelaDeSimbolos, lista_de_nodos)

for nodo in lista_de_nodos:
    print(nodo)
print(result)
print(AL.tabelaDeSimbolos)