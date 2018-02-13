"""
import sys
import numpy
# Transpose of a Matrix 1

m = [[1, 2], [3, 4], [5, 6]]
for row in m:
    print(row)

z = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in z:
    print(row)
print("\n")

# Transpose of a Matrix 2

matrix = [(1, 2, 3), (4, 5, 6,), (7, 8, 9)]
for row in matrix:
    print(row)
print("\n")

t_matrix = zip(*matrix)

for row in t_matrix:
    print(row)
# Transpose of a Matrix 3


matrix = [[1, 2, 3], [4, 5, 6] ]
print(matrix)
print("\n")

print(numpy.transpose(matrix))

"""

import sys
# Taking matrix as a input
