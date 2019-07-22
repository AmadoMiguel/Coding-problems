# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 20:20:38 2019

@author: migue
"""

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
phraseLength = 0
lineStr = ''
finalStr = ''
k = 16
for w in words:
    if phraseLength + len(w) < k and w != words[-1]:
        phraseLength += len(w) # Word length
        phraseLength += 1 # Whitespace
        lineStr += w + ' '
    else:
        # Avoid missing the last word
        if w == words[-1]:
            lineStr += w + ' '
        # Convert the line into an array    
        lineArr = lineStr.split(' ')
        # Delethe the last character (a blankspace)
        lineArr.remove(lineArr[-1])
        # Then, add spaces if needed to proper justify each line
        ind = 0 # Index of the word to add extra space to
        lenLine = len(lineStr) - 1 # Length of the line
        spReq = k - lenLine # Number of spaces required
        nSpaces = 0 # Counter for number of spaces added
        while nSpaces < spReq:
            # Restart the index to avoid non-even space add procedure
            if ind == len(lineArr)-1:
                ind = 0
            else:
                lineArr[ind] += ' ' # Add the space to the actual word
                ind += 1 # Go to next word
                nSpaces += 1 # Number of spaces added so far
        # Then, start the next line
        if w != words[-1]:
            lineStr = w + ' '
            phraseLength = len(w) + 1
        # Then, conform the final justified paragraph    
        # Separate each line with a comma (,)
        finalStr += ' '.join(lineArr) + ',' '\n'
  
print(finalStr)        