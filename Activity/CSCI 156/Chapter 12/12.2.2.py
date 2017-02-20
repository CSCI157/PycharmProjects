__author__ = 'Fossum'


def mean(*args):
    a = 0
    for i in range(len(args)):
        a += args[i]
    b = a/len(args)
    return b

print(mean(1, 2))
