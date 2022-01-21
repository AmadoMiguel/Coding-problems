# Given an array of integers, arr, where all numbers occur twice except one number which occurs once, find the number.
# Your solution should ideally be O(n) time and use constant extra space.
# Example:
# Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
# Output: 7


class Solution(object):
  # Using XOR (^ operator): XOR of a number with itself is 0. XOR of a number with 0 is itself
  def findSingle(self, nums):
    uniqueNum = nums[0]
    for n in nums[1:]:
      uniqueNum ^= n
    return uniqueNum


# nums = [1, 3, 4, 4, 1, 5, 6, 5, 6]
nums = [7, 3, 5, 5, 4, 3, 4, 8, 8]
print(Solution().findSingle(nums))
# 3