from inspect import stack
from xml.etree.ElementTree import iselement


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
    
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
            
            
class Stack: 
    def __init__(self):
       self.index = []
       self.min = None # for min 
       
    def size(self):
        return len(self.index)

    def push(self, data):
        if (self.min == None) or (self.min > data):
            self.min = data
        self.index.insert(0, data)
    
    def peek(self):
        if len(self.index) == 0:
            raise "Nothing to Peek"
        return self.index[0]
    
    def pop(self):
        if len(self.index) == 0:
            raise "Nothing to Pop"
        return self.index.pop(0)
    
    def __str__(self):
        return str(self.index)
    
    def stackMin(self):
        return self.min # To return min in O(1)
    
    
class StackOfStacks:
    def __init__(self):
        self.listStacks = []
        self.stack = Stack()
        self.listStacks.append(stack)
        self.threshold = 5 # No more than 5 elements 

    def ssPrint(self):
        for tempStacks in self.listStacks:
            print(tempStacks) 


            
    def ssPush(self, data):
        if self.stack.size() > self.threshold:

            newStack = Stack()
            newStack.push(data)
            self.listStacks.append(newStack)
            self.stack = newStack
            
        else:
            self.stack.push(data)
    
            
    def ssPop(self):
      self.stack.pop()  
            
            
        
    