class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None   #if self.head = None then it is called a empty list
        self.n = 0 #This denotes the number of nodes
    
    def __len__(self):
        return self.n
    
    def insert_head(self,value):
        #Creating a new node
        new_node = Node(value)
        #creating connection 
        new_node.next = self.head
        #assigning a new head
        self.head = new_node
        #incrementing n
        self.n = self.n+1
        
    def __str__(self): 
        #This method is also called traversing
        
        result = ""
        curr = self.head
        while(curr!=None):
            result = result + str(curr.data) + "->"
            curr = curr.next
        return result[:-2]
    
    def append(self,value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        

l = Linked_list()
l.insert_head(6)
l.insert_head(4)
l.insert_head(3)
print(l)
