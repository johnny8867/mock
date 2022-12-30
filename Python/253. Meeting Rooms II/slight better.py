import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        contain = []

        for item in intervals:
            if contain and contain[0] <= item[0]:
                heapq.heappop(contain)
            heapq.heappush(contain, item[1])
        return len(contain)
        #O(nlogn), O(n)