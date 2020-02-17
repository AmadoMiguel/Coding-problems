# Connect 4 is a game where opponents take turns dropping red or black discs into a 7 x 6 vertically suspended grid.
# The game ends either when one player creates a line of four consecutive discs of their color
# (horizontally, vertically, or diagonally), or when there are no more spots left in the grid.
#
# Design and implement Connect 4.

import numpy as np


class Connect4Game(object):
    def __init__(self):
        self.board = np.array([['_' for _ in range(6)] for _ in range(7)])
        self.isGameFinished = False
        self.isTie = False
        self.didPlayer1Win = False
        self.isPlayer1Turn = True
        self.isTie = False

    def __str__(self):
        boardStr = ""
        # Game board
        for i in range(len(self.board[:, 0])):
            for j in range(len(self.board[i, :])):
                boardStr += self.board[i, j]
                if j < len(self.board[i, :]) - 1:
                    boardStr += " "
            boardStr += "\n"
        # Game status
        if not self.isGameFinished:
            boardStr += "Next turn for: "
            if self.isPlayer1Turn:
                boardStr += "Player 1"
            else:
                boardStr += "Player 2"
            boardStr += "\n"
        else:
            if self.isTie:
                boardStr += "Game finished. Nobody wins."
            else:
                if self.didPlayer1Win:
                    boardStr += "PLAYER 1 WON!"
                else:
                    boardStr += "PLAYER 2 WON!"
        return boardStr

    # -------------------------------------------------------------------------------------
    # Business logic
    # Check if board is still available for playing
    def isBoardFull(self):
        for i in range(len(self.board[:, 0])):
            for j in range(len(self.board[i, :])):
                if self.board[i, j] == "_":
                    return False
        return True

    # Method that checks if passed colors contain 4 consecutive equal colors
    def areFourColors(self, colors, color):
        count = 0
        for c in colors:
            if c == color:
                count += 1
            else:
                count = 0
            if count == 4:
                return True
        return False

    # ---------------------------------------------------------------------------------------------
    # Helper method to get the colors of the left diagonal (from bottom to top)
    def getLeftDiagonalColors(self, board, pos, colors, side):
        if 0 <= pos[0] < len(board[:, 0]) and 0 <= pos[1] < len(board[0, :]):
            if board[pos[0], pos[1]] != "c":
                # Get current color
                if side == "left":
                    colors.insert(0, board[pos[0], pos[1]])
                else:
                    colors += [board[pos[0], pos[1]]]
                # Mark cell as visited
                board[pos[0], pos[1]] = "c"
                nextCells = [(pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] - 1)]
                for i in range(len(nextCells)):
                    side = ("left", "right")[i == 0]
                    colors = self.getLeftDiagonalColors(board, nextCells[i], colors, side)
        return colors

    # Helper method to get the colors of the right diagonal (from bottom to top)
    def getRightDiagonalColors(self, board, pos, colors, side):
        if 0 <= pos[0] < len(board[:, 0]) and 0 <= pos[1] < len(board[0, :]):
            if board[pos[0], pos[1]] != "c":
                # Get current color
                if side == "left":
                    colors.insert(0, board[pos[0], pos[1]])
                else:
                    colors += [board[pos[0], pos[1]]]
                # Mark cell as visited
                board[pos[0], pos[1]] = "c"
                nextCells = [(pos[0] - 1, pos[1] - 1), (pos[0] + 1, pos[1] + 1)]
                for i in range(len(nextCells)):
                    side = ("left", "right")[i == 0]
                    colors = self.getRightDiagonalColors(board, nextCells[i], colors, side)
        return colors
    # ---------------------------------------------------------------------------------------------

    # In this function check if current player won after placing the color
    def checkForWin(self, color, pos, player):
        # Check row
        if self.areFourColors(self.board[pos[0], :], color):
            self.isGameFinished = True
        # Check col
        if self.areFourColors(self.board[:, pos[1]], color):
            self.isGameFinished = True
        # Check left diagonal
        leftDiagColors = self.getLeftDiagonalColors(np.array(self.board), pos, [], None)
        if self.areFourColors(leftDiagColors, color):
            self.isGameFinished = True
        # Check right diagonal
        rightDiagColors = self.getRightDiagonalColors(np.array(self.board), pos, [], None)
        if self.areFourColors(rightDiagColors, color):
            self.isGameFinished = True
        # Check if current player won
        if self.isGameFinished:
            if player == "P1":
                self.didPlayer1Win = True
        # Check if board is full. In case it is, end game and declare a tie
        else:
            if self.isBoardFull():
                self.isTie = True
                self.isGameFinished = True

    # Locate the new color to the user selected position
    def placeColor(self, pos, color, player):
        pos = [int(pos[0]), int(pos[1])]
        if 0 <= pos[0] < len(self.board[:, 0]) and 0 <= pos[1] < len(self.board[0, :]):
            if self.board[pos[0], pos[1]] == "_":
                self.board[pos[0], pos[1]] = color
                # Check if after placing the current color is there a winner
                self.checkForWin(color, pos, player)
                return True
        return False

    # Method to receive current player input
    def parseInput(self):
        if not self.isGameFinished:
            if self.isPlayer1Turn:
                player = "P1"
                color = 'r'
                self.isPlayer1Turn = False
            else:
                player = "P2"
                color = 'b'
                self.isPlayer1Turn = True
            nextPlacementCell = input(player + ", please enter row and column (r,c): ")
            p = nextPlacementCell.split(",")
            while not self.placeColor(p, color, player):
                nextPlacementCell = input(player + ", please try a different cell: ")
                p = nextPlacementCell.split(",")


# Greate game instance and start game
gameObj = Connect4Game()
winner = None
while not gameObj.isGameFinished:
    print(gameObj)
    # Ask for user input. The rest is handled internally
    gameObj.parseInput()
# Show results
print(gameObj)
