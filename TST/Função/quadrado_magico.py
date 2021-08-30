def eh_quadrado_magico(quadrado):
	if len(quadrado)!=len(quadrado[0]): return False
	somas = []
	elementos = []
	linha = coluna = principal = secundaria = 0
	for i in range(len(quadrado)):
		linha=0
		coluna = 0
		for j in range(len(quadrado[0])):
			elementos.append(quadrado[i][j])
			linha+=quadrado[i][j]
			coluna+=quadrado[j][i]
			if i==j:
				principal+=quadrado[i][j]
			if i+j == len(quadrado)-1:
				secundaria+=quadrado[i][j]
		somas.append(linha)
		somas.append(coluna)

	for i in range(len(somas)-1):
		if somas[i]!=somas[i+1]:return False
	
	for i in range(len(elementos)):
		for j in range(1,len(elementos)):
			if i!=j and elementos[i]==elementos[j]:
				return False
	return True

quadrado1 = [[2,7,6],[9,5,1],[4,3,8]]
quadrado2 = [[1,2,3],[4,5,6]]
assert eh_quadrado_magico(quadrado1)
assert not eh_quadrado_magico(quadrado2)
