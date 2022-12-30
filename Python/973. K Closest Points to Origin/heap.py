import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for point in points:
            x, y = point
            val = (x ** 2 + y ** 2) ** 1 / 2
            heapq.heappush(min_heap, (val, point))

        result = []

        for i in range(k):
            result.append(heapq.heappop(min_heap)[1])

        return result
        #(nlogn + k), O(n)