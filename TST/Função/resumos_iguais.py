def agrupa_resumos_iguais(lista):
	resumos = dict()
	def In(lista, elemento):
		for e in lista:
			if e==elemento:return True
		return False
	for e in lista:
		soma = 0
		num = e
		while num>0:
			soma+=num%10
			num = num//10
		if not In(resumos.keys(), soma): resumos[soma]=[]
		resumos[soma].append(e)
	return resumos

