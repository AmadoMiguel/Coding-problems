import random
import os
import numpy as np

# Clear console function
clear = lambda: os.system('clear')      

class ticTacToeTomek():
    board = []
    gameEnds = None
    whoWins = " "
    N = 0
    def __init__(self,N):
        # Game setup
        # Main initial board
        self.N = N
        self.board = np.array([['.' for _ in range(0,N)]for _ in range(0,N)])
        # Define position of 'T'
        self.board[random.randint(0,N-1),random.randint(0,N-1)] = 'T'
        # Game starts 
        self.gameEnds = False  
    # Method that locates X in the user-requested cell
    def locateX(self):
        located = False
        while not located:
            # User X position request
            Xcell = [int(x) for x in input("Next X, Row and column: ")]
            if self.board[Xcell[0],Xcell[1]] == '.':
                located = True
                self.board[Xcell[0],Xcell[1]] = 'X'
                self.checkWin(Xcell)
            else:
                print("Cell already busy. Select another one: ")    
    # Method that locates O in a random non-busy cell            
    def locateO(self):
        located = False
        while not located:
            Ocell = [random.randint(0,3),random.randint(0,3)]
            if self.board[Ocell[0],Ocell[1]] == '.':
                located = True
                self.board[Ocell[0],Ocell[1]] = 'O'
                self.checkWin(Ocell)
    def showBoard(self):
        # Show game board
        for i in range(0,4):
            print(self.board[i,:])        
    # Every time the user or the cpu locates X or O, 
    # this method is called        
    def checkWin(self,cell):
        # Check row
        rowData = {'O':0,'X':0,'T':0}
        for c in self.board[cell[0],:]:
            # Recolect row info
            rowData[c] = rowData.get(c,0) + 1
        if rowData['X'] == 4 or (rowData['X'] == 3 and rowData['T'] == 1):
            # Check if user wins
            self.gameEnds = True
            self.whoWins = "User"
        elif rowData['O'] == 4 or (rowData['O'] == 3 and rowData['T'] == 1):
            # Check if CPU wins
            self.gameEnds = True
            self.whoWins = "CPU"

        # Check column    
        colData = {'O':0,'X':0,'T':0} 
        for c in self.board[:,cell[1]]:
            # Recolect column info
            colData[c] = colData.get(c,0) + 1
        if colData['X'] == 4 or (colData['X'] == 3 and colData['T'] == 1):
            # Check if user wins
            self.gameEnds = True
            self.whoWins = "User"
        elif colData['O'] == 4 or (colData['O'] == 3 and colData['T'] == 1):
            # Check if CPU wins
            self.gameEnds = True
            self.whoWins = "CPU"  

        # Check diagonals (depending on the cell)
        if (cell[0] == cell[1]) or (cell[0]+cell[1] == self.N-1):
            diag1_Info = {'O':0,'X':0,'T':0}
            diag2_Info = {'O':0,'X':0,'T':0}
            for i in range(0,self.N):
                # Recolect diagonals info
                diag1_Info[self.board[i,i]] = diag1_Info.get(self.board[i,i],0)+1
                diag2_Info[self.board[i,self.N-1-i]] = diag2_Info.get(self.board[i,self.N-1-i],0)+1
            
            # Check diagonal 1
            if cell[0] == cell[1]:
                # Check if user wins
                if diag1_Info['X'] == 4 or (diag1_Info['X'] == 3 and diag1_Info['T'] == 1):
                    self.gameEnds = True
                    self.whoWins = "User"
                # Check if CPU wins    
                elif diag1_Info['O'] == 4 or (diag1_Info['O'] == 3 and diag1_Info['T'] == 1): 
                    self.gameEnds = True
                    self.whoWins = "CPU"  
            # Check diagonal 2
            elif cell[0] + cell[1] == self.N -1:
                # Check if user wins
                if diag2_Info['X'] == 4 or (diag2_Info['X'] == 3 and diag2_Info['T'] == 1):
                    self.gameEnds = True
                    self.whoWins = "User"
                # Check if CPU wins    
                elif diag2_Info['O'] == 4 or (diag2_Info['O'] == 3 and diag2_Info['T'] == 1): 
                    self.gameEnds = True
                    self.whoWins = "CPU"                    



# Game object
game = ticTacToeTomek(4)

while not game.gameEnds:
    game.showBoard()
    game.locateX()
    game.locateO()
    # Clear console for more game-display realism
    clear()
# After game ends    
print("The winner is:",game.whoWins)    