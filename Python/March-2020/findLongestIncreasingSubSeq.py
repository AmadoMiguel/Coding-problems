# Given a sequence of numbers in an array, find the length of its longest increasing subsequence (LIS).
# The longest increasing subsequence is a subsequence of a given sequence in which the subsequence's elements are in
# strictly increasing order, and in which the subsequence is as long as possible. This subsequence is not necessarily
# contiguous or unique.


def longestIncreasingSubsequence(sequence):
    longestSub = []
    numElems = 0
    for n in sequence:
        if not numElems or n > longestSub[-1]:
            longestSub.append(n)
            numElems += 1
        else:
            if numElems == 1:
                if n < longestSub[0]:
                    longestSub[0] = n
            else:
                for i in range(numElems):
                    if i == 0:
                        if n < longestSub[i] and n < longestSub[i + 1]:
                            longestSub[i] = n
                            break
                    elif i == numElems - 1:
                        if longestSub[i - 1] < n < longestSub[i]:
                            longestSub[i] = n
                            break
                    elif n < longestSub[i] and longestSub[i - 1] < n < longestSub[i + 1]:
                        longestSub[i] = n
                        break
    print(longestSub)
    return numElems


sequence = [1, 231, 2, 4, 89, 32, 12, 234, 33, 90, 34, 100]
longestSubLength = longestIncreasingSubsequence(sequence)
assert longestSubLength == 7
