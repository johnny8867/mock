class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, contain):
            result.append(contain[:])

            for i in range(index, len(nums)):
                contain.append(nums[i])
                backtrack(i+1, contain)
                contain.pop()

        backtrack(0, [])

        return result
        #O(N*2^N), O(2^N)