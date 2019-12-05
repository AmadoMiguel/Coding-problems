# Hi, here's your problem today. This problem was recently asked by AirBNB:
#
# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so
# that the result equals B.
#
# Example 1:
# Input: A = "ab", B = "ba"
# Output: true
# Example 2:
#
# Input: A = "ab", B = "ab"
# Output: false
# Example 3:
# Input: A = "aa", B = "aa"
# Output: true
# Example 4:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true


def swapTwoLetters(wordToSwapAsList, refWord, ptrw1, ptrw2, isSwappable):
    if ptrw2 < len(wordToSwapAsList) and not isSwappable:
        swappedWordAsList = wordToSwapAsList[:]
        let1 = swappedWordAsList[ptrw1]
        swappedWordAsList[ptrw1] = swappedWordAsList[ptrw2]
        swappedWordAsList[ptrw2] = let1
        joinedSwappedWord = "".join(swappedWordAsList)
        if joinedSwappedWord == refWord:
            isSwappable = True
        if ptrw2 + 1 < len(wordToSwapAsList):
            ptrw2 += 1
            isSwappable = swapTwoLetters(wordToSwapAsList, refWord, ptrw1, ptrw2, isSwappable)
        else:
            ptrw1 += 1
            ptrw2 = ptrw1 + 1
            isSwappable = swapTwoLetters(wordToSwapAsList, refWord, ptrw1, ptrw2, isSwappable)
    return isSwappable


word = "aaaaaaabc"
word2 = "aaaaaaacb"
print(swapTwoLetters(list(word), word2, 0, 1, False))
