def palindromeRearranging(inputString):
    histChars = {}
    for c in inputString:
        if c in histChars.keys():
            histChars[c] += 1
        else:
            histChars[c] = 1
    if len(inputString) % 2 != 0:
        # Determine palindrome behaviour by checking the histogram
        # there must be only 1 unique character
        nOddValues = 0
        for v in histChars.values():
            if v % 2 != 0:
                nOddValues += 1
        if nOddValues > 1:
            return False
        return True
    elif len(inputString) == 1:
        return True
    else:
        # All characters should appear odd # of times
        for v in histChars.values():
            if v % 2 != 0:
                return False
        return True


print(palindromeRearranging("aaabrrt"))
