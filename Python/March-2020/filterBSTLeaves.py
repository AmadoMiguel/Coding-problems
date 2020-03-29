class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left, self.right = left, right

def showTree(root, side, level):
	if root:
		print(str(root.value), side, "level: " + str(level))
		showTree(root.left, "left", level + 1)
		showTree(root.right, "right", level + 1)
		
def isLeaf(node):
	return not node.left and not node.right

# Filter leaves with value = k, from bottom to top
def filterLeaves(root, k):
	if root:
		root.left = filterLeaves(root.left, k)
		root.right = filterLeaves(root.right, k)
		if isLeaf(root):
			if root.value == k:
				return None
			return root
	return root

n5 = Node(2)
n4 = Node(1)
n3 = Node(1, n4)
n2 = Node(1, n5)
n1 = Node(1, n2, n3)

print("Before filter:")
showTree(n1, "parent", 0)
print("\n")
n1 = filterLeaves(n1, 1)
print("After filter:")
showTree(n1, "parent", 0)
