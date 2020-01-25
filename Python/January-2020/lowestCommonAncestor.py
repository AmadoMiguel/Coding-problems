# You are given the root of a binary tree, along with two nodes, A and B. Find and return the lowest common ancestor
# of A and B. For this problem, you can assume that each node also has a pointer to its parent, along with its left
# and right child.


class TreeNode(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val

    def __str__(self):
        toString = "Current Node: " + str(self.val) + "\n\t"
        toString += "* Left Child: "
        if self.left:
            toString += str(self.left.val)
        else:
            toString += "None"
        toString += "\n\t"
        toString += "* Right Child: "
        if self.right:
            toString += str(self.right.val)
        else:
            toString += "None"

        return toString


# Traverse the tree and store the first found node which has as left/right child whether a or b
def findLowestCommonAncestor(root, a, b):
    if not root:
        return None
    if root.val == a.val or root.val == b.val:
        return root
    # Check if children mach nodes a and b
    lcaLeft = findLowestCommonAncestor(root.left, a, b)
    lcaRight = findLowestCommonAncestor(root.right, a, b)
    # In this case, a is going to be in one side of the tree and b in the other side
    if lcaLeft and lcaRight:
        return root
    # In this case, both are going to be on the left/right side of the tree
    if not lcaLeft:
        return lcaRight
    return lcaLeft


root = TreeNode('a')
root.left = TreeNode('b')
root.left.parent = root
root.right = TreeNode('c')
root.right.parent = root
a = root.right.left = TreeNode('d')
root.right.left.parent = root.right
b = root.right.right = TreeNode('e')
root.right.right.parent = root.right

print(findLowestCommonAncestor(root, a, b))
