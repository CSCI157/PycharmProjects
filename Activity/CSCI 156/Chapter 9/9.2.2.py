__author__ = 'Fossum'


def loop(n):
    b = ""
    c = input("Please enter a string: ")
    while c != "q" and c != "Q":
        b += c + "\n"
        c = input("Please enter a string or enter 'q' or 'Q' to quit: ")
    n.write(b)


def upper(m):
    m.seek(0)
    f = ""
    for line in e:
        print(line.upper().strip('\r\n'))


with open('9.2.2.txt', 'w+', encoding='utf-8') as a:
    print(a.name)
    loop(a)
with open('9.2.2.txt', 'r+', encoding='utf-8') as e:
    print("\n")
    print(e.name)
    upper(e)