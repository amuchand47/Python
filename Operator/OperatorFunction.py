import operator

a = 3
b = 4
c = operator.add(a, b)
d = operator.sub(a, b)
e = operator.mul(a, b)
f = operator.floordiv(a, b)
g = operator.pow(a, b)
h = operator.mod(a, b)

print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

if operator.le(c, d):
    print("Now I am Ready")
elif operator.ge(c, g):
    print("Koi Bat Nhi")
else:
    print("Nothing")

