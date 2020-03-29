def findWayToBottom(maze, currPos):
	# Base case: current position is in bounds
	if 0 <= currPos[0] < len(maze) and 0 <= currPos[1] < len(maze[currPos[0]]):
		# Check if current position in maze is a 0
		if maze[currPos[0]][currPos[1]] == 0:
			if currPos[0] == len(maze) - 1 and currPos[1] == len(maze[currPos[0]]) - 1:
				findWayToBottom.numWays += 1
			else:
				# Recurse going down and right using DFS approach
				findWayToBottom(maze, [currPos[0] + 1, currPos[1]])
				findWayToBottom(maze, [currPos[0], currPos[1] + 1])

def findNumWays(maze):
	findWayToBottom.numWays = 0
	# Go from initial position and find numWays to reach the bottom
	findWayToBottom(maze, [0, 0])
	return findWayToBottom.numWays
	

print(findNumWays([
	[0, 0, 0], 
	[1, 0, 0],
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0],
	[0, 1, 0], 
	[0, 0, 0],
	[1, 1, 0]
]))
