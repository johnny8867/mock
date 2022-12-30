class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index, cur, total):
            if total == target:
                result.append(cur[:])
                return
            if index >= len(candidates) or total > target:
                return
            
            cur.append(candidates[index])
            dfs(index,cur, total + candidates[index])
            cur.pop()
            dfs(index+1, cur, total)

        dfs(0,[],0)

        return result

        #O(2^T), T = target. O(T/M), M = min val amounts the candidates