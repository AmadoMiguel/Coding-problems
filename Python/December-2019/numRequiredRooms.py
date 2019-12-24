# You are given an array of tuples (start, end) representing time intervals for lectures. The intervals may be
# overlapping. Return the number of rooms that are required.
#
# For example. [(30, 75), (0, 50), (60, 150)] should return 2.


def timesOverlap(times1, times2):
    if any(n for n in times1 if n in range(times2[0], times2[1] + 1)):
        return True
    if any(n for n in times2 if n in range(times1[0], times1[1] + 1)):
        return True
    return False


def separateTimes(times):
    timesBlocks = []
    for t in times:
        if not len(timesBlocks):
            timesBlocks += [[t]]
            continue
        placedTimes = False
        # Go to currently separated times blocks, to see if:
        # The current new time overlaps with all, or...
        # It fits in to an existing block
        for b in timesBlocks:
            numNoOverlaps = 0
            for tb in b:
                if timesOverlap(tb, t):
                    continue
                numNoOverlaps += 1
            # If no overlap found, can be added to the current block (no need to separate a new classroom)
            if numNoOverlaps == len(b):
                b += [t]
                placedTimes = True
                break
        # If there was any overlap, separate a new classroom for this time block
        if not placedTimes:
            timesBlocks += [[t]]
    return timesBlocks


times = [(80, 95), (90, 104), (30, 75), (0, 50), (60, 150)]
sortedTimes = list(sorted(times))
separatedTimes = separateTimes(sortedTimes)
print(separatedTimes)
