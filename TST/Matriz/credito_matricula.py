def num_creditos(bd, matricula):
	def In(lista, elemento):
		for e in lista:
			if e==elemento:return True
		return False
	cred = 0
	for v in bd.values():
		for k, v2 in v.items():
			if In(v2, matricula):
				cred+=k[1]
	return cred

bd_ufcg = {"UASC": {("Programação I", 4): ["11624100", "11624400"], ("Programação II", 4): ["11624200"], ("Teoria dos Grafos", 2): ["11624200"]},
           "UAF": {("Física Clássica", 4): ["11624200"], ("Física Moderna", 4): ["11624300", "11624500", "11624600"]},
           "UAM": {("Cálculo I", 4): ["11624100", "11624300"], ("Álgebra Linear", 4): ["11624300"]}
           }

assert num_creditos(bd_ufcg, "11624100") == 8
