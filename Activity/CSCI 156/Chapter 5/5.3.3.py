__author__ = 'Fossum'

global a
global b
global c
global d
global e


def init():
    global a
    global b
    global c
    global d
    global e
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0


def get_name():
    global a
    a = input("Please enter the employee's name: ")


def get_salary():
    global b
    b = input("Please enter the employee's' salary: ")


def get_bday():
    global c
    c = input("Please enter the employee's birthday (mm/dd/yyyy): ")


def get_menu_choice():
    global d
    d = input("\nPlease select an input option: ")


init()
print("A. Input an employee's name \nB. Input a salary")
print("C. Input a date of birth \nD. Exit")
while e == 0:
    get_menu_choice()
    if d == "A":
        get_name()
    elif d == "B":
        get_salary()
    elif d == "C":
        get_bday()
    elif d == "D":
        e = 1
    else:
        print("\nA. Input an employee's name \nB. Input a salary")
        print("C. Input a date of birth \nD. Exit")
        print("\nPlease enter 'A', 'B', 'C', or 'D'.")
