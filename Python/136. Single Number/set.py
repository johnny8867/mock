class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2* sum(set(nums)) - sum(nums)

        #O(n), O(n)

#Time complexity : O(n+n)=O(n). 
# sum will call next to iterate through nums.
# We can see it as sum(list(i, for i in nums)) which means 
# the time complexity is O(n) because of the number 
# of elements(n) in nums.

#Space complexity : O(n+n)=O(n). set needs space for the elements in nums