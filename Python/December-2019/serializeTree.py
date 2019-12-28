# You are given the root of a binary tree. You need to implement 2 functions:
#
# 1. serialize(root) which serializes the tree into a string representation
# 2. deserialize(s) which deserializes the string back to the original tree that it represents
#
# For this problem, often you will be asked to design your own serialization format. However, for simplicity,
# let's use the pre-order traversal of the tree


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # pre-order printing of the tree.
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result


# Created in pre-order traversal
def serializeTree(root, serialVersion):
    if not root:  # Leaf is reached
        serialVersion += "#"
        return serialVersion
    serialVersion += str(root.val)
    serialVersion = serializeTree(root.left, serialVersion)
    serialVersion = serializeTree(root.right, serialVersion)

    return serialVersion


def deserializeTree(serialVersion):
    return "".join([n for n in serialVersion if n != "#"])


tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

serialTree = serializeTree(tree, "")
print(serialTree)
print(deserializeTree(serialTree))
