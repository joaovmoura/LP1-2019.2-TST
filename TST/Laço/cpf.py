
def calcula_digitos_verificacao(cpf):
    cpf=str(cpf)
    soma=0
    m=2
    for i in range(8,-1,-1):
        soma+=(int(cpf[i])*(m))
        m+=1
    digito1 = 10*soma%11 if 10*soma%11!= 10 else 0
    cpf += str(digito1)
    m=2
    soma=0
    for i in range(9,-1,-1):
        soma+=(int(cpf[i])*(m))
        m+=1
    digito2 = 10*soma%11 if 10*soma%11!= 10 else 0

    final = str(digito1)+str(digito2)
    return final 
