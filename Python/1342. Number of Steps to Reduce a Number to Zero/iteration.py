class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 0
        while num:
            if num % 2 == 1:
                num -= 1
            else:
                num //= 2
            result += 1
        return result
        #O(logn), O(1)