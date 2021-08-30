def disciplinas(aloc, prof):
	def meuin(lista, elemento):
		for e in lista:
			if e == elemento: return True
		return False
	creditos = 0
	discip = []
	
	for k,v in aloc.items():
		for e in v:
			if e == prof:
					creditos+=k[1]
					if not discip: 
						discip.append(k[0])
					elif not meuin(discip, k[0]):
						discip.append(k[0])
						
	return (discip, creditos)

alocacao = {("P1", 4): ['Jorge', 'Dalton','Wilkerson'],
         ("LP1", 4): ['Jorge', 'Dalton', 'Eliane', 'Wilkerson'],
         ("EVOL", 2): ['Dalton'],
         ("IC", 4): ['Eliane', 'Joseana'],
         ("P2", 4): ['Livia', 'Raquel', 'Nazareno'],
         ("GRAFOS", 2): ['Patricia', 'Patricia']}
'''
(disciplinas(alocacao, "Dalton"))
(disciplinas(alocacao, "Eliane"))
(disciplinas(alocacao, "Patricia"))'''
