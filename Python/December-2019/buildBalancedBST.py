# Given an unsorted array of integers which represents binary search tree keys, construct a
# height balanced BST


from collections import deque


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __str__(self):
        q = deque()
        q.append(self)
        nodesStr = ''
        while len(q):
            currNode = q.popleft()
            nodesStr += str(currNode.val)
            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
        return nodesStr


def insertNode(root, key):
    if not root:
        return TreeNode(key)

    if root.val > key:
        root.left = insertNode(root.left, key)
    if root.val < key:
        root.right = insertNode(root.right, key)

    return root


def buildTree(keys):
    root = None
    for k in keys:
        root = insertNode(root, k)
    return root


nodesValues = [7, 5, 6, 4, 1, 0, 9, 2, 3]
print(buildTree(nodesValues))
