# You are given a string s, and an integer k. Return the length of the longest substring in s that contains at most
# k distinct characters.
#
# For instance, given the string:
# aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.


def getLongestSubStringWithKChars(s, k):
    return findLongestSubString(list(s), k, 0, k, None)


def findLongestSubString(s, k, ptr1, ptr2, longestSubstr):
    currentSubStringAsList = s[ptr1:ptr2]
    print(currentSubStringAsList)
    if len(set(currentSubStringAsList)) == k:
        if longestSubstr is None or len(currentSubStringAsList) > len(longestSubstr):
            longestSubstr = "".join(currentSubStringAsList)
    if ptr1 < len(s) - k:
        if ptr2 + 1 <= len(s):
            ptr2 += 1
        else:
            ptr1 += 1
            ptr2 = ptr1 + k
        longestSubstr = findLongestSubString(s, k, ptr1, ptr2, longestSubstr)
    return longestSubstr


print(getLongestSubStringWithKChars("aabcdefff", 3))
