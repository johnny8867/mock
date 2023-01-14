class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums1)
        hold = {}

        for i in range(len(nums1)):
            hold[nums1[i]] = i

        for i in range(len(nums2)-1,-1,-1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            if stack and nums2[i] in hold:
                result[hold[nums2[i]]] = stack[-1]
            stack.append(nums2[i])

        return result
        #O(N+M), O(N)