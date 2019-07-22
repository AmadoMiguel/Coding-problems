# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 05:39:06 2019

@author: migue
"""
import re,operator

words = ['reto', 'un', 'interesante', 'aun', 'mas']
word = 'unretoaunmasinteresante'

matchIndeces = []

for w in words:
    if re.search(w,word):
        indx = word.index(w)
        # Inside this array, rely the indices of the words appereances on
        # the joined word
        matchIndeces.append(indx)
# If the specified word can be conformed with the words in the array...
if len(matchIndeces) == len(words):
    # Now, a dictionary is created in order to map each word with its appereance 
    # index
    wordsAndIndx = {}   
    wordsInd = 0
    for indx in matchIndeces:
        wordsAndIndx[words[wordsInd]] = indx
        wordsInd += 1    
    # Sort dictionary based on values
    sortedDict = sorted(wordsAndIndx.items(),key=operator.itemgetter(1))
    wordsJoined = ''
    for t in sortedDict:
        wordsJoined += t[0]
    print(wordsJoined)
# Otherwise, print it's not possible
else:
    print("The word couldn't be conformed")

    
    