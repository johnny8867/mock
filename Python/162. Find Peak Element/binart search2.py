class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            mid_left = nums[mid-1] if mid-1 >= 0 else -float('inf')
            mid_right = nums[mid+1] if mid+1 <= len(nums) -1 else -float('inf')
            
            if mid_left < nums[mid] > mid_right:
                return mid
            
            elif mid_left < nums[mid] < mid_right: #or this also works elif nums[mid] < mid_right:
                left = mid + 1
            else:
                right = mid - 1
                
        #O(logn), O(1)