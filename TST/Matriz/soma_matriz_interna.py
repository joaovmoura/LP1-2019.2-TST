def soma_matriz_interna(matriz, inicio, fim):
    l = inicio[0]
    c = inicio[1]
    retorno =0
    for i in range(inicio[0], fim[0]+1):
        for j in range(inicio[1], fim[1]+1):
            e =matriz[i][j]
            retorno+=(e)



    return retorno

