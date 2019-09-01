# Implement division of two positive integers without using the division, multiplication,
# or modulus operators. Return the quotient as an integer, ignoring the remainder.

import math

def division(num1, num2):
    # Initialize counter variable that stores the number of times num2 fits in num1
    numTimes = 0
    # Initialize the division quotient
    quotient = 0
    while True:
        # Avoid infinite loop in case num2 is 0
        if num2 == 0:
            quotient = math.inf
            break
        else:
            numTimes += num2
            if numTimes <= num1:
                quotient += 1
            else:
                break
    return quotient

print( division( 50, 2 ) )