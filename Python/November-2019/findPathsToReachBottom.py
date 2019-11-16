# You 2 integers n and m representing an n by m grid, get all possible ways you can get from the
# top-left to the bottom-right of the matrix y going only right or down.
#
# Example:
# n = 2, m = 2

import numpy as np


def findWaysToGetToBottom(m, n):
    grid = np.array([[i for i in range(n)] for _ in range(m)])
    print("Grid")
    print(grid)
    # Initialize the path array with m + n - 1 zeros
    return findPathToBottom(grid, [], [0 for _ in range(m + n - 1)], [0, 0])


def findPathToBottom(grid, allPaths, currentPath, currentPos):
    if currentPos[0] < len(grid[:, 0]) and currentPos[1] < len(grid[0, :]):
        # Assign current path element to current position index
        currentPath[sum(currentPos)] = grid[currentPos[0], currentPos[1]]
        if currentPos[0] == len(grid[:, 0]) - 1 and currentPos[1] == len(grid[0, :]) - 1:
            allPaths.append(list(currentPath))
            print("Found path", currentPath)
        # Iterate over the next possible positions
        nextPathOptions = [[currentPos[0] + 1, currentPos[1]], [currentPos[0], currentPos[1] + 1]]
        for o in nextPathOptions:
            if o[0] < len(grid[:, 0]) and o[1] < len(grid[0, :]):
                allPaths = findPathToBottom(grid, allPaths, currentPath, o)
    return allPaths


print(findWaysToGetToBottom(2, 2))
