class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def dfs(y,x, visited, prev_height):
            if 0 <= y < len(heights) and 0 <= x < len(heights[0]) and (y,x) not in visited and heights[y][x] >= prev_height:
                visited.add((y,x))

                for yy, xx in (y-1, x), (y+1, x), (y, x-1), (y, x+1):
                    dfs(yy,xx, visited, heights[y][x])

        for y in range(len(heights)):
            dfs(y, 0, pacific, heights[y][0])
            dfs(y, len(heights[0])-1, atlantic, heights[y][len(heights[0])-1])

        for x in range(len(heights[0])):
            dfs(0, x, pacific, heights[0][x])
            dfs(len(heights)-1, x, atlantic, heights[len(heights)-1][x])

        result = []
        for y in range(len(heights)):
            for x in range(len(heights[0])):
                if (y,x) in pacific and (y,x) in atlantic:
                    result.append([y,x])

        return result
        #O(M*N), O(M*N)