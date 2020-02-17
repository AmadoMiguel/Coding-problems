# This problem was asked by IBM.
#
# Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation
# would be 49578.


def findNextGreaterPerm(currentNum, remainingDigits, nextGreater, initialNum):
    if not len(remainingDigits):
        print(currentNum)
        if currentNum > initialNum and nextGreater is None:
            nextGreater = currentNum
        elif initialNum < currentNum < nextGreater:
            nextGreater = currentNum
    else:
        for i in range(len(remainingDigits)):
            num = currentNum + remainingDigits[i]
            remDigits = remainingDigits[0:i] + remainingDigits[i + 1:]
            nextGreater = findNextGreaterPerm(num, remDigits, nextGreater, initialNum)
    return nextGreater


numStr = str(48975)
print("Next greater permutation:", findNextGreaterPerm("", numStr, None, numStr))
