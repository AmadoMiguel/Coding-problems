# You have a singly linked list l, which is sorted in strictly increasing order, and an integer value.
# Add value to the list l, preserving its original sorting.


class ListNode(object):
    def __init__(self, x, next=None):
        self.value = x
        self.next = next

    def __str__(self):
        if self:
            return str(self.value)+"->"+str(self.next)
        return "None"


def iV(h,v):
    if not h:
        return ListNode(v)
    if v < h.value:
        nN = ListNode(v)
        nN.next = h
        return nN
    if h.next:
        if h.value < v < h.next.value:
            nN = ListNode(v)
            nN.next = h.next
            h.next = nN
            return h
        h.next = iV(h.next, v)
    else:
        h.next = ListNode(v)
    return h


def insertValueIntoSortedLinkedList(l, value):
    if not l:
        return ListNode(value)
    l = iV(l, value)
    return l


head = ListNode(1, ListNode(3, ListNode(4, ListNode(6))))
print(insertValueIntoSortedLinkedList(head, 5))
head = ListNode(1, ListNode(3, ListNode(4, ListNode(6))))
print(insertValueIntoSortedLinkedList(head, 10))
head = ListNode(1, ListNode(3, ListNode(4, ListNode(6))))
print(insertValueIntoSortedLinkedList(head, 0))
