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
        self.n = self.n+1
     
    def insert_after(self,after,value):
        new_node = Node(value)
        curr = self.head
        while curr!= None:
            if curr.data== after:
                break
            curr = curr.next
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n+1
        else:
            return  'Item not found'
        #Clearing a List
    def clear(self):
        self.head = None
        self.n = 0
    
    #deleting the head
    def delete_head(self):
        if self.head == None:
            return 'List is empty'
        self.head = self.head.next
        self.n = self.n-1
    
    #deleting the tail
    def pop(self):
        if self.n == 0:
            return 'empty Linked list'
        if self.n == 1:
            self.head = None
            self.n = self.n-1
            return
        curr = self.head
        while(curr.next.next!=None):
            curr = curr.next
        curr.next = None
        self.n = self.n-1
        
    #deleting a item by its value
    def remove(self,value):
        if self.head == None:
            return 'Empty Linked List'
        if self.head.data == value:
            return self.delete_head()
        curr = self.head
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        if curr.next == None:
            return 'Not found'
        else:
            curr.next = curr.next.next
    # We search the index  
    def search(self,value):
        curr = self.head
        count = 0
        while curr!= None:
            if curr.data == value:
                break
            curr = curr.next
            count = count+1
        if curr== None:
            return 'Not in the list'
        return count
    
    #getting item by idex in a linked list
    def __getitem__(self,index):
        if index>self.n-1:
            return 'invalid Index'
        curr = self.head
        count = 0
        while curr!= None:
            if count == index:
                break
            curr = curr.next
            count +=1
        
        return curr.data
   
    
    #Reversing a linked list
    def reverse_llist(self):
        curr = self.head
        prev = None
        while curr is not None:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node
        return prev
    
    #Getting Max value in the linked list
    def max_value(self):
        temp = self.head
        maxx = temp
        
        while temp != None:
            if temp.data > maxx.data:
                maxx = temp
            temp = temp.next
            
        return maxx.data
    
    
        
    
