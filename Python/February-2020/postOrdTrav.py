class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left, self.right = left, right

def printPostOrder(root):
	if root:
		printPostOrder(root.left)
		printPostOrder(root.right)
		print(root.value)
	#else:
		#print("NONE")

def create_tree(postOrder):
	if create_tree.index >= 0 and postOrder[create_tree.index] is not None:
		root = Node(postOrder[create_tree.index])
		create_tree.index -= 1
		root.right = create_tree(postOrder)
		root.left = create_tree(postOrder)
		return root
	create_tree.index -= 1
	# return
	
def buildTree(postOrderTrav):
	create_tree.index = len(postOrder) - 1
	return create_tree(postOrderTrav)


n8 = Node(7)
n7 = Node(9, None, n8)
n6 = Node(6)
n5 = Node(3)
n4 = Node(1)
n3 = Node(8, n6, n7)
n2 = Node(2, n4, n5)
root = Node(4, n2, n3)
print("This is original post order: ")
printPostOrder(root)
postOrder = [None, None, 1, None, None, 3, 2, None, None, 6, None, None, None, 7, 9, 8, 4]
print("Created post order: ")
printPostOrder(buildTree(postOrder))
