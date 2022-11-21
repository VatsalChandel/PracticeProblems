def binary_search(list, target):
    # assume list is sorted
    left = 0
    right = len(list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        elif list[mid] > target:
            right = mid - 1
        
    return "target not found"


nums = [1,2,3,4,5,6,7]
print(binary_search(nums, 2))