# You have two integer arrays, a and b, and an integer target value v. Determine whether there is a pair
# of numbers, where one number is taken from a and the other from b, that can be added together to get a
# sum of v. Return true if such a pair exists, otherwise return false.
import numpy as np


def sumOfTwo(a, b, v):
    a = np.array(a)
    a = v - a
    b = np.array(b)
    filt = np.isin(b, a)
    return True in filt
