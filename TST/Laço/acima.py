med = float(input())
s = 0
qtd=[]
elementos = []
while True:
    nums = input()
    soma=0
    if nums == 'fim':break
    nums = nums.split()
    nums = [int(e) for e in nums]
    for e in nums:
        soma+=e
    media = soma/len(nums)
    if media<med/2:break
    if media>med:
        qtd.append(len(nums))
        for e in nums:
            elementos.append(e)



for n in qtd:
    for i in range(s,s+n):
        if i != s+n-1:
            print(elementos[i], end = ' ')
        else:
            print(elementos[i])
    s+=n
