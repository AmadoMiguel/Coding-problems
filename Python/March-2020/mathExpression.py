def getIndexOfOpening(subExp):
	return subExp.index("(")

def getIndexOfClosing(subExp):
	return subExp.index(")")

# There are only + and - as operators in the input string
def isOperator(ch):
	return ch == "+" or ch == "-"

def calculateTernary(tern):
	# Handle negative numbers carefully
	firstTerm, secTerm = "", ""
	operator = ""
	try:
		firstTerm = int(tern[1:3])
		operator = tern[3]
		try:
			secTerm = int(tern[4:6])
		except:
			secTerm = int(tern[4])
	except:
		firstTerm = int(tern[1])
		operator = tern[2]
		try:
			secTerm = int(tern[3:5])
		except:
			secTerm = int(tern[3])
	if operator == "-":
		return firstTerm - secTerm
	if operator == "+":
		return firstTerm + secTerm
	

# The expression is assumed to be conformed correctly
def calculateExpression(expr):
	total = 0
	while "(" in expr and ")" in expr:
		# Recalculate indeces
		lastIndxOfOpen = len(expr) - 1 - getIndexOfOpening(expr[::-1])
		indxOfClose = lastIndxOfOpen + getIndexOfClosing(expr[lastIndxOfOpen:])
		# Current sub expression
		subExp = expr[lastIndxOfOpen:indxOfClose + 1]
		currResult = calculateTernary(subExp)
		expr = expr.replace(subExp, str(currResult))
		print(expr)
	if len(expr):
		total = calculateTernary("(" + expr + ")")
	return total
	


expression = "-1+((2+3)-(-2-4))"
print(calculateExpression(expression))
