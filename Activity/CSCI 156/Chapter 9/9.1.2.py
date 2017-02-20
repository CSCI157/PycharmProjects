__author__ = 'Fossum'

a = open('9.1.2.txt', 'w+', encoding='utf-8')
print(a.name)
global d


def init():
    global d
    d = 0


def loop():
    global d
    b = ""
    c = input("Please enter a string: ")
    d = 0
    while c != "q" and c != "Q":
        b += c + "\n"
        d += 1
        c = input("Please enter a string or enter 'q' or 'Q' to quit: ")
    print(d)
    print("")
    return b
init()
a.write(loop())
a.close()

a = open('9.1.2.txt', 'r', encoding='utf-8')
print(a.name)
for i in range(d+1):
    print(a.readline().rstrip('\r\n'))
a.close()
