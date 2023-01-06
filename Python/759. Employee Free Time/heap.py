import heapq
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        contain = []

        for interval in schedule:
            for item in interval:
                heapq.heappush(contain, (item.start, item.end))
        result = []

        cur_start, cur_end = heapq.heappop(contain)

        while contain:
            if cur_end < contain[0][0]:
                result.append(Interval(cur_end, contain[0][0]))
            cur_end = max(cur_end, contain[0][1])
            heapq.heappop(contain)
        return result
        #O(nlogn), O(n)