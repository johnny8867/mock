class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = float('inf')

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            min_val = min(min_val, nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = right - 1
        return min_val
        #O(logn), O(1)