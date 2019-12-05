# You are given the root of a binary tree. Return the deepest node (the furthest node from the root).
#
# Example:
#
#     a
#    / \
#   b   c
#  /
# d
#
# The deepest node in this tree is d at depth 3.


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def findDeepestNodeInTree(root):
    return getDeepestNode(root, root.val, None, 1)


def getDeepestNode(currentNode, deepestNodeValue, deepestPos, currentPosition):
    if currentNode is not None:
        print("current position", currentPosition, currentNode.val)
        if deepestPos is None or currentPosition > deepestPos:
            deepestPos = currentPosition
            deepestNodeValue = currentNode.val
        for n in [currentNode.right, currentNode.left]:
            deepestNodeValue, deepestPos = getDeepestNode(n, deepestNodeValue, deepestPos,
                                                          currentPosition + 1)
    return deepestNodeValue, deepestPos


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
# root.left.left.left = Node('e')
root.right = Node('c')
root.right.right = Node('f')
root.right.right.right = Node('g')

print(findDeepestNodeInTree(root))
