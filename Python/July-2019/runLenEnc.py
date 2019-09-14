# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 07:47:24 2019

@author: migue
"""

nLets = 1
encTxt = ''

def countLetts(s,i,prevLet):
    global nLets
    global encTxt
    if prevLet == s[i]:
        nLets += 1
    else:
        encTxt += str(nLets) + s[i-1] + ' ' 
        nLets = 1
    # Last letter
    if i == len(s) - 1:
        encTxt += str(nLets) + s[i]
    # Recursively call the function till i is out of range    
    if i < len(s)-1:
        countLetts(s,i+1,s[i])
    

string = "AAAABJBBCDA"
ind = 0
prevLet = string[ind]    
countLetts(string,ind+1,prevLet)
print(encTxt)