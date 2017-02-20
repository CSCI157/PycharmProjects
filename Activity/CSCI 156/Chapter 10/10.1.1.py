__author__ = 'Fossum'


m = [2, 4, 6, 8]
print(m[1])

fivem = [0, 0, 0, 0]
for i in range(len(m)):
    fivem[i] = m[i]*5
print(fivem)

m.insert(len(m), 10)
print(m)

m.insert(m.index(8), 6)
print(m)

print(m.index(8))

m.remove(8)
print(m)
