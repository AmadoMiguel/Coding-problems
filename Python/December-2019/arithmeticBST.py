# You are given a binary tree representation of an arithmetic expression. In this tree, each leaf is an
# integer value,, and a non-leaf node is one of the four operations: '+', '-', '*', or '/'.
#
# Write a function that takes this tree and evaluates the expression.
#
# Example:
#
#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
#
# This is a representation of the expression (3 + 2) * (4 + 5), and should return 45.


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def isOperator(ch):
    return ch in ['+', '-', '/', '*']


# Postfix traversal to get the arithmetic expression organized
def calculateExpression(root, expr):
    if root:
        expr = calculateExpression(root.left, expr)
        expr = calculateExpression(root.right, expr)
        print(expr)
        if isOperator(root.val):
            currExpr = str(eval(expr[-2] + root.val + expr[-1]))
            del expr[-2:]
            expr += [currExpr]
        else:
            expr += [str(root.val)]
    return expr


root = Node('*')
root.left = Node('+')
root.right = Node('+')
root.left.left = Node(3)
root.left.right = Node(2)
root.right.left = Node(4)
root.right.right = Node(5)

print(calculateExpression(root, []))
