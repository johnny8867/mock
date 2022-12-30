class Solution:
    def isValid(self, s: str) -> bool:
        table = {'(':')', '[':']', '{':'}'}
        
        stack = []
        
        for item in s:
            if item in table.keys():
                stack.append(item)
                
            elif stack and table[stack[-1]] == item:
                stack.pop()
            else:
                return False
            
        return len(stack) == 0
                
        
        #O(n), O(n)