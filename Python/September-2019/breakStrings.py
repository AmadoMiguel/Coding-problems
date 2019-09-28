# Given a string s and an integer k, break up the string into multiple lines such that each line has a
# length of k or less. You must break it up so that words don't break across lines. Each line has to
# 'have the maximum possible amount of words. If there's no way to break the text up, then return null.

# You can assume that there are no spaces at the ends of the string and that there is exactly one space
# between each word.


def splitWordsByKChars(str, k):
    wordsLessThanLength = []
    joinedWords = ""
    # Get the words of the string
    words = str.split(" ")
    print(words)
    # Iterate over the words and see if each word length is less or equal than k to see if it
    # can be added to the final array
    for w in words:
        if len(w) <= k:
            if len(joinedWords) + len(w) <= k:
                if len(joinedWords) == 0:
                    joinedWords += w
                else:
                    joinedWords += " " + w
            else:
                wordsLessThanLength.append(joinedWords)
                joinedWords = w
                # Avoid ignoring the last word
                if w == words[-1]:
                    wordsLessThanLength.append(w)
        else:
            wordsLessThanLength.append("")
    # Avoid words missing in the final array
    if joinedWords not in wordsLessThanLength:
        wordsLessThanLength.append(joinedWords)
    return wordsLessThanLength


st = "the quick brown fox jumps over the lazy dog"
print(splitWordsByKChars(st, 12))
