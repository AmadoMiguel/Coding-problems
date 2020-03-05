class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left, self.right = left, right
	
def getHeight(root):
	if not root:
		return 0
	return 1 + max(getHeight(root.left), getHeight(root.right))

def isBalanced(root):
	# Empty tree is balanced
	if not root:
		return True
	if not root.left and not root.right:
		return True
	if not root.left or not root.right:
		return False
	leftH = getHeight(root.left)
	rightH = getHeight(root.right)
	return abs(leftH - rightH) <= 1 and isBalanced(root.left) and isBalanced(root.right)


n5 = Node(5)
n4 = Node(4, None, n5)
n6 = Node(6)
n3 = Node(3, None, n6)
n2 = Node(2, n4)
root = Node(1, n2, n3)
print(isBalanced(root))
