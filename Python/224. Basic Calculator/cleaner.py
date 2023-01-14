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
        sign = '+'
        cur_val = 0
        for char in s:
            if char.isdigit():
                cur_val = cur_val * 10 + int(char)
            elif char in '+-*/':
                helper(sign, cur_val)
                sign = char
                cur_val = 0
            elif char == '(':
                stack.append(sign)
                sign = '+'
            elif char == ')':
                helper(sign, cur_val)
                cur_val = 0
                while isinstance(stack[-1], int):
                    cur_val += stack.pop()
                sign = stack.pop()
                helper(sign, cur_val)
                cur_val = 0
                sign = char
        helper(sign, cur_val)

        return sum(stack)
        #O(N), O(N)
        