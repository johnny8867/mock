class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums)+1) // 2 - 1 #odd count as big, so give the extra data point to end
        end = len(nums) - 1
        temp = [0] * len(nums)

        for i in range(len(nums)):
            if i % 2 == 0:
                temp[i] = nums[mid]
                mid -= 1
            else:
                temp[i] = nums[end]
                end -= 1
        for i in range(len(nums)):
            nums[i] = temp[i]
        #O(nlogn), O(n)