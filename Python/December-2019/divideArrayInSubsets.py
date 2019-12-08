# Given an array of positive integers, divide the array into two subsets such that the difference between the sum of
# the subsets is as small as possible.
#
# For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a difference of 5, which
# is the smallest possible difference.

from itertools import permutations


def getSubsetsWithSmallestDifference(arr):
    permContr = 1
    finalSubSet1, finalSubSet2 = None, None
    while permContr <= len(arr) / 2:
        currentPerms = permutations(range(len(arr)), permContr)
        for p in currentPerms:
            currentIndexes = [i for i in p]
            currSubSet = [arr[i] for i in currentIndexes]
            otherIndices = [i for i in range(len(arr)) if i not in p]
            permsAux = [arr[i] for i in otherIndices]
            if (not finalSubSet1 and not finalSubSet2) or \
                    (abs(sum(permsAux) - sum(currSubSet)) < abs(sum(finalSubSet1) - sum(finalSubSet2))):
                if len(set(permsAux)) == len(permsAux) and len(set(currSubSet)) == len(currSubSet):
                    print(permsAux, currSubSet)
                    finalSubSet1, finalSubSet2 = currSubSet, permsAux
        permContr += 1
    return finalSubSet1, finalSubSet2


print(getSubsetsWithSmallestDifference([5, 10, 15, 20, 25, 3, 1, 2, 5]))
