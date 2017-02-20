__author__ = 'Fossum'


l = [[1, 2], [1, -1], [5, 8], [-4, -2], [4, 3]]
m = []
for i in range(len(l)):
    maxi = max(l[i])
    m.append((maxi, l[i]))
print(m)
m.sort(reverse=True)
print(m)
l1 = []
for maxi, pair in m:
    l1.append(pair)
print(l1)
