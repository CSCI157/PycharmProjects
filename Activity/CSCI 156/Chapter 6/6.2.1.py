__author__ = 'Fossum'


def fact(m):
    factorial = 1
    for integer in range(1, m+1):
        factorial *= integer
    return factorial


def nchoosek(n,k):
    return fact(n)//(fact(k)*fact(n-k))


def foil(n):
    string = "(x+y)^" + str(n) + " = "
    for i in range(n+1):
        if i == 0:
            string += str(nchoosek(n, i)) + "*x^" + str(n-(1*i)) + " + "
        elif i != n:
            string += str(nchoosek(n, i)) + "*x^" + str(n-(1*i)) + "*y^" + str(i) + " + "
        else:
            string += str(nchoosek(n, i)) + "*y^" + str(i)
    return string

print(foil(3))