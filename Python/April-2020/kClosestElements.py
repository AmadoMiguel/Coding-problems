# Given a list of sorted numbers, and two integers k and x, find k closest numbers to the pivot x.

from functools import cmp_to_key


def closestNums(nums, k, x):
    # Sort the numbers with x as pivot
    return sorted(nums, key=cmp_to_key(lambda n1, n2: abs(n1-x) - abs(n2-x)))[:k]


print(closestNums([1, 3, 7, 8, 10, 2, 5, -4, 11, 13, 12], 4, 9))
