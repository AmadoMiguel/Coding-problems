
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        if self:
            return str(self.value) + "->" + str(self.next)
        else:
            return "None"


def merge(l1, l2):
    if not l1:
        return l2
    l1.next = merge(l1.next, l2)
    return l1


def reverse(linList):
    if linList:
        # Used to adjust how many nodes are going to be reversed
        numRev = 2
        currNumRev = 1
        revList = Node(linList.value)
        linList = linList.next
        while linList and currNumRev < numRev:
            curr = Node(linList.value)
            linList = linList.next
            curr.next = revList
            revList = curr
            currNumRev += 1
        if linList:
            merge(revList, linList)
        return revList
    return linList


head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print("Original", head)
revList = reverse(head)
print("Reversed", revList)
