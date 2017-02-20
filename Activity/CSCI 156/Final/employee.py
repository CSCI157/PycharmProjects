from Final.socialsecurity import *

__author__ = 'Fossum'


class Employees:
    def __init__(self, last=None, first=None, start=None, pay_rate=None, social=None):
        if first is None:
            self.first = input("Please enter the employee's first name: ")
            self.last = input("Please enter the employee's last name: ")
            self.start = input("Please enter the employee's start date (MM/DD/YYYY): ")
            self.pay_rate = input("Please enter the employee's pay rate per hour (xx.xx): ")
            self.social = SS()
        else:
            self.first = first
            self.last = last
            self.start = start
            self.pay_rate = pay_rate
            self.social = social

    def __str__(self):
        header = str(self.first) + " " + str(self.last) + " has the following information:\n    Date started: " + \
                 str(self.start) + "\n    Gets paid: $" + str(self.pay_rate) + "\n    Social Security Number: " + \
                 str(self.social)
        return header
