# Given a sorted list of numbers, and two integers low and high representing the lower and upper bound of a range,
# return a list of (inclusive) ranges where the numbers are missing. A range should be represented by a tuple in the
# format of (lower, upper).


def findMissingRanges(nums, searchRange):
    if len(nums):
        missing = []
        currNum = nums[0]
        for n in nums[1:]:
            if currNum + 1 != n:
                if currNum + 1 >= searchRange[0] and n - 1 <= searchRange[1]:
                    missing.append((currNum + 1, n - 1))
            currNum = n
        return missing
    return []


nums = [1, 3, 5, 10, 15, 20, 21, 22, 23, 26]
searchRange = (1, 24)
print(findMissingRanges(nums, searchRange))
