def zera_acima_ou_abaixo(m):

	def zera(mat, zeros):
		for i in range(len(mat)):
			for j in range(len(mat[0])):
				if (zeros=='cima' or zeros =='tudo') and i<j:
						mat[i][j] = 0
				elif (zeros=='baixo' or zeros =='tudo') and i>j:
						mat[i][j] = 0
	soma_acima=soma_abaixo=0
	for i in range(len(m)):
		for j in range(len(m[0])):
			if i>j:
				soma_abaixo += m[i][j]
			elif j>i:
				soma_acima += m[i][j]
	if soma_acima>soma_abaixo:
		zera(m, 'cima')
	elif soma_acima<soma_abaixo:
		zera(m, 'baixo')
	else:
		zera(m, 'tudo')

