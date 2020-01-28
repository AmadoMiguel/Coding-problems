#
# Given a non-empty array where each element represents a digit of a non-negative integer, add one to the integer.
# The most significant digit is at the front of the array and each element in the array contains only one digit.
# Furthermore, the integer does not have leading zeros, except in the case of the number '0'.
#
# Example:
# Input: [2,3,4]
# Output: [2,3,5]


def plusOne(nums):
    leftover = 0
    for i in range(len(nums) - 1, 0, -1):
        if i == len(nums) - 1:
            currNum = nums[i] + 1
            if currNum >= 10:
                leftover = int(currNum / 10)
                currNum = int(currNum % 10)
        else:
            currNum = nums[i] + leftover
            # Reset leftover
            leftover = 0
            if currNum >= 10:
                leftover = int(currNum / 10)
                currNum  = int(currNum % 10)
        nums[i] = currNum
    if leftover:
        added = nums[0] + leftover
        if added >= 10:
            remainder = int(added / 10)
            leftover = int(added % 10)
            nums[0] = leftover
            nums.insert(0, remainder)
        else:
            nums[0] = added


arr = [9, 9, 9, 9, 9, 9, 9]
plusOne(arr)
print(arr)
assert arr == [1, 0, 0, 0, 0, 0, 0, 0]
