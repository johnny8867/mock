class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        result = 0
        
        index = 0

        while index < len(nums):
            cur = 0
            while index < len(nums) and nums[index] == 1:
                cur += 1
                index += 1
            result = max(result, cur)
            index += 1

        return result
        #O(n), O(1)