__author__ = 'Fossum'


def reverse():
    a = input("Please enter a string you would like to reverse: ")
    b = ""
    for i in range(len(a)):
            b += a[len(a)-i-1]
    print(b)

reverse()