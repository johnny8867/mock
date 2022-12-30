class Solution:
    def climbStairs(self, n: int) -> int:
        contain = [1] * n
        
        for i in range(1, n):
            contain[i] = contain[i-1] + contain[i-2]
        return contain[-1]
    
    #O(n), O(n)