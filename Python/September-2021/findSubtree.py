# Given 2 binary trees t and s, find if s has an equal subtree in t, where the structure and the 
# values are the same. Return True if it exists, otherwise return False.

# Here's some starter code and an example:

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return f"(Value: {self.value} Left: {self.left} Right: {self.right})"

def are_trees_equal(t1, t2):
    if s is None and t is None:
        return True
    if s is None or t is None:
        return False
    if s.value == t.value:
        if are_trees_equal(s.left,t.left) and are_trees_equal(s.right,t.right):
            return True
    return False

def find_subtree(s, t):
    if t is None:
        return True
    if s is None:
        return False
    if are_trees_equal(s, t):
        return True
    return find_subtree(s,t.left) or find_subtree(s,t.right)

t3 = Node(4, Node(3), Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t2, t3)

s = Node(4, Node(3), Node(2))
otherS = Node(1, s)
# """
# Tree t:
#     1
#    / \
#   4   5 
#  / \ / \
# 3  2 4 -1

# Tree s:
#   4 
#  / \
# 3  2 
# """

print(find_subtree(otherS, t))
