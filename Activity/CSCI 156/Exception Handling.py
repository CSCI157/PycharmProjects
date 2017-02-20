__author__ = 'Fossum'


def validss():
    ssn = input("Please input your social security number: ")
    try:
        aaa, gg, ssss = ssn.split("-")
        try:
            int(aaa)
            int(gg)
            int(ssss)
        except ValueError:
            print("You must enter a valid social security number.\nIntError")
            return None
        if int(aaa) == 000:
            print("You must enter a valid social security number.\nZeroError")
            return None
        elif int(gg) == 00:
            print("You must enter a valid social security number.\nZeroError")
            return None
        elif int(ssss) == 0000:
            print("You must enter a valid social security number.\nZeroError")
            return None
        elif int(aaa) == 666 or int(aaa) in range(900, 1000):
            print("You must enter a valid social security number.\nFirstGError")
            return None
        elif int(aaa) == 78 and int(gg) == 5 and int(ssss) == 1120:
            print("You must enter a valid social security number.\nAdCampError")
            return None
        else:
            ssnt = aaa, gg, ssss
            print(ssnt)
    except IndexError:
        print("You must enter a valid social security number.\nIndexError")
        return None


def validss2():
    ssn = input("Please input your social security number: ")
    try:
        aaa, gg, ssss = ssn.split("-")
        try:
            int(aaa)
            int(gg)
            int(ssss)
        except ValueError:
            print("You must enter a valid social security number.\nIntError")
            return validss2()
        if int(aaa) == 000:
            print("You must enter a valid social security number.\nZeroError")
            return validss2()
        elif int(gg) == 00:
            print("You must enter a valid social security number.\nZeroError")
            return validss2()
        elif int(ssss) == 0000:
            print("You must enter a valid social security number.\nZeroError")
            return validss2()
        elif int(aaa) == 666 or int(aaa) in range(900, 1000):
            print("You must enter a valid social security number.\nFirstGError")
            return validss2()
        elif int(aaa) == 78 and int(gg) == 5 and int(ssss) == 1120:
            print("You must enter a valid social security number.\nAdCampError")
            return validss2()
        else:
            ssnt = aaa, gg, ssss
            print(ssnt)
    except IndexError:
        print("You must enter a valid social security number.\nIndexError")
        return validss2()

validss()