# The horizontal distance of a binary tree node describes how far left or right the node will be when the tree
# is printed out.
#
# More rigorously, we can define it as follows:
#
# The horizontal distance of the root is 0.
# The horizontal distance of a left child is hd(parent) - 1.
# The horizontal distance of a right child is hd(parent) + 1.
# For example, for the following tree, hd(1) = -2, and hd(6) = 0.
#
#              5
#           /     \
#         3         7
#       /  \      /   \
#     1     4    6     9
#    /                /
#   0                8
# The bottom view of a tree, then, consists of the lowest node at each horizontal distance. If there are two
# nodes at the same depth and horizontal distance, either is acceptable.
#
# For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].
#
# Given the root to a binary tree, return its bottom view.


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def findHorizontalLevels(root, depth, horLevel, horLevels):
    if not root:
        return horLevels
    if horLevel in horLevels.keys():
        if horLevels[horLevel][1] <= depth:
            horLevels[horLevel] = (root.val, depth)
    else:
        horLevels[horLevel] = (root.val, depth)
    horLevels = findHorizontalLevels(root.left, depth + 1, horLevel - 1, horLevels)
    horLevels = findHorizontalLevels(root.right, depth + 1, horLevel + 1, horLevels)
    return horLevels


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(0)
root.right.right.left = TreeNode(8)

print([v for v, _ in findHorizontalLevels(root, 0, 0, {}).values()])
