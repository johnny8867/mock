class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        cur_num = 0
        all_op = '+-*/'
        sign = '+'

        for i in range(len(s)):
            char = s[i]

            if char.isdigit():
                cur_num = (cur_num) * 10 + int(char)
            if char in all_op or i == len(s)-1:
                if sign == '+':
                    stack.append(cur_num)
                elif sign == '-':
                    stack.append(-cur_num)
                elif sign == '*':
                    stack[-1] *= cur_num
                elif sign == '/':
                    stack[-1] = int(stack[-1]/cur_num)
                    
                cur_num = 0
                sign = char

        return sum(stack)
        #O(n), O(n)