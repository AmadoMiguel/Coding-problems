# Given two cells on the standard chess board, determine whether they have the same color or not.


def chessBoardCellColor(cell1, cell2):
    letsMap = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
    coordsCell1 = [letsMap[list(cell1)[0]], int(list(cell1)[1])]
    coordsCell2 = [letsMap[list(cell2)[0]], int(list(cell2)[1])]
    difCells1 = abs(coordsCell1[0]-coordsCell1[1])
    difCells2 = abs(coordsCell2[0]-coordsCell2[1])
    if difCells1 % 2 == 0 and difCells2 % 2 == 0:
        return True
    elif difCells1 % 2 != 0 and difCells2 % 2 != 0:
        return True
    else:
        return False


print(chessBoardCellColor("A1", "H3"))
