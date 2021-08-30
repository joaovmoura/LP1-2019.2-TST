palavra = str(input())
n = int(input())

for i in range(n):
    palavra_teste = input()
    for j in range(2,len(palavra_teste)):
        if palavra_teste[j-2] == palavra[0] and palavra_teste[j-1]==palavra[1] and palavra_teste[j]==palavra[2]:
            print("{}".format(palavra_teste))

