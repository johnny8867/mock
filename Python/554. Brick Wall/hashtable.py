class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        spaces = {0:0}

        for row in wall:
            count = 0
            for i in range(len(row)-1): #we don't want to count the left, right edge
                count += row[i]
                spaces[count] = spaces.get(count, 0) + 1

        return len(wall) - max(spaces.values())
        #O(N), O(N)