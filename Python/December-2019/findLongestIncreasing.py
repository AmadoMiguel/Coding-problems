# You are given an array of integers. Return the length of the longest increasing subsequence
# (not necessarily contiguous) in the array.
#
# Example:
# [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
#
# The following input should return 6 since the longest increasing subsequence is 0, 2, 6, 9 , 11, 15.


def findLongestIncreasingSubSequence(sequence, remainingNums, longestSub):
    if not len(remainingNums):
        return True, longestSub
    else:
        for i in range(len(remainingNums)):
            seq = sequence
            if not len(sequence) or remainingNums[i] > sequence[-1]:
                seq = sequence + [remainingNums[i]]
            status, longestSub = findLongestIncreasingSubSequence(seq, remainingNums[i + 1:], longestSub)
            if status:
                if len(seq) > len(longestSub):
                    longestSub = seq
                    print(longestSub)
    return False, longestSub


numbers = [0, 13, 4, 12, 2, 10, 5, 14, 1, 9, 5, 13, 3, 11, 13, 7, 15]
print(findLongestIncreasingSubSequence([], numbers, []))
