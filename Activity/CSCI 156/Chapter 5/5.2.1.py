__author__ = 'Fossum'


def room(name):

    if (name >= "a") and (name <= "freeman"):
        print("Mr./Mrs./Ms. " + name + ", thank you for registering. You are in room 121.")
    elif (name > "freeman") and (name <= "michelson"):
        print("Mr./Mrs./Ms. " + name + ", thank you for registering. You are in room 201.")
    elif (name > "michelson") and (name <= "oppenheimer"):
        print("Mr./Mrs./Ms. " + name + ", thank you for registering. You are in room 226.")
    else:
        print("Mr./Mrs./Ms. " + name + ", thank you for registering. You are in room 232.")


room("black")
room("manos")
room("norwood")
room("shapiro")
