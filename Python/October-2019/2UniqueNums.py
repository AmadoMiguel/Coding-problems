# Given an array of integers in which two elements appear exactly once and all other elements appear exactly
# twice, find the two elements that appear only once.
#
# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.


def find2UniqueNums(arr):
    uniqueNums = [0, 0]
    indxOfUnique = 0
    for i in range(len(arr)):
        if arr[i] not in arr[i+1:] and arr[i] not in arr[:i]:
            uniqueNums[indxOfUnique] = arr[i]
            indxOfUnique += 1
    return uniqueNums


print(find2UniqueNums([2, 4, 6, 8, 10, 2, 6, 10]))
