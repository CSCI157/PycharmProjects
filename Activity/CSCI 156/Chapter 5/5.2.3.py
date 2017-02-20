from random import *
__author__ = 'Fossum'

global lessthan10
global between10n20
global between20n30
global between30n40
global between40n50
global between50n60
global between60n70
global between70n80
global between80n90
global between90n100


def init():
    global lessthan10
    global between10n20
    global between20n30
    global between30n40
    global between40n50
    global between50n60
    global between60n70
    global between70n80
    global between80n90
    global between90n100
    lessthan10 = 0
    between10n20 = 0
    between20n30 = 0
    between30n40 = 0
    between40n50 = 0
    between50n60 = 0
    between60n70 = 0
    between70n80 = 0
    between80n90 = 0
    between90n100 = 0


def show():
    global lessthan10
    global between10n20
    global between20n30
    global between30n40
    global between40n50
    global between50n60
    global between60n70
    global between70n80
    global between80n90
    global between90n100
    print("lessthan10:   ", lessthan10)
    print("between10n20: ", between10n20)
    print("between20n30: ", between20n30)
    print("between30n40: ", between30n40)
    print("between40n50: ", between40n50)
    print("between50n60: ", between50n60)
    print("between60n70: ", between60n70)
    print("between70n80: ", between70n80)
    print("between80n90: ", between80n90)
    print("between90n100:", between90n100)


def histogram(n):
    global lessthan10
    global between10n20
    global between20n30
    global between30n40
    global between40n50
    global between50n60
    global between60n70
    global between70n80
    global between80n90
    global between90n100
    if (n < 10):
        lessthan10 = lessthan10 + 1
    elif (n >= 10) and (n < 20):
        between10n20 = between10n20 + 1
    elif (n >= 20) and (n < 30):
        between20n30 = between20n30 + 1
    elif (n >= 30) and (n < 40):
        between30n40 = between30n40 + 1
    elif (n >= 40) and (n < 50):
        between40n50 = between40n50 + 1
    elif (n >= 50) and (n < 60):
        between50n60 = between50n60 + 1
    elif (n >= 60) and (n < 70):
        between60n70 = between60n70 + 1
    elif (n >= 70) and (n < 80):
        between70n80 = between70n80 + 1
    elif (n >= 80) and (n < 90):
        between80n90 = between80n90 + 1
    elif (n >= 90) and (n < 100):
        between90n100 = between90n100 + 1
    else:
        print("Please enter a number between 0 and 100.")


def rand():
    for i in (range(50)):
        histogram(randrange(1, 100))
init()
rand()
show()
