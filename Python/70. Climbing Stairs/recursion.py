class Solution:
    def climbStairs(self, n: int) -> int:
        contain = [1 for i in range((n+1))]
        def dp(num):
            if num > 1:
                contain[num] = contain[num-1] + contain[num-2]
            
            if num < n:
                dp(num+1)
        dp(0)

        return contain[n]
        #O(n), O(n)