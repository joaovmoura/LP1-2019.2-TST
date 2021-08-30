def busca_matriz(m,e):
    posicoes=list()
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==e:
                posicoes.append((i,j))

    return posicoes
