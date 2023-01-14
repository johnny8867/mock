class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        left = 0
        right = len(nums) - 1

        result = []

        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(nums[left])
                left += 1
            else:
                result.append(nums[right])
                right -= 1

        return result
        #Wiggle sort
        #O(nlogn), O(N)