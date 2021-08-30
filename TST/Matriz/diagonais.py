def diagonais(M):
    principal = []
    secundaria = []
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i == j:
                principal.append(M[i][j])
            if i+j == len(M)-1:
                secundaria.append(M[i][j])
    return [principal,secundaria]
