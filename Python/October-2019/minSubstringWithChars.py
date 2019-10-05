import re


def minSubstringWithAllChars(s, t):
    # Get the characters
    chars = [c for c in t]
    ptr1 = 0
    ptr2 = len(t)
    minSubString = ""
    minLength = None
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        if s == t:
            return s
    if len(t) == 0:
        return ""
    while ptr1 <= len(s) - len(t):
        currSub = s[ptr1:ptr2]
        # Use regular expressions to visualize appereance of characters in the string
        appereances = re.findall("{}".format(chars), currSub)
        if len(appereances) > 0:
            if len(set(appereances)) == len(t):
                if minLength is None or len(currSub) < minLength:
                    minLength = len(currSub)
                    minSubString = currSub
        # Update pointers
        if ptr2 < len(s):
            ptr2 += 1
        else:
            ptr1 += 1
            ptr2 = ptr1 + len(t)
    return minSubString


print(minSubstringWithAllChars("zqyvbfeiee", "ze"))
