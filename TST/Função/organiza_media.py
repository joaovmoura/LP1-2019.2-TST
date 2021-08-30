def organiza_por_media(lista):
    soma=0
    listaret = list()
    if not lista: return listaret
    def passa_pra_frente(l, ind,c):
        aux=0
        ok=False
        num=l[ind]
        while not ok:
            for i in range(c, ind):
                aux = l[i]
                l[i] = l[i+1]
                l[i+1] = aux
            if l[c]==num: ok=True
    for e in lista:
        soma+=e

    media=soma/len(lista)
#   print(media)
    n=0
    for i in range(len(lista)):
        e=lista[i]
        if e<=media:
            passa_pra_frente(lista,i,n)
            n+=1
    for e in lista:
        listaret.append(e)
    return listaret

#p1 = [float(num) for num in input().split()]
#print(organiza_por_media(p1))
