# Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at
# the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).
#
# Given integers N and X, write a function that returns the number of times X appears as a value
# in an N by N multiplication table


# The fastest approach should be counting the number of multiples X has in the list from 1 to N

def numTimesXinTable(N, X):
    nMultiples = len([n for n in range(1, N+1) if X % n == 0 and n != 1])
    return nMultiples


print(numTimesXinTable(8, 24))