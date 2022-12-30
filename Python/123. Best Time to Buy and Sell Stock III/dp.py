class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min = prices[0]
        right_max = prices[-1]
        
        length = len(prices)
        
        left_profit = [0] * length
        right_profit = [0] * (length + 1)
        
        for left in range(1, length):
            left_profit[left] = max(left_profit[left-1], prices[left] - left_min)
            left_min = min(left_min, prices[left])
            
            right = length - 1 - left
            
            right_profit[right] = max(right_profit[right+1], right_max - prices[right])
            right_max = max(right_max, prices[right])
        
        max_profit = 0
        for i in range(length):
            max_profit = max(max_profit,left_profit[i] + right_profit[i+1])
            
        return max_profit
    
    #O(N), O(N)