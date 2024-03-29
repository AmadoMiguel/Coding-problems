# A number can be constructed by a path from the root to a leaf. Given a binary tree, sum all the numbers that
# can be constructed from the root to all leaves.
#
# Here's an example and some starter code.

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return f"({self.value}, {self.left}, {self.right})"


def bst_numbers_sum(root, num=0):
  if root is None:
    print(num)
    return num
  bst_numbers_sum.total += bst_numbers_sum(root.left, int("".join([str(num), str(root.value)])))
  bst_numbers_sum.total += bst_numbers_sum(root.right, int("".join([str(num), str(root.value)])))
  return bst_numbers_sum.total


n5 = Node(5)
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  / \
# 4   5
bst_numbers_sum.total = 0
print(bst_numbers_sum(n1))
# 262
# Explanation: 124 + 125 + 13 = 262
