__author__ = 'Fossum'


def horizontal(x):
    a = int((x - 3) / 2)
    print("+" + a*"-" + "+" + a*"-" + "+")


def vertical(x):
    b = int((x - 3) / 2)
    print("|" + b*" " + "|" + b*" " + "|")


def box(x):
    horizontal(x)
    vertical(x)
    vertical(x)
    vertical(x)
    vertical(x)
    horizontal(x)
    vertical(x)
    vertical(x)
    vertical(x)
    vertical(x)
    horizontal(x)

box(11)

