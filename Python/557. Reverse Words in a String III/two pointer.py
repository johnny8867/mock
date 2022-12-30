class Solution:
    def reverseWords(self, s: str) -> str:
        def helper_reverse(s, left, right):
            while left < right:
                print(left, right)
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        left = 0
        right = 0
        s = list(s)
        while right < len(s):
            while right < len(s) and s[right] != ' ':
                right += 1
            helper_reverse(s, left, right-1)
            left = right + 1
            right +=1 
        return ''.join(s)
        #O(n), O(n)