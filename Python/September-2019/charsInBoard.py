# Given a 2D board of characters and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are
# those horizontally or vertically neighboring. The same letter cell may not be used more than once.

import numpy as np


def checkPositionOfLetter(letter, prevIndeces, board):
    # Check index/indeces of appereance of the current letter
    rowCurrLetterIndeces = np.where(board == letter)[0][0]
    colCurrLetterIndeces = np.where(board == letter)[1][0]
    currLetterIndeces = np.array([rowCurrLetterIndeces, colCurrLetterIndeces])
    # Compare to previous indeces to check adjacency
    difference = np.subtract(currLetterIndeces, prevIndeces)
    negInds = np.where(difference < 0)
    difference[negInds] *= -1
    if abs(np.sum(difference)) == 1:
        return True
    else:
        return False


nAdyacentLetters = 0
index = 0


def checkCharSeqInBoard(boardMatrix, word):
    global nAdyacentLetters
    global index
    # Check index of appereance of current letter being evaluated
    print(nAdyacentLetters)
    if nAdyacentLetters < len(word):
        rowIndexOfCurrentLetter = np.where(boardMatrix == word[index])[0][0]
        colIndexOfCurrentLetter = np.where(boardMatrix == word[index])[1][0]
        indecesOfCurrentLetter = np.array([rowIndexOfCurrentLetter, colIndexOfCurrentLetter])
        if len(indecesOfCurrentLetter) > 0:
            index += 1
            if checkPositionOfLetter(word[index], indecesOfCurrentLetter, boardMatrix):
                if nAdyacentLetters == 0:
                    nAdyacentLetters += 2
                else:
                    nAdyacentLetters += 1
                checkCharSeqInBoard(boardMatrix, word)
            else:
                return False
        else:
            return False
    else:
        return True


board = np.array([
                  ['A', 'B', 'X', 'W'],
                  ['Y', 'F', 'C', 'S'],
                  ['J', 'D', 'E', 'V']
                 ])
word = "ABFDEV"
print(checkCharSeqInBoard(board, word))
