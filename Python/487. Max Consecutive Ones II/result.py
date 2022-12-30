class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev = 0
        cur = 0
        result = 0
        zero = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prev = cur
                zero = 1
                cur = 0
            else:
                cur += 1
            result = max(result, prev + zero + cur)
        return result
        #O(n), O(1)