import ctypes
class Dynamic_array:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)
    def __len__(self):
        return self.n
    def append(self,item):
        if self.n == self.size:
            #resize
            self.__resize(self.size*2)
        
        #append
        self.A[self.n] =item
        self.n = self.n +1
        
    #printing the list
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i])+','
        return "["+ result[:-1] +"]"
    
    #popping the value
    def pop(self):
        if self.n == 0:
            return "empty List"
        print(self.A[self.n-1])
        self.n = self.n - 1
        
    #Accessing the list by the idex value
    def __getitem__(self,index):
        if 0<= index <self.n:
            return self.A[index]
        else:
            return "Index Error--> Not valid Index"
        
        
    def __resize(self,new_capacity):
        #create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        #copy the content of A to B
        for i in range(self.n):
            B[i]= self.A[i]
            #reassign A
        self.A = B
            
    #Making an array    
    def __make_array(self,capacity):
        return(capacity*ctypes.py_object)()
    
    #clearing the list
    def clear(self):
        self.n = 0
        self.size = 1
    
    #finding the item in the array
    def find(self,item):
        for i in range(self.n):
            if self.A[i]==item:
                return i
        return 'value error not in the list'
    
    def remove(self,item):
        pos = self.find(item)
        if type(pos)==int:
            #deleting
            self.__delitem__(pos)
        else:
            return pos
        
    
    #inserting into the list
    def insert(self,position,item):
    # We are just swaping the item in the list and making a space to insert the given
    #item
        if self.n == self.size:
            self.__resize(self.size*2)
        for i in range(self.n,position,-1):
            self.A[i] = self.A[i-1]
        self.A[position]= item
        self.n = self.n +1
        
    #Deleting a item with position
    def __delitem__(self,pos):
        for i in range(pos,self.n-2):
            self.A[i] =self.A[i+1]
        self.n = self.n-1
        
l = Dynamic_array()
l.append("Saam")
l.append("1")
l.append("silwal")
l.append("Youtube")
l.insert(2,"Tribhuwan")
print(l)
