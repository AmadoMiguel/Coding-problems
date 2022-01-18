# Write a function that takes a natural number as input and returns the number of digits the input has.
#
# Constraint: don't use any loops.

def getNumDigits(num):
    # Base Case
    if num < 10:
        return 1
    return 1 + getNumDigits(num/10)


print(getNumDigits(1))
