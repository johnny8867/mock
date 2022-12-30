class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        contain = []
        result = []
        candidates.sort()
        def backtrack(index, contain, total):
            if total == target:
                result.append(contain[:])
                return
            if total > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                contain.append(candidates[i])
                backtrack(i+1, contain, total + candidates[i])
                contain.pop()
 
        backtrack(0, contain, 0)
        return result            
        #(nlogn + 2^T), O(T/M)