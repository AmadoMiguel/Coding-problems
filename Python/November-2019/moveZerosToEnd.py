# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order
# of the non-zero elements.
#
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations


def moveZerosToEnd(array, currInd):
    print(array)
    # Find 0 from the current index, remove it and append it
    if any(k for k in array[currInd:] if k != 0) and currInd < len(array):
        indexOfFirstZero = array[currInd:].index(0) + currInd
        del array[indexOfFirstZero]
        array.append(0)
        # Recurse
        moveZerosToEnd(array, indexOfFirstZero)
    return array


print(moveZerosToEnd([0, 1, 0, 2, 4, 0, 5, 0, 3, 9, 2, 3, 12], 0))
