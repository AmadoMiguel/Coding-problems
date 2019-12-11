# A unival tree is a tree where all the nodes have the same value. Given a binary tree, return the number of
# unival subtrees in the tree.
#
# For example, the following tree should return 5:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
#
# The 5 trees are:
# - The three single '1' leaf nodes. (+3)
# - The single '0' leaf node. (+1)
# - The [1, 1, 1] tree at the bottom. (+1)


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# This function will check whether all nodes in sub-trees are the same value
# This presents inefficiency if we call this function for all nodes in the tree
def isUnival(root, value):
    if not root:
        return True
    if root.left and root.left.val != value:
        return False
    if root.right and root.right.val != value:
        return False
    if root.val == value:
        return isUnival(root.left, value) and isUnival(root.right, value)


def countUnivalTreesOn2(root, numUnivalTrees):
    if root:
        print("Current node", root.val)
        if isUnival(root, root.val):
            numUnivalTrees += 1
        nextNodes = [root.left, root.right]
        for n in nextNodes:
            numUnivalTrees = countUnivalTreesOn2(n, numUnivalTrees)

    return numUnivalTrees


def countUnivalTreesOn(root):
    totalCount, _ = findNumOfUnivalTrees(root)
    return totalCount


# This will solve the algorithm in O(n) complexity
def findNumOfUnivalTrees(root):
    if not root:  # Empty tree is considered unival
        return 0, True
    # print("current node", root.val)
    univalsAtLeft, isUnivalAtLeft = findNumOfUnivalTrees(root.left)
    univalsAtRight, isUnivalAtRight = findNumOfUnivalTrees(root.right)
    print("current node", root.val)
    treeIsUnival = True
    if not isUnivalAtLeft or not isUnivalAtRight:
        treeIsUnival = False
    if root.left and root.left.val != root.val:
        treeIsUnival = False
    if root.right and root.right.val != root.val:
        treeIsUnival = False
    if treeIsUnival:
        return univalsAtLeft + univalsAtRight + 1, True
    else:
        return univalsAtLeft + univalsAtRight, False


a = Node('a')
a.left = Node('c')
a.right = Node('b')
a.right.left = Node('b')
a.right.right = Node('d')
# a.right.left.left = Node(1)
# a.right.left.right = Node('b')
a.right.right.right = Node('d')

# print(countUnivalTreesOn2(a, 0))
print(countUnivalTreesOn(a))
