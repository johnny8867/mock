class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        result = 0
        nums.sort()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < target:
                    result += (right - left)
                    left += 1
                else:
                    right -= 1
        return result
        #O(n^2 + nlogn), O(n ~ logn)