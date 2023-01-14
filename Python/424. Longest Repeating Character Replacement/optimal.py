class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        result = 0
        left = 0
        max_freq = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            max_freq = max(max_freq, window[s[right]])
            while (right - left + 1) - max_freq > k:
                window[s[left]] -= 1
                left += 1
            result = max(result, (right - left + 1))

        return result
        #O(N), O(N)