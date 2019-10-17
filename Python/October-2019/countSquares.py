# Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

import numpy


def differentSquares(matrix):
    copyOfMatrix = numpy.array(matrix)
    return getSquares(0, 1, 0, 1, copyOfMatrix, [])


def getSquares(p1Row, p2Row, p1Col, p2Col, matrix, differentSquares):
    # Pointers out of bounds
    if p2Row < len(matrix[:, 0]) and p2Col < len(matrix[0, :]):
        # Slice current 2x2 square
        currSqStr = str(matrix[p1Row, p1Col]) + str(matrix[p1Row, p2Col]) + str(matrix[p2Row, p1Col]) + str(
            matrix[p2Row, p2Col])
        if currSqStr not in differentSquares:
            differentSquares.append(currSqStr)
        # Check pointers
        if p2Col + 1 < len(matrix[0, :]):
            getSquares(p1Row, p2Row, p1Col + 1, p2Col + 1, matrix, differentSquares)
        elif p2Row + 1 < len(matrix[:, 0]):
            getSquares(p1Row + 1, p2Row + 1, 0, 1, matrix, differentSquares)
    return len(list(differentSquares))


print(differentSquares([[1, 2, 1],
                       [2, 2, 2],
                       [2, 2, 2],
                       [1, 2, 3],
                       [2, 2, 1]]))
