# You have 2 integers n and m representing an n by m grid, determine the number of ways you can get from the
# top-left to the bottom-right of the matrix y going only right or down.
# Example:
# n = 2, m = 2
# This should return 2, since the only possible routes are:
# Right, down
# Down, right.


def findWays(sizeMatrix,nWays,currPos, endPos):
    # rightPos
    # downPos
    # Do recursion for each position
    # Check x position
    # Check y position
    # print(currPos)
    if currPos[0] < endPos[0] and currPos[1] < endPos[1]:
        nWays += 1
    if currPos != endPos:
        rightPos = [currPos[0]+1, currPos[1]]
        downPos = [currPos[0], currPos[1] + 1]
        for pos in [rightPos, downPos]:
            if pos[0] <= endPos[0] and pos[1] <= endPos[1]:
                nWays = findWays(sizeMatrix, nWays, pos, endPos)
    # Exit recursion
    return nWays


sizeMatrix = [5, 5]
print(findWays(sizeMatrix, 1, [0, 0], [sizeMatrix[0]-1, sizeMatrix[1]-1]))
