class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        carry = 0
        result = ''

        while a or b or carry:
            carry += int(a.pop() if a else 0)
            carry += int(b.pop() if b else 0)

            result += str(carry % 2)
            carry //= 2

        if carry:
            result += '1'

        return result[::-1]
        #O(n), O(n)