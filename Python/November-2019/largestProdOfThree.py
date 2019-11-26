# You are given an array of integers. Return the largest product that can be made by multiplying any 3
# integers in the array.
#
# Example:
#
# [-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.

from itertools import permutations


def findBiggestProductOfThree(arr):
    indxsPerm = permutations(range(len(arr)), 3)
    largestProd = None
    for p in indxsPerm:
        a, b, c = arr[p[0]], arr[p[1]], arr[p[2]]
        currentProd = a*b*c
        if largestProd is None or currentProd > largestProd:
            largestProd = currentProd
    return largestProd


print(findBiggestProductOfThree([-4, -4, 2, 8]))
