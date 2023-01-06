import collections
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        original = image[sr][sc]

        contain = collections.deque()

        def backtrack(y,x):
            visited.add((y,x))
            image[y][x] = color
            for yy, xx in ((y-1,x), (y+1, x), (y, x-1), (y, x+1)):
                if 0 <= yy < len(image) and 0 <= xx < len(image[0]) and (yy, xx) not in visited and image[yy][xx] == original:
                    backtrack(yy,xx)

        backtrack(sr,sc)

        return image
        #O(n), O(n)