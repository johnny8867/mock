class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while nums[left] > nums[right]:
            mid = (left+right) // 2
            
            if nums[mid] > nums[right]: #means that the min value is b/w mid to right.
                left = mid + 1
            else:
                right = mid
                
        return nums[left]