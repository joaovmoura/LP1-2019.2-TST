def primeiro_menor(num, numeros):

    for i in range(len(numeros)):
        e=numeros[i]
        if e<num:
            return i
    return -1
def main():
    lista = [int(n) for n in input().split()]
    num = int(input())
    menor = primeiro_menor(num, lista)
    if menor== -1:
        print('sem menores que %d' % num)
    else:
        print('primeiro menor que %d: %d' %(num,lista[menor]))
if __name__ == '__main__':
    main()


