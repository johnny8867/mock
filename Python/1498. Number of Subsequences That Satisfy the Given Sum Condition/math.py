class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        right = len(nums) - 1 
        res = 0
        for index, left in enumerate(nums):
            while index <= right and (left + nums[right]) > target:
                right -= 1
            if index <= right:
                res += 2 ** (right - index)
        
        return res % (10 ** 9 + 7)
        #O(nlogn), O(n)