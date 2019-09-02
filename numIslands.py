# Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
# A 1 represents land and 0 represents water, so an island is a group of 1s
# that are neighboring whose perimeter is surrounded by water.

import numpy as np

def countIslands(seaMatrix):
    # Initialize number of islands variable
    nOfIslands = 0
    # Initialize the index to check next matrix row
    index = 0
    # Initialize the array that stores the addition of the first two rows of the matrix
    rowsSum = np.array([])
    # Iterate over each row in the matrix
    for row in seaMatrix:
        if index + 1 < len(seaMatrix):
            # Add current row and next row
            if index == 0:
                # If there is at least a 1 in the row, there is at least 1 island
                if 1 in row:
                    nOfIslands += 1
                rowsSum = np.add(row, seaMatrix[index + 1])
                # If there was a 0 when adding the rows, means there is another islands
                zerosIndeces = np.where(rowsSum == 0)
                if 0 in rowsSum:
                    nOfIslands += 1
            # else:
            #     # Find 1s in the next row
            #     ones = np.where(seaMatrix[index + 1] == 0)

            index += 1
    return nOfIslands


# Define the islands matrix
islands = np.array([
                    [1, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 1, 0, 1],
                    [0, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0]
                   ])

print(countIslands(islands))