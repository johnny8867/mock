class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        contain = {}
        result = 0
        while right < len(s):
            while s[right] in contain:
                contain[s[left]] -= 1
                if contain[s[left]] == 0:
                    contain.pop(s[left])
                left += 1
            contain[s[right]] = contain.get(s[right], 0) + 1
            result = max(result, len(contain))
            right += 1

        
        return result
        #O(n), O(n)