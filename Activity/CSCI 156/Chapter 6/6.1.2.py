__author__ = 'Fossum'


def vertical(m, n):
    a = "|"
    b = " "
    y = "|" + (b*n + a)*m
    return y

print(vertical(3, 2))
