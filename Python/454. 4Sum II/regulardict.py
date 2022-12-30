class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        contain = {}
        
        result = 0
        
        for a in nums1:
            for b in nums2:
                contain[a+b] = contain.get(a+b, 0) + 1
                
        for c in nums3:
            for d in nums4:
                if -(c+d) in contain:
                    result += contain[-(c+d)]
                    
        return result
    
    #O(n^2), O(n^2)