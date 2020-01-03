# Given a binary tree, remove the nodes in which there is only 1 child, so that the binary tree is a full binary tree.
#
# So leaf nodes with no children should be kept, and nodes with 2 children should be kept as well.

from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __str__(self):
        dq = deque()
        dq.append(self)
        result = ""
        # Print the tree level by level
        while len(dq):
            l = len(dq)
            while l > 0:
                currNode = dq.popleft()
                if currNode:
                    result += str(currNode.val)
                    if currNode.left:
                        dq.append(currNode.left)
                    if currNode.right:
                        dq.append(currNode.right)
                l -= 1
            if len(dq):
                result += "\n"
        return result


def isComplete(root):
    return (root.left and root.right) or (not root.left and not root.right)


def removeIncompleteNodes(root):
    if root:
        if not isComplete(root):
            # Rewire corresponding pointer of incomplete node
            if not root.left and root.right:
                root = root.right
            elif not root.right and root.left:
                root = root.left
        if root:
            # Recurse on both sides
            root.left = removeIncompleteNodes(root.left)
            root.right = removeIncompleteNodes(root.right)
    return root


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.right = Node(4)
tree.right.left = Node(9)
tree.left.left = Node(0)
print("Before removing incomplete nodes:")
print(tree)
print("After removing incomplete nodes:")
print(removeIncompleteNodes(tree))
