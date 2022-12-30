class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        for item in s:
            if item != ']':
                stack.append(item)
                
            else:
                cur = ''
                
                while stack[-1] != '[':
                    cur = stack.pop() + cur
                    
                stack.pop()
                
                val = ''
                
                while stack and stack[-1].isdigit():
                    val = stack.pop() + val
                    
                stack.append(int(val) * cur)
                
        return ''.join(stack)
    
    #O(n), O(n)?