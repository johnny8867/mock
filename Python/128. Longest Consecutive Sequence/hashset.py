class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        longest = 0

        for item in nums:
            if item-1 not in nums:
                current_val = item
                current_streak = 1

                while current_val + 1 in nums:
                    current_val += 1
                    current_streak += 1
                
                longest = max(longest, current_streak)

        return longest
        #O(N), O(N)