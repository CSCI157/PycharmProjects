__author__ = 'Fossum'
# a will = m
# b will = n


global a
global b


def init():
    global a
    global b
    a = 0
    b = 0


def divides(m, n):
    y = 0
    z = 0
    for i in range(1, n+1):
        x = i * m
        if x == n:
            y = 1
        else:
            z += 1
    if y == 1:
        print(m, "divides", n)
    elif m == 0:
        print("I'm sorry. You cannot divide by zero.")
    else:
        print("I'm sorry,", m, "does not divide", n)


def get_numbers():
    global a
    global b
    b = int(input("Please enter the number you want to divide: "))
    a = int(input("Please enter the number you want your previous number divided by: "))

init()
get_numbers()
divides(a, b)
