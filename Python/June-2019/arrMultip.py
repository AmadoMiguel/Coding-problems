import numpy as np

def arrMultOtherIndeces(arr):
    newArr = []

    for i in arr:
        newArr.append( np.prod( [ j for j in arr if j != i ] ) )
    print(newArr)    

arr = [1,2,5]
arrMultOtherIndeces(arr)