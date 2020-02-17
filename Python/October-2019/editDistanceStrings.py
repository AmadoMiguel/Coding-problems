# Given two strings, determine the edit distance between them. The edit distance is defined as the
# minimum number of edits (insertion, deletion, or substitution) needed to change one string to the other


def checkEditDistance(str1, str2):
    # Create histogram of the characters of each string
    histStr1 = {}
    histStr2 = {}
    for l in str1:
        if l in histStr1:
            histStr1[l] += 1
        else:
            histStr1[l] = 1
    for l in str2:
        if l in histStr2:
            histStr2[l] += 1
        else:
            histStr2[l] = 1
    i = 0
    nEdits = abs(len(str1) - len(str2))
    while i < len(list(histStr1.keys())):
        # Calculate every time number of characters in strings
        nCharsStr1 = sum([v for v in histStr1.values()])
        nCharsStr2 = sum([v for v in histStr2.values()])
        # Check if current character from string 1 is in string 2
        if list(histStr1.keys())[i] in histStr2.keys():
            if histStr1[list(histStr1.keys())[i]] > histStr2[list(histStr1.keys())[i]]:
                nEdits += histStr1[list(histStr1.keys())[i]] - histStr2[list(histStr1.keys())[i]]
                histStr1[list(histStr1.keys())[i]] -= nEdits
        else:
            if nCharsStr1 == nCharsStr2:
                # Only update instead of removing the character from the string
                nEdits += 1
            else:
                # Has to be removed the number of times it appears in string 1
                nEdits += list(histStr1.values())[i]
                # Update the map in order to minimize future operations
                histStr1[list(histStr1.keys())[i]] = 0
        i += 1
    print(histStr1)
    print(histStr2)
    return nEdits


# checkEditDistance("xyzhi", "ahihi")
print(checkEditDistance("", "aabge"))
