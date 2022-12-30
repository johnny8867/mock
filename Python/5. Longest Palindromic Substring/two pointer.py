class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''

        for i in range(len(s)):
            #odd case
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(result):
                    result = s[left:right+1]
                left -= 1
                right += 1
            #even case
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(result):
                    result = s[left:right+1]
                left -= 1
                right += 1
        return result
        #O(n^3), O(1)