# Given an integer n and a list of integers l, write a function that randomly generates
# a number from 0 to n-1 that isn't in l (uniform).

import random as rand


def genNumNoInList(n, lst):
    # Generate an integer random number between 0 and n-1
    randNum = rand.randint(0, n-1)
    # If the generated random number is in the list, slightly modify it
    if randNum in lst:
        randNum = randNum + ((rand.random()*0.9) + 0.1)
        randNum = round(randNum, 2)
    return randNum


lst = [1, 2, 6, 7, 8, 4, 0, 5]
n = 8
print(genNumNoInList(n, lst))
