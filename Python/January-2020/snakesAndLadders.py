# Snakes and Ladders is a game played on a 10 x 10 board, the goal of which is get from square 1 to square 100.
# On each turn players will roll a six-sided die and move forward a number of spaces equal to the result.
# If they land on a square that represents a snake or ladder, they will be transported ahead or behind,
# respectively, to a new square.
#
# Find the smallest number of turns it takes to play snakes and ladders.
#
# For convenience, here are the squares representing snakes and ladders, and their outcomes:

# Global dictionaries for the game
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}


def minNumMovesInSnakesAndLadders(currPosition, board):
    # Base case
    if currPosition == 100:
        return True
    for diceNum in range(1, 7):
        try:
            curPos = snakes[currPosition + diceNum]
        except KeyError:
            try:
                curPos = ladders[currPosition + diceNum]
            except KeyError:
                curPos = currPosition + diceNum
        if board[curPos - 1] == 0:
            board[curPos - 1] = 1
            if minNumMovesInSnakesAndLadders(curPos, board):
                return True
            board[curPos - 1] = 0
    return False


board = [0 for _ in range(100)]
minNumMovesInSnakesAndLadders(0, board)
# print(board)
print(len([n for n in board if n == 1]))
