class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def next_num(num):
            result = 0

            while num > 0:
                result += (num % 10) ** 2 
                num //= 10
            return result

        while n != 1:
            val = next_num(n)
            if val in visited:
                return False
            visited.add(val)
            n = val
        return n == 1
        #O(logn), O(n)