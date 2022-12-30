class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        rev_num = 0
        while x > rev_num:
            rev_num = rev_num * 10 + (x % 10)
            x //= 10

        return (x == rev_num) or (rev_num//10 == x)
        #O(logn), O(1)