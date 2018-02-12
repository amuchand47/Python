'''
import sys


class df:
    def name(self):
        print("My Name Is chand")



ob = df()
ob.name()


'''

'''

import sys


class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("My name is ", self.name)


a = Person("Chand")
a.say_hi()

'''

'''
import sys


class Person:

    ab = "Chand"

    def __init__(self, roll):
        self.roll = roll


a = Person(101)
b = Person(102)

print(a.ab)
print(b.ab)
print(a.roll)
print(Person.ab)

'''



class CSStudent:
    ab = "Computer Science"

    def __init__(self, roll):
        self.add = roll
        self.roll = roll

    def set_add(self, add):
        pass

    def get_add(self):
        return self.add


a = CSStudent(101)
a.set_add("Delhi")
print(a.get_add())
