# Write a function, throw_dice(N, faces, total), that determines how many ways it is possible to throw N dice
# with some number of faces each to get a specific total.
#
# For example, throw_dice(3, 6, 7) should equal 15.


def checkTotal(throw, currTotal, diceIndex, dices, total):
	for n in dices[diceIndex]:
		throw[diceIndex] = n
		currTotal += n
		if diceIndex < len(dices) - 1:
			checkTotal(throw, currTotal, diceIndex + 1, dices, total)
		else:
			if currTotal == total:
				checkTotal.numSums += 1
				print(throw, currTotal)
		currTotal -= n


def throwDice(N, faces, total):
	dices = [
		[n for n in range(1, faces + 1)] for _ in range(N)
	]
	th = [0 for _ in range(N)]
	checkTotal.numSums = 0
	checkTotal(th, 0, 0, dices, total)
	return checkTotal.numSums


# 3 dices with 6 faces each; the number of valid configurations that
# add up to 7 is 15
assert throwDice(3, 6, 7) == 15  # Pass
# More test cases below here...
