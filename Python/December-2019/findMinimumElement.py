# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.
#
# For example, given [5, 7, 10, 3, 4], return 3.


def findMinElement(nums):
    minimum = nums[0]
    for n in nums[1:]:
        if n < minimum:
            return n
    # In case array is fully sorted without rotation
    return minimum


print(findMinElement([5, 6, 7, 8, 9, 10, 3, 4]))
