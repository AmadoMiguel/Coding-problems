# Given a sorted array of integers arr and an integer num, find all possible unique subsets of arr that add up to num.
# Both the array of subsets and the subsets themselves should be sorted in lexicographical order.
#
# Example
#
# For arr = [1, 2, 3, 4, 5] and num = 5, the output should be
# sumSubsets(arr, num) = [[1, 4], [2, 3], [5]].


def findSubSet(currSub, currSum, currStr, remNums, rem, goalNum):
    if rem <= 0:
        if currSum == goalNum:
            if currStr not in findSubSet.found:
                findSubSet.found.add(currStr)
                findSubSet.uniqueSubSets.append(currSub)
    else:
        currRem = rem
        curr = remNums[0]
        indx = 0
        if currSum:
            for i in range(rem):
                currRem -= 1
                indx = i
                if curr >= currSub[-1]:
                    break
                curr = remNums[i]
        else:
            currRem -= 1
        if currSum + curr <= goalNum:
            findSubSet(currSub + [curr], currSum + curr, currStr + " " + str(curr),
            remNums[indx + 1:], currRem, goalNum)
        if currSum <= goalNum:
            findSubSet(currSub, currSum, currStr, remNums[indx + 1:], currRem, goalNum)


def sumSubsets(arr, num):
    findSubSet.found = set()
    findSubSet.uniqueSubSets = []
    findSubSet([], 0, "", arr, len(arr), num)
    return findSubSet.uniqueSubSets


assert sumSubsets([1, 2, 3, 4, 5], 5) == [[1, 4], [2, 3], [5]]  # True
assert sumSubsets([1, 2, 2, 3, 4, 5], 5) == [[1, 2, 2], [1, 4], [2, 3], [5]]  # True
assert sumSubsets([1, 1, 1, 1, 1, 1, 1, 1, 1], 9) == [[1, 1, 1, 1, 1, 1, 1, 1, 1]]  # True
