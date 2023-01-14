class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        index = 1

        while index < len(nums)-1:
            nums[index], nums[index+1] = nums[index+1], nums[index]
            index += 2
        #O(nlogn), O(n)