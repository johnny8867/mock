class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start = 0

        for i in range(1, len(prices)):
            if prices[i] - prices[start] < 0:
                start = i
            else:
                profit = max(profit, prices[i] - prices[start])

        return profit
        #O(N), O(1)