unsorted = [1,2,4,5,3,3,3,3]

def minswap(list):
    counter = 0 
    sorted_list = sorted(list)
    sorted_dict = {}
    
    for i in range(len(sorted_list)):
        sorted_dict[i] = sorted_list[i]
        
    for j in range(len(list)):
        if list[j] != sorted_dict[j]:
            counter += 1
            
    print(sorted_dict)
    print(counter//2)
    
    
    
print(unsorted)
print(sorted(unsorted))
minswap(unsorted)