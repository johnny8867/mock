class Solution:
    def fib(self, n: int) -> int:
        dp = {0:0, 1:1}

        def helper(val):
            if val in dp:
                return dp[val]
            dp[val] = helper(val-1) + helper(val-2)
            return dp[val]
        return helper(n)
        #O(N), O(N)