class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index, value in enumerate(nums):
            if index > 0 and nums[index-1] == value:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                three_sum = value + nums[left] + nums[right]
                if three_sum == 0:
                    result.append([value, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1

        return result
        #O(nlogn + n^2), O(n)