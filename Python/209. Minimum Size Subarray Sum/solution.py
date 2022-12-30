class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        cur_sum = 0 
        left = 0

        for right in range(len(nums)):
            cur_sum += nums[right]
            while left <= right and target <= cur_sum:
                result = min(result, (right - left+1))
                cur_sum -= nums[left]
                left += 1
        
        return result if result != float('inf') else 0
        #O(n^2), O(1)