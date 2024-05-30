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
            "if", "else", "for", "new", "null"
            ]
        self.comparadores = ["<",">","!","="]
        self.simbolosEspeciais = ["(",")","[","]","{","}",";",","]
        self.operadores = ["+","-","/","*","%"]
        self.lexema = ""

    def executar(self, entrada):
        linhaAtual = 0
        with open(entrada) as arquivo:
            for linha in arquivo:
                linhaAtual += 1
                colunaAtual = 0
                for caracter in linha:
                    colunaAtual += 1
                    self.automatoFinito(caracter,linhaAtual,colunaAtual)
        return self.tabelaDeSimbolos


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
                self.estadoAtual = "CP_="
                self.lexema += caracter
                self.tipo = "CP"
            elif caracter in self.simbolosEspeciais: #Simbolo Especial
                self.estadoAtual = "SE_ACEITO"
                self.lexema += caracter
                self.tipo = "SE"
                self.inserirNaTabela(linha, coluna+1)
            elif caracter in self.operadores: #Operador
                self.estadoAtual = "OP_ACEITO"
                self.lexema += caracter
                self.tipo = "OP"
                self.inserirNaTabela(linha, coluna+1)
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
        #Estado CTN_NUM* (pode numeros)
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
            else:
                self.inserirNaTabela(linha, coluna)
                self.automatoFinito(caracter, linha, coluna)
        #Estado CP_ACEITO (nao pode comparadores)
        elif self.estadoAtual == "CP_ACEITO":
            if caracter in self.comparadores:
                self.erro(linha, coluna)
            else:
                self.inserirNaTabela(linha, coluna)
                self.automatoFinito(caracter, linha, coluna)
        #Estado ST_TUDO* (tudo dentro de aspas valido)
        elif self.estadoAtual == "ST_TUDO*":
            if caracter == "\"":
                self.inserirNaTabela(linha, coluna)
            else:
                self.lexema += caracter
        elif self.estadoAtual == "CTF_NUM*":
            if caracter.isnumeric():
                self.lexema += caracter
            else:
                self.inserirNaTabela(linha, coluna)
                self.automatoFinito(caracter, linha, coluna)


    def inserirNaTabela(self, linha, coluna):
        if self.lexema not in self.tabelaDeSimbolos:
            #{var: {tipo: 'ID', posicao: [(1,3), (3,8)]}}
            self.tabelaDeSimbolos[self.lexema] = {}
            if self.tipo == "ID" and self.lexema in self.palavrasReservadas:
                self.tabelaDeSimbolos[self.lexema]["tipo"] = "PR"
            else:
                self.tabelaDeSimbolos[self.lexema]["tipo"] = self.tipo
            self.tabelaDeSimbolos[self.lexema]["posicao"] = [(linha, coluna-len(self.lexema))]
        else:
            self.tabelaDeSimbolos[self.lexema]["posicao"].append((linha, coluna-len(self.lexema)))
        self.estadoAtual = "INICIO"
        self.lexema = ""
        self.tipo = None #TALVEZ N PRECISA

    def erro(self, linha, coluna):
        print(f"ERRO LÉXICO NA LINHA {linha} E COLUNA {coluna}")
        self.estadoAtual = "INICIO"
        self.lexema = ""


al = AnalisadorLexico()
print(al.executar("testeSimples.txt"))
#print(al.executar("causaErroLexico.txt"))
            
            
