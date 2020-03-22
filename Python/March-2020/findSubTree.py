# Given 2 binary trees t and s, find if s has an equal subtree in t, where the structure and the values are the same.
# Return True if it exists, otherwise return False.


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def areEqual(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 and tree2:
        return False
    if tree1 and not tree2:
        return False
    return tree1.value == tree2.value \
           and areEqual(tree1.left, tree2.left) \
           and areEqual(tree1.right, tree2.right)


def containsSubTree(root, subRoot):
    if root:
        return areEqual(root, subRoot) \
               or containsSubTree(root.left, subRoot) \
               or containsSubTree(root.right, subRoot)
    return False


def findSubtree(mainTree, subTree):
    if not subTree:
        return True
    return containsSubTree(mainTree, subTree)


# Main tree
t3 = Node(4, Node(3), Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t3, t2)
# Sub tree
s = Node(4, Node(3), Node(2))

assert findSubtree(t, s)  # True
