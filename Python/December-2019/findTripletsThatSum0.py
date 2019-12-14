# Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that
# a + b + c = 0. Note that there may not be any triplets that sum to zero in nums, and that the triplets must not
# be duplicates.
#
# Example:
# Input: nums = [0, -1, 2, -3, 1]
# Output: [0, -1, 1], [2, -3, 1]


def findTripletsThatSum0(nums):
    if len(nums) >= 3:
        return findTriplets(nums, 0, 1, 2, [])


def findTriplets(nums, ptr1, ptr2, ptr3, triplets):
    if ptr1 <= len(nums) - 3:
        n1, n2, n3 = nums[ptr1], nums[ptr2], nums[ptr3]
        if n1 + n2 + n3 == 0:
            triplets.append([n1, n2, n3])
        # Set pointers
        if ptr3 + 1 < len(nums):
            ptr3 += 1
        else:
            if ptr2 + 1 < len(nums) - 1:
                ptr2 += 1
                ptr3 = ptr2 + 1
            else:
                ptr1 += 1
                ptr2 = ptr1 + 1
                ptr3 = ptr2 + 1
        triplets = findTriplets(nums, ptr1, ptr2, ptr3, triplets)
    return triplets


nums = [-1, 2, -3, 1, 5, -5, 7, 6, -7]
print(findTripletsThatSum0(nums))
