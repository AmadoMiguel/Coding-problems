def findLongestSubarrayBySum(s, arr):
    # Initialize array pointers
    ptr1 = 0
    ptr2 = 1
    maxRange = None
    indexesOfSubArray = None
    currSum = 0
    # Start traversing and slice using the pointers until the end of the array is reached.
    # The final condition is that ptr1 is equal to length of array - 1
    while ptr1 <= len(arr) and ptr2 <= len(arr) + 1:
        # Find current sum of subarray
        currSum = sum(arr[ptr1:ptr2])
        # Check if sum equals s
        if currSum == s:
            if maxRange == None or (ptr2 + 1 - (ptr1 + 1)) > maxRange:
                maxRange = (ptr2 + 1 - (ptr1 + 1))
                indexesOfSubArray = [ptr1 + 1, ptr2]
            if ptr2 == len(arr):
                break
            else:
                ptr2 += 1
        else:
            # Check value of the sum and change pointer values accordingly
            if currSum <= s:
                ptr2 += 1
            else:
                ptr1 += 1
            # If pointers hit each other, reset
            if ptr1 > ptr2:
                ptr1 = ptr2
                ptr2 += 1
    # Return the indexes (1-based) of the longest sub array with sum s
    if indexesOfSubArray is not None:
        return indexesOfSubArray
    else:
        # If the sub array wasn't found, return
        return [-1]


print(findLongestSubarrayBySum(15,  [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10]))

# Other solution

# from itertools import accumulate as accum
#
# def findLongestSubarrayBySum(s, arr):
#     # Traverse the array from beggining and start accumulating
#     for i in range(0, len(arr)):
#         startIndex = i
#         # Accumulate array
#         accumulated = arr[:i] + list(accum(arr[i:]))
#         # Check if s is in the array
#         if s in accumulated:
#             # Get the index from last to first
#             sumIndexOnAcum = accumulated[::-1].index(s)
#             endIndex = len(accumulated) - sumIndexOnAcum
#             return [startIndex + 1, endIndex]
#     return [-1]

