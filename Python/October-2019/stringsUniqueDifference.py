import itertools


def stringsRearrangement(inputArray):
    allPermutations = list(itertools.permutations(inputArray))
    return checkStringsArray(allPermutations)


def checkStringsArray(permuts):
    for p in permuts:
        # If this equals len(stringsArray) - 1, return True
        nUniqueConsecDiff = 0
        # Check current permutation behaviour
        for i in range(len(p)):
            if checkDifference(p[i], p[i + 1]):
                nUniqueConsecDiff += 1
        if nUniqueConsecDiff == len(p) - 1:
            return True
    return False


# Checks if the difference between the strings being compared
# is only 1 character
def checkDifference(str1, str2):
    nDiff = 0
    for i in range(len(str1)):
        if list(str1)[i] != list(str2)[i]:
            nDiff += 1
    if nDiff != 1:
        return False
    return True


print(stringsRearrangement(["abc",
 "bef",
 "bcc",
 "bec",
 "bbc",
 "bdc"]))
