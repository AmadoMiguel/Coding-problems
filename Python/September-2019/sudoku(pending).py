# Sudoku is a puzzle where you are given a partially-filled 9 by 9 grid with digits. The objective
# is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain
# all of the digits from 1 to 9.

import numpy as np
import random as rand

lengthSudoku = 9
firstRowIndexOfGrid = 0
secondRowIndexOfGrid = int(np.sqrt(lengthSudoku))
firstColIndexOfGrid = 0
secondColIndexOfGrid = int(np.sqrt(lengthSudoku))
# Define the numbers of the sudoku
sudokuNumbers = [i for i in range(1, lengthSudoku + 1)]

def solveSudoku(sudoku):
    # Define grid indexes as global
    global firstRowIndexOfGrid, secondRowIndexOfGrid, firstColIndexOfGrid, secondColIndexOfGrid, sudokuNumbers
    # Define current grid
    currentGrid = sudoku[firstRowIndexOfGrid: secondRowIndexOfGrid, firstColIndexOfGrid: secondColIndexOfGrid]
    # Define current indexes in order to assign values to each cell
    currentRowIndex = firstRowIndexOfGrid
    currentColIndex = firstColIndexOfGrid
    # Traverse on each grid row
    for r in currentGrid:
        # Traverse each number
        for n in r:
            if n == 0:
                print("hi")

            # Continue to next cell indexes if they are within the current grid range
            if currentColIndex < secondColIndexOfGrid:
                currentColIndex += 1
            elif currentRowIndex < secondRowIndexOfGrid:
                currentRowIndex += 1
                currentColIndex = firstColIndexOfGrid
            else:
                # Advance to the grid at the right side
                if secondColIndexOfGrid + int(np.sqrt(lengthSudoku)) <= len(sudoku[0, :]):
                    # Readjust grid indexes accordingly
                    firstColIndexOfGrid = secondColIndexOfGrid
                    secondColIndexOfGrid += int(np.sqrt(lengthSudoku))
                    firstRowIndexOfGrid = 0
                    secondRowIndexOfGrid = int(np.sqrt(lengthSudoku))
                    # Call the function again
                    solveSudoku(sudoku)
                # Advance to the grid below
                elif secondRowIndexOfGrid + int(np.sqrt(lengthSudoku)) <= len(sudoku[:, 0]):
                    # Readjust grid indexes accordingly
                    firstColIndexOfGrid = 0
                    secondColIndexOfGrid = int(np.sqrt(lengthSudoku))
                    firstRowIndexOfGrid = secondRowIndexOfGrid
                    secondRowIndexOfGrid += int(np.sqrt(lengthSudoku))
                    # Call the function again
                    solveSudoku(sudoku)
                else:
                    # The sudoku can no longer be traversed
                    return sudoku



# Define length of sudoku, create sudoku matrix and define only the first number of it randomly
sudokuMatrix = np.array([[0 for _ in range(0, lengthSudoku)] for _ in range(0, lengthSudoku)])
sudokuMatrix[0, 0] = rand.randint(1, 9)
solveSudoku(sudokuMatrix)
