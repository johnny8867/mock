class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        contain = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in contain:
                return [i, contain[complement]]
            contain[nums[i]] = i
        #O(n), O(n)