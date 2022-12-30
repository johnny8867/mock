import collections
#bfs
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        queue = collections.deque()

        for y in range(len(mat)):
            for x in range(len(mat[0])):
                if mat[y][x] == 0:
                    visited.add((y,x))
                    queue.append((y,x))

        while queue:
            row, col = queue.popleft()
            for yy, xx in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                if 0 <= yy < len(mat) and 0 <= xx < len(mat[0]) and (yy, xx) not in visited:
                    mat[yy][xx] = mat[row][col] + 1
                    visited.add((yy,xx))
                    queue.append((yy,xx))

        return mat
        #O(n), O(n)