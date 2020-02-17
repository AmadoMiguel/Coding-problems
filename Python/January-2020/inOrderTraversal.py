
class Node(object):
    def __init__(self, v):
        self.v = v
        self.left, self.right = None, None


def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.v)
        printInOrder(root.right)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.right = Node(4)
tree.right.left = Node(9)
tree.left.left = Node(0)
printInOrder(tree)
