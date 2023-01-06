class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstbuy = float('inf')
        secondbuy = float('inf')
        firstsell = 0
        secondsell = 0

        for value in prices:
            firstbuy = min(firstbuy, value)
            firstsell = max(firstsell, value - firstbuy)
            secondbuy = min(secondbuy, value - firstsell)
            secondsell = max(secondsell, value - secondbuy)
        return secondsell
        #O(n), O(1)