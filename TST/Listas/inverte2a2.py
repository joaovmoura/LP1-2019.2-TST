def inverte2a2_condicional(seq):
    n = len(seq) if len(seq)%2==0 else len(seq)-1
    for i in range(0,n,2):
        if seq[i]>seq[i+1]:
            seq[i], seq[i+1] = seq[i+1], seq[i]

