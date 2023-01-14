class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            index = abs(nums[i]) - 1

            if 0 <= index < len(nums):
                if nums[index] > 0:
                    nums[index] *= -1
                elif nums[index] == 0:
                    nums[index] = -(len(nums)+1)

        for i in range(len(nums)):
            if nums[i] >=0:
                return i+1

        return len(nums)+1
        #O(N), O(1)