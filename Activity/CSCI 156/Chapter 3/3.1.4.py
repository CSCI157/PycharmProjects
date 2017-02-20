__author__ = 'Fossum'


def spacer(a):
    print(a*"-"+"\n")


def setup(x, y):
    print(x + ".\n" + x, "who?")
    print(x + y + "\n")


def knockknockintro():
    print("Knock, Knock")
    print("Who's there?")


def knockknock(intro, punchline):
    knockknockintro()
    setup(intro, punchline)


knockknock("Canoe", " Canoe help me with my homework?")
spacer(20)
knockknock("Iva", " Iva got to come up with a better knock knock joke.")
