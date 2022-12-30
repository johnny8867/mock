class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        contain = {}
        def backtrack(index, total):
            if index >= len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            if (index, total) in contain:
                return contain[(index, total)]
            
            contain[(index, total)] = backtrack(index+1, total + nums[index]) + backtrack(index+1, total - nums[index])

            return contain[(index, total)]
        return backtrack(0, 0)
        #O(2^n), O(n)