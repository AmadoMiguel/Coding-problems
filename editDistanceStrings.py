# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 07:28:53 2019

@author: migue
"""

def calcEditDistance(str1,str2):
    editDistance = 0
    
    # Convert both strings to arrays
    str1_arr = [str1[i] for i in range(0,len(str1))]
    str2_arr = [str2[i] for i in range(0,len(str2))]
    
    for ind in range(0,len(str2_arr)):
        if ind > len(str1_arr) - 1:
            break
        if str1_arr[ind] != str2_arr[ind]:
            editDistance += 1
            str1_arr[ind] = str2_arr[ind]
            
    # Then, compare length
    # If first array is shorter than second array
    if len(str1_arr) < len(str2_arr):
        for c in str2_arr[len(str1_arr):]:
            str1_arr.append(c)
            editDistance += 1
    # If is greater, elements must be deleted
    elif len(str1_arr) > len(str2_arr):
        for i in range(0,len(str1_arr)-len(str2_arr)):
            del str1_arr[-1]
            editDistance += 1
    print(str1_arr)
    print(str2_arr)
    return editDistance

string1 = "aghuacate"
string2 = "agua"
print(calcEditDistance(string1,string2))