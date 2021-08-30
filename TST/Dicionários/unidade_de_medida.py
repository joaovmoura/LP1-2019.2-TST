medidas = {'km':1000, 'hm':100, 'dam':10, 'm':1, 'dm':0.1,'cm':0.01, 'mm':0.001}
somas = []
while True:
    n = input()
    n = n.split()
    soma = (int(n[0])*medidas[n[1]])+(int(n[2])*medidas[n[3]])
    if soma==0: break
    somas.append(soma)

for e in somas:
    print('{:.2f} m'.format(e))
