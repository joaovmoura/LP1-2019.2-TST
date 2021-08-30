def busca(seq, valor):
    for i in range(len(seq)):
        e = seq[i]
        if e == valor:
            return i
    return -1
