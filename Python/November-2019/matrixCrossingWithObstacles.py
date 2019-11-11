# You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to
# reach the bottom right corner?
#
# You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.
#
# For example, given the following matrix:
#
# [[0, 0, 1],
#  [0, 0, 1],
#  [1, 0, 0]]
# Return two, as there are only two ways to get to the bottom right:
#
# Right, down, down, right
# Down, right, down, right
# The top left corner and bottom right corner will always be 0.

import numpy as np


def findWaysToGoToBottom(matrix):
    return checkIfPathTakesToBottom(matrix, [0, 0], 0)


def checkIfPathTakesToBottom(matrix, currentPosition, nWays):
    print(currentPosition)
    # Recursion condition
    if currentPosition[0] < len(matrix[:, 0]) and currentPosition[1] < len(matrix[0, :]):
        # If current position is right-bottom corner, a path was found (algorithm goal)
        if currentPosition[0] == len(matrix[:, 0]) - 1 and currentPosition[1] == len(matrix[0, :]) - 1:
            print('arrived')
            nWays += 1
        # Check path options (right and down)
        down = [currentPosition[0] + 1, currentPosition[1]]
        right = [currentPosition[0], currentPosition[1] + 1]
        nextPathOptions = [down, right]
        # Iterate recursively (backtracking) over the options to find out if it takes to a path
        for pathOption in nextPathOptions:
            if pathOption[0] < len(matrix[:, 0]) and pathOption[1] < len(matrix[0, :]):
                # Check if value is 1. In that case, skip it since 1 is an obstacle
                if matrix[pathOption[0], pathOption[1]] == 1:
                    continue
                else:
                    # Recurse until the end is reached
                    nWays = checkIfPathTakesToBottom(matrix, pathOption, nWays)
            else:  # Go to next option
                continue
    return nWays


print(findWaysToGoToBottom(np.array([[0, 0, 1],
                                     [0, 0, 1],
                                     [1, 0, 0]])))
