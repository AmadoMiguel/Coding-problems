newArr = []

def revSubArrs(arr,k,startInd,endInd):
    global newArr

    auxRevSub = arr[startInd:endInd]
    auxRevSub.reverse()
    newArr.append(auxRevSub)
    if endInd <= len(arr)-1:
        revSubArrs(arr,k,startInd+k,endInd+k)    
        
arr = [1,2,3,4,5,6,7,8,9,10]
revSubArrs(arr,3,0,3)    
print(newArr)