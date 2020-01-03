# Given a string with a certain rule: k[string] should be expanded to string k times. So for example, 3[abc] should
# be expanded to abcabcabc. Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.


# This function assumes the encoded string is well formed
def decodeString(encodedString):
    stringAsList = list(encodedString)
    while '[' in stringAsList and ']' in stringAsList:
        # Find index of brackets and number, and concatenate [enclosed] sub array the amount specified there
        # from the first index of ]. Repeat process until there are no more '[' or ']' in the array
        lastNumIndx = len(stringAsList) - 1 - (stringAsList[::-1].index('[') + 1)
        nTimes = int(stringAsList[lastNumIndx])
        lastOpenIndx = lastNumIndx + 1
        firstCloseIndx = stringAsList.index(']')
        innerStr = stringAsList[lastOpenIndx + 1: firstCloseIndx]
        del stringAsList[firstCloseIndx]
        stringAsList[:firstCloseIndx] += (innerStr * (nTimes - 1))
        del stringAsList[lastOpenIndx]
        del stringAsList[lastNumIndx]
        print(stringAsList)
    return "".join(stringAsList)


# encStr = "3[abc]"
encStr = "2[a2[b]c]"
print(decodeString(encStr))
