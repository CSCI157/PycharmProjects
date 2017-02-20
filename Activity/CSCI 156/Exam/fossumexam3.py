__author__ = 'Fossum'


employees = dict()


def employeeinput(dictionary):
    name = input("Please enter the employees name (first last): ")
    tuple1 = name.split(" ")
    tuple2 = tuple1[1], tuple1[0]
    wage = float(input("Please enter the employees hourly wage: "))
    startyear = int(input("Please enter the year the employee started: "))
    address = input("Please enter the employee's street address: ")
    town = input("Please enter the employee's town: ")
    state = input("Please enter the employee's state. (Ex. New York = NY): ")
    zipcode = int(input("Please enter the employee's zip code: "))
    dictionary[tuple2] = [wage, startyear, address, town, state, zipcode]


def employeedelete(dictionary):
    name = input("Please enter the employees name (first last): ")
    tuple1 = name.split(" ")
    tuple2 = tuple1[1], tuple1[0]
    try:
        del dictionary[tuple2]
    except KeyError:
        print("Please enter a valid name.")
        return employeedelete(dictionary)


def employeeprint():
    name = input("Please enter the employees name (first last): ")
    tuple1 = name.split(" ")
    tuple2 = tuple1[1], tuple1[0]
    employeeprint1(tuple2)


def employeeprint1(arg):
    key = arg
    print(str(key[1]) + " " + str(key[0]))
    try:
        print("    Makes $" + str(employees[key][0]) + " per hour and started working for the company in " +
              str(employees[key][1]) + ".")
        print("    Lives at:")
        print("        " + str(employees[key][2]))
        print("        " + str(employees[key][3]) + ", " + str(employees[key][4]) + " " + str(employees[key][5]))
    except KeyError:
        print("Please enter a valid name.")
        return employeeprint()


def employeeprintall(dictionary):
    for key in dictionary:
        employeeprint1(key)


def options():
    menu = ("1. Input an employee.", "2. Delete an employee.", "3. Print out all of the employees.", "4. Quit.")
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
while selection != 4:
    selection = options()
    if selection == 1:
        employeeinput(employees)
    elif selection == 2:
        employeedelete(employees)
    elif selection == 3:
        employeeprintall(employees)

employeeprint()
