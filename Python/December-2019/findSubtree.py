# Given two binary trees t1 and t2, determine whether the second tree is a subtree of the first tree. A subtree
# for vertex v in a binary tree t is a tree consisting of v and all its descendants in t. Determine whether or
# not there is a vertex v (possibly none) in tree t1 such that a subtree for vertex v (possibly empty) in t1 equals t2.


class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None


def areEqual(t1, t2, equal):
    if not t1 and not t2:
        return equal
    if not t1 and t2:
        return False
    if t1 and not t2:
        return False
    if equal:
        if t1.value != t2.value:
            equal = False
        equal = areEqual(t1.left, t2.left, equal)
        equal = areEqual(t1.right, t2.right, equal)
    return equal


def findSubtree(t1, t2, found):
    if not found:
        if not t1:
            return found
        if areEqual(t1, t2, True):
            found = True
        found = findSubtree(t1.left, t2, found)
        found = findSubtree(t1.right, t2, found)
    return found


def isSubtree(t1, t2):
    if not t2:
        return True
    return findSubtree(t1, t2, False)


root1 = Tree(5)
root1.left = Tree(10)
root1.right = Tree(7)
root1.left.left = Tree(4)
root1.left.right = Tree(-6)
root1.left.left.left = Tree(1)
root1.left.left.right = Tree(2)
root1.left.right.right = Tree(-1)

root2 = root1.left

print(isSubtree(root1, root2))
