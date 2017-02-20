__author__ = 'Fossum'

global a
global b
global c
global d
print("A. Input an employee's name \nB. Input a salary")
print("C. Input a date of birth")


def init():
    global a
    global b
    global c
    global d
    a = 0
    b = 0
    c = 0
    d = 0


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
    d = input("Please select an input option: ")

init()
get_menu_choice()
if d == "A":
    get_name()
elif d == "B":
    get_salary()
elif d == "C":
    get_bday()
else:
    print("Please run again and enter 'A', 'B', or 'C'.")
