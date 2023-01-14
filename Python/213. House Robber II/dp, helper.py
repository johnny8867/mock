class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(nums):
            dp = [0] * len(nums)
            for i in range(len(nums)):
                if i == 0:
                    dp[i] = nums[i]
                elif i == 1:
                    dp[i] = max(dp[i-1], nums[i])
                else:
                    dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            return max(dp)

        return max(helper(nums[1:]), helper(nums[:-1]))
        #O(N), O(N)