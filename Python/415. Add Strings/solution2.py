class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len = max(len(num1), len(num2))
        
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)
        
        result = []
        carry = 0
        
        for i in range(max_len-1,-1,-1):
            val1 = ord(num1[i]) - ord('0')
            val2 = ord(num2[i]) - ord('0')
            
            val = (val1 + val2 + carry)
            
            carry = val // 10
            
            result.append(str(val % 10))
            
        if carry == 1:
            result.append(str(carry))
            
        result.reverse()
        
        return ''.join(result)
            