k = int(input())
c = 0
while True:
    entrada = input()
    if entrada=='fim':break
    n1,n2 = entrada.split()
    n1 = int(n1)
    n2 = int(n2)
    if n1%k==0 and n2%k==0:
        c+=1

print(c)
