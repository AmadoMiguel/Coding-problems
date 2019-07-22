from math import pow

pairs = []
arr1 = [1,2,3,6,5,8]
arr2 = [5,7,1,12,6,20]
secArrInd = 0

def checkPowPairs(a1,a2):
    global pairs
    global secArrInd

    y = a2[secArrInd]
    for x in a1:
        if pow(x,y) > pow(y,x):
            pairs.append((x,y))
            
    if secArrInd < len(a2) - 1:
        secArrInd += 1
        checkPowPairs(a1,a2)        

    return pairs


allPairs = checkPowPairs(arr1,arr2)
print(allPairs)