# Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the
# bishop can capture the pawn in one move.


def bishopAndPawn(bishop, pawn):
    letsMap = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    bishopCoords = [letsMap[list(bishop)[0]], int(list(bishop)[1])]
    sumBishopCoords = sum(bishopCoords)
    pawnCoords = [letsMap[list(pawn)[0]], int(list(pawn)[1])]
    sumPawnCoords = sum(pawnCoords)

    evens = [i for i in range(2, 17) if i % 2 == 0]
    odds = [i for i in range(3, 17) if i % 2 != 0]

    # Any of the diagonals from left-top to right-bottom
    if sumBishopCoords == sumPawnCoords and sumBishopCoords in evens:
        return True
    elif sumBishopCoords == sumPawnCoords and sumBishopCoords in odds:
        return True
    else:
        # In the main diagonal
        if len(set(bishopCoords)) == 1 and len(set(pawnCoords)) == 1:
            return True
        # Other diagonals from left-bottom to right-top
        if sumBishopCoords in evens and sumPawnCoords in evens:
            if bishopCoords[0] == pawnCoords[0] or bishopCoords[1] == pawnCoords[1]:
                return False
            return True
        if sumBishopCoords in odds and sumPawnCoords in odds:
            if bishopCoords[0] == pawnCoords[0] or bishopCoords[1] == pawnCoords[1]:
                return False
            return True
    return False


print(bishopAndPawn('a3', 'b5'))
