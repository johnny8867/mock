import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while len(stones) >= 2:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first > second:
                heapq.heappush(stones, -(first - second))

        return -stones[0] if len(stones) > 0 else 0
        #n + nlogn + nlogn
        #O(n)