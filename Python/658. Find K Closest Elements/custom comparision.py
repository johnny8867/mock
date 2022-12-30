class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = sorted(arr, key = lambda val: abs(x - val))
        
        result = []
        for i in range(k):
            result.append(arr[i])
            
        return sorted(result)
    
    #O(nlogn + klogk)
    
    #O(N)