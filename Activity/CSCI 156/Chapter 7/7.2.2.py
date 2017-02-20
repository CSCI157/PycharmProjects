__author__ = 'Fossum'


def sumint(m, n=None):
    if n is None:
        a = 0
        for i in range(1, m+1):
            a += i
    else:
        a = 0
        for i in range(m, n+1):
            a += i
    return a
print(sumint(5, 10))
