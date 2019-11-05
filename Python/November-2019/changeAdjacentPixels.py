# Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace
# the color of the given pixel and all adjacent same colored pixels with C.
#
# For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:
#
# B B W
# W W W
# W W W
# B B B
# Becomes
#
# B B G
# G G G
# G G G
# B B B

import numpy as np


def changeAdjacentPixels(matrix, pixelLocation, color):
    copyOfMatrix = np.array(matrix)
    # Handle pixelLocation out of bounds possible error
    if pixelLocation[0] > len(copyOfMatrix[:, 0]) - 1 or pixelLocation[1] > len(copyOfMatrix[0, :]) - 1:
        return "Pixel location out of bounds"
    # Change the color of the pointed pixel
    originalPixelColor = copyOfMatrix[pixelLocation[0], pixelLocation[1]]
    copyOfMatrix[pixelLocation[0], pixelLocation[1]] = color
    return changePixelColor(copyOfMatrix, pixelLocation, originalPixelColor, color)


# The idea is to use recursion to change the color of the adjacent pixels and spread the color change
# taking into account that the color must be the same. The recursion finishes when the adjacent cells
# are out of bounds
def changePixelColor(matrix, currentPixel, originalPixelColor, newPixelColor):
    print(matrix, currentPixel)
    # First get adjacent pixels to current one
    adjacentDown = [currentPixel[0] + 1, currentPixel[1]]
    adjacentUp = [currentPixel[0] - 1, currentPixel[1]]
    adjacentLeft = [currentPixel[0], currentPixel[1] - 1]
    adjacentRight = [currentPixel[0], currentPixel[1] + 1]
    adjacentPixels = [adjacentUp, adjacentDown, adjacentLeft, adjacentRight]
    if 0 <= currentPixel[0] < len(matrix[:, 0]) and 0 <= currentPixel[1] < len(matrix[0, :]):
        for p in adjacentPixels:
            # Avoid index out of range
            if 0 <= p[0] < len(matrix[:, 0]) and 0 <= p[1] < len(matrix[0, :]):
                # Check if the color is the same, otherwise, go to the next available adjacent pixel
                if matrix[p[0], p[1]] == originalPixelColor:
                    matrix[p[0], p[1]] = newPixelColor
                    # Recurse in order to spread the change to all adjacent pixels possible
                    matrix = changePixelColor(matrix, p, originalPixelColor, newPixelColor)
    return matrix


print(changeAdjacentPixels([['B', 'B', 'W'],
                            ['W', 'W', 'W'],
                            ['W', 'W', 'W'],
                            ['B', 'B', 'B']], [1, 2], 'A'))
