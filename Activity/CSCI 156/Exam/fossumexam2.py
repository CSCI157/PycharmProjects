__author__ = 'Fossum'

global a
a = input("Please enter the student's name (First Last): ")
with open('fossumfileexam2.csv', 'w+', encoding='utf-8') as h:
    h.write("")
    h.seek(0)

# def grade is number 1 part A, B, and C
def grade():
    with open('fossumfileexam2.csv', 'a', encoding='utf-8') as g:
        global a
        while a != "q":
            b = input("Please enter the grade of page 1: ")
            c = input("Please enter the grade of page 2: ")
            d = input("Please enter the grade of page 3: ")
            e = input("Please enter the grade of page 4: ")
            f = int(b)+int(c)+int(d)+int(e)
            g.write(str(a.strip()) + "," + str(b) + "," + str(c) + "," + str(d) + "," + str(e) + "," + str(f) + "\n")
            print(str(a.strip()) + "," + str(b) + "," + str(c) + "," + str(d) + "," + str(e) + "," + str(f) + "\n")
            a = input("Please enter the student's name (First Last): ")
            return grade()

# def grades is the bonus
def grades(i):
    with open(i, 'r', encoding='utf-8') as j:
        l = [line.strip('\n').split(",") for line in j]
    print(l)

grade()
grades('fossumfileexam2.csv')
