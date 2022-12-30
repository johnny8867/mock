class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        result = []
        
        while nums1 and nums2:
            if nums1[-1] > nums2[-1]:
                nums1.pop()
                
            elif nums1[-1] < nums2[-1]:
                nums2.pop()
                
            else:
                result.append(nums1[-1])
                nums1.pop()
                nums2.pop()
                
        return result
    
    #O(nlogn), o(1) if result doesn't count for return