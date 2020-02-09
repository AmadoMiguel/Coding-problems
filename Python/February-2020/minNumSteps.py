
def jumpToEnd(currIndx, currNumSteps, stepsArr, lenOpts, maxPlusOne):
	# Base case: Return the number of steps required to get to the end
	if currIndx == lenOpts - 1:
		return currNumSteps
	# Base case: Index out of bounds. Return a big number to avoid considering
	# it as option, unless is the only option.
	if currIndx >= lenOpts:
		return maxPlusOne
	if currIndx < lenOpts - 1:
		currPos = stepsArr[currIndx]
		# Base case: current position is a 0; which means there's no way to advance.
		# Similar handling as index out of bounds
		if currPos == 0:
			return maxPlusOne
		nextOpts = [currIndx + i for i in range(1, currPos + 1)]
		return min([jumpToEnd(opt, currNumSteps + 1, stepsArr, lenOpts, maxPlusOne) for opt in nextOpts])


stepOptions = [8, 2, 4, 0, 1, 1, 3, 0, 0, 9]
maxPlusOne = max(stepOptions) + 1
lenOpts = len(stepOptions)
minNumSteps = jumpToEnd(0, 0, stepOptions, lenOpts, maxPlusOne)
# This is the default value that represents no possibility to jump to the final position
if minNumSteps == maxPlusOne:
	print("No possible way to jump to the end")
else:
	print("Min num steps possible: ", minNumSteps)
