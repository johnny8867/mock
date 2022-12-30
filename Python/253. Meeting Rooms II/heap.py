import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        min_heap = []
        heapq.heappush(min_heap, intervals[0][1])

        for meeting in intervals[1:]:
            if min_heap[0] <= meeting[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, meeting[1])

        return len(min_heap)

        #O(nlogn + nlogn), O(n)