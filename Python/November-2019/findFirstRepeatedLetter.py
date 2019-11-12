# Given a string, return the first recurring character in it, or null if there is no recurring character.
#
# For example, given the string "acbbac", return "b". Given the string "abcdef", return null.


def findFirstRepeatedLetter(string):
    strAsList = list(string)
    firstIndexOfRepeated = None
    for i in range(len(strAsList)):
        currentLetter = strAsList[i]
        if currentLetter in strAsList[i+1:]:
            # Find index of repetition
            indexOfRepeated = i + 1 + strAsList[i+1:].index(currentLetter)
            if firstIndexOfRepeated is None or indexOfRepeated < firstIndexOfRepeated:
                firstIndexOfRepeated = indexOfRepeated
    return firstIndexOfRepeated, strAsList[firstIndexOfRepeated]


print(findFirstRepeatedLetter('acdoklmjoefebbac'))
