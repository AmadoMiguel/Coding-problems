# Given an array of integers, arr, where all numbers occur twice except one number which occurs once, find the number.
# Your solution should ideally be O(n) time and use constant extra space.
# Example:
# Input: arr = [3, 3, 5, 5, 4, 7, 4, 8, 8]
# Output: 7


def findUniqueNum(nums):
    tempNums = []
    for n in nums:
        if n not in tempNums:
            tempNums += [n]
        else:
            del tempNums[tempNums.index(n)]
    return tempNums[0]


print(findUniqueNum([3, 3, 5, 5, 4, 7, 4, 8, 8]))
