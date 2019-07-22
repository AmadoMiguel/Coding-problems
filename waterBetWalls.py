# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 07:07:43 2019

@author: migue
"""

def fillWaterBetween(wallsArr):
    nWaterUnits = 0
    
    # Store first and last elements of the array
    firstWall = wallsArr[0]
    lastWall = wallsArr[-1]
    # Check which one is the max
    tallestWall = max([firstWall,lastWall])
    # Then iterate over the array and see the walls shorter than these ones
    for w in wallsArr:
        # Check if each wall is shorter than the tallest wall on one of the
        # extremes
        if w < max(wallsArr[0],wallsArr[-1]):
            # Add to the overall number of water units
            nWaterUnits += tallestWall - w
    return nWaterUnits        

walls = [2,1,3,5,0,3,2,0,5,2]
print("Number of water units to be stored:",fillWaterBetween(walls))