__author__ = 'Fossum'


class Employee:
    def __int__(self):
        self.ss = None
    pass


class InvalidSocial(ValueError):
    pass


def validatess(employee_class):
    try:
        aaa, gg, ssss = employee_class.ss.split("-")
        try:
            int(aaa)
            int(gg)
            int(ssss)
        except ValueError:
            raise InvalidSocial ("One or more classes were not integers.")
        if int(aaa) == 0 or int(gg) == 0 or int(ssss) == 0:
            raise InvalidSocial ("One or more classes were all zero.")
        elif int(aaa) == 666 or int(aaa) in range(900, 1000):
            raise InvalidSocial ("First class in invalid.")
        elif int(aaa) == 78 and int(gg) == 5 and int(ssss) == 1120:
            raise InvalidSocial ("That is not a real SS#.")
        elif len(aaa) != 3 or len(gg) != 2 or len(ssss) != 4:
            raise InvalidSocial ("One or more classes are not the correct length.")
        else:
            pass
    except IndexError:
        raise InvalidSocial ("Social was not entered as aaa-gg-ssss.")


def getsocial(employee_class):
    employee_class.ss = input("Please enter your Social Security Number: ")
    try:
        validatess(employee_class)
    except InvalidSocial:
        print("Invalid Social Security Number, please try again\n")
        getsocial(employee_class)

emp = Employee()
getsocial(emp)
print(emp.ss)
