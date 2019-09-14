# Find all possible permutations of a word
from math import factorial as f

def numPossibPerms(word):
    auxArr = []
    nRepLets = 0
    for l in word:
        if l in auxArr:
            nRepLets += 2
        auxArr.append(l)
    # Then determine how many permutations can be done
    nTotalPerm = f(len(originalWord)) / f(nRepLets)
    print(nTotalPerm)

originalWord = "Hello"
numPossibPerms(originalWord)