class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        contain = {}
        
        for index, value in enumerate(nums):
            if value in contain and abs(index - contain[value]) <= k:
                return True
            contain[value] = index
            
        return False
    
    #O(n), O(n)