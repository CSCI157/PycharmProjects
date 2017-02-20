__author__ = 'Fossum'


def exits(m):
    b = 0
    c = 0
    while b < m:
        c += 1
        b += c*c
    b -= c*c
    c -= 1
    return c, b

print(exits(18))