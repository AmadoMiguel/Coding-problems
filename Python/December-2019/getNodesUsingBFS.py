# Given a binary tree of integers t, return its node values in the following format:
#
# The first element should be the value of the tree root;
# The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the
# leftmost to the rightmost one;
# The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1)
# ordered in the same way;
# Etc.

from collections import deque


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


# Get nodes in level order (parent, children, grand-children, etc.) with its corresponding level and
# the greatest node per level
def traverseTree(t):
    nodes = []
    maxNodes = []
    treeQueue = deque()
    # Add the root to the queue
    treeQueue.append((t, 0))
    while len(treeQueue):
        # Get current node and its level
        currentNode, level = treeQueue.popleft()
        if currentNode:
            nodes += [(currentNode.value, level)]
            if not len(maxNodes):
                maxNodes += [currentNode.value]
            # Left child
            if currentNode.left:
                l = level + 1
                if l < len(maxNodes):
                    curMax = maxNodes[l]
                    if currentNode.left.value > curMax:
                        maxNodes[l] = currentNode.left.value
                else:
                    maxNodes += [currentNode.left.value]
                treeQueue.append((currentNode.left, l))
            # Right child
            if currentNode.right:
                l = level + 1
                if l < len(maxNodes):
                    curMax = maxNodes[l]
                    if currentNode.right.value > curMax:
                        maxNodes[l] = currentNode.right.value
                else:
                    maxNodes += [currentNode.right.value]
                treeQueue.append((currentNode.right, l))
    return nodes, maxNodes


root = Tree(1)
root.left = Tree(2)
root.right = Tree(4)
root.left.right = Tree(3)
root.right.left = Tree(5)

print(traverseTree(root))
