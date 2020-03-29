class Node(object):
	def __init__(self, value, next = None):
		self.value = value
		self.next = next
	
	def __str__(self):
		if self:
			return str(self.value) + "->" + str(self.next)
		return ""


# Recursively swap linked list every 2 nodes
def swapNodes(head):
	if head and head.next:
		temp = head.value
		head.value = head.next.value
		head.next.value = temp
		swapNodes(head.next.next)


n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
head = Node(1, n2)
print(head)

swapNodes(head)
print(head)
