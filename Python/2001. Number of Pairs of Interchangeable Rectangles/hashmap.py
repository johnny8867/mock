class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hold = {}
        for width, height in rectangles:
            hold[width/height] = hold.get(width/height, 0) + 1

        result = 0
        for values in hold.values():
            while values >= 2:
                result += values - 1
                values -= 1

        return result
        #O(N), O(N)