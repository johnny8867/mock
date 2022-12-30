# class Solution: #
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         if len(s) == 0:
#             return ''
#         return s[-1] + self.reverseString(s[:-1]) #This method isn't done in place

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(s, left, right):
            if left > right:
                return
            s[left],s[right] = s[right], s[left]
            
            helper(s, left + 1, right - 1)
        
        helper(s, 0, len(s)-1)
        
        #O(n) to perform N/2 swap, #O(n) to keep the recursion stack