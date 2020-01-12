# Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7.
# The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.


def findNthSevenishNum(nth):
    currSevenish = 1
    sevenPowsSum = 1
    currSevenishIndex = 1
    while currSevenishIndex < nth:
        # Number could be a power of 7...
        sevenPowsSum *= 7
        currSevenishIndex += 1
        if currSevenishIndex == nth:
            return sevenPowsSum
        # Or the sum of powers of 7
        currSevenish += sevenPowsSum
        currSevenishIndex += 1
        if currSevenishIndex == nth:
            return currSevenish
    # Default return in case nth == 1
    return currSevenish


print(findNthSevenishNum(3))

