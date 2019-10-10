# Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral!
# You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its '
# content.
#
# The pixels in the input image are represented as integers. The algorithm distorts the input image in the following
# way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3
# square that has its center at x, including x itself. All the pixels on the border of x are then removed.
#
# Return the blurred image as an integer, with the fractions rounded down.

import numpy as np


def boxBlur(image):
    imageCopy = np.array(image)
    indxRow1 = 0
    indxRow2 = 3
    indx1Col = 0
    indx2Col = 3
    resultingMatrix = np.array(
        [[0 for _ in range(0, (len(imageCopy[0, :]) - 3) + 1)]
         for _ in range(0, (len(imageCopy[:, 0]) - 3) + 1)])
    currentFinalRow = 0
    currentFinalCol = 0
    while indxRow2 <= len(imageCopy[:, 0]) and indx2Col <= len(imageCopy[0, :]):
        currGrid = imageCopy[indxRow1:indxRow2, indx1Col:indx2Col]
        currentPixelValue = calculateCurrentPixel(currGrid)
        resultingMatrix[currentFinalRow, currentFinalCol] = currentPixelValue
        # Update grid slicing indexes
        if indx2Col + 1 <= len(imageCopy[0, :]):
            currentFinalCol += 1
            indx2Col += 1
            indx1Col += 1
        else:
            if indxRow2 + 1 <= len(imageCopy[:, 0]):
                indxRow2 += 1
                indxRow1 += 1
                currentFinalRow += 1
                currentFinalCol = 0
                indx1Col = 0
                indx2Col = 3
            else:
                break
    return resultingMatrix


def calculateCurrentPixel(currGrid):
    currentSum = 0
    for r in range(0, 3):
        for c in range(0, 3):
            currentSum += currGrid[r, c]
    return currentSum // 9
