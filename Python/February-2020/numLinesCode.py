
def getBonusesPerCoder(numLines):
	bonuses = [1 for _ in range(len(numLines))]
	if len(numLines) > 1:
		for i in range(len(numLines)):
			if i == 0 :
				if numLines[i] > numLines[i + 1]:
					bonuses[i] = bonuses[i + 1] + 1
			elif i == len(numLines) - 1:
				if numLines[i] > numLines[i - 1]:
					bonuses[i] = bonuses[i - 1] + 1
			else:
				if numLines[i] > numLines[i - 1] and numLines[i] > numLines[i + 1]:
					bonuses[i] = max(bonuses[i-1], bonuses[i+1]) + 1
				elif numLines[i] > numLines[i - 1]:
					bonuses[i] = bonuses[i-1] + 1
				elif numLines[i] > numLines[i + 1]:
					bonuses[i] = bonuses[i+1] + 1
	return bonuses

numLines = [10, 40, 200,  1000, 60, 30]
print(getBonusesPerCoder(numLines))
