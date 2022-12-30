class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[right] - prices[left] > 0:
                profits += prices[right] - prices[left]
            left = right
        return profits
        #O(N), O(1)