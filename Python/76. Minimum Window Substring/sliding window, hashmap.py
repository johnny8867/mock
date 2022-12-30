class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ''
        if t == '':
            return result

        contain_t = {}
        for char in t:
            contain_t[char] = contain_t.get(char, 0) + 1
        
        window = {}
        result_len = float('inf')
        left = 0
        have, need = 0, len(contain_t)
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in contain_t and window[s[right]] == contain_t[s[right]]:
                have += 1
            while have == need:
                if right - left + 1 < result_len:
                    result_len = (right - left + 1)
                    result = s[left:right+1]

                window[s[left]] -= 1

                if s[left] in contain_t and window[s[left]] < contain_t[s[left]]:
                    have -= 1
                left += 1
        return result if result_len != float('inf') else ''
        #O(s+t), O(s+t)