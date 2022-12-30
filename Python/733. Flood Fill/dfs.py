import collections
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        temp_color = image[sr][sc]
        queue = [(sr,sc)]

        while queue:
            cur_y, cur_x = queue.pop()
            if image[cur_y][cur_x] == color:
                continue
            image[cur_y][cur_x] = color
            for y, x in ((cur_y+1, cur_x), (cur_y-1, cur_x), (cur_y, cur_x+1), (cur_y, cur_x-1)):
                if 0 <= y < len(image) and 0 <= x < len(image[0]) and image[y][x] == temp_color:
                    queue.append((y,x))
        return image
        #O(N), O(N)