def findLowIntArr(arr):
    # Store only positive integers in new array
    posInts = [i for i in arr if i >= 0]
    # All numbers are negative         
    if len(posInts) == 0:    
        lowInt = 1    
    else:
        # Sort integer numbers in array
        posInts = sorted(posInts)
        # Index variable
        ind = 0
        for p in posInts:
            # lowInt is the nest integer after the largest
            # int in the array.
            if ind == len(posInts)-1:
                lowInt = p + 1  
                break  
            # lowInt is the smallest integer not in array    
            elif p + 1 < posInts[ind + 1]:  
                lowInt =  p + 1
                break
            # Keep going inside array    
            else: 
                ind += 1
    return lowInt          

a = [-1, -2,-2, -1]
lInt = findLowIntArr(a)
print(lInt)