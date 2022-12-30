# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 0
        right = 2
        
        while reader.get(right) < target:
            left = right
            right **= 2
            
        while left <= right:
            mid = (left + right) // 2
            
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return -1
    
    # O(log(T))  T is the index of the target value ? O(1)