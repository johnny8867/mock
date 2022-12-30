import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        fresh = 0
        time = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    queue.append((y,x))
                if grid[y][x] == 1:
                    fresh += 1

        while queue and fresh:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for yy, xx in ((row+1, col), (row-1, col), (row, col-1), (row, col+1)):
                    if 0 <= yy < len(grid) and 0 <= xx < len(grid[0]) and grid[yy][xx] == 1:
                        grid[yy][xx] = 2
                        queue.append((yy,xx))
                        fresh -= 1
            time += 1

        return time if not fresh else -1
        #O(n*m), O(n)