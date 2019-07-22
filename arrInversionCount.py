invCount = 0

def arrInvCount(arr,n,ind):
    global invCount

    for i in arr[ind+1:]:
        if n > i:
            invCount += 1

    if ind+1 < len(arr) - 1:
        arrInvCount(arr,arr[ind+1],ind+1)        

    return invCount 

a = [3,1,5,6,2,7]

invertedCount = arrInvCount(a,a[0],0)

print(invertedCount)