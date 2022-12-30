class Solution:
    def getSum(self, a: int, b: int) -> int:
        x = abs(a)
        y = abs(b)
        
        if y > x:
            return self.getSum(b,a) #we want to make a the bigger value, so swap if b is bigger)
        
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            while y: #the smaller val
                x,y = (x ^ y), (x & y) << 1
        else:
            while y:
                x, y = (x ^ y), (~x & y) << 1
                
        return x * sign
    
    #O(32), O(1)