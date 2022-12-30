class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max + nums[i])
            result = max(cur_max, result)
        return result
        #O(n), O(1)