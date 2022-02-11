# Write a program that, given an array A[] of n numbers and another number x, determines whether or not there
# exist two elements in A[] whose sum is exactly x. Return the indexes of the numbers

def findNumSumIndx(nums, num):
    numInd = {}
    for i in range(len(nums)):
        currNum = nums[i]
        comp = num - currNum
        if comp in numInd:
            return i, numInd[comp]
        numInd[currNum] = i
    return -1


# print(findNumSumIndx([0, -1, 2, -3, 1], -2))
print(findNumSumIndx([1, 4, 45, 6, -10, 8], -2))
