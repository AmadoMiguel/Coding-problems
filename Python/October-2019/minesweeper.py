# In the popular Minesweeper game you have a board with some mines and those cells that don't contain '
# 'a mine have a number in it that indicates the total number of mines in the neighboring cells. '
# 'Starting off with some arrangement of mines we want to create a Minesweeper game setup.


import numpy as np


def minesweeper(matrix):
    matrixCopy = np.array(matrix)
    resultingMatrix = np.array([[0 for _ in range(len(matrixCopy[0,:]))] for _ in range(len(matrixCopy[:,0]))])
    # Initialize number of neighboring mines for current cell
    nMines = 0
    # Initialize index of traversal for searching neighboring mines
    curRow = 0
    curCol = 0
    while True:
        if curRow - 1 >= 0:
            if matrixCopy[curRow-1, curCol]:
                nMines += 1
            if curCol - 1 >= 0:
                if matrixCopy[curRow-1, curCol-1]:
                    nMines += 1
        if curCol - 1 >= 0:
            if matrixCopy[curRow, curCol-1]:
                nMines += 1
            if curRow + 1 < len(matrixCopy[:,0]):
                if matrixCopy[curRow+1,curCol-1]:
                    nMines += 1
        if curCol + 1 < len(matrixCopy[0,:]):
            if matrixCopy[curRow, curCol+1]:
                nMines += 1
            if curRow - 1 >= 0:
                if matrixCopy[curRow-1, curCol+1]:
                    nMines += 1
            if curRow + 1 < len(matrixCopy[:, 0]):
                if matrixCopy[curRow+1, curCol+1]:
                    nMines += 1
        if curRow + 1 < len(matrixCopy[:, 0]):
            if matrixCopy[curRow+1, curCol]:
                nMines += 1
        # Assign nMines to current cell and restart nMines
        resultingMatrix[curRow, curCol] = nMines
        nMines = 0
        if curCol+1 < len(matrixCopy[0, :]):
            curCol += 1
        elif curRow+1 < len(matrixCopy[:, 0]):
            curRow += 1
            curCol = 0
        else:
            break
    return resultingMatrix


print(minesweeper([[True, False, False],
                   [False, True, False],
                   [False, False, False]]))
