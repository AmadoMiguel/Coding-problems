# Main element inside the linked list
class Node:
    def __init__(self,val):
        self.value = val
        self.rightVal = None
    def insert(self,data):
        if self.value == data:
            return False       
        else:
            # Check if there is a child node at the right side
            if self.rightVal:
                return self.rightVal.insert(data)
            else:
                # If not, a new node is created with data assigned to it
                self.rightVal = Node(data)     
                return True    
    def find(self,data):
        # If the value at the actual node equals the data being searched
        if self.value == data:
            return True
        else:
            # If actual node's value doesn't correspond to data, 
            # go to the next one.
            if self.rightVal:
                return self.rightVal.find(data)
            else:
                return False   

class linkedList:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            # If the data to asign to the node
            self.root = Node(data)
            return True 
    # Returns a boolean that tells if data is in the tree or not
    def find(self,data):
        # Check for a root
        if self.root:
            # Calls the Node class find() method
            return self.root.find(data)
        else: 
            # In case there is no root node..
            # The data is not in the tree
            return False       

def searchInterNodes(l1,l2):
    commonNodes = []
    val = l1.root   
    while val.value:
        print(val.value)
        if l2.find(val.value):
            commonNodes.append(val.value)
        # Go to the next node    
        val = val.rightVal      
        if val is None:
            break  
    return commonNodes    

l1 = linkedList()
l1.insert(3)
l1.insert(7)
l1.insert(8)
l1.insert(10)

l2 = linkedList()
l2.insert(99)
l2.insert(1)
l2.insert(8)
l2.insert(1)

print( searchInterNodes(l1,l2) )