class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('inf')
        for index, value in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            
            while left < right:
                three_sum = value + nums[left] + nums[right]
                if abs(result-target) > abs(three_sum - target):
                    result = three_sum
                if three_sum < target:
                    left += 1
                else:
                    right -= 1
        return result
        #O(n^2 + nlogn), #(logn to n) depend on sorting algo