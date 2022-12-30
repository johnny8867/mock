class Solution:
    def climbStairs(self, n: int) -> int:
        contain = [1] * (n+1)
             
        for i in range(n-2,-1,-1):
            contain[i] = contain[i+1] + contain[i+2]  
            
        return contain[0]
    
    #O(N), #O(N)