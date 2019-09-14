from __future__ import division
import math,numpy as np


nPtsCrc = 0
nPtsSqr = 0


def countPoints(nSquare):
    global nPtsCrc,nPtsSqr
    # Try with random coordinates numbers
    if nSquare == 1:
        xStart,yStart = (0.0,0.0)
        xEnd,yEnd = (0.9,0.9)
    if nSquare == 2:
        xStart,yStart = (-0.9,-0.9)
        xEnd,yEnd = (-0.1,0.0)
    if nSquare == 3:
        xStart,yStart = (-0.9,0.0)
        xEnd,yEnd = (0.0,0.9) 
    if nSquare == 4:
        xStart,yStart = (0.0,-0.9)
        xEnd,yEnd = (0.9,0.0)                 

    # Try with random values
    nPtsCrc += len( [ (x,y) for x in np.arange(xStart,xEnd,0.1) for y in np.arange(yStart,yEnd,0.1) if round(math.pow(x,2) + math.pow(y,2),2)  <= round(1,2) ] ) 
    nPtsSqr += len( [ (x,y) for x in np.arange(xStart,xEnd,0.1) for y in np.arange(yStart,yEnd,0.1) if round(x + y,2) < round(2,2) ] )
    
    if nSquare < 4: 
        countPoints(nSquare+1)

    return nPtsCrc,nPtsSqr    

def calcPi(ptsCrc,ptsSqr):
    monteCarloPi = 4 * (ptsCrc/ptsSqr)
    return monteCarloPi

ptsCrc,ptsSqr = countPoints(1)
roundedPi = calcPi(ptsCrc,ptsSqr)

print(roundedPi)