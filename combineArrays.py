# Second in each array
def secInArr(arr):
    return arr[1]

l1 = ['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5']
print( sorted(l1,key=secInArr) )