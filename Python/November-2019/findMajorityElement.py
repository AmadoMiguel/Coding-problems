from math import floor

# Given a list of elements, find the majority element, which appears more than half the time
# (>floor(len(lst) / 2.0)


def findMajorityElement(numsList):
    # Create histogram
    numsHist = {}
    # Fill histogram
    for n in numsList:
        if n in numsHist.keys():
            numsHist[n] += 1
        else:
            numsHist[n] = 1
    # Check amount of times numbers appear and find out majority element
    if any(numTimes > floor(len(numsList) / 2.0) for numTimes in numsHist.values()):
        for n, nTimes in numsHist.items():
            if nTimes > floor(len(numsHist) / 2.0):
                return n
    return None


print(findMajorityElement([1, 2, 1, 1, 3, 4, 0]))
