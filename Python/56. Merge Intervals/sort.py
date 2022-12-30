class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []

        for item in intervals:
            if not result or item[0] > result[-1][1]:
                result.append(item)
            else:
                result[-1][1] = max(result[-1][1], item[1])

        return result
        #O(nlogn*n), O(n)