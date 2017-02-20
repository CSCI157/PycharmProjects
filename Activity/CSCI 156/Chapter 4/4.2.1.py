__author__ = 'Fossum'


def less(n):
    x = ""
    for i in reversed(range(1, n)):
        x = x + str(i) + ","
    print(x)

less(9)
