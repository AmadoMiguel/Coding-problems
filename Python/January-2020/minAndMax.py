# Given a list of numbers of size n, where n is greater than 3, find the maximum and minimum of the list using less
# than 2 * (n - 1) comparisons.


# No. of comparisons -> n - 1
def findMinAndMax(nums):
    minNum, maxNum = None, None
    if len(nums):
        if len(nums) == 1:
            minNum, maxNum = nums[0], nums[0]
        else:
            if nums[0] >= nums[1]:
                maxNum, minNum = nums[1], nums[0]
            else:
                maxNum, minNum = nums[0], nums[1]
            for i in range(2, len(nums)):
                # Check whether current number is greater than max OR less than min
                if nums[i] > maxNum:
                    maxNum = nums[i]
                elif nums[i] < minNum:
                    minNum = nums[i]
    return minNum, maxNum


print(findMinAndMax([3, 5, 1, 2, 4, 8]))
