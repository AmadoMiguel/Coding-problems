subArr = []
foundSubArr = False
indArr = 0

def checkSubArraySum(arr,s,ind):
    global subArr
    global foundSubArr
    global indArr

    # Check sub array length in order to start sub array from another index
    if len(subArr) == len( range(indArr,len(arr)-1) ) or len(subArr) == len( range(indArr,len(arr)) ):
        # Restart sub array
        subArr = []
        # Avoid index out of range
        if indArr <= len(arr)-1 : indArr += 1
        # Recall the function with new starting point
        checkSubArraySum(arr,s,indArr)    
    else:
        # Add next element to sub array
        subArr.append(arr[ind])
    # Iterate over array to conform dynamic sub array and check its sum
    for n in arr[ind+1:]:
        subArr.append(n)
        # Check if the sum of the sub array elements corresponds to s
        if sum(subArr) == s:
            foundSubArr = True
            break
        else:
            # Take n out
            subArr.remove(n)     
    # Check if sub array was found in order to stop calling the function
    if not foundSubArr:
        checkSubArraySum(arr,s,ind+1)
    # Return the conformed sub array    
    return subArr    

print( checkSubArraySum([52,10,9,9,1,5],6,0) )