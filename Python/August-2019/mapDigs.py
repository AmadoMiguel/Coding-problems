

def listsCombo(listOfLists, ptr1, ptr2):
    return findAllCombinations(listOfLists, ptr1, ptr2, [], [])


def findAllCombinations(allLists, p1, p2, currentCombo, allCombos):
    if p1 >= 0 and p2 >= 0:
        # Add number to current combination
        currentCombo.append(allLists[p1][p2])
        # New combination found
        if len(currentCombo) == len(allLists):
            allCombos.append(list(reversed(currentCombo)))
        # Analise next possible combination options
        nextOptions = [[p1 - 1, len(allLists[p1 - 1]) - 1], [p1, p2 - 1]]
        for o in nextOptions:
            if o[0] >= 0 and o[1] >= 0:
                allCombos = findAllCombinations(allLists, o[0], o[1], currentCombo, allCombos)
            else:
                if len(currentCombo):
                    del currentCombo[-1]
    return allCombos


# Get all combinations of these two lists
# arr = [[1, 2, 3], [4, 5, 6], [6], [7, 8]]
# arr = [[1, 2, 3], [4, 5, 6]]
arr = [[1, 2, 3], [4], [7, 9], [5, 8]]
finalPtr1, finalPtr2 = len(arr) - 1, len(arr[-1]) - 1
print(listsCombo(arr, finalPtr1, finalPtr2))
