def time_campeao(dados):
	campeao = list()
	pontuacao = -1
	for k in dados.keys():
		pontos = dados[k][0]		
		if pontos>=pontuacao:
			if campeao and pontos>pontuacao:
				campeao.pop()
				campeao.append(k)
			else:
				campeao.append(k)
			pontuacao = pontos
	return campeao

dados = {"Botafogo": [59, 43, 39],
    "São Paulo": [52, 44, 36],
    "Palmeiras": [80, 62, 32],
    "Santos": [72, 59, 35]}
print(time_campeao(dados))
