class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lookup_table = {0:1}
        cur_sum = 0
        result = 0
        for item in nums:
            cur_sum += item
            diff = cur_sum - k
            result += lookup_table.get(diff, 0)
            lookup_table[cur_sum] = lookup_table.get(cur_sum, 0) + 1

        return result
        #O(N), O(N)