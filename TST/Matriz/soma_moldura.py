def soma_moldura(m, k):
	soma = 0
	ultimal = len(m)-1
	ultimac = len(m[0]) -1
	for i in range(len(m)):
		for j in range(len(m[0])):
			if (i==k or i==ultimal-k) and k<=j<=ultimac-k:
				soma+=m[i][j]
			elif (k<i<ultimal-k) and (j==k or j==ultimac-k):
				soma+=m[i][j]
	return soma
M = [[1,  2,  3,  4 ], [5,  6,  7,  8 ], [9,  10, 11, 12],[14, 15, 16, 17]]
#print(soma_moldura(M, 0))
#print(soma_moldura(M, 1))
