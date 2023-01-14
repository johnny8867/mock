class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        check_val = nums[0]

        for val in nums:
            if val < check_val:
                result += (check_val - val)
                check_val += 1
            else:
                check_val = val + 1
        return result
        #O(nlogn + n), O(n)