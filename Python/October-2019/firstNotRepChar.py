# Given a string s consisting of small English letters, find and return the first
# instance of a non-repeating character in it. If there is no such character, return '_'.

def firstNotRepeatingCharacter(s):
    firstNotRepeated = '_'
    hist = {}
    for l in s:
        if l not in hist.keys():
            hist[l] = 1
        else:
            hist[l] += 1
    minorIndex = -1
    for k in hist.keys():
        if hist[k] == 1:
            if minorIndex == -1 or list(s).index(k) < minorIndex:
                minorIndex = list(s).index(k)
                firstNotRepeated = k
    return firstNotRepeated