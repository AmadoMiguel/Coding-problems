# Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example,
# given the string "abracadabra" and the pattern "abr", you should return [0, 7].


def findPatternIndexes(string, pat):
    indexes = []
    indxOfFound = string.find(pat)
    rem = 0
    while indxOfFound != -1:
        print(string)
        indexes += [indxOfFound + rem]
        rem += len(string[:indxOfFound + 1])
        string = string[indxOfFound + 1:]
        indxOfFound = string.find(pat)
    return indexes


s = "abracadabraplazaabracreoteabrauinwhjwerabrtrhjk"
p = "abr"
print(findPatternIndexes(s, p))
