class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        result = 0
        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            while (right - left + 1) - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1
            result = max(result, (right - left + 1))

        return result
        #O(26*N), O(N)