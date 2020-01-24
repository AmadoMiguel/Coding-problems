# Given the root of a binary tree, print its level-order traversal. For example:
# #
# #   1
# #  / \
# # 2   3
# #    / \
# #   4   5
# #
# # The following tree should output 1, 2, 3, 4, 5.

from collections import deque


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        queue = deque()
        levelOrderPrint = ""
        # Add root
        queue.append(self)
        while len(queue):
            currNode = queue.popleft()
            if currNode:
                levelOrderPrint += str(currNode.val)
                # Check children from left to right and add to the queue
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
        return levelOrderPrint


root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
print(root)
