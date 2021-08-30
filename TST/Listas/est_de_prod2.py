def distribui_materia_prima(esteira_de_materia_prima, n):
    esteiras=[]
    k= 0

    for i in range(n):
        esteiras.append([])

    for e in esteira_de_materia_prima:
        if k<n:
            esteiras[k].append(e)
            k+=1
        else:
            esteiras[0].append(e)
            k=1

    return esteiras


