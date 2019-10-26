# You are given two linked-lists representing two non-negative integers. The digits are stored in reverse
# order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addLinkedLists(l1, l2):
    rem = 0
    result = ''
    a = l1
    b = l2
    while a is not None and b is not None:
        currSum = a.val + b.val + rem
        if currSum < 10:
            result += str(currSum)
        else:
            rem = currSum // 10
            result += str(currSum % 10)
        print(a.val, b.val, result, rem)
        a = a.next
        b = b.next
    if rem:
        result += str(rem)
    return result


# Initialize first linked list
linkList1 = ListNode(9)
linkList1.next = ListNode(9)
linkList1.next.next = ListNode(9)
linkList1.next.next.next = ListNode(9)
# Initialize second linked list
linkList2 = ListNode(9)
linkList2.next = ListNode(9)
linkList2.next.next = ListNode(9)
linkList2.next.next.next = ListNode(9)

print(addLinkedLists(linkList1, linkList2))
