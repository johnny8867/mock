class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1 
        right = 1
        result = [1] * len(nums)

        for i in range(len(nums)):
            result[i] *= left
            left *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            result[i] *= right
            right *= nums[i]

        return result

        #O(2*n), O(1)