class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        cur_sum = 0
        sign = 1

        for char in s:
            if char.isdigit():
                cur_sum = (cur_sum) * 10 + int(char)
            elif char == '+':
                result += (sign * cur_sum)
                cur_sum = 0
                sign = 1
            elif char == '-':
                result += (sign * cur_sum)
                cur_sum = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += (sign * cur_sum)
                result *= stack.pop()
                result += stack.pop()
                cur_sum = 0
                sign = 1

        return result + (sign * cur_sum)
        #O(n), O(n)