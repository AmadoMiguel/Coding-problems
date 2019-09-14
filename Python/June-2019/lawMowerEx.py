import random,re
import numpy as np

class lawn():
    # Matrix that stores the height per 1x1m grass square
    pat = []
    # Heigth and width of the lawn
    M = 0
    N = 0
    # Position (x,y) of the mower
    # Can only be set while mower not in lawn
    posMow = []
    dirMow = " "
    # Direction of the mower
    def __init__(self,he,wi,initPos):
        # Define lawn dimensions
        self.M = he
        self.N = wi
        # Initialize grass heigth pattern
        self.pat = np.array([[100 for _ in range(0,self.N)] for _ in range(0,self.M)])
        # Define mower start position and direction
        self.posMow = initPos
    # Mow lawn method. Grass cuts are performed here.    
    def mowLawn(self,desPat):
        if self.posMow == [0,0]:
            if self.dirMow == 'S':
                self.pat[:,0] = desPat 
            if self.dirMow == 'E':
                self.pat[0,:] = desPat    
                
    def showGrassPat(self):
        # Show the user how the grass is being cut
        print(self.pat)               

# Initialize lawn and mower characteristics before the user test
l = lawn(4,4,[0,0])
l.showGrassPat()

# Perform an user test script
while True:    
    usrPatReq = str(input("Enter the pattern grass pattern you desire (put a dot at the end): "))
    if usrPatReq == "No":
        break
    grassPat = re.findall('([0-9]*)[,.]',usrPatReq)
    grassPat = [int(i) for i in grassPat]
    print(grassPat)
    usrPosReq = str(input("Enter the position from where you want to start mowing (only edges): "))
    mowPos = re.findall('[0-9]',usrPosReq)
    mowPos = [int(j) for j in mowPos]
    print(mowPos)
    l.posMow = mowPos
    mowDir = "E"
    l.dirMow = mowDir
    # Start mowing the lawn
    l.mowLawn(grassPat)

    l.showGrassPat()