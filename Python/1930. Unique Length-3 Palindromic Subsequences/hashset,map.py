class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = {}

        for val in s:
            right[val] = right.get(val, 0) + 1

        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])

            for j in range(26):
                c = chr(ord('a')+j)
                if c in left and c in right:
                    res.add((s[i], c))
            left.add(s[i])

        return len(res)
        #(26*N), O(N)