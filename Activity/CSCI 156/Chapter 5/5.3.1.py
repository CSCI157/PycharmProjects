__author__ = 'Fossum'

a = input("Please enter a knock knock intro. :")
b = input("Please enter a knock knock punch line. :")

def setup(x, y):
    print(x + ".\n" + x, "who?")
    print(x + y + "." + "\n")


def knockknockintro():
    print("")
    print("Knock, Knock")
    print("Who's there?")


def knockknock(intro, punchline):
    knockknockintro()
    setup(intro, punchline)

knockknock(a, b)
