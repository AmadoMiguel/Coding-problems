# Given a non-empty list of words, return the k most frequent words. The output should be sorted from highest to
# lowest frequency, and if two words have the same frequency, the word with lower alphabetical order comes first.
# Input will contain only lower-case letters.
#
# Example:
# Input: ["daily", "interview", "pro", "pro",
# "for", "daily", "pro", "problems"], k = 2
# Output: ["pro", "daily"]


def getTopKWords(words, k):
    hist = {}
    for i in range(len(words)):
        hist[words[i]] = hist.setdefault(words[i], 0) + 1

    # Provide a callback to sort keys by value descending
    return sorted(hist, key=lambda keyVal:(keyVal[0], keyVal[1]), reverse=True)[:k]


print(getTopKWords(["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"], 2))
