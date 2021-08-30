polinomios=[]
aplicacoes=[]
qtdaplic = []
ap=0
while True:
    entrada = input()

    if entrada=='fim': break
    if entrada[0]=='p' and entrada[1]==':':
        if ap!=0:
            qtdaplic.append(ap)
            ap=0
        polinomios.append(entrada)

    else:
        aplicacoes.append(entrada)
        ap+=1
if ap!=0: qtdaplic.append(ap)
#print(ap)
#print(qtdaplic)
k=0
for c in range(len(polinomios)):
    print('novo polinomio')
    e=polinomios[c]
    result = 0
    pol = e.split(' ')
    for j in range(qtdaplic[c]):
        for i in range(1, len(pol)):
            coef = pol[i]
            #print(coef, aplicacoes[k], i-1)
            result+=int(coef)*int(aplicacoes[k])**(i-1)
        k+=1
        print(result)
        result = 0
