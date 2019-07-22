# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 09:52:37 2019

@author: migue
"""

runMedian = []

def calcRunMedian(arr,ind):
    global runMedian
    
    # Retrieve (sorted) sub-array till the indicated index
    subArr = sorted(arr[:ind+1])
    # Check if length is even or odd in order to  calculate the median
    if len(subArr) % 2 != 0: # Odd
        # Median is the middlemost value in the array
        median = subArr[ round((len(subArr)-1)/2) ]
    else: # Even
        # Median is the average of the two middlemost values in the array
        median = (subArr[round(len(subArr)/2)-1] + subArr[round(len(subArr)/2)]) / 2
    # Add running median to the array    
    runMedian.append(median)
    
    # Check end condition of function call
    if ind < len(arr)-1:
        calcRunMedian(arr,ind+1)
    
        
nums = [2,1,5,7,2,0,5]
calcRunMedian(nums,0)
print(runMedian)