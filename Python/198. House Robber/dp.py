class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            val = nums[i]
            if i == 0:
                dp[i] = val
            elif i == 1:
                dp[i] = max(dp[0], val)
            else:
                dp[i] = max(val+dp[i-2], dp[i-1])

        return max(dp[-1], dp[-2])
        #O(n), O(n)