class Solution:
    def fib(self, n: int) -> int:
        contain = [0] + [1] *n
        
        
        for i in range(1, len(contain)): #can start from 1 or 2, if 1 -> 0 + 1 still 1 so pointless
            contain[i] = contain[i-1] + contain[i-2]
        
        
        return contain[-1]
    
    #O(N), O(N)