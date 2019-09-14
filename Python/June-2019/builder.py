import numpy as np

def assignColors(N,K):
    houseMat = np.array( [[ 0 for _ in range(0,K) ] for _ in range(0,N)] )
    indHouse = 0
    indCol = 0
    colNum = 1
    while indHouse < len(houseMat[:,0]):
        houseMat[indHouse,indCol] = colNum
        indCol += 1
        indHouse += 1
        colNum += 1
        if indCol == len(houseMat[0,:]):
            indCol = 0
            colNum = 1
    return houseMat        

nHouses = 8
nColors = 6

housesAndColors = assignColors(nHouses,nColors)
print(housesAndColors)