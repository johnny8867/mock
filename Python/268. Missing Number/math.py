class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        result = length * (length+1) // 2
        for item in nums:
            result -= item

        return result
        #O(n), O(1) #math