#ID -> (alfa)(alfa|num|&)*
#SE -> ((|)|[|]{|}|;|,)
#OP -> (+|-|*|/|%)
#CP -> (<|>|=|!)(&|=)
#CTN -> (num)*
#ST -> "(tudo)*"
#CTF -> num*.num*

class AnalisadorLexico:
    def __init__(self):
        self.tabelaDeSimbolos = {}
        self.estadoAtual = "INICIO"
        self.tipo = None
        self.palavrasReservadas = [
            "def", "int", "float", "string",
            "break", "print", "read", "return",
            "if", "else", "for", "new", "null", "endif"
            ]
        self.comparadores = ["<",">","!","="]
        self.simbolosEspeciais = ["(",")","[","]","{","}",";",","]
        self.operadores = ["+","-","/","*","%"]
        self.lexema = ""
        self.tokens = []
        self.posicoesLexemasDaTabelaDeSimbolos = {}

    def executar(self, entrada):
        linhaAtual = 0
        with open(entrada) as arquivo:
            for linha in arquivo:
                linhaAtual += 1
                colunaAtual = 0
                for caracter in linha:
                    colunaAtual += 1
                    self.automatoFinito(caracter,linhaAtual,colunaAtual)


    def automatoFinito(self, caracter, linha, coluna):
        #Estado INICIAL
        if self.estadoAtual == "INICIO": 
            if caracter.isalpha(): #Identificador 
                self.estadoAtual = "ID_ALNUM*"
                self.lexema += caracter
                self.tipo = "ID"
            elif caracter.isnumeric(): #Numero Constante
                self.estadoAtual = "CTN_NUM*"
                self.lexema += caracter
                self.tipo = "CTN"
            elif caracter in self.comparadores: #Comparador
                if caracter == "!":
                    self.estadoAtual = "DIF_="
                    self.lexema += caracter 
                else:
                    self.estadoAtual = "CP_="
                    self.lexema += caracter
                self.tipo = "CP"
            elif caracter in self.simbolosEspeciais: #Simbolo Especial
                self.estadoAtual = "SE_ACEITO"
                self.lexema += caracter
                self.tipo = "SE"
                self.resetar()
            elif caracter in self.operadores: #Operador
                self.estadoAtual = "OP_ACEITO"
                self.lexema += caracter
                self.tipo = "OP"
                self.resetar()
            elif caracter == "\"": #String
                self.estadoAtual = "ST_TUDO*"
                self.tipo = "ST"
            elif caracter.isspace():
                pass
            else:
                self.erro(linha, coluna)
        #Estado ID_ALNUM* (pode alfabetos ou numeros)
        elif self.estadoAtual == "ID_ALNUM*":
            if caracter.isalnum():
                self.lexema += caracter
            else:
                self.inserirNaTabela(linha, coluna)
                #como leu caracter a mais, executa essa funcao de novo com o mesmo caracter 
                self.automatoFinito(caracter, linha, coluna) 
        #Estado CTN_NUM* (pode numeros ou "." do float)
        elif self.estadoAtual == "CTN_NUM*":
            if caracter.isnumeric():
                self.lexema += caracter
            elif caracter == ".": #Float
                self.estadoAtual = "CTF_NUM*"
                self.tipo = "CTF"
                self.lexema += caracter
            else:
                self.inserirNaTabela(linha, coluna)
                self.automatoFinito(caracter, linha, coluna)
        #Estado CP_= (so pode "=" ou nada)
        elif self.estadoAtual == "CP_=":
            if caracter == "=":
                self.estadoAtual = "CP_ACEITO"
                self.lexema += caracter
            self.resetar()
            #self.automatoFinito(caracter, linha, coluna)
        #Estado DIF_= (precisa de = em seguida de !)
        elif self.estadoAtual == "DIF_=":
            if caracter == "=":
                self.lexema += caracter
                self.resetar()
                #self.automatoFinito(caracter, linha, coluna)
        #Estado ST_TUDO* (tudo dentro de aspas valido)
        elif self.estadoAtual == "ST_TUDO*":
            if caracter == "\"": #se eh fecha aspas
                self.inserirNaTabela(linha, coluna)
            else:
                self.lexema += caracter
        #Estado CTF_NUM* (pode numeros que seriam decimais)
        elif self.estadoAtual == "CTF_NUM*":
            if caracter.isnumeric():
                self.lexema += caracter
            else:
                self.inserirNaTabela(linha, coluna)
                self.automatoFinito(caracter, linha, coluna)

    def resetar(self):
        self.tokens.append(self.lexema)
        self.estadoAtual = "INICIO"
        self.lexema = ""

    def inserirNaTabela(self, linha, coluna):
        if self.lexema not in self.palavrasReservadas:
            if self.lexema not in self.tabelaDeSimbolos:
                self.tabelaDeSimbolos[self.lexema] = {}
                self.tabelaDeSimbolos[self.lexema]["posicao"] = [(linha, coluna-len(self.lexema))]
            else:
                self.tabelaDeSimbolos[self.lexema]["posicao"].append((linha, coluna-len(self.lexema)))

            self.posicoesLexemasDaTabelaDeSimbolos[str(len(self.tokens))] = self.lexema

            if self.tipo == "ID": #se for identificador
                self.lexema = "ident" #troca para "ident"
            elif self.tipo == "CTN": #se numero constante
                self.lexema = "int_constant" #troca para "int_constante"
            elif self.tipo == "CTF": #se float constante
                self.lexema = "float_constant" #troca para "float_constante"
            elif self.tipo == "ST": #se string constante
                self.lexema = "string_constant" #troca para "string_constante"
        self.resetar()

    def erro(self, linha, coluna):
        print(f"ERRO LÉXICO NA LINHA {linha} E COLUNA {coluna} -> '{self.lexema}'")
        self.estadoAtual = "INICIO"
        self.lexema = ""
