leaders = []
# Starts on second element of the array
indx = 0

def findLeaders(arr,ind):
    global leaders
    global indx
    isLeader = True

    for n in arr[indx+1:]:
        if arr[indx] >= n:
            continue
        else:
            isLeader = False
            break 

    if isLeader:
        if arr[indx] not in leaders: leaders.append(arr[indx])        

    if indx + 1 < len(arr):
        indx += 1
        findLeaders(arr,indx)      

    return leaders      

        
a = [7,4,5,7,3]
lead = findLeaders(a,indx)

print(lead)