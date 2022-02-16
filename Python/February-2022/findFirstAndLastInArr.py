# Given a sorted array of ints 'arr' and an int 'target', find the index of the first and last pos of 'target' in 'arr'.
# If 'target' cannot be found in 'arr', return [-1, -1]

def findFirstAndLast(arr, target):
    lArr = len(arr)
    # Base cases
    if not lArr:
        return [-1, -1]
    if lArr == 1:
        if arr[0] == target:
            return [0, 0]
        else:
            return [-1, -1]
    p1, p2 = 0, lArr - 1
    # In case target is not within the array min and max
    if arr[p1] > target or arr[p2] < target:
        return [-1, -1]
    moveP1, moveP2 = True, True
    indxs, foundBoth = [-1, -1], False
    while p1 <= p2 and not foundBoth:
        if arr[p1] == target and moveP1:
            indxs[0] = p1
            moveP1 = False
        if arr[p2] == target and moveP2:
            indxs[1] = p2
            moveP2 = False
        if moveP1:
            p1 += 1
        if moveP2:
            p2 -= 1
        if not moveP2 and not moveP1:
            foundBoth = True
    return indxs


print(findFirstAndLast([2, 9, 4, 5, 5, 5, 5, 5, 7, 2, 9], 3))
