# Given a list of words in a string, reverse the words in-place (ie don't create a new string and reverse the words).
# Since python strings are not mutable, you can assume the input will be a mutable sequence (like list).


def swapWords(w1, w2):
    temp = w1
    w1, w2 = w2, temp
    return w1, w2


def reverseWords(words):
    start, end = 0, len(words) - 1
    while start < end:
        words[start], words[end] = swapWords(words[start], words[end])
        start, end = start + 1, end - 1


wordsList = "Where is my cat".split(" ")
reverseWords(wordsList)
print(" ".join(wordsList))
