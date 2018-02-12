
# Typecasting
# Int Character
# list , tuple , Set
import sys

s = "101010"

c = int(s, 2)
print("After Converting this to Integer", end=" ")
print(c)

e = float(c)

print("After converting to Float", end=" ")
print(e)


d = '1'
cd = ord(d)
print("After converting Character to Integer", end=" ")
print(cd)

dd = 'Geekforgeeks'
c = tuple(dd)
print(c)

x = set(dd)
print(x)

y = list(dd)
print(y)