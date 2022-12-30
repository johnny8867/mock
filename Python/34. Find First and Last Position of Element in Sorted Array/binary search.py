class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        def findLow(nums, target):
            left = 0
            right = len(nums) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return left
        
        
        def findHigh(nums, target):
            left = 0
            right = len(nums) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return right
        
        left = findLow(nums, target)
        right = findHigh(nums, target)
        if 0 <= left <= right <= len(nums)-1:
            return [left, right]
        return [-1, -1]
        
        #O(logn), O(1)