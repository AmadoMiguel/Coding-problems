# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 01:29:22 2019

@author: migue
"""

arrBrack = []
isWellFormed = True

# Determine if string contains a sets of balanced brackets (well-formed)
def checkWellFormedBracks(arrStr,ind):
    global arrBrack
    global isWellFormed
    newAdded = arrStr[ind]
    arrBrack.append(arrStr[ind])
    print(arrBrack)
    if newAdded == ')':
        if '(' in arrBrack:
            indxOp = arrBrack.index( "(" )
            indxCl = arrBrack.index( ")" )
            if (indxCl - indxOp) % 2 == 0:
                isWellFormed = False  
                ind = 0
            else:
                arrBrack.remove('(')
                arrBrack.remove(')')
    elif newAdded == '(':
        if ')' in arrBrack:
            indxOp = arrBrack.index( "(" )
            indxCl = arrBrack.index( ")" )
            if (indxOp - indxCl) % 2 == 0:
                isWellFormed = False    
                ind = 0
            else:
                arrBrack.remove('(')
                arrBrack.remove(')')    
        else:
            isWellFormed = False
            ind = 0
    elif newAdded == ']':
        if '[' in arrBrack:
            indxOp = arrBrack.index( "[" )
            indxCl = arrBrack.index( "]" )
            if (indxCl - indxOp) % 2 == 0:
                isWellFormed = False  
                ind = 0
            else:
                arrBrack.remove('[')
                arrBrack.remove(']')    
    elif newAdded == '[':
        if ']' in arrBrack:
            indxOp = arrBrack.index( "[" )
            indxCl = arrBrack.index( "]" )
            if (indxOp - indxCl) % 2 == 0:
                isWellFormed = False     
                ind = 0
            else:
                arrBrack.remove('[')
                arrBrack.remove(']')     
        else:
             isWellFormed = False        
             ind = 0
    if newAdded == '}':
        if '{' in arrBrack:
            indxOp = arrBrack.index( "{" )
            indxCl = arrBrack.index( "}" )
            if (indxCl - indxOp) % 2 == 0:
                isWellFormed = False      
                ind = 0
            else:
                arrBrack.remove('{')
                arrBrack.remove('}')             
    if newAdded == '{':
        if '}' in arrBrack:
            indxOp = arrBrack.index( "{" )
            indxCl = arrBrack.index( "}" )
            if (indxOp - indxCl) % 2 == 0:
                isWellFormed = False
                ind = 0
            else:
                arrBrack.remove('{')
                arrBrack.remove('}')   
        else:
             isWellFormed = False      
             ind = 0
                
    if ind > 0:
        checkWellFormedBracks(arrStr,ind-1)
    return isWellFormed    
    
a =  "([)]"
print( checkWellFormedBracks(a,len(a)-1) )