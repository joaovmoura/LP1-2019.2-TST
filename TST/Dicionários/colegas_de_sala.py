def colegas_de_sala(salasprofs, professor):
    colegas=list()
    for k in salasprofs.keys():
        if salasprofs[k]==salasprofs[professor] and k!=professor:
            colegas.append(k)
    return colegas

salasprofs = {
'Franklin': 206,    'Tiago':206,        'Eliane': 206,
'Adalberto':209,    'Wilkerson':207,    'Dalton': 204,
'Jorge': 204
}

