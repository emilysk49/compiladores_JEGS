
def analisador_sintatico(glc, predicts, actions, codigo):
    pilha = ['$', glc.S]
    codigo += ["$"]
    cabecote = 1

    while pilha != []:
        if pilha[-1] not in glc.Ps:
            if pilha[-1] == codigo[0]:
                pilha.pop(-1)
                codigo.pop(0)
                cabecote += 1
                continue
            else:
                return codigo[0] + " Inesperado, posição " + str(cabecote)
        else:
            if pilha[-1] == '$':
                if codigo[0] == '$':
                    break
                else:
                    return codigo[0] + " Inesperado, posição " + str(cabecote)
            if codigo[0] not in predicts[pilha[-1]]:
                return codigo[0] + " Inesperado, posição " + str(cabecote)
            prod = predicts[pilha[-1]][codigo[0]]
            result = actions[prod]
            if not result:
                return codigo[0] + " Inesperado, posição " + str(cabecote)
            pilha.pop(-1)

            for s in result[::-1]:
                if s == '&':
                    continue
                pilha.append(s)
    return "Sucesso!"
