# Given an array of integers, find the maximum possible sum you can get from one of its contiguous
# subarrays. The subarray from which this sum comes must contain at least 1 element.


def arrayMaxConsecutiveSum2(inputArray):
    globalMax = None
    currentMax = 0

    for n in inputArray:
        currentMax += n
        if globalMax == None or currentMax > globalMax:
            globalMax = currentMax
        if currentMax < 0:
            currentMax = 0
    return globalMax


print(arrayMaxConsecutiveSum2([-2, 2, 5, -11, 6]))
