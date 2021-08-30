def quantidade_usuarios(cadastros):
    c = 0
    for v in cadastros.values():
        for e in v:
            if e!='administrador': c+=1
    return c
