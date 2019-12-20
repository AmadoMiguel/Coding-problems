# Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset
# (i, j) satisfies either i % j = 0 or j % i = 0.
#
# For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24],
# return [1, 3, 6, 24].


def satifiesModulo(arr):
    for i in range(len(arr) - 1):
        n1 = arr[i]
        for j in range(i + 1, len(arr)):
            n2 = arr[j]
            if n2 > n1:
                if n2 % n1 != 0:
                    return False
            elif n1 > n2:
                if n1 % n2 != 0:
                    return False
    return True


def findLongestModuloSubArray(arr, remElems, longestSubArray):
    if len(arr) >= 2:
        if satifiesModulo(arr):
            if longestSubArray is None or len(arr) > len(longestSubArray):
                longestSubArray = arr

    if len(remElems):
        for i in range(len(remElems)):
            currArr = arr + [remElems[i]]
            longestSubArray = findLongestModuloSubArray(currArr, remElems[i+1:], longestSubArray)

    return longestSubArray


nums = [5, 4, 3, 1, 100, 49, 200, 7, 10, 11, 21, 20, 30]
# nums = [1, 3, 6, 24]
# nums = [3, 5, 10, 20, 21]
print(findLongestModuloSubArray([], nums, []))
