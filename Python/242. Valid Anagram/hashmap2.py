class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        contain_s = {}

        if len(s) != len(t):
            return False

        for item in s:
            contain_s[item] = contain_s.get(item, 0) + 1
        
        for item in t:
            if item not in contain_s or contain_s[item] == 0:
                return False
            contain_s[item] -= 1

        return True
        #O(n), O(n) or O(26) for space