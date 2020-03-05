class Node(object):
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
	def __str__(self):
		if self:
			return str(self.value) + " " + str(self.next)
		return ""

def appendNode(head, value):
	if not head:
		return Node(value)
	else:
		head.next = appendNode(head.next, value)
	return head

def appendList(l1, l2):
	if not l1:
		return l2
	else:
		l1.next = appendList(l1.next, l2)
	return l1

def rotateListByK(list, k):
	aux = None
	numPlaces = 0
	while numPlaces < k and list:
		aux = appendNode(aux, list.value)
		list = list.next
		numPlaces += 1
	list = appendList(list, aux)
	return list
		
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
newList = rotateListByK(head, 2)
print(newList)
