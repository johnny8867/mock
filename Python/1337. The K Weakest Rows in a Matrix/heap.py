import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        min_heap = []
        
        for i in range(len(mat)):
            soldier = mat[i].count(1)
            heapq.heappush(min_heap, (soldier, i))
            
        result = []
        
        for i in range(k):
            result.append(heapq.heappop(min_heap)[1])
            
        return result
        #O(n^2logn + klogn)
        O(n)