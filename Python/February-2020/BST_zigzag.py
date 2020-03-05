class Node(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def getNodesInZigZag(root):
    allValues = []
    # Simulate queue with raw array.
    # Initialize with a tuple containing
    # root node and level number (root is level 0)
    q = [(root, 0)]
    while len(q):
        (currNode, level) = q.pop(0)
        if currNode:
            if level < len(allValues):
                if level == 1 or level % 2 != 0:
                    allValues[level].insert(0, currNode.value)
                else:
                    allValues[level].append(currNode.value)
            else:
                allValues += [[currNode.value]]
            if currNode.left:
                q.append((currNode.left, level + 1))
            if currNode.right:
                q.append((currNode.right, level + 1))
    joinedValues = []
    for values in allValues:
        for v in values:
            joinedValues += [v]
    return joinedValues


n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)
print(getNodesInZigZag(n1))
