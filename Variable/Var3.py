"""
import sys


def Pt():
    s = "I am in Local Scope"
    print(s)


s = "I am a Global Variable"
Pt()
print(s)


"""

'''
x = "I am in Global"


def Glob():
    global x
    print(x)
    x = "I am local"
    print(x)


Glob()
print(x)

'''

'''
a = 1


def DF():
    print(a)


def DG():
    a = 2
    print(a)


def DH():
    global a
    a = 3
    print(a)


print(a)
DF()
print(a)
DG()
print(a)
DH()
print(a)

'''