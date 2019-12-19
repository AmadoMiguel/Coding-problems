# Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all
# values under a node, including the node itself.
#
# For example, given the following tree:
#
#   5
#  / \
# 2  -5
# Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def getSubTreeSum(root):
    if not root:
        return 0
    return root.val + getSubTreeSum(root.left) + getSubTreeSum(root.right)


def findSumsFrequency(root, frequency):
    if not root:
        return frequency
    currentSubTreeSum = getSubTreeSum(root)
    frequency[currentSubTreeSum] = frequency.setdefault(currentSubTreeSum, 0) + 1
    findSumsFrequency(root.left, frequency)
    findSumsFrequency(root.right, frequency)
    return frequency


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-5)
print(findSumsFrequency(root, {}))
