# Given a list of words, and an arbitrary alphabetical order, verify that the words are in order of the alphabetical order.
#
# Example:
# Input:
# words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"
#
# Output: False
# Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'


# -1 means the words are sorted
def compareWords(w1, w2, alphabet):
    ptr1, ptr2 = 0, 0
    while ptr1 < len(w1) and ptr2 < len(w2):
        if alphabet.index(w1[ptr1]) < alphabet.index(w2[ptr2]):
            return -1
        if alphabet.index(w1[ptr1]) > alphabet.index(w2[ptr2]):
            return 1
        ptr1, ptr2 = ptr1 + 1, ptr2 + 1
    if len(w2) > len(w1):
        return -1
    if len(w1) > len(w2):
        return 1
    return 0  # Default return


def checkIfWordsAreSorted(wordsList, alphaList):
    if len(wordsList):
        smallWord, indxOfSmallest = wordsList[0], 0
        for w in wordsList[1:]:
            comp = compareWords(smallWord, w, alphaList)
            if comp == -1 or comp == 0:
                smallWord = w
            elif comp == 1:
                return False
        return True
    return "No words in list"


alphabet = "zyxwvutsrqponmlkjihgfedcba"
alphaList = list(alphabet)

# words = ["abcd", "efgh"]
words = ["zyx", "zyxw", "zyxwy"]

print(checkIfWordsAreSorted(words, alphaList))
