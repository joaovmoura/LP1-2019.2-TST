n = int(input())
times = []
pontuação = []
posição = []
for i in range(n):
    times.append(input())
    pontuação.append(input())
    posição.append(i+1) 
for i in range(1,n):
    if pontuação[i] == pontuação[i-1]:
        posição[i]=posição[i-1]
for i in range(n):
    print('{}. {} ({})'.format(posição[i], times[i], pontuação[i]))
