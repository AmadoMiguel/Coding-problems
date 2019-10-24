# Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's
# and return its area.
#
# For example, given the following matrix:
#
# [[1, 0, 0, 0],
#  [1, 0, 1, 1],
#  [1, 0, 1, 1],
#  [0, 1, 0, 0]]

# Return 4.


import numpy as np


# Very important to consider rectangles both horizontally and vertically
def findMaxRectangleArea(matrix):
    if len(matrix[0, :]) < 2 or len(matrix[:, 0]) < 2:
        return 0
    maxArea = 0
    secRowIndx = 1
    curRowIndx = 0
    # Iterate over each row
    for r in matrix:
        print("Current row", r)
        # Get max set of indexes for which the row contains only 1s
        setsOfIndexes = findIndexesOfContOnes(r, 0, 1, [])
        for colIndexes in setsOfIndexes:
            print("Continues ones at", colIndexes)
            currArea = 0
            if len(colIndexes) >= 2:
                while secRowIndx < len(matrix[:, 0]):
                    if 0 not in matrix[secRowIndx, colIndexes]:
                        # Only add the area when at least 2 rows with ones at same indexes are found
                        if not currArea:
                            currArea += 2 * len(colIndexes)
                        else:
                            currArea += len(colIndexes)
                        secRowIndx += 1
                    else:
                        break
                # Reassign maxArea in case at least a rectangle of ones was found
                if currArea > maxArea:
                    maxArea = currArea
            # Reset second row index for next set of column indexes
            secRowIndx = curRowIndx + 1
        # Update index for current row
        curRowIndx += 1
        secRowIndx = curRowIndx + 1
    return maxArea


# Find all possible continuous indexes for which the passed row contains only ones
def findIndexesOfContOnes(row, ptrCol1, ptrCol2, setsOfIndexes):
    if 0 not in row[ptrCol1: ptrCol2+1] and ptrCol2 - ptrCol1 > 0:
        setsOfIndexes.append(list(range(ptrCol1, ptrCol2+1)))
    if ptrCol2 + 1 <= len(row)-1:
        setsOfIndexes = findIndexesOfContOnes(row, ptrCol1, ptrCol2 + 1, setsOfIndexes)
    elif ptrCol1+1 < len(row):
        setsOfIndexes = findIndexesOfContOnes(row, ptrCol1+1, ptrCol1+1, setsOfIndexes)
    return setsOfIndexes


print(findMaxRectangleArea(np.array([[0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
                                     [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                                     [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                                     [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0]])))
