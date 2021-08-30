def caixa_alta(frase):
	string=frase
	auxiliar=''
	fraseaux=''
	proximo = None
	for i in range(len(string)):
		e = string[i]
		if i<len(string)-1:proximo = string[i+1]
		if len(string)==1:
			fraseaux+=e.lower()
		elif i==0 and proximo ==' ' and e.isupper():
			fraseaux+=e.lower()
		elif i>0:
			anterior = string[i-1]
			if i==(len(string)-1) and anterior==' ':
				fraseaux+=e.lower()
			elif proximo and proximo==' ' and anterior==' ' and e.isupper():
				fraseaux+=e.lower()
			elif e.islower() and anterior==' ' and proximo!=' ':
				fraseaux+=e.upper()
			else:
				fraseaux+=e
		else:
			fraseaux+=e.upper()
	frase=''
	for i in range(len(fraseaux)):
		frase+=fraseaux[i]
	return frase

