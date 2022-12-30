class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contain = {}
        
        left = 0
        result = 0
        
        for right in range(len(s)):
            while s[right] in contain:
                contain[s[left]] -= 1
                if contain[s[left]] == 0:
                    contain.pop(s[left])
                left += 1
            contain[s[right]] = contain.get(s[right], 0) + 1
            result = max(result, len(contain)) # or right - left + 1
            
        return result