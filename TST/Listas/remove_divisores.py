def remove_divisores_k(lista, k, n):
    div = 0
    c = len(lista)-1
    def tiradalista(l,ind):
        for i in range(ind, len(l)-1):
            l[i],l[i+1]=l[i+1],l[i]
        lista.pop()
    while True:
        if div==n or c==-1: break
        e=lista[c]
        if k%e==0:
            div+=1
            tiradalista(lista, c)
        c-=1

