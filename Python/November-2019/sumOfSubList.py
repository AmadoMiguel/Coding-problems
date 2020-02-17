


from itertools import accumulate


def sum(i, j, lst):
    accumulatedList = [0] + list(accumulate(lst))
    print(accumulatedList)
    return accumulatedList[j] - accumulatedList[i]


print(sum(1, 7, [1, 2, 3, 4, 5, -1, 4, 6, 5, -2]))
