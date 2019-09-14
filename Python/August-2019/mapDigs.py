
# Append each one of the elements to the number initialized inside a list in order
# to return the combinations for that number
def appendElem(num, arr):
    combs = []
    numAsList = [num]
    for i in arr:
        numAsList.append(i)
        combs.append(numAsList)
        numAsList = [num]
    return combs

# All combinations will be stored in this list
allCombs = []
# This function will store combination of the numbers of each list
def listsCombo(listOfLists, indexOfList):
    # Make the combinations array global
    global allCombs
    # If there is other list in the listOfLists after the current index position
    if indexOfList+1 < len(listOfLists):
        for i in listOfLists[indexOfList]:
            allCombs.append(appendElem(i, listOfLists[indexOfList+1]))
        if indexOfList + 1 == len(listOfLists)-1:
            return allCombs
        else:
            listsCombo(listOfLists, indexOfList+1)

# Get all combinations of these two lists
arr = [[1, 2, 3], [4, 5, 6]]
print(listsCombo(arr,0))