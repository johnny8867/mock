class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_y = 0
        start_x = len(matrix[0]) - 1

        while start_y < len(matrix) and start_x >= 0: #boundries
            if matrix[start_y][start_x] == target:
                return True
            if matrix[start_y][start_x] > target:
                start_x -= 1
            else:
                start_y += 1

        return False
#O(n+m),the len of row and col. Space:  O(1)