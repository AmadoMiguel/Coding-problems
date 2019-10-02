# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that
# each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the
# numbers from 1 to 9 one time.
#
# Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle
# according to the layout rules described above. Note that the puzzle represented by grid does not have to
# be solvable.

import numpy as np


def sudoku2(grid):
    gridCopy = np.array(grid)
    # This is built only for a 9x9 matrix
    gridInitIndRow = 0
    gridFinIndRow = 3
    gridInitIndCol = 0
    gridFinIndCol = 3
    nRows = 0

    # Analize all rows and columns
    while nRows < 9:
        # Get current Row
        currRow = gridCopy[nRows, :]
        rowNums = [i for i in currRow if i != '.']
        currCol = gridCopy[:, nRows]
        colNums = [i for i in currCol if i != '.']
        if len(rowNums) != len(set(rowNums)) or len(colNums) != len(set(colNums)):
            return False
        nRows += 1

    # Analize all grids
    while gridFinIndRow <= 9 and gridFinIndCol <= 9:
        # Find current grid
        currGrid = gridCopy[gridInitIndRow:gridFinIndRow, gridInitIndCol:gridFinIndCol]
        # Resize
        currGrid = np.array(np.resize(currGrid, (1, 9)))[0]
        print(currCol)
        # Transform to a set and verify if are there repeated numbers
        # by comparing length between array version and set version
        listCurrGrid = [i for i in currGrid if i != '.']
        setCurrGrid = set(listCurrGrid)
        if len(setCurrGrid) == len(listCurrGrid):
            # Verify indexes
            if gridFinIndCol == 9 and gridFinIndRow == 9:
                # If the end of the matrix was reached, then the sudoku can be completed
                return True
            else:
                # Update indexes
                # Advance vertically to the bottom
                if gridFinIndCol == 9:
                    gridInitIndRow += 3
                    gridFinIndRow += 3
                    gridInitIndCol = 0
                    gridFinIndCol = 3
                else:
                    # Advance horizontally to the right
                    gridInitIndCol += 3
                    gridFinIndCol += 3
        else:
            return False
