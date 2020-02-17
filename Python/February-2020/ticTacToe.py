
import numpy as np


class Board(object):
    def __init__(self, size: int):
        self.size = size
        self.board = np.array(
            [['-' for _ in range(size)] for _ in range(size)]
        )

    def addToken(self, row, col, token):
        if 0 <= row < self.size:
            if 0 <= col < self.size:
                if self.board[row, col] == '-':
                    self.board[row, col] = token
                    return True
        return False

    def isFull(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i, j] == '-':
                    return False
        return True

    def aiPlaceToken(self, token):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i, j] == '-':
                    self.board[i, j] = token
                    return True
        raise Exception("Board is already full")

    def __str__(self):
        board = ""
        for i in range(len(self.board[:])):
            for j in range(len(self.board[i, :])):
                board += self.board[i, j] + "|"
            board = board[:-1] + "\n"
        return board


board = Board(4)
print(board)
while not board.isFull():
    userInput = input("Please enter row and column").split(",")
    board.addToken(int(userInput[0]) - 1, int(userInput[1]) - 1, 'X')
    board.aiPlaceToken('O')
    print(board)
    print(board.isFull())
board.aiPlaceToken('O')
