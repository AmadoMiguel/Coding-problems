def findMaxPerSubArr(arr,k,ind):
    global maxPerSubArr
    print( max(arr[ind:ind+k]) )
    if ind+(k-1) < len(arr)-1:
        findMaxPerSubArr(arr,k,ind+1)

a = [10, 5, 2, 7, 8, 7]
findMaxPerSubArr(a,3,0)    