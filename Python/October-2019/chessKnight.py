# Given a position of a knight on the standard chessboard, find the number of different moves the
# knight can perform.
#
# The knight can move to a square that is two squares horizontally and one square vertically, or two
# squares vertically and one square horizontally away from it. The complete move therefore looks like
# the letter L. Check out the image below to see all valid moves for a knight piece that is placed on
# one of the central squares.


def chessKnight(cell):
    cell = list(cell)
    cell[1] = int(cell[1])
    letsMap = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    possibleMovePositions = [[letsMap[cell[0]]-2, cell[1]-1], [letsMap[cell[0]]-1, cell[1]-2],
                             [letsMap[cell[0]]+1, cell[1]-2], [letsMap[cell[0]]+2, cell[1]-1],
                             [letsMap[cell[0]]+1, cell[1]+2], [letsMap[cell[0]]+2, cell[1]+1],
                             [letsMap[cell[0]]-2, cell[1]+1], [letsMap[cell[0]]-1, cell[1]+2]]
    nPossibleMoves = 0
    for move in possibleMovePositions:
        if move[0] in range(1, 9) and move[1] in range(1, 9):
            nPossibleMoves += 1
    return nPossibleMoves


print(chessKnight('a2'))
