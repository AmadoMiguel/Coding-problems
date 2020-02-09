class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
	
	def __str__(self):
		toString = []
		queue = [(self, 0)]
		while len(queue):
			(currNode, level) = queue[0]
			queue.pop(0)
			if currNode:
				if level < len(toString):
					toString[level] += currNode.value
				else:
					toString += [currNode.value]
				if currNode.left:
					queue.append((currNode.left, level + 1))
				if currNode.right:
					queue.append((currNode.right, level + 1))
		return "\n".join(toString)
	
	
root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')
root.right.right = Node('g')

print(root)
