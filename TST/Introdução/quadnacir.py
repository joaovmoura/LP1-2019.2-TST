from math import pi
raio = float(input())

lado = 2*raio/2**0.5
areancomum = pi*raio**2 - lado**2
print('Área não comum: %.5f' % areancomum)
