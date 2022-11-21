def stringSqueeze(string, letter):
    result = ""
    for letters in string:
        if letters != letter:
            result = result + letters
    return result

print(stringSqueeze("vatsal", "t"))
            
def isPalindrome(string):
    return (string == string[::-1])

def isNamePossible(name):
    listTable = [""]# List of all elements in periodic table 
    
    #CLONA 
    
    isPossible = False

    for i in range(len(name)):
        if name[i] in listTable:
            isPossible = True
        else:
            if i > 0:
                tempElement = name[i - 1] + name[i]
                if tempElement in listTable:
                    isPossible = True 
                else:
                    return False
                    
                    
    return isPossible

def subString():
    input = "howiwouldlearndropshipping"
    key = "dropdfdf"
    index = 0

    if key in input:
        c = key[0]
        for chars in input:
            if chars == c:
                if input[index:index+len(key)] == key:
                    print(index)
            index += 1
    print(-1)
                    
tempList = ([1,2],[3,4],[2,3])
#(a,b) -> (c,d) if b < c
def chainPairs(tempList):
    newList = []
    b = 0
    tempList = sorted(tempList)
    for things in tempList:
        if b < things[0]:
            newList.append(things)
            b = things[1]
    print(len(newList))   

#chainPairs(tempList) 


def anagrams(s1, s2):
    s1Dict = {}
    s2Dict = {}
    if len(s1) != len(s2):
        print("false")
    i = 0
    while i < len(s1):
        if s1[i] in s1Dict:
            s1Dict[s1[i]] += 1
        else:
            s1Dict[s1[i]] = 1
            
        if s2[i] in s2Dict:
            s2Dict[s2[i]] += 1
        else:
            s2Dict[s2[i]] = 1
        i += 1
    print(s1Dict == s2Dict)
        
s1 = "garden"
s2 = "dangasdasder"
anagrams(s1,s2)

def firstLast(arr, target):
    #return first and last index of target in arr
    firstIndex = -1
    
    for i in range(len(arr)):
        if arr[i] == target:
            firstIndex = i
            while i + 1 < len(arr) and arr[i+1] == target:
                i += 1
            print(firstIndex, i)
                


arr = [2,4,5,5,5,5,5,7,9,9]
target = 5  
firstLast(arr, target)  