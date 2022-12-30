class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left+right) // 2 # mid = left + (right-left) // 2 can prevent overflow
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
                
        return -1
    
    #O(logn), O(1)