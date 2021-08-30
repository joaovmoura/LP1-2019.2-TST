palavra = input() 
verificado = False 
vogal = 0 
consec = seis = False
for i in range(0, len(palavra) - 2):
    if palavra[i] == palavra[i+1] == palavra[i+2]:
         print('Chave insegura. 3 caracteres consecutivos iguais.')
         consec = True
         break
for e in palavra: 
    if not consec and e in 'aeiou':
         vogal+=1  
    if vogal>5:
         print('Chave insegura. 6 vogais.')
         break 
        
     
if not consec and vogal<6:print('Chave segura!')
        

