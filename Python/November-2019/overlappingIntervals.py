# You are given an array of intervals - that is, an array of tuples (start, end). The array may not be sorted,
# and could contain overlapping intervals. Return another array where the overlapping intervals are merged.
#
# For example:
# [(1, 3), (5, 8), (4, 10), (20, 25)]
#
# This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).


def mergeOverlappingIntervals(i, mergedIntervals, currIndexMerge):
    print(i, mergedIntervals)
    if len(mergedIntervals):
        if len(i):
            currentInterval = i[0]
            currentMergedInterval = mergedIntervals[currIndexMerge]
            if any(n for n in currentInterval if n in range(currentMergedInterval[0],
                                                            currentMergedInterval[1] + 1)):
                mergedIntervals[currIndexMerge] = (min(currentMergedInterval[0], currentInterval[0]),
                                                   max(currentMergedInterval[1], currentInterval[1]))
                del i[0]
                mergedIntervals = mergeOverlappingIntervals(i, mergedIntervals, currIndexMerge)
            else:
                mergedIntervals.append(currentInterval)
                del i[0]
                mergedIntervals = mergeOverlappingIntervals(i, mergedIntervals, currIndexMerge + 1)
    elif len(i):
        mergedIntervals.append(i[0])
        del i[0]
        mergedIntervals = mergeOverlappingIntervals(i, mergedIntervals, currIndexMerge)
    return mergedIntervals


intervals = [(1, 3), (5, 8), (2, 6), (4, 10), (12, 21), (20, 25)]
sortedIntervals = list(sorted(intervals))
print(mergeOverlappingIntervals(sortedIntervals, [], 0))
