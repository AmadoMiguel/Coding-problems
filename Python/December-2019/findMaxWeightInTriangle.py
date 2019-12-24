# You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers.
# For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:
#
#   1
#  2 3
# 1 5 1
# We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually
# ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.
#
# Write a program that returns the weight of the maximum weight path.


triangleRows = [[1], [2, 3], [1, 5, 1], [1, 4, 5, 9], [1, 2, 3, 4, 5]]


def calculateMaxWeightShort(triangleRows):
    maxWeight = 0
    for r in triangleRows:
        maxWeight += max(r)
    return maxWeight


def calculateWeight(rowIndx,  currWeight, maxWeight, currPath):
    for n in triangleRows[rowIndx]:
        currWeight += n
        currPath += [n]
        if rowIndx + 1 < len(triangleRows):
            maxWeight = calculateWeight(rowIndx + 1, currWeight, maxWeight, currPath)
        if currWeight > maxWeight:
            print("Max path found", currPath)
            maxWeight = currWeight
        # Backtrack
        currWeight -= n
        del currPath[-1]
    return maxWeight


print(calculateWeight(0, 0, 0, []))
print(calculateMaxWeightShort(triangleRows))
