

def getBoardWithNumMines(gameBoard, minesBoard):
	for i in range(0, len(gameBoard)):
		for j in range(0, len(gameBoard[i])):
			if gameBoard[i][j] == 'M':
				minesBoard[i][j] += 1
			nextOpts = [
				[i+1, j], [i-1, j], [i, j-1], [i, j+1],
				[i-1, j-1], [i-1, j+1], [i+1, j-1], [i+1, j+1]
			]
			for opt in nextOpts:
				if 0 <= opt[0] < len(gameBoard) and 0 <= opt[1] < len(gameBoard[i]):
					if gameBoard[opt[0]][opt[1]] == 'M':
						minesBoard[i][j] += 1

gameBoard = [
	['E', 'E', 'E', 'E', 'E'],
	['E', 'E', 'M', 'E', 'E'],
	['E', 'E', 'E', 'E', 'E'],
	['E', 'E', 'E', 'E', 'E']
]
minesBoard = [[0 for _ in range(len(gameBoard[0][:]))] for _ in range(len(gameBoard))]
getBoardWithNumMines(gameBoard, minesBoard)
print(minesBoard)
