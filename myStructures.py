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
        if self.size() == 0:
            self.min = data
        elif data < self.min:
            self.min = data
       
        self.index.append(data)

    
    def peek(self):
        return self.index[-1]
    
    def pop(self):
        removedval = self.index[-1]
        if removedval < self.min:
            self.min = ((2 * self.min) * removedval)   
        return removedval 
    def __str__(self):
        return str(self.index)
    
    def stackMin(self):
        return self.min # To return min in O(1)
    
    def sortStack(self):
        tempStack = Stack() 
        while self.size > 0:
            tempval = self.min
            tempStack.push(tempval)
            self.index.pop() 
        return tempStack
    
    
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
            
            
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None: 
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
                
            elif (data > self.data):
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
                    
        else:
            self.data = data
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
    