class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        flag = 0
        contain = {}
        for char in s:
            contain[char] = contain.get(char, 0) + 1

        for key, value in contain.items():
            if value >= 2:
                result += (value // 2) * 2
            if value % 2 == 1:
                flag = 1

        return result + flag

        #O(n), O(n)