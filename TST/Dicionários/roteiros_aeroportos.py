def eh_roteiro(iata, voos, roteiro):
	def In(lista, elemento):
		for e in lista:
			if e==elemento:return True
		return False
	roteiro=[e for e in roteiro.split('/')]
	for i in range(len(roteiro)):
		roteiro[i] = iata[roteiro[i]]
	for k,v in voos.items():
		chave = k
		aeroporto = v
		if chave==roteiro[0]:
			for i in range(1,len(roteiro)):
				if not In(aeroporto, roteiro[i]):
					return False
				else: 
					chave=roteiro[i]
					aeroporto=voos[chave]
			break
	return True

iata = {"Campina Grande": "CPV",
       "Recife": "REC",
       "Salvador": "SSA",
       "Brasilia": "BSB",
       "Sao Paulo": "GRU",
       "Rio de Janeiro": "GIG"}


voos = {"CPV": ["REC", "SSA"],
       "REC": ["CPV", "BSB", "GRU", "GIG"],
       "SSA": ["REC", "GRU", "GIG"],
       "BSB": ["CPV", "GIG", "GRU"],
       "GRU": ["GIG", "BSB"],
       "GIG": ["GRU", "REC"]}
assert eh_roteiro(iata, voos, "Campina Grande/Recife/Rio de Janeiro")
assert eh_roteiro(iata, voos, "Sao Paulo/Rio de Janeiro/Recife/Brasilia")
assert not eh_roteiro(iata, voos, "Recife/Rio de Janeiro/Salvador/Recife")
