# Let X be a set of n intervals on the real line. We say that a set of points P "stabs" X if every interval in X
# contains at least one point in P. Compute the smallest set of points that stabs X.
#
# For example, given the intervals [(1, 4), (3, 5), (4, 5), (7, 9), (9, 12)], you should return [4, 9].


def findOverlapSegment(i1, i2):
    # Check overlap from last point of interval 1
    if i1[1] in range(i2[0], i2[1] + 1) or i2[0] in range(i1[0], i1[1] + 1):
        return [n for n in range(i2[0], i1[1] + 1)]
    return []


def mergeOverlappedIntervals(i1, i2):
    return i1[0], i2[1]


def findStabbingSegments(intervals):
    # Initialize final intervals array
    mergedOverlapped = [intervals[0]]
    stabbingSegments = []
    for i in intervals[1:]:
        placedOverlapped = False
        for mo in mergedOverlapped:
            overLapSeg = findOverlapSegment(mo, i)
            if len(overLapSeg):
                stabbingSegments += [overLapSeg]
                placedOverlapped = True
                mergedOverlapped[-1] = mergeOverlappedIntervals(mo, i)
                break
        if not placedOverlapped:
            mergedOverlapped += [i]
    print("Merged overlapped intervals", mergedOverlapped)
    return stabbingSegments


inters = [(1, 4), (5, 6), (7, 9), (9, 12)]
print("Stabbing points", findStabbingSegments(inters))
