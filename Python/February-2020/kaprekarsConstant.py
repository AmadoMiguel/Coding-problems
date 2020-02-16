# Kaprekar's Constant is the number 6174. This number is special because it has the property where for any 4-digit
# number that has 2 or more unique digits, if you repeatedly apply a certain function it always reaches the number 6174.
#
# This certain function is as follows:
# - Order the number in ascending form and descending form to create 2 numbers.
# - Pad the descending number with zeros until it is 4 digits in length.
# - Subtract the ascending number from the descending number.
# - Repeat.
#
# Given a number n, find the number of times the function needs to be applied to reach Kaprekar's constant.


def orderNum(numStr, isDescending):
    for i in range(len(numStr)):
        minIndex = i
        for j in range(i + 1, len(numStr)):
            if not isDescending:
                if numStr[j] < numStr[minIndex]:
                    minIndex = j
            else:
                if numStr[j] > numStr[minIndex]:
                    minIndex = j
        temp = numStr[i]
        numStr[i] = numStr[minIndex]
        numStr[minIndex] = temp
    return "".join(numStr)


def findNumIterations(num):
    numIter = 0
    while num != 6174:
        numStr = str(num)
        ascOrder = orderNum(list(numStr), False)
        descOrder = orderNum(list(numStr), True)
        while len(descOrder) < 4:
            descOrder += "0"
        num = int(descOrder) - int(ascOrder)
        numIter += 1
    return numIter


assert findNumIterations(123) == 3  # True
