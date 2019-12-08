# Given a binary tree, return all values given a certain height h.


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def findNodesAtHeight(root, h):
    return getNodeAtHeight(root, 1, h, [])


def getNodeAtHeight(node, currentHeight, goalHeight, nodesAtHeigth):
    if node is not None:
        if currentHeight == goalHeight:
            nodesAtHeigth.append(node.val)
        nextNodes = [node.left, node.right]
        for n in nextNodes:
            nodesAtHeigth = getNodeAtHeight(n, currentHeight + 1, goalHeight, nodesAtHeigth)
    return nodesAtHeigth


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.right.right = TreeNode(7)
a.left.left.left = TreeNode(6)
a.left.right.left = TreeNode(8)
a.right.right.right = TreeNode(10)

height = 3
print(findNodesAtHeight(a, height))
