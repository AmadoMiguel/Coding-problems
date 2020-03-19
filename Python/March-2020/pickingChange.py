# Given a 2d n x m matrix where each cell has a certain amount of change on the floor, your goal is to start from
# the top left corner mat[0][0] and end in the bottom right corner mat[n - 1][m - 1] with the most amount of change.
# You can only move either right or down.


def pickMaxChange(mtx, mtxLen, mtxRowLen, currPos, currChange):
    for pos in [
        [currPos[0] + 1, currPos[1]], [currPos[0], currPos[1] + 1]
    ]:
        if 0 <= pos[0] < mtxLen and 0 <= pos[1] < mtxRowLen:
            pickMaxChange(mtx, mtxLen, mtxRowLen, pos, currChange + mtx[pos[0]][pos[1]])
        elif currPos[0] == mtxLen - 1 and currPos[1] == mtxRowLen - 1:
            if pickMaxChange.maxChange is None or currChange > pickMaxChange.maxChange:
                pickMaxChange.maxChange = currChange


def getMaxChange(matrix):
    pickMaxChange.maxChange = None
    pickMaxChange(matrix, len(matrix), len(matrix[0]), [0, 0], 0)
    return pickMaxChange.maxChange


mat = [
    [0, 3, 0, 2],
    [1, 2, 3, 3],
    [6, 0, 3, 2]
]

getMaxChange(mat)
