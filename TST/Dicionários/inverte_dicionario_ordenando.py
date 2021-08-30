def inverte_dicionario(dicionario):
    novodicionario = dict()
    for k,v in dicionario.items():
        if v not in novodicionario.keys():
            novodicionario[v] = [k]
        else:
            novodicionario[v].append(k)
            for i in range(len(novodicionario[v])-1, 0, -1):
                troca = False
                if ord(novodicionario[v][i].lower())<ord((novodicionario[v][i-1]).lower()):
                    novodicionario[v][i], novodicionario[v][i-1] = novodicionario[v][i-1], novodicionario[v][i]
                    troca = True
                if not troca:break
    return novodicionario
m = {"a": 2, "b": 3, "c": 2}
