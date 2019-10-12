# Let's define digit degree of some positive integer as the number of times we need to replace this number with the
# sum of its digits until we get to a one digit number.
#
# Given an integer, find its digit degree.


def digitDegree(n):
    if len(str(n)) == 1:
        return 0
    return sumDigits(n, 0)


def sumDigits(num,nDigitsSum):
    print(num)
    numAsStr = str(num)
    currSum = 0
    for d in numAsStr:
        currSum += int(d)
    nDigitsSum += 1
    if len(str(currSum)) != 1:
        nDigitsSum = sumDigits(currSum, nDigitsSum)
    return nDigitsSum
