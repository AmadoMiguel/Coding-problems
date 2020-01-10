# We say a number is sparse if there are no adjacent ones in its binary representation. For example,
# 21 (10101) is sparse, but 22 (10110) is not. For a given input N, find the smallest sparse number
# greater than or equal to N.
#
# Do this in faster than O(N log N) time.


def isSparse(num):
    currResult = None
    while num > 1:
        rem = num % 2
        num = int(num / 2)
        if rem:
            if currResult is None:
                currResult = rem
            else:
                return False
        else:
            if currResult is not None:
                currResult = None
    if num == 1 and currResult:
        return False
    return True


def findClosestSparseNumber(n):
    while not isSparse(n):
        n += 1
    return n


print(findClosestSparseNumber(90))
