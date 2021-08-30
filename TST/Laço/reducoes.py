def reducoes(seq):
    lista = []
    if len(seq)==1 or not seq:
        return lista
    for i in range(len(seq)-1):
        e = seq[i]
        p = seq[i+1]
        calculo = (e-p) if (e-p)>0 else 0
        lista.append(calculo)
    return lista
