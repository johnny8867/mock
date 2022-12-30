class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        result = 0

        def dfs(y,x):
            grid[y][x] = '0'
            for yy, xx in (y-1,x), (y+1, x), (y, x-1), (y, x+1):
                if 0 <= yy < len(grid) and 0<= xx < len(grid[0]) and grid[yy][xx] == '1':
                    dfs(yy,xx)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    dfs(y,x)
                    result += 1

        return result

#O(M×N), O(MXN)