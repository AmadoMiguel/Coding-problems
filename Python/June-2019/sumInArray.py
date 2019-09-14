# Global variable had to be used in order to recall
# the sumNums function and avoid re-initializing it
totalSum = 0

def sumNums(l):
    global totalSum
    for item in l:
        # Check for lists inside the list and so on
        if isinstance(item,list):
            # Important to use recursion
            sumNums(item)
        else:
            totalSum += item
    return totalSum   

print( sumNums( [ 1,2,[ 3,4,[ 5,[ 1,2,3 ] ] ],3 ] ) )