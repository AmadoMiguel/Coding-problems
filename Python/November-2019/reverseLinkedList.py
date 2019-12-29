# Reverse a singly linked list


# Class for Nodes in LinkedList
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def insertKey(linkList, node):
    if not linkList:
        linkList = node
        linkList.next = None
        return linkList
    linkList.next = insertKey(linkList.next, node)
    return linkList


def reverseLinkedListBruteForce(linkList, reversed):
    if linkList:
        reversed = reverseLinkedListBruteForce(linkList.next, reversed)
        reversed = insertKey(reversed, linkList)
    return reversed


def reverseLinkedListIter(linkList):
    # If head is None or there's only one node
    if not linkList or not linkList.next:
        return linkList
    # Get next nodes of the list and initialize reversed list
    restOfList = linkList.next
    reversedList = linkList
    reversedList.next = None
    while restOfList:
        tempNode = restOfList
        # Advance to next node and re-wire nodes
        restOfList = restOfList.next
        tempNode.next = reversedList
        reversedList = tempNode
    return reversedList


def reverseLinkedListRecur(linkedList):
    if not linkedList or not linkedList.next:
        return linkedList
    # Exhaust until reaching the ent of the list
    reversedList = reverseLinkedListRecur(linkedList.next)
    linkedList.next.next = linkedList
    linkedList.next = None
    return reversedList


# Create a linked list with some elements
linkedList = LinkedList(1)
linkedList.next = LinkedList(2)
linkedList.next.next = LinkedList(3)
linkedList.next.next.next = LinkedList(4)
linkedList.next.next.next.next = LinkedList(5)


revLinkedList = reverseLinkedListBruteForce(linkedList, None)
# revLinkedList = reverseLinkedListIter(linkedList)
# revLinkedList = reverseLinkedListRecur(linkedList)
while revLinkedList:
    print(revLinkedList.value)
    revLinkedList = revLinkedList.next
