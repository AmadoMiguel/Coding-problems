# Let A be an N by M matrix in which every row and every column is sorted.
#
# Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].
#
# For example, given the following matrix:
#
# [[1, 3, 7, 10, 15, 20],
#  [2, 6, 9, 14, 22, 25],
#  [3, 8, 10, 15, 25, 30],
#  [10, 11, 12, 23, 30, 35],
#  [20, 25, 30, 35, 40, 45]]
# And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.

import numpy as np


def countMinorsAndMayors(mat, i1, j1, i2, j2):
    minThresh, maxThresh = mat[i1, j1], mat[i2, j2]
    totalMinOrMay = 0
    for r in range(len(mat[:, 0])):
        for c in range(len(mat[0, :])):
            if mat[r, c] < minThresh or mat[r, c] > maxThresh:
                totalMinOrMay += 1
    return totalMinOrMay


i1, j1 = 1, 1
i2, j2 = 3, 3
mat = np.array([[1, 3, 7, 10, 15, 20],
                [2, 6, 9, 14, 22, 25],
                [3, 8, 10, 15, 25, 30],
                [10, 11, 12, 23, 30, 35],
                [20, 25, 30, 35, 40, 45]])
print(countMinorsAndMayors(mat, i1, j1, i2, j2))
