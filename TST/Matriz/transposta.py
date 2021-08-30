def transposta(M):
    transp=[]
    for i in range(len(M[0])):
        transp.append([])
    for i in range(len(M)):
        for j in range(len(M[0])):
                transp[j].append(M[i][j])

    return transp

