from __future__ import division
from random import randint

def getNextPossibleMoves(x, y):
    return [
        (x + 2, y + 1), (x + 2, y - 1),
        (x - 2, y + 1), (x - 2, y - 1), 
        (x + 1, y + 2), (x + 1, y - 2),
        (x - 1, y + 2), (x - 1, y - 2) 
    ]

def isInBounds(x, y):
    if 0 <= x < 8 and 0 <= y <= 8:
        return True
    return False

def isKnightOnBoard(x, y, k, cache=[]):
    numMoves = 0
    # Get possible next moves of a check night ("L" movement)
    nextMoves = getNextPossibleMoves(x, y)
    # Choose a random move from the next possible moves
    randNext = randint(0, len(nextMoves) - 1)
    randomMove = nextMoves[randNext]

    perc = 100
    while numMoves < k:
        numMoves += 1
        print(randomMove)
        if not isInBounds(randomMove[0], randomMove[1]):
            perc -= (100 * (numMoves/k))
            break
        nextMoves = getNextPossibleMoves(randomMove[0], randomMove[1])
        randNext = randint(0, len(nextMoves) - 1)
        randomMove = nextMoves[randNext]
    return perc

print(isKnightOnBoard(0, 0, 5))
