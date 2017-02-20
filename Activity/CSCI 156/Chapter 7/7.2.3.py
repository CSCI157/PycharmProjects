__author__ = 'Fossum'


def corners(m, n):
    a = " +"
    b = " -"
    x = "+" + (b*m + a) + "\n"
    return x


def vertical(m, n):
    a = " |"
    b = "  "
    y = "|" + (b*m + a) + "\n"
    return y


def box(m, n = None):
    if n is None:
        n = m
        z = corners(m, n) + (vertical(m, n))*n + corners(m, n)
        return z
    else:
        z = corners(m, n) + (vertical(m, n))*n + corners(m, n)
        return z

print(box(5))
