
def containsCloseNums(nums, k):
    # Define indexes of number in a map
    indexesMap = {}
    index = 0
    distIndexes = None
    # Traverse all the list in order to avoid leaving loose ends...
    for n in nums:
        if n not in indexesMap.keys():
            indexesMap[n] = index
        else:
            # Only update the distance whenever it's <= k
            if abs(index - indexesMap[n]) <= k:
                distIndexes = abs(index - indexesMap[n])
            # Update the map in case there are more numbers after that
            # meet the condition
            indexesMap[n] = index
        # Update index of traversal of nums
        index += 1
    if distIndexes is not None:
        return True
    else:
        return False
