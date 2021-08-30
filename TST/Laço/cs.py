chave = input()

vogais = 0
ultimo = chave[0]
consec = 0
printou = False
for char in chave:
    if char in 'AEIOUaeiou': vogais += 1
    
    if char == ultimo: consec += 1
    else:
        ultimo = char
        consec = 1

    if consec == 3:
        print('Chave insegura. 3 caracteres consecutivos iguais.')
        printou = True
        break

    if vogais > 5 and consec == 1:
        print('Chave insegura. 6 vogais.')
        printou = True
        break

if not printou: print('Chave segura!')
