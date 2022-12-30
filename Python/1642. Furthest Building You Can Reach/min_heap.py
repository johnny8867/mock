import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []

        for i in range(len(heights)-1):
            climb = heights[i+1] - heights[i]
            if climb > 0:
                heapq.heappush(min_heap, climb)
                if ladders > 0:
                    ladders -= 1
                    continue
                
                bricks -= heapq.heappop(min_heap)
                #we dont add ladder back caz it's used in line 9

                if bricks < 0:
                    return i
        
        return len(heights) - 1

        #O(nlogl) or O(nlon), O(n)

        