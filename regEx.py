# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:06:49 2019

@author: migue
"""

def checkRegExMatch(regEx,str):
    dotIndx = regEx.index('.')
    if dotIndx == 0:
        # More than one character after regExp string pattern
        if '*' in regEx:
            # Search the index in which * appears
            crossInd = regEx.index('*')
            # Store the string pattern after the * character
            leftStr = regEx[crossInd+1:]
            # Try finding the stored string pattern index inside the string
            try:
                indxLeftStr = str.index(leftStr)
            except:
                indxLeftStr = None
            # Check for matching    
            if indxLeftStr and leftStr == str[indxLeftStr:]:
                return True
            else:
                return False
        # Only one character after regExp string pattern    
        else:
            if len(regEx) == len(str):
                if regEx[dotIndx+1:] == str[dotIndx+1:]:
                    return True
                else:
                    return False
    # Same process from above, but slightly different    
    else:
        if '*' in regEx:
            leftStr = regEx[:dotIndx]
            # Check for matching    
            if leftStr == str[:dotIndx]:
                return True
            else:
                return False
        else:    
            if regEx[:dotIndx] == str[:dotIndx]:
                return True
            else:
                return False

print( checkRegExMatch('art.*','artisimo') )