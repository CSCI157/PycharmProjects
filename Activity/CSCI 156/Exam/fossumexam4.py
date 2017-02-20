__author__ = 'Fossum'


class Parent:
    def __init__(self, first=None, last=None, age=None):
        if first is None:
            self.first = input("Please enter the parent's first name: ")
        else:
            self.first = first
        if last is None:
            self.last = input("Please enter the parent's last name: ")
        else:
            self.last = last
        if age is None:
            self.age = input("Please enter the age of the parent: ")
        else:
            self.age = age
        self.children = []

    def __str__(self):
        header = self.first + " " + self.last + " is " + str(self.age) + " years old and has " +\
                 str(len(self.children)) + " child/children:\n"
        for nchild in range(len(self.children)):
            line = str(self.children[nchild][1]) + " who is " + str(self.children[nchild][2]) + "\n"
            header += line
        return header

    def add_child(self, child=None):
        if child is None:
            self.children.append((input("Please enter the child'd last name: "),
                                  input("Please enter the child's first name: "),
                                  input("Please enter the child's age: ")))
        else:
            self.children.append(child)

JF = Parent('Justin', 'Fossum', 21)
JF.add_child(('Fossum', 'Jane', 1))
print(JF)
