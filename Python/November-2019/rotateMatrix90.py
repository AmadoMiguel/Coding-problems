# Given an N by N matrix, rotate it by 90 degrees clockwise.
#
# For example, given the following matrix:
#
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# you should return:
#
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
# Follow-up: What if you couldn't use any extra space?


import numpy as np


def rotateMatrix90(m, r1Ind, c1Ind, r2Ind, c2Ind):
    print(m)
    if r1Ind < r2Ind and c1Ind > c2Ind:
        firstRow, lastCol, \
        lastRow, firstCol = np.array(m[r1Ind, c2Ind:c1Ind+1]), np.array(m[r1Ind:r2Ind+1, c1Ind]), \
                            np.array(m[r2Ind, c2Ind:c1Ind+1]), np.array(m[r1Ind:r2Ind+1, c2Ind])
        m[r1Ind, c2Ind:c1Ind+1] = firstCol[::-1]
        m[r1Ind:r2Ind+1, c1Ind] = firstRow
        m[r2Ind, c2Ind:c1Ind+1] = lastCol[::-1]
        m[r1Ind:r2Ind+1, c2Ind] = lastRow

        # Recurse
        rotateMatrix90(m, r1Ind + 1, c1Ind - 1, r2Ind - 1, c2Ind + 1)
    return m


m = 6
mat = np.array([[n + m*(x-1) for n in range(x, x + m)] for x in range(1, m + 1)])
rotateMatrix90(mat, 0, len(mat[0, :])-1, len(mat[:, 0]) - 1, 0)
