# You are given the root of a binary tree. Find the level for the binary tree with the minimum sum,
# and return that value.
#
# For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10, and 4 + 1 + 2 = 7.
# So, the answer here should be 7.

from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def findLevelWithMinSum(root):
    levelsNodes = deque()
    # Store current node and its corresponding level (root is 0)
    levelsNodes.append((root, 0))
    levelsSums = []
    while len(levelsNodes):
        currChild, level = levelsNodes.popleft()
        if currChild:
            # Store current node value in the array, taking into account the level. If level index fits in the
            # array, add it to that index. Otherwise, add the current node value to the array.
            if level < len(levelsSums):
                levelsSums[level] += currChild.val
            else:
                levelsSums.append(currChild.val)
            # Store child nodes with their corresponding level
            if currChild.left:
                levelsNodes.append((currChild.left, level + 1))
            if currChild.right:
                levelsNodes.append((currChild.right, level + 1))

    return levelsSums


node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

levelsSums = findLevelWithMinSum(node)
print(levelsSums)
assert min(levelsSums) == 7  # True
