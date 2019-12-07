# Determine whether a tree is a valid binary search tree.
#
# A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in
# the left child must be less than or equal to the root and the key in the right child must be greater than or equal
# to the root.


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def checkIfTreeIsValid(root, isValid):
    if root and isValid:
        if root.left and root.right:
            if not root.left.val < root.val <= root.right.val:
                isValid = False
        elif root.left:
            if not root.val > root.left.val:
                isValid = False
        elif root.right:
            if not root.val <= root.right.val:
                isValid = False
        nextNodes = [root.left, root.right]
        for n in nextNodes:
            isValid = checkIfTreeIsValid(n, isValid)
    return isValid


root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(checkIfTreeIsValid(root, True))
