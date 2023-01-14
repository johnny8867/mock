class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        left = 0
        right = len(s)

        for i in range(len(t)):
            if t[i] == s[left]:
                left += 1
                if left == right:
                    return True
        return False
        #O(N), O(1)