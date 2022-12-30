class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        contain = {}
        for item in nums:
            if item in contain.keys():
                return True
            contain[item] = contain.get(item, 0) + 1

        return False

        #O(N), O(N)