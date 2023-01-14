class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = 1
        cur_max = 1
        result = max(nums)

        for val in nums:
            if val == 0:
                cur_min, cur_max = 1, 1
                continue
            temp_min = cur_min
            temp_max = cur_max
            cur_min = min(temp_min * val, temp_max * val, val)
            cur_max = max(temp_min * val , temp_max * val, val)
            result = max(result, cur_max)

        return result
        #O(N), O(1)