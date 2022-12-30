class Solution:
    def isPalindrome(self, s: str) -> bool:
        contain = ''

        for item in s:
            if item.isalnum():
                contain+= item

        return contain.lower() == contain.lower()[::-1]
        
        #O(n), O(n)