class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = nums[0]
        count = 0
        for item in nums:
            if num == item:
                count += 1
            else:
                count -= 1
                if count == 0:
                    count = 1
                    num = item
        return num
        #O(n), O(1)