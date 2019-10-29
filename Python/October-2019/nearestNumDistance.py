# Given an array of numbers and an index i, return the index of the nearest larger number of the number
# at index i, where distance is measured in array indices.
#
# For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.
#
# If two distances to larger numbers are the equal, then return any one of them. If the array at i
# doesn't have a nearest larger integer, then return null.
#
# Follow-up: If you can preprocess the array, can you do this in constant time?


import numpy as np


def findNearestNumberDistance(arr, indx):
    # Initial filter
    if indx < len(arr):
        if indx == len(arr) - 1:
            return np.where(np.array(arr) > arr[indx])[0][-1]
        if indx == 0:
            return np.where(np.array(arr) > arr[indx])[0][0]
        firstSubArr = np.where(np.array(arr[:indx]) > arr[indx])[0]
        secSubArr = np.where(np.array(arr[indx:]) > arr[indx])[0]
        if len(firstSubArr) and len(secSubArr):
            if abs(indx - firstSubArr[-1]) > abs(indx - (secSubArr[0]+1)):
                return secSubArr[0] + indx
            return firstSubArr[-1]
        elif len(firstSubArr):
            return firstSubArr[-1]
        elif len(secSubArr):
            return secSubArr[0] + indx
        else:
            return None
    else:
        return "Index out of bounds"


print(findNearestNumberDistance([5, 9, 1, 3, 6, 7, 10, 11, 4, 1, 3, 5, 6], 5))
