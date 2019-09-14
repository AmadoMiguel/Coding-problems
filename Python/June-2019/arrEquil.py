indx = None

def findFirstEquil(arr,ind):
    global indx

    if sum( arr[:ind] ) == sum(arr[ind+1:]):
        indx = ind
    elif ind + 1 < len(arr):
        findFirstEquil(arr,ind+1)
        
    return indx
       
arr = [1,3,5,2,2,6,1]        
# Call the function, starting on position 1 of array (that is, 2nd position)
firEquPos = findFirstEquil(arr,1)

print(findFirstEquil(arr,1))