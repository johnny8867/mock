class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(s) < len(p):
            return result
        contain_p = {}
        contain_s = {}

        for i in range(len(p)):
            contain_p[p[i]] = contain_p.get(p[i], 0) + 1
            contain_s[s[i]] = contain_s.get(s[i], 0) + 1

        left = 0
        if contain_p == contain_s:
            result.append(0)

        for right in range(len(p), len(s)):
            contain_s[s[right]] = contain_s.get(s[right], 0) + 1
            contain_s[s[left]] -= 1

            if contain_s[s[left]] == 0:
                contain_s.pop(s[left])
            left += 1
            if contain_s == contain_p:
                result.append(left)

        return result
        #O(s +n), O(26)