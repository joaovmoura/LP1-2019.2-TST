def top_3(lista):
    def passa_pra_frente(l,c):
        maior=lista[c]
        aux=0
        indice=c
        ordenado = False
        for i in range(c, len(l)):
            if l[i]>maior:
                maior = l[i]
                indice = i
        while not ordenado:
            for i in range(c, indice):
                aux = l[i]
                l[i] = l[i+1]
                l[i+1] = aux
            if l[c]==maior: ordenado=True
    for i in range(3):
        passa_pra_frente(lista,i)

'''
while True:
    lista = [int(e) for e in input().split()]
    top_3(lista)
    print(lista)
    cont = input()
    if cont == '0':break
