from __future__ import division
from math import ceil

def substractFractions(num1, den1, num2, den2):
    comDen = den1 * den2
    return ((comDen/den1) * num1) - ((comDen/den2) * num2), comDen


def expressAsEgyptianFraction(num, den):
    if num == 0 or den == 0:
        return ""
    # Get max unit fraction out of current fraction
    divCeil = int(ceil(den / num))
    newNum, newDen = substractFractions(num, den, 1, divCeil)
    return "1/" + str(divCeil) + " " + expressAsEgyptianFraction(newNum, newDen)

print(expressAsEgyptianFraction(12, 13))
