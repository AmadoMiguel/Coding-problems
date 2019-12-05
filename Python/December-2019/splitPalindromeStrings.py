# Given a string, split it into as few strings as possible such that each string is a palindrome.
#
# For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].
#
# Given the input string abc, return ["a", "b", "c"]


def collectAllPalindromesFromWord(wordAsList, ptr1, ptr2, palindromes):
    if ptr1 <= len(wordAsList) - 1:
        currentFragment = wordAsList[ptr1:ptr2]
        # Palindrome found
        if currentFragment == currentFragment[::-1]:
            palindromes.append("".join(currentFragment))
            del wordAsList[ptr1:ptr2]
            ptr1, ptr2 = 0, len(wordAsList)
            palindromes = collectAllPalindromesFromWord(wordAsList, ptr1, ptr2, palindromes)
        if ptr2 > ptr1:
            ptr2 -= 1
            palindromes = collectAllPalindromesFromWord(wordAsList, ptr1, ptr2, palindromes)
        else:
            ptr1 += 1
            ptr2 = len(wordAsList)
            palindromes = collectAllPalindromesFromWord(wordAsList, ptr1, ptr2, palindromes)
    return palindromes


word = "racecarannakayak"
# word = "abc"
print(collectAllPalindromesFromWord(list(word), 0, len(word), []))
