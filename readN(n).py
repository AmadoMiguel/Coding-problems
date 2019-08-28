# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 07:05:10 2019

@author: migue
"""

# This function reads N characters from a file, n times; each time it reads
# N characters it continues with the next N characters until the whole file is
# readed, or until n times are reached.

def readN(N,n,file):
    # Index of the slice start position of the file content
    index = 0
    # Array that holds the slices or portions of the file content
    portionsOfFile = []
    # Start reading the file, but check if the slice indeces are not out of
    # bounds
    for i in range(0,n): # Number of portions to be extracted from the file
        if index+N < len(file):
            portionsOfFile.append(file[index:index + N]) 
            index = index + N
        else:
            portionsOfFile.append(file[index:])
            break
    return portionsOfFile
    
# In this case, we will have a string instead of an external file

file = '''This string is going to be used for the example instead of opening an
 external file'''
print(readN(20,15,file))       