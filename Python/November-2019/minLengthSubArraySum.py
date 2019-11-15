# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous
# subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# Example:
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.


def findMinSubArrayThatSumK(arr, k):
    return checkCurrentSubArray(arr, 0, 1, k, None)


def checkCurrentSubArray(arr, ptr1, ptr2, k, minSubArr):
    # Check current sub array
    currSubArr = arr[ptr1:ptr2]
    print(currSubArr)
    if sum(currSubArr) >= k:
        if minSubArr is None or len(currSubArr) < len(minSubArr):
            minSubArr = currSubArr
    # Update indexes
    if ptr1 <= len(arr) - 1:
        if ptr2 < len(arr):
            ptr2 += 1
        else:
            ptr1 += 1
            ptr2 = ptr1 + 1
        # Recurse
        minSubArr = checkCurrentSubArray(arr, ptr1, ptr2, k, minSubArr)
    return minSubArr


print("Smallest sub array found:", findMinSubArrayThatSumK([2, 3, 1, 2, 4, 3], 6))
