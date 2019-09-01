# Given an array of integers, write a function to determine whether the array could become
# non-decreasing by modifying at most 1 element.

# The rule is that there should not be more than one decrease in the array.

def checkNonDescendant(arr):
    # Initialize the number of decreases the array has
    nDecreases = 0
    # Initialize the number being evaluated
    evalNum = arr[0]
    index = 1
    # Iterate over the array from position #1 and compare if number is greater than the next one
    for n in arr[1:]:
        # If number being evaluated is greater than current number in array...
        if evalNum > n:
            # Add number of decreases
            nDecreases += 1
            # Update number being evaluated
            evalNum = arr[index]
            index += 1
        else:
            if index + 1 < len(arr):
                index += 1
                # Update number being evaluated
                evalNum = arr[index]
            else:
                break
    if nDecreases > 1:
        return "Array can't be transformed into non-decreasing"
    else:
        return "Array can be transformed into non-decreasing"

print( checkNonDescendant( [1,5,2,3,4] ) )