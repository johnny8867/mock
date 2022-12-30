class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end = intervals[0][1]
        result = 0
        for cur_start, cur_end in intervals[1:]:
            if end > cur_start:
                result += 1
                end = min(end, cur_end)
            else:
                end = cur_end

        return result
        #O(nlogn + n), O(1)