class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} #key (index: int, canbuy: bool) : value (result)

        def dfs(index, canbuy):
            if index >= len(prices):
                return 0
            if (index, canbuy) in dp:
                return dp[(index, canbuy)]

            if canbuy:
                buy = dfs(index+1, not canbuy) - prices[index] #when we buy, we need to subtract it from our profit
                cooldown = dfs(index+1, canbuy)
                dp[index, canbuy] = max(buy, cooldown)
            else:
                sell = dfs(index+2, True) + prices[index] #when we buy, we need to add to our profit
                cooldown = dfs(index+1, canbuy)
                dp[index, canbuy] = max(sell, cooldown)
            return dp[(index, canbuy)]

        return dfs(0, True)
        #O(N), O(N)