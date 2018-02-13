import operator

# Set Item , Delete Item, Get Item

li = [1, 2, 3, 4]
print(li)
operator.setitem(li, 3, 8)
print(li)

d = operator.getitem(li, 3)
print(d)

operator.delitem(li, 0)
print(li)

lis = [1, 2, 3, 4, 5]
print(lis)
operator.setitem(lis, slice(0, 2), [5, 6, 7])
print(lis)
s = operator.getitem(lis, slice(0, 4))
print(s)
operator.delitem(lis, slice(0, 4))
print(lis)

s1 = "GeekforGeeks"
s2 = "Communication"
print(operator.concat(s1, s2))

if operator.contains(s1, s2):
    print("It contains Geekforgeeks")
else:
    print("It does not contain anything")


# Logical Operator

a = 1
b = 0
print(operator.and_(a, b))
print(operator.or_(a, b))
print(operator.xor(a, b))
print(operator.invert(a))

w, e, r = 4, 5, 6
if w < e < r:
    print("Right")
else:
    print("Wrong")
