# Given a list of integers, return the bounds of the minimum range that must be sorted so that the
# whole list would be sorted.
#
# Example:
# Input: [1, 7, 9, 5, 7, 8, 10]
# Output: (1, 5)
# Explanation:
# The numbers between index 1 and 5 are out of order and need to be sorted.


def swapNums(arr, indx1, indx2):
    temp = arr[indx1]
    arr[indx1] = arr[indx2]
    arr[indx2] = temp


def moveToBeginning(arr, indxOfMoved):
    wasMoved, finalIndex = False, indxOfMoved
    while finalIndex > 0:
        if arr[finalIndex] < arr[finalIndex - 1]:
            swapNums(arr, finalIndex, finalIndex - 1)
            finalIndex -= 1
            if not wasMoved:
                wasMoved = True
        else:
            break
    return wasMoved, finalIndex


def moveToEnd(arr, indxOfMoved):
    wasMoved, finalIndex = False, indxOfMoved
    while finalIndex < len(arr) - 1:
        if arr[finalIndex] > arr[finalIndex + 1]:
            swapNums(arr, finalIndex, finalIndex + 1)
            finalIndex += 1
            if not wasMoved:
                wasMoved = True
        else:
            break
    return wasMoved, finalIndex


def findSortingRange(arr):
    minSortIndx, maxSortIndx = None, None
    currIndx = 0
    while currIndx < len(arr):
        print(arr)
        if arr == list(sorted(arr)):  # If array is already sorted no need to resort
            break
        # If needed, move greater elements in the front to the end
        didMove, indxOfMove = moveToEnd(arr, currIndx)
        if didMove:
            if maxSortIndx is None or indxOfMove > maxSortIndx:
                maxSortIndx = indxOfMove

        # If needed, move smaller elements in the end to the front
        didMove, indxOfMove = moveToBeginning(arr, currIndx)
        if didMove:
            if minSortIndx is None or indxOfMove < minSortIndx:
                minSortIndx = indxOfMove

        # Advance normal array pointer
        currIndx += 1
    return minSortIndx, maxSortIndx


# a = [1, 7, 9, 5, 7, 8, 10]
a = [1, 7, 4, 2, 5, 3, 0, 5, 7, 9, 10]
print(findSortingRange(a))
