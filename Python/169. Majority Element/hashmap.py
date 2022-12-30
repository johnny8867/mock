class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        contain = {}
        for item in nums:
            contain[item] = contain.get(item, 0) + 1

        most = 0
        for key, value in contain.items():
            most = max(most, value)

        for key, value in contain.items():
            if value == most:
                return key

        #O(N), O(N)