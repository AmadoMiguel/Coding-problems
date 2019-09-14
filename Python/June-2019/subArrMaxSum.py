import numpy as np

subArr = []
indArr = 0
maxSum = 0
maxSumSubArr = []
nLoops = 0

def checkSubArraySum(arr,ind):
    global subArr
    global indArr
    global maxSum
    global maxSumSubArr
    global nLoops

    # Check sub array length in order to start sub array from another index
    if len(subArr) == len( range(indArr,len(arr)-1) )+1 or len(subArr) == len( range(indArr,len(arr)) )+1:
        # Restart sub array
        subArr = []
        # Add a loop
        nLoops += 1
        # Avoid index out of range
        if indArr < len(arr) : indArr += 1
        # Recall the function with new starting point
        checkSubArraySum(arr,indArr)    
        # Add next item
        subArr.append(arr[indArr])
    else:
        # Check continuously for the subarray with the max sum
        npSubArr = np.array(subArr)
        if np.sum(npSubArr) > maxSum:
            maxSum = np.sum(npSubArr)
            maxSumSubArr = subArr
        # Add next element to sub array
        subArr.append(arr[ind])
    print(subArr)
    # Check end of possible sub arrays condition
    if nLoops < len(arr)-2:
        checkSubArraySum(arr,ind+1)    
    else:
        return
    # Return maxSum and its corresponding subArray   
    return maxSum,maxSumSubArr    

print( checkSubArraySum([-52,0,1,9,-1,-5],0) )