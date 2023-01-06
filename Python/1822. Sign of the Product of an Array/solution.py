class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for item in nums:
            result  *= item

        if result > 0:
            return 1
        elif result < 0:
            return -1 
        else:
            return 0
        #O(n), O(1)