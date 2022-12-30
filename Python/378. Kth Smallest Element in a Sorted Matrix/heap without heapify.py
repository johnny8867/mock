import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        contain = []

        for i in range(min(k, len(matrix))):
            contain.extend(matrix[i])

        min_heap = []

        for item in contain:
            heapq.heappush(min_heap, item)
        
        for i in range(k):
            result = heapq.heappop(min_heap)

        return result

        #O(n +nlogn + klogn), O((n))