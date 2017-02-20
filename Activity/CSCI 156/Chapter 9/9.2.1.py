__author__ = 'Fossum'


def loop(n):
    b = ""
    c = input("Please enter a string: ")
    while c != "q" and c != "Q":
        b += c + "\n"
        c = input("Please enter a string or enter 'q' or 'Q' to quit: ")
    n.write(b)


with open('9.2.1.txt', 'w+', encoding='utf-8') as a:
    print(a.name)
    loop(a)
