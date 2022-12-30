class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        cur = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                cur = 0
            else:
                cur += 1
            result = max(result, cur)

        return result
        #O(n), O(1)