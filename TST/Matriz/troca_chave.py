def troca_chave(dic):
    inverso = {}
    valores = []
    chaves = []
    for v,k in dic.items():
        valores.append(v)
        chaves.append(k)
    for i in range(len(chaves)):
        inverso[chaves[i]] = valores[i]
    return inverso
assert troca_chave({1:2, 2:3, 3:4}) == {2:1, 3:2, 4:3}
