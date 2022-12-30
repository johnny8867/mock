class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        exp = abs(n)
        while exp != 0:
            if exp % 2 == 0:
                x = x * x
                exp //= 2
            else:
                result = result * x
                x = x * x
                exp = (exp-1) //2
            
        return result if n >= 0 else 1/result
    
    #log(n), O(1)