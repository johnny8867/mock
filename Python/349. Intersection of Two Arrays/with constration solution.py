class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # if the lists are already sorted and you're told to solve in O(n) time and O(1) space:
        nums1.sort()
        nums2.sort()
        
        result = []
        
        while nums1 and nums2:
            if nums1[-1] > nums2[-1]:
                nums1.pop()
            elif nums1[-1] < nums2[-1]:
                nums2.pop()
            else:
                #avoid dup.
                if not result or result[-1] != nums1[-1]:
                    result.append(nums1[-1])
                nums1.pop()
                nums2.pop()
                
                
        return result
    
    #O(min(len(nums1), len(nums2))), O(1)
        
        