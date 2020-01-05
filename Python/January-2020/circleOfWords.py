# Two words can be 'chained' if the last character of the first word is the same as the first character of the
# second word.
#
# Given a list of words, determine if there is a way to 'chain' all the words in a circle.
#
# Example:
# Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
# Output: True
# Explanation:
# The words in the order of ['apple', 'eggs', 'snack', 'karat', 'tuna'] creates a circle of chained words.


def isCircle(words):
    if len(words):
        if words[-1][-1] == words[0][0]:
            for i in range(len(words)):
                if i < len(words) - 1:
                    if words[i][-1] != words[i + 1][0]:
                        return False
            return True
    return False


def findWordsCircle(currentWords, remainingWords):
    if not len(remainingWords):
        if isCircle(currentWords):
            print(currentWords)
            return True
    for i in range(len(remainingWords)):
        curr = currentWords + [remainingWords[i]]
        rem = remainingWords[:i] + remainingWords[i + 1:]
        if findWordsCircle(curr, rem):
            return True
    return False


words = ['eggs', 'karat', 'apple', 'snack', 'tuna']
print(findWordsCircle([], words))
