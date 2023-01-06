"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        #contain = [item for interval in schedule for item in interval]
        contain = []
        for interval in schedule:
            for item in interval:
                contain.append(item)
        contain.sort(key = lambda x:x.start)
        end = contain[0].end
        result = []
        for i in range(1, len(contain)):
            if end < contain[i].start:
                result.append(Interval(end, contain[i].start))
            end = max(end, contain[i].end)
        return result
        #O(nlogn), O(n)