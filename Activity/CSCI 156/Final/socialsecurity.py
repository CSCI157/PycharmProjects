__author__ = 'Fossum'


class SS:
    class InvalidSocial(Exception):
        pass

    def __init__(self):
        self.social = self.get_social()

    def validate_ss(self, s):
        try:
            aaa, gg, ssss = s.split("-")
            try:
                int(aaa)
                int(gg)
                int(ssss)
            except ValueError:
                raise self.InvalidSocial("One or more classes were not integers.")
            if int(aaa) == 0 or int(gg) == 0 or int(ssss) == 0:
                raise self.InvalidSocial("One or more classes were all zero.")
            elif int(aaa) == 666 or int(aaa) in range(900, 1000):
                raise self.InvalidSocial("First class in invalid.")
            elif int(aaa) == 78 and int(gg) == 5 and int(ssss) == 1120:
                raise self.InvalidSocial("That is not a real SS#.")
            elif len(aaa) != 3 or len(gg) != 2 or len(ssss) != 4:
                raise self.InvalidSocial("One or more classes are not the correct length.")
            else:
                pass
        except IndexError:
            raise self.InvalidSocial("Social was not entered as aaa-gg-ssss.")

    def get_social(self):
        ss = input("Please enter the employee's SSN (xxx-xx-xxxx): ")
        try:
            self.validate_ss(ss)
        except self.InvalidSocial:
            print("Invalid Social Security Number, please try again\n")
            ss = self.get_social()
        return ss

    def __str__(self):
        return self.social
