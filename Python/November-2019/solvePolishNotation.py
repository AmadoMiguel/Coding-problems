# Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.
#
# The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.
#
# For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent
# to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.
#
# You can assume the given expression is always valid.


def calculateExpression(a, b, oper):
    return eval(str(a) + oper + str(b))


def calculatePolishNotation(polishNotation):
    print(polishNotation)
    for i in range(len(polishNotation)):
        if len(polishNotation[i:]) >= 3:
            if polishNotation[i + 2] in ['-', '+', '*', '/']:
                num1, num2, sign = polishNotation[i], polishNotation[i + 1], polishNotation[i + 2]
                polishNotation.insert(i, int(calculateExpression(num1, num2, sign)))
                del polishNotation[i+1:i+4]
                calculatePolishNotation(polishNotation)
    return polishNotation


print("Result", sum(calculatePolishNotation([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'])))
