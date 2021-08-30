def insere_nome(aluno1, duplas, aluno2):
    def insere_antes(lista, indice):
        for i in range(len(lista)-1, indice, -1):
            lista[i],lista[i-1]=lista[i-1], lista[i]
    duplas.append(aluno1)
    for i in range(len(duplas)):
        e = duplas[i]
        if e == aluno2:
            insere_antes(duplas, i)
            break
'''        print(duplas)
duplas = ['joel', 'juliano', 'cesar', 'auri', 'zito']
assert insere_nome('gil', duplas, 'juliano') == None
#assert duplas == ['joel', 'gil', 'juliano', 'cesar', 'auri', 'zito']
assert insere_nome('marta', duplas, 'vera') == None
#assert duplas == ['joel', 'gil', 'juliano', 'cesar', 'auri', 'zito', 'marta']'''
