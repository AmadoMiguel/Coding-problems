# Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling
# (larger than or equal to) of k. If either does not exist, then print them as None.


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def findFloorAndCeilOfK(root, k, ceil, floor):
    if root is not None:
        if root.val >= k:
            if ceil is None or root.val <= ceil:
                ceil = root.val
        elif root.val <= k:
            if floor is None or root.val >= floor:
                floor = root.val
        nextNodes = [root.left, root.right]
        for n in nextNodes:
            ceil, floor = findFloorAndCeilOfK(n, k, ceil, floor)
    return ceil, floor


root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(findFloorAndCeilOfK(root, 5, None, None))
