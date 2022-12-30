class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
            
    #O(nlogn + n), O(n) sort() takes O(n) space