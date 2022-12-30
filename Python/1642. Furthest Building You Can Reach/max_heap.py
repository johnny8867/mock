import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap_bricks = []

        for i in range(len(heights)-1):
            climb = heights[i+1] - heights[i]
            if climb > 0:
                heapq.heappush(max_heap_bricks, -climb)
                bricks -= climb

                if bricks < 0:
                    if ladders <= 0:
                        return i
                    bricks += -heapq.heappop(max_heap_bricks)
                    ladders -= 1

        return len(heights) - 1
        #O(nlogn), O(n)