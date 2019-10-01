# Given a string, find the longest palindromic contiguous substring. If there are more than one
# with the maximum length, return any one.

import numpy as np

palindromes = []
initIndex = 0
finalIndex = 2


def findPalindromeSubstrings(str):
    global palindromes
    global initIndex
    global finalIndex

    if len(str) < 3 and len(str) > 1:
        letts = str.split("")
        if letts[0] == letts[1]:
            palindromes.append(str)
            return palindromes
    elif len(str) == 1:
        palindromes.append(str)
        return palindromes
    else:
        # Slice the current substring
        currentSubString = "".join(list(str)[initIndex:finalIndex])
        # Get the reversed version
        reversedSubString = "".join(reversed(currentSubString))
        # Check equality and append to palindromes in case is a palindrome
        if currentSubString == reversedSubString and currentSubString not in palindromes:
            palindromes.append(currentSubString)
        # Update slice indexes
        if finalIndex < len(str) + 1:
            finalIndex += 1
            findPalindromeSubstrings(str)
        elif initIndex < len(str) - 2:
            initIndex += 1
            finalIndex = initIndex + 2
            findPalindromeSubstrings(str)
    return palindromes


print(findPalindromeSubstrings("bananas"))
