import collections
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        visited = set()
        queue = collections.deque()

        for y in range(len(rooms)):
            for x in range(len(rooms[0])):
                if rooms[y][x] == -1:
                    visited.add((y,x))
                elif rooms[y][x] == 0:
                    queue.append((y,x))
                    visited.add((y,x))

        while queue:
            r, c = queue.popleft()
            for yy,xx in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= yy < len(rooms) and 0 <= xx < len(rooms[0]) and (yy,xx) not in visited:
                    queue.append((yy,xx))
                    visited.add((yy,xx))
                    rooms[yy][xx] = rooms[r][c] + 1
        #O(r*c*4), O(m*n)
        