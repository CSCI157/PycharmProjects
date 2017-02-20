__author__ = 'Fossum'


def fifth():
    a = input("Please enter a string: ")
    if len(a) >= 5:
        b = a[4]
    else:
        b = "None. This string has fewer than five elements."
    return b

print(fifth())