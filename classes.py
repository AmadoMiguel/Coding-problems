# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 05:39:06 2019

@author: migue
"""

nRooms = 0
def nRoomsReq(schedule,ind):
    global nRooms   
    actClass = schedule[ind]
    prevClasses = schedule[0:ind]
    for c in prevClasses:
        # Avoid comparing to the same class
        if actClass[0] == c[0] and actClass[1] == c [1]:
            continue
        # Check if schedule between classes overlaps
        if actClass[0] <= c[1]:
            nRooms += 1       
            break
    if ind < len(schedule)-1:
        nRoomsReq(schedule,ind+1)
    else:
        return

s = [(30, 75), (0, 50), (60, 150),(55,70),(76,80)]
nRoomsReq(s,1)
print(nRooms)        