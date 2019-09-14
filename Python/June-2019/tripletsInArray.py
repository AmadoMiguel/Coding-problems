import re
triplets = []

def trInArr(arr,i1,i2):
    global triplets
    # Search for triplets    
    for n in arr[i2+1:]:
        if arr[i1] + arr[i2] == n:
            triplets.append([arr[i1],arr[i2],n])
    # Check indeces values and recall the function
    # Use recursivity avoiding out of range indexing
    if i2 < len(arr) - 2:
        trInArr(arr,i1,i2+1)     
    elif i1 < len(arr) - 3:
        trInArr(arr,i1+1,i1+2)
    return triplets        

arr = [1,2,3,4,7,6,9,10]
sumTrip = trInArr(arr,0,1)

print(sumTrip)