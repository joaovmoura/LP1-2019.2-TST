p = float(input())
a = float(input())

imc = p/a**2
pi = 24.9*a**2

print('IMC atual = {:.2f}' .format(imc))
print('Peso a ser ganho/perdido = {:.2f}' .format(pi - p))
