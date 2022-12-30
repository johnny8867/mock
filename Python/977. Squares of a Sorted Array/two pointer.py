class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[right]) > abs(nums[left]):
                result[i] = nums[right] ** 2
                right -= 1
            else:
                result[i] = nums[left] ** 2
                left += 1
        return result
        #O(n), O(n)