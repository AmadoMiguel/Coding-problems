# Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.
# Example:
# Input: [1, 3, 5, 3, 1, 3, 1, 5]
# Output: 4
# The longest sequence that contains just 2 unique numbers is [3, 1, 3, 1]


def findSeqUniqueNums(nums, indx1, indx2, longestSubList):
    currSubList = nums[indx1:indx2]
    # If there are only 2 unique values
    # Assign until the max length is found
    if len(set(currSubList)) == 2 and len(currSubList) > len(longestSubList):
        longestSubList = currSubList
    # Update slicing indexes
    if indx2 < len(nums):
        indx2 += 1
        # Recursion call
        longestSubList = findSeqUniqueNums(nums, indx1, indx2, longestSubList)
    elif indx1 < len(nums) - 1:
        indx1 += 1
        indx2 = indx1 + 1
        # Recursion call
        longestSubList = findSeqUniqueNums(nums, indx1, indx2, longestSubList)
    # Exit recursion if index 1 is last - 1 number
    return longestSubList


longestSubList = findSeqUniqueNums([1, 3, 5, 3, 1, 3, 1, 5], 0, 1, [])
print("Longest sub list found", longestSubList)
