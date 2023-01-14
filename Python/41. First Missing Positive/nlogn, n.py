class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        nums = set(nums)
        for i in range(1, (len(nums)+1)):
            if i not in nums:
                return i
        return len(nums) + 1
        #O(nlogn), O(n)