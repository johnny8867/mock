class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_val = float('inf')
        while left <= right:
            mid = (left + right) // 2
            min_val = min(min_val, nums[mid])

            while left <= mid and nums[left] == nums[mid]:
                left += 1

            if left >= mid:
                continue
            
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid - 1

        return min_val
        #O(logn), O(1)