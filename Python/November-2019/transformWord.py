# Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence
# from start to end such that only one letter is changed at each step of the sequence, and each transformed word
# exists in the dictionary. If there is no possible transformation, return null. Each word in the dictionary have
# the same length as start and end and is lowercase.
#
# For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, return
# ["dog", "dot", "dat", "cat"].
#
# Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as there is no
# possible transformation from dog to cat.


def isDifferenceOneLetter(word1, word2) -> bool:
    noOfDifferences = 0
    word1List, word2List = list(word1), list(word2)
    for i in range(len(word1List)):
        if word1List[i] != word2List[i]:
            noOfDifferences += 1
    return noOfDifferences == 1


def isAnyLetterInSamePosition(word1, word2, currentWord) -> bool:
    word1List, word2List = list(word1), list(word2)
    for i in range(len(word1List)):
        if word1List[i] == word2List[i] and word1List[i] not in currentWord:
            return True
    return False


def isFinalWordInDictionary(word, dic) -> bool:
    return word in dic


def transformWordIfPossible(startWord, endWord, shortestTransform, currentWordInd, wordsDict) -> list:
    print(shortestTransform)
    if currentWordInd <= len(wordsDict) and isFinalWordInDictionary(endWord, wordsDict):
        if startWord != endWord and currentWordInd < len(wordsDict):
            # Check differences between current letter and goal letter
            if isDifferenceOneLetter(startWord, wordsDict[currentWordInd]):
                currentWord = wordsDict[currentWordInd]
                if isAnyLetterInSamePosition(currentWord, endWord, startWord):
                    startWord = currentWord
                    shortestTransform.append(currentWord)
            shortestTransform = transformWordIfPossible(startWord, endWord, shortestTransform,
                                                        currentWordInd + 1, wordsDict)
        elif endWord not in shortestTransform:
                shortestTransform = [None]
    else:
        shortestTransform = [None]
    return shortestTransform


print(transformWordIfPossible("dog", "cat", ["dog"], 0, ["dot", "dop", "dav", "mel", "cau", "cot", "cat", "cay"]))
