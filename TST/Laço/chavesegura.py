palavra = input()

verificado =  False

m='Chave'

vogal = 0 
consec = 1

while not verificado:

    for e in palavra:
        if e in 'aeiouAEIOU':
            vogal+=1

        
    for i in range(0, len(palavra) - 2):
        if palavra[i] == palavra[i+1]:
                consec += 1

    verificado=True

    if consec>=3:
        m += ' insegura. 3 caracteres consecutivos iguais.'
    elif vogal>5:
        m += ' insegura. 6 vogais.'
    else:
        m += ' segura!'

print(m)
