# Given an array of values. The task is to implement a Binary Search Tree using values of the array where every node
# stores the maximum number of nodes in the path starting from the node itself and ending at any leaf of the tree.
#
# Note: The maximum number of nodes in the path from any node to any leaf node in a BST is the height of the subtree
# rooted at that node.

# Re adapted -> Count the number of underlying nodes per node

from collections import deque


class TreeNode(object):
    def __init__(self, val, nNodes):
        self.info = {"val": val, "nNodes": nNodes}
        self.left, self.right = None, None

    def __str__(self):
        nodesStr = ""
        qu = deque()
        qu.append(self)
        while len(qu):
            currNode = qu.popleft()
            nodesStr += "Current key, # child nodes: "
            nodesStr += "(" + str(currNode.info["val"]) + ", " + str(currNode.info["nNodes"]) + ")" + '\n'
            if currNode.left:
                qu.append(currNode.left)
            if currNode.right:
                qu.append(currNode.right)
        return nodesStr


def insertAndCountNodes(root, key):
    if not root:
        # A leaf has 0 underlying nodes
        return TreeNode(key, 0)

    # Count underlying nodes
    root.info["nNodes"] += 1
    if key > root.info["val"]:
        root.right = insertAndCountNodes(root.right, key)
    if key < root.info["val"]:
        root.left = insertAndCountNodes(root.left, key)

    return root


keys = [4, 12, 10, 5, 11, 8, 7, 6, 9]
root = None
for k in keys:
    root = insertAndCountNodes(root, k)
print(root)
