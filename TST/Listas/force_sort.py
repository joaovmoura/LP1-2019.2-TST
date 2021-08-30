def force_sort(seq):
    diferencas = []
    originais = []
    for e in seq:
        originais.append(e)
    for i in range(len(seq)-1):
        elemento = seq[i]
        proximo = seq[i+1]
        if elemento > proximo:
            seq[i+1]=seq[i]
    for e, el in zip(seq, originais):
        diferencas.append(e-el)
    return diferencas

