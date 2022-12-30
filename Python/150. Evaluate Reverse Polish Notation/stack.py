class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        contain = []

        for item in tokens:
            if item == '+':
                contain.append(contain.pop()+ contain.pop())
            elif item == '-':
                first = contain.pop()
                second = contain.pop()
                contain.append(second - first)
            elif item == '*':
                contain.append(contain.pop() * contain.pop())            
            elif item == '/':
                first = contain.pop()
                second = contain.pop()
                contain.append(int(second/first))
            else:
                contain.append(int(item))
        return contain[0]
        #O(N), O(N)