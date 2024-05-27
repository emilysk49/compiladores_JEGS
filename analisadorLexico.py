#analise lexica (com tabela de simbolos) -> identicador e lista com linha x coluna 

class AnalisadorLexico:
    def __init__(self):
        self.tabelaDeSimbolos = {}
        self.palavrasReservadas = [
            "def", "int", "float", "string",
            "break", "print", "read", "return",
            "if", "else", "for", "new", "null"
            ]
        self.simbolosEspeciais = [";", "(", ")", "[", "]", "{", "}", ","]
        self.operadores = ["+", "-", "*", "/", "%"]
        self.comparadores = ["=", "<", ">", "!"]
        
    def executar(self, entrada):
        tipo = None
        lexemaAtual = []
        linhaAtual = 0
        with open(entrada) as arquivo:
            for linha in arquivo:
                linhaAtual += 1
                colunaAtual = 0
                for caracter in linha:
                    colunaAtual += 1
                    #se eh primeira caracter da lexema lendo
                    if tipo == None:
                        if caracter.isalpha():
                            lexemaAtual.append(caracter)
                            tipo = "ID"
                        elif caracter in self.simbolosEspeciais:
                            lexemaAtual.append(caracter)
                            tipo = "SE"
                        elif caracter in self.operadores:
                            lexemaAtual.append(caracter)
                            tipo = "OP"
                        elif caracter in self.comparadores:
                            lexemaAtual.append(caracter) 
                            tipo = "CP"
                        elif caracter.isnumeric():
                            lexemaAtual.append(caracter)
                            tipo = "CT"
                        elif caracter == " ":
                            pass
                        else:
                            self.erro(linhaAtual, colunaAtual)
                    elif tipo == "ID" and caracter.isalnum():
                        lexemaAtual.append(caracter)
                    elif tipo == "SE" and caracter in self.simbolosEspeciais:
                        lexemaAtual.append(caracter)
                    elif tipo == "OP" and caracter in self.operadores:
                        lexemaAtual.append(caracter)
                    elif tipo == "CP" and caracter in self.comparadores:
                        lexemaAtual.append(caracter)
                    elif tipo == "CT" and caracter.isnumeric(): #talvez precisa tratar float (ex: 1.3)
                        lexemaAtual.append(caracter)

                    else:
                        self.inserirToken("".join(lexemaAtual), tipo, linhaAtual, colunaAtual)

                        lexemaAtual = []
                        if caracter == " ":
                            tipo = None
                        elif caracter in self.simbolosEspeciais:
                            lexemaAtual.append(caracter)
                            tipo = "SE"
                        elif caracter in self.operadores:
                            lexemaAtual.append(caracter)
                            tipo = "OP"
                        elif caracter in self.comparadores:
                            lexemaAtual.append(caracter)
                            tipo = "CP"
                        elif caracter.isalpha():
                            lexemaAtual.append(caracter)
                            tipo = "ID"
                        elif caracter.isnumeric():
                            lexemaAtual.append(caracter)
                            tipo = "CT"
        return self.tabelaDeSimbolos
                            

    def erro(self, linha, coluna):
        print(f"ERRO LÉXICO na linha {linha} e coluna {coluna}")

    def inserirToken(self, token, tipo, linha, coluna):
        if token not in self.tabelaDeSimbolos:
            #{var: {tipo: 'ID', posicao: [(1,3), (3,8)]} }
            self.tabelaDeSimbolos[token] = {}
            if tipo == "ID" and token in self.palavrasReservadas:
                self.tabelaDeSimbolos[token]['tipo'] = "PR"
            else:
                self.tabelaDeSimbolos[token]['tipo'] = tipo
            self.tabelaDeSimbolos[token]['posicao'] = [(linha, coluna-len(token))]
        else:
            self.tabelaDeSimbolos[token]['posicao'].append((linha,coluna-len(token)))

al = AnalisadorLexico()
print(al.executar("teste.txt"))

                