x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

l1 = ((x1-x2)**2 + (y1-y2)**2)**0.5
l2 = ((x1-x3)**2 + (y1-y3)**2)**0.5
l3 = ((x3-x2)**2 + (y3-y2)**2)**0.5

p = l1+l2+l3

print('O perímetro é de %.2f' % p)
