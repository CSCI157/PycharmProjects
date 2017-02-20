__author__ = 'Fossum'


def less(m, n):
    x = ""
    for i in reversed(range(m, n)):
        x = x + str(i) + ","
    print(x)

less(5, 9)
