# Given a string, determine whether any permutation of it is a palindrome.
#
# For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome.
# daily should return false, since there's no rearrangement that can form a palindrome.


def checkPalindromRearrange(word):
    # Transform to list for indexing purposes
    wordAsList = list(word)
    for i in range(len(wordAsList)):
        if i == 0:
            if wordAsList == wordAsList[::-1]:
                print(wordAsList)
                return True
        elif i == len(word) - 1:
            rearrangedFromLast = [wordAsList[i]] + wordAsList[:i]
            if rearrangedFromLast == rearrangedFromLast[::-1]:
                print(rearrangedFromLast)
                return True
        else:
            rearrangedFromOtherPosition = wordAsList[i:] + wordAsList[:i]
            if rearrangedFromOtherPosition == rearrangedFromOtherPosition[::-1]:
                print(rearrangedFromOtherPosition)
                return True
    return False


print(checkPalindromRearrange('carrace'))
