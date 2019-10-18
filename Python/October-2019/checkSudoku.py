# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column,
# each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.
#
# This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

import numpy as np


def sudoku(grid):
    sudokuCopy = np.array(grid)
    return checkAllRowsAndColumns(sudokuCopy) and checkGrids(sudokuCopy)


# Check all rows and all columns
def checkAllRowsAndColumns(sudoku):
    numsFrom1To9 = np.array(range(1, 10))
    for i in range(9):
        if False in list(np.array(list(sorted(sudoku[i, :]))) == numsFrom1To9) or False in list(
                np.array(list(sorted(sudoku[:, i]))) == numsFrom1To9):
            return False
    return True


# Check all grids
def checkGrids(sudoku):
    ptr1Row = 0
    ptr2Row = 3
    ptr1Col = 0
    ptr2Col = 3
    numsFrom1To9 = np.array(range(1, 10))
    while ptr2Row <= 9:
        currSubGrid = sudoku[ptr1Row:ptr2Row, ptr1Col:ptr2Col]
        currSubGridAsRow = list(sorted(np.reshape(currSubGrid, (1, 9))[0]))
        if False in list(currSubGridAsRow == numsFrom1To9):
            return False
        if ptr2Col + 3 <= 9:
            ptr1Col += 3
            ptr2Col += 3
        else:
            ptr1Row += 3
            ptr2Row += 3
            ptr1Col = 0
            ptr2Col = 3
    return True


print(sudoku([[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]))

