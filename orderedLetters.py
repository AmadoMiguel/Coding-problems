# You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns
# that can be removed to ensure that each row is ordered from top to bottom lexicographically.
# That is, the letter at each column is lexicographically later as you go down each row. It does
# not matter whether each row itself is ordered lexicographically.

import numpy as np

# A way of solving it should be comparing each last letter of each row to all letters on the next row

def checkOrderedLetters(lettersMatr):
    index = 0
    numColumnsToRemove = 0
    indecesOfRemovedColumns = []
    # Iterate over each row
    for r in lettersMatr:
        # Avoid index out of bounds
        if index + 1 < len(lettersMatr):
            # Index the current row in the last position to get the last letter of it
            lastLetterOfRow = r[-1]
            # Iterate over each letter of the next row and compare each to the last letter of the
            # current row
            for l in lettersMatr[index+1]:
                if lastLetterOfRow >= l:
                    # Take the index of the letter to be removed
                    indexOfRemoval = list(lettersMatr[index+1]).index(l)
                    # Check if it doesn't correspond to a column already considered to be removed
                    if indexOfRemoval not in indecesOfRemovedColumns:
                        numColumnsToRemove += 1
                        indecesOfRemovedColumns.append(indexOfRemoval)
        else:
            break
        index += 1
    return numColumnsToRemove, sorted(indecesOfRemovedColumns)


lettersMatr = np.array([['c', 'b', 'a'],
                        ['d', 'a', 'f'],
                        ['b', 'h', 'i']
                        ])
print("Column(s) to be removed and its index/indeces:", checkOrderedLetters(lettersMatr))
