class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        contain = []

        def backtrack(index, contain, total):
            if total == target:
                result.append(contain[:])
                return
            if total > target:
                return 

            for i in range(index, len(candidates)):
                contain.append(candidates[i])
                backtrack(i, contain, total + candidates[i])
                contain.pop()

        backtrack(0, contain, 0)

        return result
        ##2^T, O(T/M)