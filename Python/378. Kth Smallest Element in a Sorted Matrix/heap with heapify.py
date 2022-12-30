import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        contain = []

        for i in range(min(k, len(matrix))):
            contain.extend(matrix[i])

        heapq.heapify(contain)

        for i in range(k):
            result = heapq.heappop(contain)

        return result

        #O(n + klogn), O((n))