# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
#
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we
# would take elements 42, 14, -5, and 86.


maxSumSubArr = 0
subArrWithMaxSum = []
initIndex = 0
finalIndex = 2


def findMaxSumInArray(arr):
    global maxSumSubArr
    global subArrWithMaxSum
    global initIndex
    global finalIndex

    # Start adding up numbers and compare to maxSumSubArr
    currSum = 0
    currArr = []
    for n in arr[initIndex:finalIndex]:
        currSum += n
        currArr.append(n)
    if currSum > maxSumSubArr:
        maxSumSubArr = currSum
        subArrWithMaxSum = currArr
    # Check indexes
    if initIndex == 0 and finalIndex == len(arr):
        if initIndex < len(arr) - 1:
            initIndex += 1
        else:
            return maxSumSubArr, subArrWithMaxSum
        finalIndex = initIndex + 2
        findMaxSumInArray(arr)
    else:
        if finalIndex <= len(arr):
            finalIndex += 1
        else:
            initIndex += 1
            finalIndex = initIndex + 2
        if initIndex == len(arr):
            return maxSumSubArr, subArrWithMaxSum
        else:
            findMaxSumInArray(arr)


findMaxSumInArray([34, -50, -42, 14, 90, 96])
print(maxSumSubArr, subArrWithMaxSum)
