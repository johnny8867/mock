class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        first = len(num1) - 1 
        second = len(num2) - 1
        result = ''
        while first >= 0 or second >= 0:
            val1 = num1[first] if first >= 0 else 0
            val2 = num2[second] if second >= 0 else 0
            val = int(val1) + int(val2) + carry

            to_add = val % 10 

            result =str(to_add) +  result
            carry = (int(val1) + int(val2) + carry) // 10

            first -= 1
            second -= 1
        if carry:
            result ='1' +  result
        return result
        #O(n), O(1)
