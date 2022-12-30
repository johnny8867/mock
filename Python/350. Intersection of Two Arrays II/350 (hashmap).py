class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        contain = {}
        
        for i in range(len(nums1)):
            if nums1[i] not in contain:
                contain[nums1[i]] = 1
            else:
                contain[nums1[i]] += 1
                
        result = []
        
        for item in nums2:
            if item in contain and contain[item] > 0:
                contain[item] -= 1
                result.append(item)
                
        return result
    
    #O(max(nums1, nums2)), O(n)

print(Solution().intersect([1,2,2,1], [2,2]))