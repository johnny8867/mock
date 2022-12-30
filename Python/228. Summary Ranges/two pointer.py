class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = 0
        right = 0
        result = []
        while right < len(nums):
            while right+1 < len(nums) and nums[right] + 1 == nums[right+1]:
                right += 1
            if left == right:
                result.append(str(nums[left]))
            else:
                result.append(str(nums[left]) + '->' + str(nums[right]))
            left = right + 1
            right += 1

        return result
        #O(n^2), O(n)