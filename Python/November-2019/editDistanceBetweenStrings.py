# Given two strings, determine the edit distance between them. The edit distance is defined as the minimum
# number of edits (insertion, deletion, or substitution) needed to change one string to the other.
#
# For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).

# Use the edit distance table theory (Stanford university)

import numpy as np


def findEditDistanceBetweenWords(word1, word2):
    editDistanceTable = np.array([[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)])
    # Initialize first row and column properly
    (editDistanceTable[:, 0], editDistanceTable[0, :]) = (range(len(word2)+1), range(len(word1)+1))
    # Based on the table, find the edit distance
    return findMinEditDistance(editDistanceTable, list(word1), list(word2))


def findMinEditDistance(editDistanceTable, word1, word2):
    currentEditDistance = 0
    for i in range(len(editDistanceTable[0, :]) - 1):
        for j in range(len(editDistanceTable[:, 0]) - 1):
            # According to edit distance table theory
            previousRowSameCol = editDistanceTable[j, i + 1] + 1
            previousColSameRow = editDistanceTable[j + 1, i] + 1
            if word1[i] != word2[j]:
                # Originally update requires a deletion and an insert (2 operations)
                # But for the case of this exercise, is going to be assumed as 1 operation
                previousAdjacentDiag = editDistanceTable[j, i] + 1
            else:
                previousAdjacentDiag = editDistanceTable[j, i]
            # Get the minimum
            currentEditDistance = min(previousAdjacentDiag, previousColSameRow, previousRowSameCol)
            # Update edit distance in the table
            editDistanceTable[j + 1, i + 1] = currentEditDistance
    editDistanceTable[-1, -1] = currentEditDistance
    print(editDistanceTable)
    return currentEditDistance


print(findEditDistanceBetweenWords('catzilla', 'rats'))
