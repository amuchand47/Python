# Partial Funtion
from functools import partial


def Add(a, b, c, x):  # Partial Function
    return 1000 * a + 100 * b + 10 * c + x


g = partial(Add, 1, 2, 3)
print(g(3))


def PfAdd(a, b, c, d):
    return 1000 * a + 100 * b + 10 * c + d


add_part = partial(PfAdd, b=1, c=2, d=3)
print(add_part(5))


# Packing and Unpacking

def func(a, b, c, d):
    print(a, b, c, d)


my_list = [1, 2, 3, 4]
func(*my_list)


def mysum(*args):
    s = 0
    for i in range(0, len(args)):
        s = s + args[i]
    return s


print(mysum(1, 2, 3, 4, 4))
print(mysum(3, 4, 494, 56))


def fun1(a, b, c):
    print(a, b, c)


def fun2(*args):
    args = list(args)
    args[0] = "ChandAlam"
    args[1] = "India"

    fun1(*args)


fun2("Indian", "Chand", "Alam")


# ** used for dictionary

def dictionary(a, b, c):
    print(a, b, c)


d = {'a': 2, 'b': 3, 'c': 4}
dictionary(**d)


def fund(**kwargs):
    print(type(kwargs))

    for key in kwargs:
        print("%s = %s" %(key, kwargs[key]))


fund(name="Geek", ID="CS101", language="Python")
