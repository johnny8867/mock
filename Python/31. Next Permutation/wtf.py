class Solution:
    def swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]

    def reverse(self, nums, start, end):
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #find pivot
        pivot = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                pivot = i
                break
        #if pivot not found, means it's in ascending order, then reverse whole thing then return
        if pivot == 0:
            self.reverse(nums, 0, len(nums)-1)
            return
        #swap nums[pivot-1] with value greater than nums[pivot-1] from right
        swap = len(nums) - 1
        while nums[pivot-1] >= nums[swap]:
            swap -= 1

        self.swap(nums, pivot-1, swap)
        #swap from pivot to end of list
        self.reverse(nums, pivot, len(nums)-1)
        #O(n), O(1)
