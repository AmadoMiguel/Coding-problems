# Given a list of integers, return the largest product that can be made by multiplying any three integers.

import numpy as np

def findMaxProdNums(lst):
    # First, copy the list in order to modify it
    listCopy = lst[:]
    # Next, convert all numbers to positive
    negIndeces = np.where(lst < 0)
    listCopy[negIndeces] *= (-1)
    # Then, sort the list
    listCopy = sorted(listCopy)
    # Now, return proper result
    if len(listCopy) < 3:
        return "This list only contains", len(listCopy), "elements."
    else:
        return np.array(listCopy[-3:])



lst = np.array([1, -20, 4, 5, 10, -45])
print(findMaxProdNums(lst))
