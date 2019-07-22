import numpy as np

def compareNums(i1,j1,i2,j2,m):
    # Convert matrix into list (row-wise)
    mToLi = [n for l in m for n in l]
    print(mToLi)
    # First index in list (2D to 1D coordinates transformation)
    ind1 = (i1*len(m[0])) + j1
    # Second index in list (2D to 1D coordinates transformation)
    ind2 = (i2*len(m[0])) + j2
    # Count hoy many numbers smaller than the number at ind1
    print(mToLi[ind1],mToLi[ind2])
    n1 = len( [n for n in mToLi if n < mToLi[ind1]] )
    # Count hoy many numbers greater than the number at ind2
    n2 = len( [n for n in mToLi if n > mToLi[ind2]] )
    # Print result
    print( n1 + n2 )

A = [[1, 3, 7, 10, 15, 20],
    [2, 6, 9, 14, 22, 25],
    [3, 8, 10, 15, 25, 30],
    [10, 11, 12, 23, 30, 35],
    [20, 25, 30, 35, 40, 45]]

compareNums(1,0,1,3,A)