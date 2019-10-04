# You have an array of integers nums and an array queries, where queries[i] is a pair of indices (0-based).
# Find the sum of the elements in nums from the indices at queries[i][0] to queries[i][1] (inclusive)
# for each query, then add all of the sums for all the queries together. Return that number modulo 109 + 7.

from itertools import accumulate


def sumInRange(nums, queries):
    accum = [0] + list(accumulate(nums))
    totalSum = sum([accum[j + 1] - accum[i] for i, j in queries])
    return totalSum % 1000000007


print(sumInRange([3, 0, -2, 6, -3, 2],
                 [[0, 2],
                  [2, 5],
                  [0, 5]]
                 ))
