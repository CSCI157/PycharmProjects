from Final.employee import *

__author__ = 'Fossum'

database = []



def options():
    menu = ("1. Input an employee.", "2. Print out all of the employees.", "3. Quit.")
    end = len(menu)
    inputcommand = "\nYou must input a number from 1 to " + str(end) + ": "
    while True:
        for j in menu:
            print(j)
        choice = input("\nPlease make a choice 1 - " + str(end) + ": ")
        try:
            num = int(choice)
            if 1 <= num <= end:
                return num
            else:
                print(inputcommand)
                print("\n")
                return options()
        except ValueError:
            print(inputcommand)
            print("\n")
            return options()

selection = 0
while selection != 3:
    selection = options()
    if selection == 1:
        new = Employees()
        database.append(new)
        print("\n")
    elif selection == 2:
        print("\n"+"="*45)
        for employee in range(len(database)):
            print(database[employee])
            print("="*45)
        print("\n")
