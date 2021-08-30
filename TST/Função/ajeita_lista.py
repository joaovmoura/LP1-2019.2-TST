def ajeita_lista(lista):
    def traz_pro_comeco_ordenando(l, ind):
        for i in range(ind, 0, -1):
            e = l[i] #elemento que eu estou colocando em ordem
            a = l[i-1] #elemento anterior ao que eu quero ordenar

            if a%2!=0:#se o elemento anterior é impar, eles trocam de lugar

                l[i], l[i-1] = l[i-1], l[i]

            elif a<e:
                #se ele não é ímpar, eles só trocam de lugar se o elemento que eu quero é maior que o anterior, pra ficar na ordem decrescente
                l[i], l[i-1] = l[i-1], l[i]

    #inicializando um contador para a qtd de elementos pares
    pares = 0

    for i in range(len(lista)):
        e = lista[i]
#percorrendo a lista e verificando quais são pares
        if e%2==0:
#se o elemento é par, eu coloco ele no começo, já na ordem, usando uma função definida dentro da função
            traz_pro_comeco_ordenando(lista,i)
#contando os pares pra saber onde vai estar o priemiro impar 
            pares+=1
    #bubblesort para ordenar os impares
    while True:
        trocou = False
#o for começa na de pares, porque é o primeiro indice de um elemento impar, ja que os pares estã no começo da lista
        for i in range(pares, len(lista)-1):
            if lista[i]>lista[i+1]:
                trocou = True
                lista[i], lista[i+1] = lista[i+1], lista[i]
        if not trocou:break

lista = [int(n) for n in input().split()]
ajeita_lista(lista)
print(lista)
