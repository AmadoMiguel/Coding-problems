# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:10:09 2019

@author: migue
"""

import numpy as np

class boolBoardGame():
    board = None
    startPoint = []
    actualPos = []
    endPoint = []
    nMinSteps = None
    N,M = 0
    def __init__(self,N,M,start,end):
        self.N = N
        self.M = M
        self.board = np.array( [['f' for _ in range(0,M)] for _ in range(0,N)] )
        # Randomly put the walls around the board
        randIndcsN = np.random.randint(0,N-1,3)
        randIndcsM = np.random.randint(0,M-1,3)
        self.board[randIndcsN,randIndcsM] = 't'

        self.startPoint = start
        self.actualPos = start
        self.endPoint = end
        self.nMinSteps = 0
    def checkPossible(self):
        if self.board(self.endPoint[0] + 1,self.endPoint[1]) == 't' 
        if self.endPoint == 't':
            return False
        else:
            return True
            
game = boolBoardGame(3,4,[2,2],[1,3])
while game.actualPos != game.endPoint:
    print(game.board)
    if game.checkPossible():
        print("It's possible to get to end point")
    else:
        print("It's not possible to get to end point")
        break
    