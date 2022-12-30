class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        contain = set(nums)
        result = []
        for i in range(1, len(nums)+1):
            if i not in contain:
                result.append(i)

        return result
        #O(n), O(n)