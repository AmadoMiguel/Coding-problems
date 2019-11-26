# Given a string s and a list of words words, where each word is the same length, find all starting indices
# of substrings in s that is a concatenation of every word in words exactly once.
#
# For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], since "dogcat" starts
# at index 0 and "catdog" starts at index 13.
#
# Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings composed of
# "dog" and "cat" in s.
#
# The order of the indices does not matter.


def findConcatWordsInString(s, words):
    sList = list(s)
    words, words2 = "".join(words), "".join(words[::-1])
    indexesOfConcat = []
    for i in range(len(sList)):
        if i + len(words) <= len(sList):
            sortedCurrent = "".join(sList[i: i + len(words)])
            if sortedCurrent == words or sortedCurrent == words2:
                print("Found one match:", sortedCurrent)
                indexesOfConcat.append(i)
    return indexesOfConcat


print(findConcatWordsInString("dogcatcatcodecatdog", ["cat", "dog"]))
