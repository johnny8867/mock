class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            #odd case:
            left = right = i
            while 0 <= left and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
            
            left = i
            right = i + 1
            while 0 <= left and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
        return result
            #O(N^2), O(1)