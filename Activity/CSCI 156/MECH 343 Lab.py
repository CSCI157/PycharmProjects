__author__ = 'Fossum'

import math

# n = math.sqrt(4)
# print(n)

global P
global dP
global Y
global dY
global A
global dA
global E
global dE
global I
global dI


def init():
    global P
    global dP
    global Y
    global dY
    global A
    global dA
    global E
    global dE
    global I
    global dI
    P = 0
    dP = 0
    Y = 0
    dY = 0
    A = 0
    dA = 0
    E = 7.4 * 10**10
    dE = 0
    I = 0
    dI = 0


def getp():
    global P
    global dP
    P = float(input("Please enter the force applied in Newtons: "))
    dP = float(input("Please enter the uncertainty in force applied in Newtons: "))


def gety():
    global Y
    global dY
    Y = float(input("Please enter the height of the strain gauge in Meters (1mm = 0.001m): "))
    dY = float(input("Please enter the uncertainty in the strain gauge in Meters (1mm = 0.001m): "))


def geta():
    global A
    global dA
    A = float(input("Please enter the value you found for 'a' in Meters (1mm = 0.001m): "))
    dA = float(input("Please enter the uncertainty in the value you found for a in Meters (1mm = 0.001m): "))


def geti():
    global I
    global dI
    I = float(input("Please enter the inertia in Meters^4: "))
    dI = float((input("Please enter the uncertainty in the inertia Meters^4 (I took care of 10^-8, just enter the number): ")))*10**(-8)


def sigma():
    global P
    global dP
    global Y
    global dY
    global A
    global dA
    global E
    global I
    global dI
    S = math.sqrt((((-A*Y)/(2*E*I))**2)*((dP)**2) + (((-P*Y)/(2*E*I))**2)*((dY)**2) + (((-P*A)/(2*E*I))**2)*((dY)**2) + (((P*A*Y)/(2*E*I))**2)*((dI)**2))
    return S

def run():
    init()
    getp()
    gety()
    geta()
    geti()
    print(sigma())


run()