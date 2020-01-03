# You are given a stream of numbers. Compute the median for each new element .
#
# Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]


from __future__ import division


def findMedian(nums):
    nums = list(sorted(nums))
    if len(nums) == 1:
        return nums[0]
    elif len(nums) % 2 != 0 and len(nums) > 1:
        return nums[int((len(nums) - 1) / 2)]
    elif len(nums) % 2 == 0 and len(nums) > 1:
        return nums[int((len(nums) - 1) / 2)] + ((nums[int((len(nums) - 1) / 2) + 1] -
                                                 nums[int((len(nums) - 1) / 2)]) / 2)


def calculateRunningMedian(numList):
    runMedian = [0 for _ in range(len(numList))]
    for i in range(len(numList)):
        runMedian[i] = findMedian(numList[:i + 1])
    return runMedian


nums = [2, 1, 4, 7, 2, 0, 5, 15, 20, 3, 5, 6]
print(calculateRunningMedian(nums))
