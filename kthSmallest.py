def findKthSmallest(arr,k):
    c = 0
    kthSmallest = None
    sortedArr = sorted(arr)
    print(sortedArr)
    for n in sortedArr:
        if kthSmallest == None or n != kthSmallest:
            kthSmallest = n
            c += 1
        if c >= k:
            return n
            break

a = [1,10,2,4,6,90,23,5,6,2,5]
kthSml = findKthSmallest(a,5)
print(kthSml)