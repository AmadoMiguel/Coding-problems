# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None


def isListPalindrome(l):
    normal = []
    current = l
    while current != None:
        normal.append(current.value)
        current = current.next

    return "".join([str(n) for n in normal]) == "".join([str(n) for n in reversed(normal)])
