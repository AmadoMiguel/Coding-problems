# You are given the preorder and inorder traversals of a binary tree in the form of arrays. Write a function
# that reconstructs the tree represented by these traversals.
#
# Example:
# Preorder: [a, b, d, e, c, f, g]
# Inorder: [d, b, e, a, f, c, g]
#
# The tree that should be constructed from these traversals is:
#
#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g

from collections import deque


class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __str__(self):  # Similar to java's toString()
        q = deque()
        q.append(self)
        nodes = ''
        while len(q):
            currNode = q.popleft()
            nodes += currNode.val
            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
        return nodes


class TreeBuilder(object):
    def __init__(self, inorder, preorder):
        self.inorder = inorder
        self.preorder = preorder
        self.preOrdIndx = 0

    def findValueInInOrderSlice(self, inOrdStart, inOrdEnd, key):
        for i in range(inOrdStart, inOrdEnd + 1):
            if self.inorder[i] == key:
                return i
        return -1

    def reconstructTree(self, inOrdStart, inOrdEnd):
        if inOrdStart > inOrdEnd:
            return None

        # Initialize tree and advance preOrder index
        root = Tree(self.preorder[self.preOrdIndx])
        self.preOrdIndx += 1

        if inOrdStart == inOrdEnd:
            return root
        # Find current preorder value in current inorder slice
        inOrdIndx = self.findValueInInOrderSlice(inOrdStart, inOrdEnd, root.val)

        # Conform left tree
        root.left = self.reconstructTree(inOrdStart, inOrdIndx - 1)
        # Conform right tree
        root.right = self.reconstructTree(inOrdIndx + 1, inOrdEnd)

        return root


def restoreBinaryTree(inorder, preorder):
    if len(inorder) == 1:
        return Tree(inorder[0])
    solver = TreeBuilder(inorder, preorder)
    return solver.reconstructTree(0, len(inorder) - 1)


indexOfPre2 = 0


def restoreBinaryTree2(inorder, preorder):
    global indexOfPre2
    if not len(inorder): # Leaves are reached
        return None
    curr = preorder[indexOfPre2]
    indexOfPre2 += 1
    root = Tree(curr)
    indxOfCurrInOrd = inorder.index(curr)
    # Values to the left of current preorder root in inorder traversal are left children.
    # ""     ""  "" right "" ""      ""      ""   ""  ""     ""         "" right "".
    root.left = restoreBinaryTree2(inorder[:indxOfCurrInOrd], preorder)
    root.right = restoreBinaryTree2(inorder[indxOfCurrInOrd + 1:], preorder)

    return root


preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
solver = TreeBuilder(inorder, preorder)
tree = solver.reconstructTree(0, len(inorder) - 1)
tree2 = restoreBinaryTree2(inorder, preorder)
print(tree)
print(tree2)
