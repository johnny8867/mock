class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        contain = set(nums)
        for i in range(len(nums)+1):
            if i not in contain:
                return i
        #O(n), O(n)