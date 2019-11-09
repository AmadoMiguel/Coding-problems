import math
# Given a positive integer n, find the smallest number of squared integers which sum to n.
# For example, given n = 13, return 2, since 3**2 + 2**2 = 9 + 4


def findNumWithBiggestSquare(n):
    biggestNumSquare = 0
    for i in range(n + 1):
        if i ** 2 <= n:
            if i > biggestNumSquare:
                biggestNumSquare = i
        else:
            break
    return biggestNumSquare


def findMinNumOfSquaredNums(n):
    minNumOfSquares = 0
    while n > 0:
        print(n)
        n = n - (findNumWithBiggestSquare(n) ** 2)
        minNumOfSquares += 1
    return minNumOfSquares


print("Minimum number of squares:", findMinNumOfSquaredNums(13))
