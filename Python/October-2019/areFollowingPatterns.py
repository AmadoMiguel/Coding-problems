
def areFollowingPatterns(strings, patterns):
    # Create a map to define the correspondences
    patternsMap = {}
    for i in range(len(strings)):
        if patterns[i] in patternsMap.values():
            prevKey = list(patternsMap.keys())[list(patternsMap.values()).index(patterns[i])]
            if prevKey != strings[i]:
                return False
        elif strings[i] in patternsMap.keys():
            prevVal = list(patternsMap.values())[list(patternsMap.keys()).index(strings[i])]
            if prevVal != patterns[i]:
                return False
        patternsMap[strings[i]] = patterns[i]
    return True
