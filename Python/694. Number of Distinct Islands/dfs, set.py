class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        result = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    self.word = ''
                    self.dfs(grid, y, x, 's')
                    result.add(self.word)
        return len(result)

    def dfs(self, grid, y, x, dir):
        if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == 1:
            grid[y][x] = 0
            self.word += dir
            self.dfs(grid, y + 1, x, "d")
            self.dfs(grid, y - 1, x, "u")
            self.dfs(grid, y, x + 1, "r")
            self.dfs(grid, y, x - 1, "l")
            self.word += 'e'

        #O(M*N), O(M*N)