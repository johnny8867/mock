class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        contain = collections.defaultdict(int)
        
        result = 0
        
        for a in nums1:
            for b in nums2:
                contain[a+b] += 1
        
        for c in nums3:
            for d in nums4:
                result += contain[-(c+d)]
        return result
    
    #O(n^2), all 4 array are length on n,
    
    #O(n^2) max of n * n keys