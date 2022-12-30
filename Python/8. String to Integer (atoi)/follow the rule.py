class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        sign = 1
        result = 0

        max_val = 2 ** 31 -1 
        min_val = - 2**31

        while index < len(s) and s[index] == ' ':
            index += 1
        
        if index < len(s) and (s[index] in '+-'):
            sign = 1 if s[index] == '+' else -1
            index += 1

        while index < len(s) and s[index].isdigit():
            result = (result *10) + int(s[index])
            index += 1

        if sign == -1:
            return max(min_val, result * sign)
        else:
            return min(max_val, result)

        #O(n), O(1)