# Given an array of integers, return a new array where each element in the new array is the number of smaller
# elements to the right of that element in the original input array.
#
# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:
#
# There is 1 smaller element to the right of 3
# There is 1 smaller element to the right of 4
# There are 2 smaller elements to the right of 9
# There is 1 smaller element to the right of 6
# There are no smaller elements to the right of 1


def findSmallerElementsToTheRight(arr, currInd):
    if currInd < len(arr) - 1:
        arr[currInd] = len([n for n in arr[currInd:] if n < arr[currInd]])
        findSmallerElementsToTheRight(arr, currInd + 1)
    return arr


print(findSmallerElementsToTheRight([3, 4, 9, 6, 1, 2, 5, 7, 0, 10], 0))
