class Solution:
    def romanToInt(self, s: str) -> int:
        contain = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)):
            if i+1 < len(s) and contain[s[i]] < contain[s[i+1]]:
                result -= contain[s[i]]
            else:
                result += contain[s[i]]
        return result
        #O(n), O(n)