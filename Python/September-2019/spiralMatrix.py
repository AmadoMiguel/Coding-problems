# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

import numpy as np


def getSpiralFromMatrix(m):
    # Initialize the list that will contain the elements in spiral order
    spiral = []
    # Initialize border indeces
    upIndx = 0 # Is going to increment
    rightIndex = m[0].size - 1 # is going to decrement
    bottomIndex = len([r for r in m]) - 1 # is going to decrement
    leftIndex = 0 # is going to increment
    # Start iterating the matrix from left to right until all elements are added
    while len(spiral) < m.size:
        # From left to right in the top border index
        for n in m[upIndx]:
            # Avoid repeated elements
            if n not in spiral:
                spiral.append(n)
        # Transpose the matrix
        m = np.transpose(m)
        # From top to bottom in the right border index
        for n in m[rightIndex]:
            if n not in spiral:
                spiral.append(n)
        m = np.transpose(m)
        # From right to left in the bottom border index
        for n in np.flip(m[bottomIndex]):
            if n not in spiral:
                spiral.append(n)
        m = np.transpose(m)
        # From bottom to top in the left border index
        for n in np.flip(m[leftIndex]):
            if n not in spiral:
                spiral.append(n)
        # Transpose back the matrix to its original shape
        m = np.transpose(m)
        # Decrement/increment each index of traversal of the matrix
        upIndx += 1
        rightIndex -= 1
        leftIndex += 1
        bottomIndex -= 1
    return spiral


# Create matrix
mat = np.array([[1,  2,  3,  4,  5],
                [6,  7,  8,  9,  10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]])
print(getSpiralFromMatrix(mat))
