def filtra_alunos(alunos, inscritos, media):
	indices = []
	k=0
	def novo_in(lista, e):
		for el in lista:
			if el == e:
				return True
		return False
	def remove_elementos(lista, indices):
		for i in range(len(indices)):
			for j in range(indices[i], len(lista)-1):
				lista[j], lista[j+1] = lista[j+1], lista[j]
			lista.pop()
	for i in range(len(alunos)):
		if not novo_in(inscritos, alunos[i][0]):
			indices.append(i-k)
			k+=1
		elif alunos[i][1]<media:
			indices.append(i-k)
			k+=1
	remove_elementos(alunos, indices)
	return k

inscritos = [121, 123, 124]
alunos = [ (120,8.0), (121,7.5), (122,5.0), (123,6.0), (124,9.0), (125,4.0) ]
#print(filtra_alunos(alunos, inscritos, 7.0))
#print(alunos)
