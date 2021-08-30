conta = (input())
soma=0
for i in range(5):
    soma += int(conta[i])
digito = soma%11

print("{:5}-{:02}".format(conta, digito))
