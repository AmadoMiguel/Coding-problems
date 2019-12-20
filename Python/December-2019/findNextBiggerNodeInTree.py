# Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.
#
# For example, the inorder successor of 22 is 30.
#
#    10
#   /  \
#  5    30
#      /  \
#    22    35
# You can assume each node has a parent pointer.


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def findNextBiggerNode(root, k, nextBiggerNode):
    if not root:
        return nextBiggerNode
    if nextBiggerNode is None or root.val < nextBiggerNode:
        if root.val > k:
            nextBiggerNode = root.val
    nextBiggerNode = findNextBiggerNode(root.left, k, nextBiggerNode)
    nextBiggerNode = findNextBiggerNode(root.right, k, nextBiggerNode)
    return nextBiggerNode


root = TreeNode(6)
root.left = TreeNode(4)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(3)

nextBigElem = findNextBiggerNode(root, 5, None)
print(nextBigElem)
