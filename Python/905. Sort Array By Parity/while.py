class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) -1 

        index = 0

        while index <= right:
            if nums[index] % 2 == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
            index += 1
        
        return nums
        #O(n), O(1)