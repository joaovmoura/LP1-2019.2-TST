def conta_votos(votacoes,id_votacao):
    aux=''
    sim=nao=0
    cada_vot=[]
    for e in votacoes:
        for el in e:
            if el!=',':
                aux+=el
            elif aux!='':
                cada_vot.append(aux)
                aux=''
        if aux!='':
            cada_vot.append(aux)
        if cada_vot[2]==str(id_votacao):
            if cada_vot[1]=='sim':
                sim+=1
            else:
                nao+=1
        cada_vot=[]

    contagem = []
    contagem.append(sim)
    contagem.append(nao)
    return contagem

