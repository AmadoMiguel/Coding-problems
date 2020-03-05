class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
	
	def __str__(self):
		result = str(self.value)
		if self.left:
			result += str(self.left)
		if self.right:
			result += str(self.right)
		return result

def insertValue(value, root):
	if not root:
		root = Node(value)
		return root
	if value < root.value:
		root.left = insertValue(value, root.left)
	elif value > root.value:
		root.right = insertValue(value, root.right)
	return root

def buildTrees(currRoot, currValues, remValues, trees):
	if not len(remValues):
		#print(currValues)
		print(currRoot)
		trees += [currRoot]
	else:
		for i in range(len(remValues)):
			curr = currValues + [remValues[i]]
			root = insertValue(remValues[i], currRoot)
			buildTrees(root, curr, remValues[:i] + remValues[i + 1:], trees)

def generateBSTs(n):
	allTrees = []
	values = [i + 1 for i in range(n)]
	buildTrees(None, [], values, allTrees)
	return allTrees

bsts = generateBSTs(3)