class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums1)
        lookup = {value:index for index, value in enumerate(nums1)}

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and stack[-1] < cur:
                val = stack.pop()
                index = lookup[val]
                result[index] = cur
            
            if cur in nums1:
                stack.append(cur)

        return result
        #O(n+m)
        #O(nums1)