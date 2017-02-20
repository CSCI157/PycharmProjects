__author__ = 'Fossum'


def corners(m, n):
    a = "+"
    b = "-"
    x = "+" + (b*n + a)*m
    return x

print(corners(3, 2))

