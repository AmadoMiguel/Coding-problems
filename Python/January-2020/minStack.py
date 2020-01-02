# Design a simple stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
# Note: be sure that pop() and top() handle being called on an empty stack.

from collections import deque


class StackNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def prePendNode(head, num):
    newNode = StackNode(num)
    newNode.next = head
    head = newNode
    return head


# LIFO Linked List
class Stack(object):
    def __init__(self):
        self.head = None
        self.headMinNums = None

    def push(self, n):
        self.head = prePendNode(self.head, n)
        if not self.headMinNums or self.headMinNums.value > n:
            self.headMinNums = prePendNode(self.headMinNums, n)

    def pop(self):
        if self.head:
            v = self.head.value
            if self.headMinNums:
                if self.headMinNums.value == v:
                    self.headMinNums = self.headMinNums.next
            self.head = self.head.next

    def top(self):
        if self.head:
            return self.head.value
        return None

    def getMin(self):
        if self.headMinNums:
            return self.headMinNums.value
        return None

    def __str__(self):
        stackStr = "Stack elements: "
        dq = deque()
        dq.append(self.head)
        while len(dq):
            currNode = dq.popleft()
            if currNode:
                stackStr += str(currNode.value) + ","
                dq.append(currNode.next)
        return stackStr[:-1]


minStackImpl = Stack()
minStackImpl.push(-2)
minStackImpl.push(0)
minStackImpl.push(-3)
minStackImpl.push(8)
minStackImpl.push(-20)
minStackImpl.push(13)
print(minStackImpl)
print(minStackImpl.getMin())
minStackImpl.pop()
minStackImpl.pop()
print(minStackImpl)
print(minStackImpl.top())
print(minStackImpl.getMin())
