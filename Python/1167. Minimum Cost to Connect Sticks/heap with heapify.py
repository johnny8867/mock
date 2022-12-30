import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_heap = sticks
        result = 0
        heapq.heapify(min_heap)

        while len(min_heap) > 1:
            first = heapq.heappop(min_heap)
            second = heapq.heappop(min_heap)
            to_add = first + second

            result += to_add

            heapq.heappush(min_heap, to_add)

        return result
        #(nlogn + len(n)), O(n)