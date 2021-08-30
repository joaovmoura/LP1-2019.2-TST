def divisor(num, lista):
    for i in range(len(lista)):
        e = lista[i]
        if e%num==0:
            return i

    return -1
