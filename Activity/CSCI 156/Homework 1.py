__author__ = 'Fossum'

global end
global info
global menu
menu = ("1. Input employee first name.", "2. Input employee last name.", "3. Input employee DOB",
        "4. Input employee SS#", "5. Input employee street address.", "6. Input employee city.",
        "7. Input employee zip", "8. Print out employee information.", "9. Quit")
end = len(menu)
info = ["", "", "", "", "", "", ""]

def formatnames(s):
    a = s[0].upper()
    for i in range(1, len(s)):
        a += s[i].lower()
    return a


def firstname():
    global info
    b = input("\nPlease enter the employees first name: ")
    info[0] = formatnames(b.strip())


def lastname():
    global info
    c = input("\nPlease enter the employees last name: ")
    info[1] = formatnames(c.strip())


def dob():
    global info
    validdob = False
    while validdob is False:
        print("\nPlease enter the employee's birthday and all dates should be in the mm/dd/yyyy format")
        d = str(input("Month: "))
        e = str(input("Day: "))
        f = str(input("Year: "))
        if int(d) == 1:
            if 1 <= int(e) <= 31:
                validdob = True
            else:
                print("Pleae enter a valid date.")
        elif int(d) == 2:
            if 1 <= int(e) <= 28:
                validdob = True
            else:
                print("Pleae enter a valid date.")
        elif int(d) == 3:
            if 1 <= int(e) <= 31:
                validdob = True
            else:
                print("Pleae enter a valid date.")
        elif int(d) == 4:
            if 1 <= int(e) <= 30:
                validdob = True
            else:
                print("Pleae enter a valid date.")
        elif int(d) == 5:
            if 1 <= int(e) <= 31:
                validdob = True
            else:
                print("Pleae enter a valid date.")
        elif int(d) == 6:
            if 1 <= int(e) <= 30:
                validdob = True
            else:
                print("Pleae enter a valid date.")
        elif int(d) == 7:
            if 1 <= int(e) <= 31:
                validdob = True
            else:
                print("Pleae enter a valid date.")
        elif int(d) == 8:
            if 1 <= int(e) <= 31:
                validdob = True
            else:
                print("Pleae enter a valid date.")
        elif int(d) == 9:
            if 1 <= int(e) <= 30:
                validdob = True
            else:
                print("Pleae enter a valid date.")
        elif int(d) == 10:
            if 1 <= int(e) <= 31:
                validdob = True
            else:
                print("Pleae enter a valid date.")
        elif int(d) == 11:
            if 1 <= int(e) <= 31:
                validdob = True
            else:
                print("Pleae enter a valid date.")
        elif int(d) == 12:
            if 1 <= int(e) <= 31:
                validdob = True
            else:
                print("Pleae enter a valid day.")
        else:
            print("Please enter a valid month.")
        dobp = d.strip()+"/"+e.strip()+"/"+f.strip()
    info[2] = dobp


def ss():
    global info
    g = input("\nPlease enter the first two (2) digits of the employee's SS#: ")
    h = input("\nPlease enter the next three (3) digits of the employee's SS#: ")
    k = input("\nPlease enter the last four (4) digits of the employee's SS#: ")
    ssn = g.strip()+"-"+h.strip()+"-"+k.strip()
    info[3] = ssn


def street():
    global info
    l = input("\nPlease enter the street name where the employee lives: ")
    m = input("\nPlease enter the house number where the employee lives: ")
    live = m.strip()+" "+l.strip()
    info[4] = live


def city():
    global info
    n = input("\nPlease enter the City the employee lives: ")
    info[5] = n.strip()


def zipcode():
    global info
    o = input("\nPlease enter the employee's zip code: ")
    info[6] = o.strip()


def printinfo():
    global info
    for p in range(len(info)):
        q = p+1
        print(str(q)+". "+str(info[p]))


def oprtions():
    global menu
    global end
    inputcommand = "\nYou must input a number from 1 to " + str(end) + ": "
    while True:
        print("\n")
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
                return oprtions()
        except ValueError:
            print(inputcommand)
            print("\n")
            return oprtions()

selection = 0
while selection != end:
    selection = oprtions()
    if selection == 1:
        firstname()
    elif selection == 2:
        lastname()
    elif selection == 3:
        dob()
    elif selection == 4:
        ss()
    elif selection == 5:
        street()
    elif selection == 6:
        city()
    elif selection == 7:
        zipcode()
    elif selection == 8:
        printinfo()
