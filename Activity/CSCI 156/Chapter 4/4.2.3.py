__author__ = 'Fossum'


def reverse(m):
    for i in (range(1, m + 1)):
        x = str(i) + "."
        space = ""
        for j in reversed(range(1, i+1)):
            space = space + str(j) + ","
        print(x, space)

reverse(5)
