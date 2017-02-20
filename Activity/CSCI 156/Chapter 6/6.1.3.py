__author__ = 'Fossum'


def corners(m, n):
    a = "+"
    b = "-"
    x = "+" + (b*n + a)*m + "\n"
    return x


def vertical(m, n):
    a = "|"
    b = " "
    y = "|" + (b*n + a)*m + "\n"
    return y


def box(m, n, o, p):
    z = corners(m, n) + (vertical(m, n)*p + corners(m, n))*o
    return z

print(box(2, 2, 2, 2))
