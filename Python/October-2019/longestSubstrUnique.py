# Find longest substring with unique characters


def findLongestSubString(string):
    return checkCurrentSubString(string, 0, 1, "", 0)


def checkCurrentSubString(string, ptr1, ptr2, longSubStr, lenLongestSubStr):
    # Convert current sub-string into list
    subStrAsList = list(string[ptr1:ptr2])
    # If current sub-string contains non-repeated characters
    if len(set(subStrAsList)) == len(subStrAsList):
        # Check length and compare to longest so far
        if len(subStrAsList) > lenLongestSubStr:
            lenLongestSubStr = len(subStrAsList)
            longSubStr = "".join(subStrAsList)
    # Check pointers for recursion
    if ptr1 < len(string) - 1:
        if ptr2 < len(string):
            ptr2 += 1
            longSubStr = checkCurrentSubString(string, ptr1, ptr2, longSubStr, lenLongestSubStr)
        else:
            ptr1 += 1
            ptr2 = ptr1 + 1
            longSubStr = checkCurrentSubString(string, ptr1, ptr2, longSubStr, lenLongestSubStr)
    return longSubStr


print(findLongestSubString("whateabcdefghijkerstringyfezwxyo"))
