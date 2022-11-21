nums = [4,5,6,7,0,1,2]
target = 10 

def search(nums, target: int) -> int:
        l, r = 0, len(nums) - 1
        nums = sorted(nums)
        print(nums)

        while (l <= r):
            mid = (l + r)// 2
            if nums[mid] == target:
                return mid
            elif (target < nums[mid]):
                r = mid - 1
            elif (target > nums[mid]):
                l = mid + 1
            
        return mid  
    
print(search(nums, target))