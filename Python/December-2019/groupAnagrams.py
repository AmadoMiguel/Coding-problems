# Given a list of words, group the words that are anagrams of each other. (An anagram are words
# made up of the same letters).
#
# Example:
#
# Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
# Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]


def areAnagram(w1, w2):
    if len(w1) == len(w2):
        for l in w1:
            if l not in w2:
                return False
        return True
    return False


def groupAnagrams(words):
    groupedAnas = []
    for w in words:
        placedAnagram = False
        if not len(groupedAnas):
            groupedAnas += [[w]]
            continue
        for g in groupedAnas:
            if areAnagram(w, g[0]):
                g += [w]
                placedAnagram = True
                break
        if not placedAnagram:
            groupedAnas += [[w]]
    return groupedAnas


words = ["abc", "bca", "efg", "feg", "dce", "bed", "acb"]
print(groupAnagrams(words))
