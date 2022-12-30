class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        contain = set()

        for item in nums:
            if item not in contain:
                contain.add(item)
            if len(contain) == 4:
                contain.remove(min(contain))

        if len(contain) == 3:
            return min(contain)
        return max(contain)
        #O(n), O(n)