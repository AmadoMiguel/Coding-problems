
def canFormCircle(currCircle, remWords, originalLength):
	if not len(remWords):
		# If last word's last letter is equal to first word's first letter
		if currCircle[-1][-1] == currCircle[0][0] and len(currCircle) == originalLength:
			return True
	else:	
		for i in range(len(remWords)):
			curr = currCircle
			if not len(curr) or (curr[-1][-1] == remWords[i][0] and remWords[i] not in curr):
				curr += [remWords[i]]
			if canFormCircle(curr, remWords[:i] + remWords[i + 1:], originalLength):
				return True
	return False

words = ["chair", "height", "racket", "touch", "tunic"]
circle = []
if canFormCircle(circle, words, len(words)):
	print(circle)
else:
	print("Cannot conform circle with given words")
