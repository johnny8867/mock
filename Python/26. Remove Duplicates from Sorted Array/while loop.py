class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        index = 0
        while index <= len(nums)-1:
            
            if nums[index] != nums[left]:
                left += 1
                nums[left] = nums[index]
            index += 1
        return left+1
        #O(n), O(1)