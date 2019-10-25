# You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at
# matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the
# bottom right corner.
#
# For example, in this matrix
#
# 0 3 1 1
# 2 0 0 4
# 1 5 3 1
# The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.

import numpy as np


def findPathWithMaxNumOfCoins(matrix):
    return collectCoinsInPath(matrix, 0, 0, 0, 0)


def collectCoinsInPath(matrix, currRow, currCol, currentTotal, maxTotal):
    if currCol <= len(matrix[0, :]) - 1 and currRow <= len(matrix[:, 0]) - 1:
        currentTotal += matrix[currRow, currCol]
        if currCol == len(matrix[0, :]) - 1 and currRow == len(matrix[:, 0]) - 1:
            print("total found:", currentTotal)
            if currentTotal > maxTotal:
                maxTotal = currentTotal
            currentTotal = 0
        nextSteps = [ [currRow, currCol+1], [currRow+1, currCol] ]
        for step in nextSteps:
            if step[0] <= len(matrix[:, 0]) - 1 and step[1] <= len(matrix[0, :]) - 1:
                maxTotal = collectCoinsInPath(matrix, step[0], step[1], currentTotal, maxTotal)
            else:
                continue
    return maxTotal


print(findPathWithMaxNumOfCoins(np.array([[0, 3, 1, 1, 4],
                                          [2, 8, 6, 4, 3],
                                          [1, 5, 2, 1, 2],
                                          [2, 8, 6, 4, 3],
                                          [1, 5, 2, 1, 2]])))
