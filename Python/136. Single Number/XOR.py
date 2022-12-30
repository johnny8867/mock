class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for item in nums:
            result ^= item

        return result

        #O(n), O(1)