'''

MD Chand Alam
Aligarh Muslim University

'''

import sys

# List

# Constructor

x = list()
x = [1, 2, 3, 4]
for i in range(0, len(x)):
    print(x[i])

# Comprehension

y = [m for m in range(8)]
z = [n*n for n in range(5) if n>2]
print(y)
print(z)


# delete
a = [1, 2, 3]
del(a[1])
print(a)
del a

# Append

c = [1, 2, 3]
c.append(4)
print(c)

# Extend

x = [1, 2, 3]
y = [4, 5]
x.extend(y)
print(x)


# Insert      insert(index,item)

s = [1, 2, 4, 5]
s.insert(2, 3)
print(s)
s.insert(5, [6, 7, 8])
print(s[5])


#  Pop

t = [1, 3, 4, 5]
t.pop()
print(t)

# Remove  Remove first item in the list

m =[1, 2, 4, 4]
m.remove(4)
print(m)

# Reverse

p = [1, 2, 3, 4, 5]
p.reverse()
print(p)

# Sort

g = [47, 5546, 55546, 554645, 34]
g.sort()
print(g)

