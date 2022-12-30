class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contain = set()
        result = 0
        left = 0
        
        for right in range(len(s)):
            while s[right] in contain:
                contain.remove(s[left])
                left += 1
            contain.add(s[right])
            result = max(result, right - left + 1)
            
        return result
    
    #O(n), #(n)