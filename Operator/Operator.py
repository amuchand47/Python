import sys

a = not True              # negation
b = not False
print(a)
print(b)

print(~a)
print(~b)

i = 0                   # There is not like ++ or -- operator in Python
while i < 10:
    print(i)
    i += 1

# Ternary Operator

a, b = 10, 20
min = a if a < b else b
print(min)

# using Tuple and Lambda Selection

a, b = 10, 20
print((b, a)[a < b])
c, d = 20, 30
print((lambda: d, lambda: c)[c < d]())


# Divison

a, b = 20, 30
print(b//a)    # Modulo Divison
print(b/a)     # Float Divison


# any , all

print(all([True, True, False]))
print(any([True, False, True]))


import operator
x = 10
y = 20

z = operator.add(x, y)
print(z)

d = operator.iadd(x, y)
print(d)


a = [1, 2, 3, 4]
z = operator.add(a, [5, 6, 7])
print(z)
print(a)
g = operator.iadd(a, [3, 4, 56, 6])
print(g)