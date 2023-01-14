class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin_val in coins:
                if i - coin_val >= 0:
                    dp[i] = min(1 + dp[i-coin_val], dp[i])

        return dp[amount] if dp[amount] != amount+1 else -1
        #O(A*C), O(A+1)