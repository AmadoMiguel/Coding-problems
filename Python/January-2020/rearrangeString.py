# Given a string, rearrange the string so that no character next to each other are the same. If no such arrangement
# is possible, then return None.
#
# Example:
# Input: abbccc
# Output: cbcbca


def checkAdjacency(st):
    if len(st):
        curChar = st[0]
        for c in st[1:]:
            if curChar == c:
                return False
            curChar = c
        return True
    return True


# For now, kind of brute-force solution by checking a lot of the permutations of the string
# Find the first permutation that satisfies the requirement
def reArrangeString(currString, remainingChars, finalString):
    if finalString is None:
        if not len(remainingChars):
            if checkAdjacency(currString):
                finalString = currString
        for i in range(len(remainingChars)):
            # Truncate some unnecessary permutations
            if len(currString):
                if currString[-1] == remainingChars[0]:
                    break
            cur = currString + remainingChars[i]
            finalString = reArrangeString(cur,
                                          remainingChars[:i] + remainingChars[i+1:],
                                          finalString)
    return finalString


print(reArrangeString("", "abbccc", None))
