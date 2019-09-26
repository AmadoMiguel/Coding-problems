# Given a 2D matrix of characters and a target word, write a function that returns whether the word
# can be found in the matrix by going left-to-right, or up-to-down.

import numpy as np


def findWordInMatrix(mat, w):
    # Get the word length
    wordLength = len(w)
    # Get the indexes of appearance of the first letter of the word
    indexes = np.where(mat == w[0])
    rowIndexes = []
    colIndexes = []
    if len(indexes) > 0:
        for i in indexes[0]:
            rowIndexes.append(i)
        for j in indexes[1]:
            colIndexes.append(j)
        # Go into each index of appearance and find out if the word can be found from left to right
        # or from top to bottom
        mapOfIndeces = dict(zip(rowIndexes, colIndexes))
        print("Coordinates of appearance of the first letter of the word", mapOfIndeces)
        for r, c in mapOfIndeces.items():
            print("Current pair of coordinates", r, c)
            # Check from up to down
            if w == "".join(mat[r:r+len(w), c]):
                return "The word is in the matrix from up to down:", w, mat[r:r+len(w), c]
            # Check from left to right
            if w == "".join(mat[r, c:c+len(w)]):
                return "The word is in the matrix from left to right:", w, "to", mat[r, c:c+len(w)]
        return "The word is not in the matrix"
    else:
        return "The word is not in matrix"


word = 'IPB'
# Avoid repeated and contiguous (at the same time) letters
matrix = np.array([['F', 'A', 'C', 'I'],
                   ['O', 'B', 'Q', 'P'],
                   ['A', 'N', 'O', 'B'],
                   ['M', 'A', 'S', 'F']])

print(findWordInMatrix(matrix, word))
