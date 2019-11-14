# You are given a 2D array of characters, and a target string. Return whether or not the word target word
# exists in the matrix. Unlike a standard word search, the word must be either going left-to-right, top-to
# -bottom or both simultaneously in the matrix.
#
# Example:
#
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
#
# Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down
# in the first column.

import numpy as np


def findWordInMatrix(matrix, word):
    return searchWord(matrix, [0, 0], 0, list(word), False)


def searchWord(matrix, currentPosition, currentLetterIndex, wordAsList, wordIsInMatrix):
    # Recursion condition
    if currentPosition[0] < len(matrix[:, 0]) and currentPosition[1] < len(matrix[0, :]) and not wordIsInMatrix:
        print(currentPosition)
        if currentLetterIndex < len(wordAsList):
            # Main condition should be that the current position equals current letter
            if matrix[currentPosition[0], currentPosition[1]] == wordAsList[currentLetterIndex]:
                print(matrix[currentPosition[0], currentPosition[1]], wordAsList[currentLetterIndex])
                # If letter is last one, means that the letter was found
                if currentLetterIndex == len(wordAsList) - 1:
                    wordIsInMatrix = True
                else:  # Recurse
                    currentLetterIndex += 1
                    nextPositionDown = [currentPosition[0] + 1, currentPosition[1]]
                    nextPositionRight = [currentPosition[0], currentPosition[1] + 1]
                    nextPositions = [nextPositionDown, nextPositionRight]
                    for pos in nextPositions:
                        if pos[0] < len(matrix[:, 0]) and pos[1] < len(matrix[0, :]):
                            wordIsInMatrix = searchWord(matrix, pos, currentLetterIndex, wordAsList, wordIsInMatrix)
            else:
                currentLetterIndex += 1
                wordIsInMatrix = False

    return wordIsInMatrix


print(findWordInMatrix(np.array([['F', 'A', 'C', 'I'],
                                 ['O', 'B', 'Q', 'P'],
                                 ['A', 'N', 'O', 'B'],
                                 ['M', 'A', 'S', 'S']]), 'FACQO'))
