class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        intervals.sort()
        time = intervals[0][1]
        for i in range(1, len(intervals)):
            if time > intervals[i][0]:
                return False
            else:
                time = intervals[i][1]
        return True
        #O(N), O(1)
