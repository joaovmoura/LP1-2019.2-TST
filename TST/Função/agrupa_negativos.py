def agrupa_negativos(lista):
    grupos = {'nao-negativos':[], 'negativos':[]}
    for e in lista:
        if e < 0:
            grupos['negativos'].append(e)
        else:
            grupos['nao-negativos'].append(e)
    return grupos
