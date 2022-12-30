class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        fix = 31
        while n:
            result += (n & 1) << fix #(n & 1 checks the most right bit)
            n = n >> 1
            fix -= 1
        return result
        #O(1), O(1)