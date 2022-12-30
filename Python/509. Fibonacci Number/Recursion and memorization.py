class Solution:
    def fib(self, n: int) -> int:
        contain = {}
        
        
        def helper(val):
            if val in contain:
                return contain[val]
            
            if val < 2:
                result = val
            else:
                result = helper(val-1) + helper(val-2)  
            contain[val] = result
            
            return result
        
        return helper(n)
    
    #O(N), O(N)