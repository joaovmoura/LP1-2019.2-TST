def numero_disciplinas(m1, m2, pagas):
    pode_pagar=0
    hor = []
    def meu_in1(lista, elemento):
        for e in lista:
            if e==elemento: return True
        return False
    def meu_in2(lista1, lista2):
        c=0
        for e in lista2:
            for el in lista1:
                if e==el:c+=1
        if c==len(lista2):return True
        return False
    for k,v in m1.items():
        if not meu_in1(pagas, k) and meu_in2(pagas, v) and not meu_in1(hor, m2[k]):
            hor.append(m2[k])
            pode_pagar+=1
    return pode_pagar

grade = {"p1": [], "lp1": [], "ic": [],"calc1": [], "p2": ["ic", "p1", "lp1"],
"lp2": ["ic", "p1", "lp1"], "grafos": ["ic", "p1", "lp1"], "calc2"  : ["calc1"],
"edados": ["ic", "p1", "lp1", "p2", "lp2", "grafos"],
"leda": ["ic", "p1", "lp1", "p2", "lp2", "grafos"]}

horarios= {"p1": "s082", "lp1": "x082", "ic": "i142", "calc1": "q082", "p2": "t162",
"lp2": "s082", "grafos": "q082", "calc2": "x162", "edados": "x162", "leda": "t102"}

