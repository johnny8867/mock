class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lookup_table ={}

        for item in nums:
            lookup_table[item] = lookup_table.get(item,0) +1

        for key, value in lookup_table.items():
            if value == 1:
                return key

        #O(n), O(n)