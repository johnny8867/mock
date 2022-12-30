import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        contain = []
        for stone in stones:
            heapq.heappush(contain, -stone)

        while len(contain) > 1:
            first = -heapq.heappop(contain)
            second = -heapq.heappop(contain)

            if first > second:
                heapq.heappush(contain, -(first - second))

        return -contain[0] if contain else 0

        #nlogn + nlogn
        #O(n)