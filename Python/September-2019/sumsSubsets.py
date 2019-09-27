# Given a multiset of integers, return whether it can be partitioned into two subsets
# whose sums are the same.

import numpy as np

sumsSubsets = []
nNums = 1
indexes = [0]
def subsetsOfEqualSums(nums):
    global sumsSubsets
    global indexes
    global nNums
    # Copy of the nums
    copyOfNums = np.array(nums)
    copyWithoutIndexes = np.array(np.delete(copyOfNums, indexes))
    # Prepare list of first subset
    firstSubset = np.array(copyOfNums[indexes])
    # Prepare list of second subset
    secondSubset = np.array(copyWithoutIndexes)
    # Check the sum of both
    if np.sum(firstSubset) == np.sum(secondSubset):
        print("Eureka ->", firstSubset, secondSubset)
        return
    elif nNums < len(nums):
        indexes.append(nNums)
        nNums += 1
        print(firstSubset, secondSubset)
        subsetsOfEqualSums(nums)
    else:
        print("Not possible")
        return


arrOfNums = np.array([15, 5, 20, 10, 35, 15, 10])
# Sort the array in order to find more easily the subset of sums in case they exist
arrOfNums = np.sort(arrOfNums)
subsetsOfEqualSums(arrOfNums)
