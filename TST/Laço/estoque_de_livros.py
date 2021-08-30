def ausentes(estoque):
	zerados = 0
	for v in estoque.values():
		if v==0:zerados+=1
	return zerados
