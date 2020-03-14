# Given a binary tree, find and return the largest path from root to leaf

from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        toString = []
        dq = deque()
        dq.append((self, 0))
        while len(dq):
            curr, lev = dq.popleft()
            if curr:
                if lev < len(toString):
                    toString[lev] += str(curr.value) + " "
                else:
                    toString += [str(curr.value) + " "]
                dq.append((curr.left, lev + 1))
                dq.append((curr.right, lev + 1))
        return "\n".join(toString)


def isLeaf(node):
    if not node:
        return False
    return not node.left and not node.right


def findPath(currPath, currSum, root):
    if isLeaf(root):
        currPath += [root.value]
        currSum += root.value
        if findPath.longestSum is None or currSum > findPath.longestSum:
            findPath.longestSum = currSum
            findPath.longestPath = currPath
    else:
        if root.left:
            findPath(currPath + [root.value], currSum + root.value, root.left)
        if root.right:
            findPath(currPath + [root.value], currSum + root.value, root.right)


def findLongestSumPath(root):
    findPath.longestPath = []
    findPath.longestSum = None
    findPath([], 0, root)
    return findPath.longestPath


tree = Node(1)
tree.left = Node(3)
tree.right = Node(2)
tree.right.left = Node(4)
tree.left.right = Node(5)
print(tree)
assert findLongestSumPath(tree) == [1, 3, 5]  # True
