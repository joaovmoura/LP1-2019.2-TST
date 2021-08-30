import math

velocidade = float(input())
diam = float(input())
secao = math.pi * (diam/ 2) ** 2
vazao = velocidade*secao*1000
tempo = int(input())
quant_agua = tempo * vazao

print("Quantidade de água = {:.2f} litros.".format(quant_agua))
