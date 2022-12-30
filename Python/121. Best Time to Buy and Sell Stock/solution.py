class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[right] - prices[left] < 0:
                left = right
            result = max(result, prices[right] - prices[left])
        
        return result
        #O(n), O(1)
            