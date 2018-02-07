'''
Mohammad Chand Alam
ALIGARH MUSLIM UNIVERSITY
'''

# Python  Data Structure
# Index

import sys
'''
str = 'CHAND'
print(str[0])         # Indexing
print(str[0:4])       #  0 to 3  (Some part)
print(str[3:])        #  ND (Last Part)
print(str[:3])        #  CHA (Start Part)
print(str[-1])        # Last D (End Point)
print(str[-3:])       # Last Three AND
print(str[:-2])       # Start Two CHA
print(str[1:6:3])     #   [start:end+1:step]

#  Adding or Concatenating
Comb = 'Chand' + "Alam"  #String
print(Comb)

A =['a','b']             #List
B =['c']
C=A+B
print(C[0])             ['a','b','c']

#Multiplying

st = input()             #String abc
print(3*st)              # abcabcabc


'''

'''
# Checking Membership

d = input()
if 'a' in d:
    print("Found")
else:
    print("Not Found")
Str = ['a','b','c']
if 'z' not in Str:
    print("Not Found in Str")
else:
    print("Found in Str")

'''


'''
# Iterating

k = [1, 2, 3]
for i in k:
    if i*2 == 4:
        print("This is my Number")
    else:
        print("This is not my Number")

# Index and Item
k = [1, 2, 3]
for index, item in enumerate(k):
    print(index,item)
    
'''

'''
# Length & Minimum & Maximum
st = input()
print(len(st))
print(min(st))  # Alphabetically
print(max(st))
'''

'''
# Sum

x = [1, 2, 3, 4, 5]
print(sum(x))
print(sum(x[2:]))

# Sort

s = 'chand'
print(sorted(s))

x = [3, 2, 234, 5]  # Original x will not Change
print(sorted(x))



# Count & Index

s = 'chandalam'
print(s.count('a'))
print(s.index('a'))

lst = [1, 2, 3, 4, 1]
print(lst.count(1))
print(lst.index(1))


# Unpacking

lf = ['CHAND', 'ALAM', 'ALIGARH']
a, b, c = lf
print(a)
print(b)
print(c)

'''