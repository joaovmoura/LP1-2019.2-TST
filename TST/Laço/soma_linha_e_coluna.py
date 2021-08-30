def soma_linha_e_coluna(matriz, l, c):
    soma = 0
    for i in range(len(matriz)):
        if i!=l:soma+=matriz[i][c]
    for j in range(len(matriz[0])):
        if j!=c:soma+=matriz[l][j]
    return soma




