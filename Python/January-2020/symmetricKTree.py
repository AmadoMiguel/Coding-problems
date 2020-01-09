# A k-ary tree is a tree with k-children, and a tree is symmetrical if the data of the left side of the tree is the
# same as the right side of the tree.
#
# Here's an example of a symmetrical k-ary tree.
#         4
#      /     \
#     3        3
#   / | \    / | \
# 9   4  1  1  4  9
# Given a k-ary tree, figure out if the tree is symmetrical.


class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []


def isPalindrome(arr):
    ptr1, ptr2 = 0, len(arr) - 1
    while ptr1 < ptr2:
        if arr[ptr1] != arr[ptr2]:
            return False
        ptr1, ptr2 = ptr1 + 1, ptr2 - 1
    return True


def getChildrenAndLevels(tree, level, levels):
    if level in levels.keys():
        levels[level] += [tree.value]
    else:
        levels[level] = [tree.value]

    if len(tree.children):
        for ch in tree.children:
            levels = getChildrenAndLevels(ch, level + 1, levels)

    return levels


def isSymmetric(tree):
    childrenAtLevels = getChildrenAndLevels(tree, 0, {})
    print(childrenAtLevels)
    for ch in childrenAtLevels.values():
        if len(ch) > 1:
            if len(ch) % 2 == 0:
                if not isPalindrome(ch):
                    return False
            else:
                return False
    return True


tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]

print(isSymmetric(tree))
