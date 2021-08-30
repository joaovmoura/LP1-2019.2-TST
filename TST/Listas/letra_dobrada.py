n = int(input())
palavras = []
palavra_dobrada = []
palavra_n_dobrada = []

for i in range(n):
    ja_escrita = False
    tem_duplicada=False
    palavras.append(str(input()))
    p_aux = palavras[i]
    for j in range(1,len(p_aux)):
        if p_aux[j] == p_aux[j-1] and not ja_escrita:
            palavra_dobrada.append(p_aux)
            tem_duplicada=True
            ja_escrita= True
    if not tem_duplicada:
        palavra_n_dobrada.append(p_aux)

qtd_pal_dobr = len(palavra_dobrada)
sem_letra_dobrada = len(palavra_n_dobrada)


print('%d palavra(s) com letras dobradas:' % qtd_pal_dobr)

for i in range(qtd_pal_dobr):
    print(palavra_dobrada[i])


print('---')
print('%d palavra(s) sem letras dobradas:' %sem_letra_dobrada)

for i in range(sem_letra_dobrada):
    print(palavra_n_dobrada[i])
