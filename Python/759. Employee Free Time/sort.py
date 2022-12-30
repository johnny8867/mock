"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted([interval for s in schedule for interval in s], key = lambda x: x.start)

        result = []
        end = intervals[0].end
        
        for i in range(1, len(intervals)):
            if intervals[i].start > end:
                result.append(Interval(end, intervals[i].start))
            end = max(end, intervals[i].end)

        return result
        #O(nlogn), O(n)