import random

def mergeSort():
    mergedSorted = []
    nLists = random.randint(2,5)
    listsSet = []
    for _ in range(nLists):
        nRandomNums = [random.randint(0,20) for _ in range(1,random.randint(2,5))]
        listsSet.append(nRandomNums)

    for lst in listsSet:
        for n in lst:
            if n in mergedSorted:
                continue    
            mergedSorted.append(n)

    return(sorted(mergedSorted))

print(mergeSort())