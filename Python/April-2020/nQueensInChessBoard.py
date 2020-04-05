# In chess, queens can move any number of squares vertically, horizontally, or diagonally. The n-queens puzzle is the
# problem of placing n queens on an n × n chessboard so that no two queens can attack each other.
#
# Given an integer n, print all possible distinct solutions to the n-queens puzzle. Each solution contains distinct
# board configurations of the placement of the n queens, where the solutions are arrays that contain permutations
# of [1, 2, 3, .. n]. The number in the ith position of the results array indicates that the ith column queen is placed
# in the row with that number. In your solution, the board configurations should be returned in lexicographical order.

import numpy as np


def checkRow(row, board):
    for p in board[row, :]:
        if p:
            return True
    return False


def checkCol(col, board):
    for p in board[:, col]:
        if p:
            return True
    return False


def checkDiags(row, col, board, lenBoard):
    for r in range(lenBoard):
        for c in range(lenBoard):
            if c != col and r != row:
                if r - c == row - col:
                    if board[r, c]:
                        return True
                if r + c == row + col:
                    if board[r, c]:
                        return True
    return False


def isAttacked(row, col, board, lenBoard):
    if checkRow(row, board):
        return True
    if checkCol(col, board):
        return False
    if checkDiags(row, col, board, lenBoard):
        return True
    return False


def locateQueen(nColumn, board, boardLen, positions):
    # Base case
    if nColumn >= boardLen:
        return True
    for r in range(boardLen):
        if not isAttacked(r, nColumn, board, boardLen):
            board[r, nColumn] = 1
            positions.append(r + 1)
            if locateQueen(nColumn + 1, board, boardLen, positions):
                locateQueen.allPossible.append(positions[:])
                # print(positions)
            # Backtrack
            board[r, nColumn] = 0
            if len(positions):
                positions.pop()
    return False


boardSize = 4
chess = np.array([[0 for _ in range(boardSize)] for _ in range(boardSize)])
locateQueen.allPossible = []
locateQueen(0, chess, boardSize, [])
print(locateQueen.allPossible)
