import random
__author__ = 'Fossum'

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    a[i] += random.randrange(1, 100)
print(a)

for j in range(10):
    for k in range(9):
        b = int(a[k])
        c = int(a[k+1])
        #print(b)
        #print(c)
        if b > c:
            a[k] = c
            a[k+1] = b
        print(a)
