#can be use for Basic Calculator I
class Solution:
    def calculate(self, s: str) -> int:
        cur_val = 0
        sign = '+'
        stack = []
        def helper(op, num):
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack[-1] *= num
            elif op == '/':
                stack[-1] = int(stack[-1]/num)

        for i in range(len(s)):
            char = s[i]

            if char.isdigit():
                cur_val = cur_val * 10 + int(char)

            elif char == '(':
                stack.append(sign)
                sign = '+'

            elif char in  '+-*/)':
                helper(sign, cur_val)
                if s[i] == ')':
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