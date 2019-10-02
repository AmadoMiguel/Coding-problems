# You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

import numpy as np


def rotateImage(a):
    copyOfArr = np.array(a)
    copyOfArr = np.transpose(copyOfArr)
    rotated = []
    for r in copyOfArr:
        rotated.append(np.flip(r))
    return rotated


print(rotateImage([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]))
