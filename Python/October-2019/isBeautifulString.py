# A string is said to be beautiful if each letter of the alphabet appears at most as many times as than the
# previous letter; ie: b occurs no more times than a; c occurs no more times than b; etc.
#
# Given a string, check whether it is beautiful.


def isBeautifulString(inputString):
    sortedStr = list(sorted(inputString))
    letsHist = {}
    for l in sortedStr:
        if l in letsHist:
            letsHist[l] += 1
        else:
            letsHist[l] = 1
    if list(letsHist.keys())[0] != 'a':
        return False
    prevNTimes = list(letsHist.values())[0]
    for i in range(1, len(list(letsHist.values()))):
        # If the previous letter in the alphabet appears the same or more times than
        # the next one
        if prevNTimes >= list(letsHist.values())[i]:
            # If the next letter in the histogram is the next letter in the alphabet
            if ord(list(letsHist.keys())[i-1])+1 == ord(list(letsHist.keys())[i]):
                prevNTimes = list(letsHist.values())[i]
                continue
            else:
                return False
        else:
            return False
    return True


print(isBeautifulString("bbbaacdafe"))
