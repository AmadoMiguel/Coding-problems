# Define the base data structure inside a linked list (node)
# Left-side childs decrease its value; right-side ones, increases
class Node:
    def __init__(self,val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
    # Recursive insert method
    def insert(self,data):
        if self.value == data:
            return False
        # If value to insert is less than actual node...    
        elif self.value > data:
            # Check if there is a child node at the left side
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                # if not, a new node is created with data assigned to it
                self.leftChild = Node(data)    
                return True
        # If value to insert is greater than actual node...          
        else:
            # Check if there is a child node at the right side
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                # If not, a new node is created with data assigned to it
                self.rightChild = Node(data)     
                return True          
    # Recursive find method
    def find(self,data):
        # If the value at the actual node equals the data being searched
        if self.value == data:
            return True
        # If the data being searched is less than the actual node's value..    
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)    
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False         
    # Ordering methods
    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()   
            if self.rightChild:
                self.rightChild.preorder()
    def postorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.postorder()   
            if self.rightChild:
                self.rightChild.postorder()
    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder() 
            print(str(self.value))    
            if self.rightChild:
                self.rightChild.inorder()                                   

class Tree:
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
            return self.root.find(data)
        else: 
            # In case there is no root node..
            # The data is not in the tree
            return False    
    # Ordering methods
    def preorder(self):
        print("PreOrder")
        self.root.preorder()        
    def postorder(self):
        print("PostOrder")
        self.root.preorder()
    def inorder(self):
        print("InOrder")
        self.root.preorder()        

t = Tree()
t.insert(10)        
t.insert(9)
t.insert(15)
t.insert(2)
t.insert(8)
