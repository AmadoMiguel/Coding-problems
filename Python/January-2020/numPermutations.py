# You are given an array of integers. Return all the permutations of this array.


def getNumsPermuts(currentNums, remainingNums, permuts):
    # Base case
    if not len(remainingNums):
        permuts += [currentNums]
    else:
        for i in range(len(remainingNums)):
            curPermut = currentNums + [remainingNums[i]]
            permuts = getNumsPermuts(curPermut,
                                     remainingNums[:i] + remainingNums[i+1:],
                                     permuts)
    return permuts


print(getNumsPermuts([], [1, 2, 3], []))
