class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(lists, left, right):
            while left < right:
                lists[left], lists[right] = lists[right], lists[left]
                left += 1
                right -= 1
        
        k %= len(nums)

        reverse(nums, 0, len(nums)-1) 
        reverse(nums, 0, k-1) #can't just do nums[:3]
        reverse(nums, k, len(nums)-1)

        return nums
        #O(N), O(1)