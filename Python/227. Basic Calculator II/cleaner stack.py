class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        def helper(op, cur_val):
            if op == '+':
                stack.append(cur_val)
            elif op == '-':
                stack.append(-cur_val)
            elif op == '*':
                stack[-1] *= cur_val
            elif op == '/':
                stack[-1] = int(stack[-1]/cur_val)

        cur_val = 0
        sign = '+'

        for char in s:
            if char.isdigit():
                cur_val = cur_val * 10 + int(char)
            elif char in '+-*/':
                helper(sign, cur_val)
                sign = char
                cur_val = 0

        helper(sign, cur_val)

        return sum(stack)
        #O(N), O(N)