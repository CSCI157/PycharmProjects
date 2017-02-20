__author__ = 'Fossum'


def code():
    a = input("Please enter a string you would like the code of: ")
    for i in range(len(a)):
        b = str(ord(a[i]))
        print("Character #" + str(i) + " has the ASCII/UTF-8 code of " + b)


code()
