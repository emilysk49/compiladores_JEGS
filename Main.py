import os
import pprint
from Gramatica_em_dicionario import *
from analisador_sintatico import *
from analisador_lexico import *

print("Integrantes: Emily Sayuri Kiba, Gabriel Turatti Andrade, Julien Hervot de Mattos Vaz e Stephan Krug\n")

class GLC():
    def __init__(self, NTs, Ts, Ps, As, S, cifrao, epsilon):
        self.NTs = NTs
        self.Ts = Ts
        self.Ps = Ps
        self.As = As
        self.S = S
        self.cifrao = cifrao
        self.epsilon = epsilon

arquivo_teste = os.path.join(os.path.dirname(__file__), "testes", "testeSimples.txt")

AL = AnalisadorLexico()
AL.executar(arquivo_teste)

Trab = GLC(NTs, Terminais, Producoes, AcoesSemanticas, PROGRAM, CIFRAO, EPSILON)

lista_de_nodos = []
result = analisador_sintatico(Trab, LL1Predict, LL1Action, AL.tokens, AL.posicoesLexemasDaTabelaDeSimbolos, AL.tabelaDeSimbolos, lista_de_nodos)


if result == "Sucesso!":
    print("=== Árvores de expressão ===")
    for i, raiz in enumerate(lista_de_nodos):
        print(f"Árvore {i}:")
        print(raiz)
    print("============================\n")

    print("==== Tabela de símbolos ====")
    pprint.pp(AL.tabelaDeSimbolos)
    print("============================\n")

    print("======== Compilação ========")
    print("Expressões aritméticas válidas.")
    print("Declarações de variáveis por escopo válidas.")
    print("Todo break está no escopo de um for.")

    print("============================\n")

    print("=== Código intermediário ===")
    print("Coming soon...")
    print("============================")
else:
    print(result)
