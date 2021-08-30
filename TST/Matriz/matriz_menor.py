def matriz_menor(M1, M2):
    M = []
    for i in range(len(M1)):
        M.append([])
    for i in range(len(M1)):
        for j in range(len(M1[0])):
            if M1[i][j]<M2[i][j]:
                M[i].append(M1[i][j])
            else:
                M[i].append(M2[i][j])
    return M
