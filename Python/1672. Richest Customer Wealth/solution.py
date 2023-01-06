class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for item in accounts:
            
            result = max(result, sum(item))

        return result
        #O(n), O(1)