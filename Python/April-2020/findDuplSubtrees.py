# Given a binary tree, find all duplicate subtrees (subtrees with the same value and same structure) and return
# them as a list of list [subtree1, subtree2, ...] where subtree1 is a duplicate of subtree2 etc.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left and self.right:
            return f"({self.value}, {self.left}, {self.right})"
        if self.left:
            return f"({self.value}, {self.left})"
        if self.right:
            return f"({self.value}, None, {self.right})"
        return f"({self.value})"


def findDupl(root):
    if root:
        findDupl(root.left)
        findDupl(root.right)
        if root.__repr__() in findDupl.hM.keys():
            findDupl.dT.append(root)
        else:
            findDupl.hM[root.__repr__()] = 0


n3_1 = Node(3)
n2_1 = Node(2, n3_1)
n3_2 = Node(3)
n2_2 = Node(2, n3_2)
n1 = Node(1, n2_1, n2_2)
findDupl.hM = {}
findDupl.dT = []
findDupl(n1)
print(findDupl.dT)
