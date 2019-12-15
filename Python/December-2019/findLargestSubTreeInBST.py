# You are given the root of a binary tree. Find and return the largest subtree of that tree, which is a valid
# binary search tree.

from collections import deque


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __str__(self):
        qu = deque()
        qu.append(self)
        nodesStr = ""
        while len(qu):
            currNode = qu.popleft()
            nodesStr += str(currNode.val)
            if currNode.left:
                qu.append(currNode.left)
            if currNode.right:
                qu.append(currNode.right)
        return nodesStr


def isValid(root):
    if not root:
        return True

    if root.left:
        if root.left.val > root.val:
            return False
    if root.right:
        if root.val > root.right.val:
            return False

    return isValid(root.left) and isValid(root.right)


def getTreeHeight(root, height):
    if not root:
        return height
    if root.left or root.right:
        height += 1
    return max(getTreeHeight(root.left, height), getTreeHeight(root.right, height))


def findLongestSubTree(root, longestSubTree):
    if not root:  # Exit recursion
        return longestSubTree
    if root.left or root.right:
        if root.left:
            if longestSubTree is None or getTreeHeight(root.left, 1) > getTreeHeight(longestSubTree, 1):
                if isValid(root.left):
                    longestSubTree = root.left
        if root.right:
            if longestSubTree is None or getTreeHeight(root.right, 1) > getTreeHeight(longestSubTree, 1):
                if isValid(root.right):
                    longestSubTree = root.right

    longestSubTree = findLongestSubTree(root.left, longestSubTree)
    longestSubTree = findLongestSubTree(root.right, longestSubTree)
    return longestSubTree


node = TreeNode(5)
node.left = TreeNode(3)
node.right = TreeNode(6)
node.left.left = TreeNode(4)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
node.right.left.left = TreeNode(2)
node.right.left.right = TreeNode(5)

longestSubTree = findLongestSubTree(node, None)
print(longestSubTree)
