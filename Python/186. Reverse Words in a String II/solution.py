class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

        def help_reverse(s, left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        start, end = 0, 0
        length = len(s)

        while end < length:
            while end < length and s[end] != ' ':
                end += 1
            help_reverse(s, start, end-1)
            start = end + 1
            end += 1