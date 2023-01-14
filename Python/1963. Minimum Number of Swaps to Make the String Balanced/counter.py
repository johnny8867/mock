class Solution:
    def minSwaps(self, s: str) -> int:
        max_close = 0
        close = 0
        for item in s:
            if item == ']':
                close += 1
                max_close = max(max_close, close)
            else:
                close -= 1

        return (max_close) // 2 + max_close % 2
        #O(N), O(1)