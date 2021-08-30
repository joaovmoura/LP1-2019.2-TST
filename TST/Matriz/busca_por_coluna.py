def busca_todos_por_coluna_em_matriz(m,e):
    posicoes = []
    for j in range(len(m[0])):
        for i in range(len(m)):
            if m[i][j] == e:
                posicoes.append((i,j))

    return posicoes


