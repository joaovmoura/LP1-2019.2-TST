def busca_matriz(m, e):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == e:
                return (i,j)
    return None
