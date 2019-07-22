array = [1,5,3,8,5,16,2]

nextInd = 1

for i in array[:-1]:
    if i > array[nextInd]:
        array[nextInd-1] = array[nextInd]
        array[nextInd] = i
        nextInd += 1
    else:
        nextInd += 1

print(array)