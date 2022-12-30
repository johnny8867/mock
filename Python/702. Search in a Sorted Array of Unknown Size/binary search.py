# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 0 
        right = 10000
        
        while left <= right:
            mid = (left + right) // 2
            
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return -1
    
    #O(log(n)), O(1)