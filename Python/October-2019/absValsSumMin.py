# Given a sorted array of integers a, your task is to determine which element of a is closest to all other
# values of a. In other words, find the element x in a, which minimizes the following sum:

# abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)


def absoluteValuesSumMinimization(a):
    return calculateSum(0, a, None, None)


def calculateSum(index, a, minSum, closestNum):
    currSum = 0
    for i in range(len(a)):
        if i == index:
            continue
        else:
            currSum += abs(a[i] - a[index])
    if minSum is None or minSum > currSum:
        minSum = currSum
        closestNum = a[index]
    if index < len(a) - 1:
        closestNum = calculateSum(index + 1, a, minSum, closestNum)
    return closestNum
