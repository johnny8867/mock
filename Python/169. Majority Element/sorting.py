class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums) // 2 
        return nums[mid]

        #O(nlogn), O(1) if in place is must