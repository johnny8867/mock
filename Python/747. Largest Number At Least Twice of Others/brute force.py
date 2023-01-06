class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index = 0

        for i in range(1, len(nums)):
            if nums[max_index] < nums[i]:
                max_index = i

        for i in range(len(nums)):
            if i != max_index and nums[max_index] < nums[i] * 2:
                return -1
        
        return max_index
        #O(n), O(1)