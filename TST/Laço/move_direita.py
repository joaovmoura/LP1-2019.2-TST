def move_direita(labirinto):
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if labirinto[i][j] =='*':
                if j!=len(labirinto[0])-1:
                    if labirinto[i][j+1]==' ':
                        labirinto[i][j], labirinto[i][j+1] = labirinto[i][j+1], labirinto[i][j]
                        return (i, j+1)
                return(i,j)
