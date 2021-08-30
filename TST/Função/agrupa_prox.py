def agrupa_proximos(lista, valor, criterio):
    lista2 = list()
    for e in lista:
        teste = abs(valor-e)
        if  teste < criterio:lista2.append(e)

    return lista2

#lista=[int(num) for num in input().split()]
#x = agrupa_proximos(lista, 4, 2)
#print(x)
