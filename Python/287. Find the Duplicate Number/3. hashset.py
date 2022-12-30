class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique = set()
        
        for item in nums:
            if item in unique:
                return item
            unique.add(item)
    
    #O(n), O(n)