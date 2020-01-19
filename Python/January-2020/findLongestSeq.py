# You are given an array of integers. Return the length of the longest consecutive elements sequence in the array.
#
# For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence 1, 2, 3, 4, and thus,
# you should return its length, 4.


def findLengthOfLongestConsecSequence(nums):
    lenLongestSeq = 0
    # Sort the numbers
    sortedNums = sorted(nums)
    currNumConsec = 1
    prev, curr = sortedNums[0], None
    for n in sortedNums[1:]:
        curr = n
        print(prev, curr)
        if prev + 1 == curr:
            currNumConsec += 1
        else:
            currNumConsec = 0
        if currNumConsec > lenLongestSeq:
            lenLongestSeq = currNumConsec
        prev = curr
    return lenLongestSeq


print(findLengthOfLongestConsecSequence([100, 4, 200, 1, 3, 2]))
