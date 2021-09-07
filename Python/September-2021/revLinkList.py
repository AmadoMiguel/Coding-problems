# Reverse a Linked List:
# 1 -> 2 -> 3 -> 4 -> 5 -> None
# 5 -> 4 -> 3 -> 2 -> 1 -> None

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self) -> str:
        if self is None:
            return "None"
        return str(self.value) + " -> " + self.next.__repr__()

def rev_link_list(link_list):
    if link_list is None or link_list.next is None:
        return link_list
    rev_list = rev_link_list(link_list.next)
    link_list.next.next = link_list
    link_list.next = None
    return rev_list

link_list = Node(1,Node(2,Node(3,Node(4,Node(5)))))
print(link_list)
rever_link_list = rev_link_list(link_list)
print(rever_link_list)