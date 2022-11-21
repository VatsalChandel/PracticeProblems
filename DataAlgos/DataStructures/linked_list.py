class Node:
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):  
        self.head = None
  
    def insert(self, data):
        newNode = Node(data)
        
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        counter = 0
        while(current):
            counter += 1
            current = current.next 
        return counter 
    
    def search(self, key):
        current = self.head
        while(current):
            if current == key:
                return current
            else:
                current = current.next 
        return "key not found"
    
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
            
            
