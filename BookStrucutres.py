from inspect import stack
from myStructures import *  # For LinkedList


def main():
    #chapter1()
    
    chapter2()
    
    #chapter3()
    
    


    
    
# Chapter 1
def chapter1(): 
    print("IsUnique")
    temp_string = "hello"
    print(isUnique(temp_string))
    
    print()

    print("isPermutation")
    a = "Hello"
    b = "Holel"
    print(isPermutation(a, b))
    
    print()

    print("URLify")
    url = "Hello World"
    print(URLify(url))
    
    print()

    print("PalindromePermutation")
    perm = "Kayak"
    print(palindromePermutation(perm))
    
    print()

    print("oneAway")
    print(oneAway("pale", "pales"))
    
    print()
    
    print("StringCompression")
    print(stringCompression("aabcccccaaa"))
    
       
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

def palindromePermutation(str):
    str = str.lower()
    str = str.replace(' ', '')
    
    letter_dict = {}
    
    for letters in str:
        if letters in letter_dict:
            letter_dict[letters] += 1
        else:
            letter_dict[letters] = 1
    odd = 0
    for k,v in letter_dict.items():
        if letter_dict[k] % 2 != 0 and odd == 0:
            odd += 1
        elif letter_dict[k] % 2 != 0 and odd != 0:
            return False
    return True


def oneAway(str1, str2):
    #Remove, rephhhlace, insert
    if str1 == str2:
        return True
    
    elif len(str1) == len(str2):
        
        changed = False
        for c1,c2 in zip(str1,str2):
            if c1 != c2:
                if changed:
                    return False
                changed = True 
        return True
    
    elif (len(str1) + 1 == len(str2)) or (len(str1) -1 == len(str2)):
        
        i,j = 0,0
        changed = False
        while i < len(str1) and j < len(str2):
            if str1[i] != str2[j]:
                if changed:
                    return False
                changed = True 
            else:
                i += 1
                j += 1
        return True
    
    else:
        return False
                
def stringCompression(string):
    #compress strings back to back 
    compressed = []
    counter = 0
    
    for i in range(len(string)):
        if i != 0 and (string[i] != string[i-1]):
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1
        
    if counter: 
        compressed.append(string[-1] + str(counter))
        
    final_compressed = ""
    for things in compressed:
        final_compressed =  final_compressed + things
    
    if len(final_compressed) >= len(string):
        return string
    else:
        return final_compressed

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
    
    print("Delete Middle Node")
    ll.insert(4)
    ll.insert(5)
    
    ll.printLL()


    delMidNode(ll)
    print()
    ll.printLL()
    
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
    
    print("LinkedList Palindrome")
    ll4 = LinkedList()
    ll4.insert(1)
    ll4.insert(2)
    ll4.insert(2)
    ll4.insert(1)
    print(palindrome(ll4))
    print(palindrome(ll1))
    
    print()
    
    print("Trying to detect Loop in List")
    ll3 = LinkedList()
    ll3.insert(3)
    ll3.insert(6)
    ll3.insert(9)
    ll3.insert(12)
    ll3.head.next = ll3.head # creates loop in LinkedList
    print(loopDetection(ll3))
    
    print()
    

    
    
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

def delMidNode(self):
    counter = 0
    temp = self.head

    while temp is not None:
        counter += 1
        temp = temp.next 
        
    mid = counter // 2
    
    while mid > 1:
        mid -= 1
        self.head.next = self.head.next
        
    self.head.next.next = self.head.next.next.next
    return self
        
        
  
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
       
def palindrome(l1):
    temp = l1.head
    number = ""
    while temp: 
        number = number + str(temp.data)
        temp = temp.next
    return number == number[::-1]        
            
        
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