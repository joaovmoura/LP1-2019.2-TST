n = int(input())
conj = []

for i in range(n):
    conj.append(int(input()))

maior = conj[0]
menor = conj[0]

for i in range(1,n):
    if conj[i] > maior:
        maior = conj[i]
    if conj[i] < menor:
        menor = conj[i]

med = maior/2+menor/2
k=0
c=0
for i in range(n):
    if conj[i]>med:
        k+=1
    if conj[i]<med:
        c+=1
print('Menor número: {}'.format(menor))
print('Maior número: {}' .format(maior))
print('Média dos extremos: {:.2f}' .format(med))
print('{} número(s) abaixo da média' .format(c))
print('{} número(s) acima da média' .format(k))
