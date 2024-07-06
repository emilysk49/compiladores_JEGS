def analisador_sintatico(glc, predicts, actions, codigo, posicoes_lexemas_na_tabela_de_simbolos, tabela_de_simbolos, lista_de_nodos):
    pilha = [glc.cifrao, glc.S]
    codigo += ['$']
    tables_stack = [{}]
    cabecote = 0


    while pilha != []:
        if pilha[-1].name not in glc.Ps:
            if pilha[-1].name == codigo[0]:
                pilha.pop(-1)
                codigo.pop(0)
                cabecote += 1
                continue
            elif pilha[-1] in glc.As: # Análise semântica + Geração de código intermediário
                acao_semantica = pilha.pop(-1)

                cabecote_str = str(cabecote)
                if cabecote_str in posicoes_lexemas_na_tabela_de_simbolos:
                    acao_semantica.lexeme = posicoes_lexemas_na_tabela_de_simbolos[cabecote_str]

                acao_semantica.symbol_table = tabela_de_simbolos
                acao_semantica.nodes_list = lista_de_nodos
                acao_semantica.tables_stack = tables_stack

                erro = acao_semantica.exec()
                if erro:
                    return f"{erro} Posição: {str(cabecote)}"
            else:
                return codigo[0] + " Inesperado, posiçãoA " + str(cabecote)
        else:
            if pilha[-1] == glc.cifrao:
                if codigo[0] == glc.cifrao.name:
                    break
                else:
                    return codigo[0] + " Inesperado, posiçãoB " + str(cabecote)

            if codigo[0] not in predicts[pilha[-1].name]:
                return codigo[0] + " Inesperado, posiçãoC " + str(cabecote)

            prod = predicts[pilha[-1].name][codigo[0]]
            result = actions[prod]

            if not result:
                return codigo[0] + " Inesperado, posiçãoD " + str(cabecote)
            pilha.pop(-1)

            for s in result[::-1]:
                if s == glc.epsilon:
                    continue
                pilha.append(s)

    return "Sucesso!"
