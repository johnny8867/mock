class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2)+1)] for i in range(len(text1)+1)]

        for y in range(1, len(text1)+1):
            for x in range(1, len(text2)+1):
                if text1[y-1] == text2[x-1]:
                    dp[y][x] = dp[y-1][x-1] + 1
                else:
                    dp[y][x] = max(dp[y-1][x], dp[y][x-1])
                    
        return dp[len(text1)][len(text2)]
        #O(N*M), O(N*M)