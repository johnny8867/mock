class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1
        #O(n^2), O(1)