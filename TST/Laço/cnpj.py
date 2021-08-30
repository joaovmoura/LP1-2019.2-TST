cnpj =input().strip()
cnpj += '/0001-'
digito = 0
for i in [0,1,3,4,5,7,8,9,11,12,13,14]:
    digito += int(cnpj[i])
cnpj += str('{:02}'.format(digito))

print(cnpj)
