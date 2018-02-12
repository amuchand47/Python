import sys

a = 'Geekforgeeks'
c = b'Geekforgeeks'

d = a.encode('ASCII')

if d == c:
    print("Encoding Completed")
else:
    print("Not Completed")

f = c.decode('ASCII')

if f == a:
    print("Decode Successful")
else:
    print("Not Decoded")
