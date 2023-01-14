class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(1, len(nums)):
            prev = nums[i-1]
            now = nums[i]

            if i % 2 == 1:
                #check if greater
                if prev >= now:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
            else:
                if prev <= now:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
            #O(N), O(1)