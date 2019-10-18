# Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order,
# starting from top-left and in clockwise direction.

import numpy as np


def spiralNumbers(n):
    # Build a matrix full of 0s
    spiralMatrix = np.array([[0 for _ in range(n)] for _ in range(n)])
    # Define the initial number (1)
    currentNum = 1
    # Define pointers
    rowPtr,colPtr = (0,0)
    # Start by traversing to the right
    # According to the movement the matrix pointers are increasing/decreasing
    movR,movD,movL,movU = (True,False,False,False)
    while currentNum <= n*n:
        if not spiralMatrix[rowPtr, colPtr]:
            # Assign current cell
            spiralMatrix[rowPtr,colPtr] = currentNum
            currentNum += 1
        # Update pointers accordingly
        if movR: # Move right
            if colPtr + 1 < len(spiralMatrix[0,:]) and not spiralMatrix[rowPtr,colPtr+1]:
                colPtr += 1
            else:
                # Moving down
                movR,movD,movL,movU = (False,True,False,False)
        if movD: # Move down
            if rowPtr + 1 < len(spiralMatrix[:,0]) and not spiralMatrix[rowPtr+1,colPtr]:
                rowPtr += 1
            else:
                # Moving left
                movR,movD,movL,movU = (False,False,True,False)
        if movL: # Move left
            if colPtr - 1 >= 0 and not spiralMatrix[rowPtr,colPtr-1]:
                colPtr -= 1
            else:
                # Moving up
                movR,movD,movL,movU = (False,False,False,True)
        if movU: # Move up
            if rowPtr - 1 >= 0 and not spiralMatrix[rowPtr-1,colPtr]:
                rowPtr -= 1
            else:
                # Moving right
                movR,movD,movL,movU = (True,False,False,False)
    return spiralMatrix


print(spiralNumbers(4))
