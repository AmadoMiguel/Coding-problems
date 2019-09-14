import numpy as np
import os

# Clear console function
clear = lambda: os.system('clear')      

def conformStructure():
    # Ask the user for the width of the structure
    nCol = int(raw_input("# of total columns: "))
    # Ask the user for the number of traps per column
    nTrapsPerCol = []
    def putColumns(nCol):
        if nCol > 0:
            nTraps = int(raw_input("# of traps for column %s"%(str(nCol))+": "))
            # Organize the number of traps per column in a list
            nTrapsPerCol.append(nTraps)
            putColumns(nCol-1)
    putColumns(nCol)
    nTrapsPerCol.reverse()
    # Then, create a numpy array that represents the general structure
    genStruct = np.array( [["   " for _ in range(0,nCol)] for _ in range(0,max(nTrapsPerCol))] )
    # Function that creates the general structure
    def locateTraps(i,c):
        # Locate traps for column i
        lastPos = len(genStruct[:,0])-1
        for t in range(lastPos,lastPos-nTrapsPerCol[i],-1):
            genStruct[t,c] = "|_|"
        if c < len(genStruct[0,:])-1:
            locateTraps(i+1,c+1)    
    locateTraps(0,0)    
    return genStruct

# Then, calculate the number of in-between gaps
waterUnits = 0
def calculateWaterUnits(trap):
    startInd = 0
    # Remove the row with only one trap
    for r in trap:
        # Cast to list in order to access the count method
        r = list(r)
        if r.count("|_|") == 1:
            startInd += 1
        else:
            break
    # Function to calculate in-between blank spaces        
    def calcBlankSpaces(ind):
        global waterUnits
        for i in trap[ind,:]:
            if i != "|_|":
                waterUnits += 1
        if ind < len(trap[:,0])-1:
            calcBlankSpaces(ind+1)        

    calcBlankSpaces(startInd)    
    return waterUnits       

# Clear the console
clear()
trapWater = conformStructure()
wUnits = calculateWaterUnits(trapWater)
print(trapWater)
print(wUnits)