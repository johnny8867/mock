class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        contain_s = {}
        contain_t = {}

        for item in s:
            contain_s[item] = contain_s.get(item, 0) + 1
        
        for item in t:
            contain_t[item] = contain_t.get(item, 0) + 1
        
        return contain_s == contain_t
        #O(n), O(n) or O(26) for space