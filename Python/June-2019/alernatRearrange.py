altArr = []
ind = 0

def alternRearrange(arr,i,lArr):
    global altArr
    global ind
    
    if i % 2 == 0:
        altArr.append(max(arr))
        arr.remove(max(arr))
    else:
        altArr.append(min(arr))
        arr.remove(min(arr))

    if i < lArr-1:
        ind += 1
        alternRearrange(arr,ind,lArr)
    
    return altArr

arr = [1,2,3,4,5,6]
newArr = alternRearrange(arr,0,len(arr))
print(newArr)