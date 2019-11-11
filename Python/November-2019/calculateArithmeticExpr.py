# Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate the
# expression. Assume the expression is properly formed.

# Example:
# Input: - ( 3 + ( 2 - 1 ) )
# Output: -4

import re


def calculateExpression(exprStr):
    # Extract nums and symbols from expression string
    nums = re.findall('[0-9]+', exprStr)
    symbols = re.findall('[-+]', exprStr)
    symbolsIndx = 0
    # If length of both is the same, means that expression starts with '-', assuming
    # that the expression is well formed
    if len(nums) == len(symbols):
        result = -1 * int(nums[0])  # Initialize result with the first number as negative
        symbolsIndx += 1  # Advance to next symbol
        if len(nums) > 1:  # Avoid out of bounds error
            for n in nums[1:]:
                if symbols[symbolsIndx] == '+':
                    result += int(n)
                elif symbols[symbolsIndx] == '-':
                    result -= int(n)
                if symbolsIndx + 1 < len(symbols):
                    symbolsIndx += 1
    else:  # Expression doesn't start with '-'
        result = int(nums[0])  # Initialize result with first number
        for n in nums[1:]:
            if symbols[symbolsIndx] == '+':
                result += int(n)
            elif symbols[symbolsIndx] == '-':
                result -= int(n)
            if symbolsIndx + 1 < len(symbols):
                symbolsIndx += 1
    return result


def evaluateArithmeticExpression(exprStr, result):
    print(exprStr)
    if '(' in exprStr and ')' in exprStr:
        # Find last index of '('
        lastIndxOfOpenPar = len(exprStr) - 1 - exprStr[::-1].index('(')
        # Find next index of ')', which is the first overall
        nextIndexOfClosePar = exprStr[lastIndxOfOpenPar:].index(')') + len(exprStr[:lastIndxOfOpenPar])
        # Then solve the expression in between those parenthesis with the calculateExpression function
        obtainedResult = str(calculateExpression("".join(exprStr[lastIndxOfOpenPar+1:nextIndexOfClosePar])))
        # Remove all that indexes range and replace it with the result that was obtained
        # Check previous sign in order to avoid having things like '2 -+ 1'
        if exprStr[lastIndxOfOpenPar - 1] == '+':
            if '-' in obtainedResult:
                exprStr[lastIndxOfOpenPar - 1] = '-'
                # Remove sign from number
                obtainedResult = str(int(obtainedResult) * (-1))
        elif exprStr[lastIndxOfOpenPar - 1] == '-':
            if '-' in obtainedResult:
                exprStr[lastIndxOfOpenPar - 1] = '+'
                # Remove sign from number
                obtainedResult = str(int(obtainedResult) * (-1))
        # Insert the result in the corresponding index
        exprStr.insert(lastIndxOfOpenPar, obtainedResult)
        # Remove expression indexes range
        del exprStr[lastIndxOfOpenPar+1: nextIndexOfClosePar+2]
        # Assing obtained result to global results
        result = int(obtainedResult)
        # Recurse
        result = evaluateArithmeticExpression(exprStr, result)
    # Before returning, check sign
    if '-' in exprStr:
        result = result * (-1)
        del exprStr[0]
    return result


print(evaluateArithmeticExpression(list('(3-(9-8+(0-3+(2+1)))+(2-1)+(7+(2-5)))'), 0))
