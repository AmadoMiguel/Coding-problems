import random

def selRanItem(st):
    # Random index within the set, generated with uniform probability.
    randInd = random.randint(0,len(st)-1)
    return st[randInd]
# This way the large set is not stored in memory, but passed to the function
print( selRanItem(range(0,100000)) )    