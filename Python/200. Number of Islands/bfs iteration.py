import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = collections.deque()
        result = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    queue.append((y,x))
                    grid[y][x] = '0'

                    while queue:
                        row, col = queue.popleft()
                        for yy, xx in (row+1,col), (row-1,col), (row,col+1), (row,col-1): 
                            if 0 <= yy < len(grid) and 0 <= xx < len(grid[0]) and grid[yy][xx] == '1':
                                queue.append((yy,xx))
                                grid[yy][xx] = '0'
                    result += 1

        return result
        #O(MXN), space O(min(M,N))