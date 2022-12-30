class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        contain = {}
        
        for item in nums:
            if item in contain:
                return item
            contain[item] = 1
            
        #O(n), O(n)