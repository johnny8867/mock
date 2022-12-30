class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        contain = {}
        most = 0
        for index, value in enumerate(nums):
            if value not in contain:
                contain[value] = [1, [index]]
            else:
                contain[value][0] += 1
                contain[value][1].append(index)
            most = max(most, contain[value][0])
            
        result = float('inf')
        for value in contain.values():
            if value[0] == most:
                result = min(result, value[1][-1] -value[1][0] + 1)
        return result
        #O(n), O(n)