def insere_ordenado_primeiro(lista):
    menor = lista[0]
    indice=0
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            lista[i],lista[i+1]=lista[i+1],lista[i]

#lista = [int(e) for e in input().split()]
#insere_ordenado_primeiro(lista)
#print(lista)
