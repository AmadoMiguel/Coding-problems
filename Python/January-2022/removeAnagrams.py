# Given a list of words, remove the ones that are anagrams from existing words

def isAnagram(word, set):
    word = "".join(sorted(word))
    if word in set:
        return True
    else:
        set[word] = True
        return False


def removeAnagrams(words):
    set = {}
    removedAnagrams = []
    for w in words:
        if not isAnagram(w, set):
            removedAnagrams.append(w)
    return removedAnagrams


print(removeAnagrams(["have","ahve","frame","avhe","farme","code","abc","ehav"]))
