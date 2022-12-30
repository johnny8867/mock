class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        prev = 0
        cur = 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                result += min(prev, cur)
                prev = cur
                cur = 1
            else:
                cur += 1

        result += min(prev, cur)

        return result
        #O(n), O(1)