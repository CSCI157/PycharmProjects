__author__ = 'Fossum'

global email
email = input("Please enter an email: ")


def validemail():
    global email
    try:
        tuple1 = email.split("@")
        tuple2 = tuple1[1].split(".")
        username, domain, gTLD = tuple1[0], tuple2[0], tuple2[1]
    except IndexError:
        print("You must enter a valid email.")
        email = input("Please enter an email: ")
        return validemail()
    if str(gTLD) in ("com", "gov", "edu", "org", "mil", "net"):
        print((username, domain, gTLD))
    else:
        print("gTLD Error")
        print("You must enter a valid email.")
        email = input("Please enter an email: ")
        return validemail()

validemail()
