__author__ = 'Fossum'

a = open('9.1.1.txt', 'w+', encoding='utf-8')
print(a.name)


def loop():
    b = ""
    c = input()
    while c != "q" and c != "Q":
        b += c + "\n"
        c = input()
    return b
a.write(loop())
a.close()
