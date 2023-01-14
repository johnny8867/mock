class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            result += self.helper(s, i, i)
            result += self.helper(s, i, i+1)
        return result

    def helper(self, s, left, right):
        result = 0
        while 0 <= left and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1
        return result
            #O(N^2), O(1)