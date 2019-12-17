# Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks), count the number of islands
# present in the grid. The definition of an island is as follows:
# 1.) Must be surrounded by water blocks.
# 2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
# Assume all edges outside of the grid are water.
#
# Example:
# Input:
# 10001
# 11000
# 10110
# 00000
#
# Output: 3

import numpy as np


def isInBounds(grid, cell):
    if 0 <= cell[0] < len(grid[:, 0]):
        if 0 <= cell[1] < len(grid[0, :]):
            return True
    return False


# Convert adjacent 1's to -1's in order to mark each island
def markIslandTerrain(grid, cell):
    grid[cell[0], cell[1]] = -1
    nextCells = [[cell[0]-1, cell[1]], [cell[0]+1, cell[1]],
                 [cell[0], cell[1]-1], [cell[0], cell[1]+1]]
    for n in nextCells:
        if isInBounds(grid, n):
            if grid[n[0], n[1]] == 1:
                markIslandTerrain(grid, n)


def countNumIslands(grid):
    nIslands = 0
    for r in range(len(grid[:, 0])):
        for c in range(len(grid[0, :])):
            print(grid)
            if grid[r, c] == 1:
                nIslands += 1
                markIslandTerrain(grid, [r, c])
    return nIslands


grid = np.array([
                    [1, 0, 0, 0, 1],
                    [1, 1, 0, 0, 0],
                    [1, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0]
                ])
print(countNumIslands(grid))
