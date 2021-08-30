def caixa_alta(frase):
	caracteres = ''
	frase = ' ' + frase + ' '

	for i in range(1 , len(frase) - 1):

		if frase[i - 1] == ' ' and frase[i + 1] == ' ':
			caracteres += frase[i].lower()

		elif frase[i - 1] == ' ' and frase[i + 1] != ' ':
			caracteres += frase[i].upper()

		elif frase[i - 1] != ' ' or frase[i + 1] == ' ':

			caracteres += frase[i]

	return caracteres
