class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_cost = float('inf')
        for price in prices:
            min_cost = min(min_cost, price)
            result = max(result, price - min_cost)
        return result
        #O(n), O(1)