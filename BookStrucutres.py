from inspect import stack
from myStructures import *  # For LinkedList


def main():
    #chapter1()
    
    #chapter2()
    
    chapter3()
    


    
    
# Chapter 1
def chapter1(): 
    temp_string = "hello"
    print(isUnique(temp_string))
    
    a = "Hello"
    b = "Holel"
    print(isPermutation(a, b))
    
    url = "Hello World"
    print(URLify(url))
       
def isUnique(string):
    temp_dictionary = {}
    for letters in string: 
        if letters in temp_dictionary:
            return False
        else:
            temp_dictionary[letters] = 1
    return True

def isPermutation(a, b):
    if len(a) != len(b):
        return False
    else: 
        a = str(''.join(sorted(a)))   
        b = str(''.join(sorted(b)))   
        if a != b:
            return False
    return True

def URLify(url): 
    return url.replace(' ', '%20')
# Chapter 1


# Chapter 2
def chapter2():
     #Chapter 2 
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    print("Before removing dups:")
    ll.printLL()
    removeDups(ll)
    print("After removing dups")
    ll.printLL()  

    print()
        
    print("Finding kth to last element")
    kthLast(ll, 2)
    
    print()
    
    print("Adding LinkedList")
    ll1 = LinkedList()
    ll1.insert(5)
    ll1.insert(9)
    ll1.insert(2)
    
    ll2 = LinkedList()
    ll2.insert(7)
    ll2.insert(1)
    ll2.insert(6)
    sumLists(ll1, ll2)    
    
    print()
    
    print("Trying to detect Loop in List")
    ll3 = LinkedList()
    ll3.insert(3)
    ll3.insert(6)
    ll3.insert(9)
    ll3.insert(12)
    ll3.head.next = ll3.head # creates loop in LinkedList
    print(loopDetection(ll3))
    
def removeDups(self):
    current = self.head 
    prev = None
    uniqueSet = set()
    while current != None:
        if current.data in uniqueSet:
            prev.next = current.next
        else:
            uniqueSet.add(current.data)
            prev = current
        current = prev.next
        
def kthLast(self, k):
    temp = self.head
    temp1 = self.head
    counter = 0 
    while temp is not None: 
        counter += 1
        temp = temp.next 
    if k > counter:
        print("Location is out of Bounds!")
    else: 
        for i in range(counter - k):
            temp1 = temp1.next
        print(temp1.data)
    
def sumLists(ll1, ll2):
    finalSum = 0
    
    ll1Sum = ""
    ll2Sum = ""

    temp2 = ll2.head
    temp1 = ll1.head
    
    while temp1 != None: 
        ll1Sum = str(temp1.data) + ll1Sum
        temp1 = temp1.next
    
    while temp2 != None: 
        ll2Sum = str(temp2.data) + ll2Sum
        temp2 = temp2.next
        
    finalSum = int(ll1Sum) + int(ll2Sum)
    finalList = LinkedList() 
    while finalSum != 0: 
        digit = finalSum % 10
        finalList.insert(digit)
        finalSum = finalSum // 10 
    finalList.printLL()
        
def loopDetection(self):
    temp = self.head
    temp2 = self.head
    while (temp2 != None and temp2.next != None):
        temp = temp.next
        temp2 = temp2.next.next
        if temp == temp2:
            return "Loop Detected"
    else: return "No Loop"
# Chapter 2 
    
# Chapter 3
def chapter3(): 
    stack = Stack()
    for i in range(4, 11):
        stack.push(i)
    #print(stack)
   
    #print(stack.stackMin())
    
    stackst = StackOfStacks()
    for i in range(0, 11):
        stackst.ssPush(i)
    
    stackst.ssPrint()


# Chapter 3 
    
    
    
        
        

if __name__ == "__main__":
    main()