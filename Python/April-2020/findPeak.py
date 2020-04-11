# Given an unsorted array, in which all elements are distinct, find a "peak" element in O(log N) time.
#
# An element is considered a peak if it is greater than both its left and right neighbors. It is guaranteed that
# the first and last elements are lower than all others.


def findFirstPeak(nms,start,stop):
    if start < stop:
        mid = start + (stop-start)//2
        if nms[mid] > nms[mid-1] and nms[mid] > nms[mid+1]:
            return nms[mid]
        pL = findFirstPeak(nms,start,mid-1)
        if pL is not None:
            return pL
        pR = findFirstPeak(nms,mid+1,stop)
        if pR is not None:
            return pR
    return None


def findPeak(nums):
    start,stop=0,len(nums)
    return findFirstPeak(nums,start,stop)


tests = [[1,2,3,1], [1,2,1,3,5,6,4], [10, 20, 15, 2, 23, 90, 67], [1, 1, 1, 1, 1, 1, 1]]
for t in tests:
    print(findPeak(t))
